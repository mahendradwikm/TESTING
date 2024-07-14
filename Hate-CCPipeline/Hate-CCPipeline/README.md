# Submission 1: Machine Learning Pipeline - Hate Speech Prediction
Nama: Fira Areta Apsarini

Username dicoding: fira_areta_apsarini

| | Deskripsi |
| ----------- | ----------- |
| Dataset | [People Slurs Dataset](https://www.kaggle.com/datasets/sinatavakoli/people-slurs-dataset) |
| Masalah | Setiap orang memiliki pengalaman yang tidak mengenakan yang datang dari orang lain, seperti mendapatkan perkataan yang tidak baik diucapkan dari pihak lain. Terkadang pengalaman tersebut selalu diingat oleh beberapa orang karena intensnya cemooh pihak lain tersebut. Namun apakah semua orang selalu mengingat hal yang tidak menyenangkan itu? |
| Solusi machine learning | Machine Learning dapat mengetahui apakah orang tersebut selalu mengingat pengalaman itu atau dapat melupakannya hanya dengan tulisan. |
| Metode pengolahan | Dataset untuk Hate Speech Prediction terdapat dua feature yang digunakan yaitu "text" yang berisikan pengalaman setiap orang dan "recalled" sebagai label penentuan. Data tersebut diproses dengan melakukan split data train dan eval dengan rasio 8:2 kemudian mengubah text feature menjadi lowercase dan recalled feature menjadi integer. |
| Arsitektur model | Model ini menggunakan arsitektur embedding yang terdiri dari beberapa lapisan, yaitu vectorize_layer untuk vektorisasi data teks, kemudian mengubah vektor tersebut menjadi embedding dengan dimensi 16, lalu AveragePooling1D dan Dense layer 64, 32 masing masing dengan aktivasi ReLU dan Sigmoid Model ini menggunakan loss binary_crossentropy dengan optimizer Adam dan metrik BinaryAccuracy. |
| Metrik evaluasi | Metrik evaluasi yang digunakan adalah ExampleCount, AUC, FalsePositives, TruePositives, FalseNegatives, TrueNegatives, dan BinaryAccuracy |
| Performa model | Evaluasi model diperoleh yaitu binary accuracy sebesar 88% dengan loss sebesar 0.3 |
| Opsi Deployment | Proses model deployment memanfaatkan aplikasi Railway |
| Web App | hate-pipeline-production.up.railway.app/v1/models/hate-prediction-model/metadata |
| Monitoring | Monitoring dari hasil model serving menggunakan Prometheus |
