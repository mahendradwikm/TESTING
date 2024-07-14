"""Local Pipeline module
"""

import os
from typing import Text

from absl import logging
from tfx.orchestration import metadata, pipeline
from tfx.orchestration.beam.beam_dag_runner import BeamDagRunner

PIPELINE_NAME = "hate-pipeline"

# Pipeline inputs
DATA_ROOT = "data"
TRANSFORM_MODULE_FILE = "modules/hate_transform.py"
TRAINER_MODULE_FILE = "modules/hate_trainer.py"

# Pipeline outputs
OUTPUT_BASE = "output"
SERVING_MODEL_DIR = os.path.join(OUTPUT_BASE, 'serving_model')
PIPELINE_ROOT = os.path.join(OUTPUT_BASE, PIPELINE_NAME)
METADATA_PATH = os.path.join(PIPELINE_ROOT, "metadata.sqlite")

def init_local_pipeline(
    components, pipeline_root: Text
) -> pipeline.Pipeline:
    """Combine TFX Components"""

    logging.info(f"Pipeline root set to: {pipeline_root}")
    beam_args = [
        "--direct_running_mode=multi_processing"
        # 0 auto-detect based on on the number of CPUs available
        # during execution time.
        "----direct_num_workers=0"
    ]

    return pipeline.Pipeline(
        pipeline_name=PIPELINE_NAME,
        pipeline_root=pipeline_root,
        components=components,
        enable_cache=True,
        metadata_connection_config=metadata.sqlite_metadata_connection_config(
            METADATA_PATH
        ),
        eam_pipeline_args=beam_args
    )


if __name__ == "__main__":
    logging.set_verbosity(logging.INFO)

    from components import init_components

    components = init_components(
        DATA_ROOT,
        training_module=TRAINER_MODULE_FILE,
        transform_module=TRANSFORM_MODULE_FILE,
        training_steps=5000,
        eval_steps=1000,
        serving_model_dir=SERVING_MODEL_DIR,
    )

    pipeline_instance = init_local_pipeline(components, PIPELINE_ROOT)
    BeamDagRunner().run(pipeline=pipeline_instance)
