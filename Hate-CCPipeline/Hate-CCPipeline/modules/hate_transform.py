"""Transform module
"""

import tensorflow as tf
LABEL_KEY = "recalled"
FEATURE_KEY = "text"


def transformed_name(key):
    """Renaming transformed features"""
    return key + "_xf"


def preprocessing_fn(inputs):
    """
    Preprocess input features into transformed features

    Args:
        inputs: map from feature keys to raw features.

    Return:
        outputs: map from feature keys to transformed features.
    """

    outputs = {}

    if LABEL_KEY in inputs and inputs[LABEL_KEY] is not None:
        outputs[transformed_name(LABEL_KEY)] = tf.cast(
            inputs[LABEL_KEY], tf.int64)
    else:
        raise ValueError(f"Missing or None value for {LABEL_KEY}")

    if FEATURE_KEY in inputs and inputs[FEATURE_KEY] is not None:
        outputs[transformed_name(FEATURE_KEY)] = tf.strings.lower(
            inputs[FEATURE_KEY])
    else:
        raise ValueError(f"Missing or None value for {FEATURE_KEY}")

    return outputs
