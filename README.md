# Machine Learning Operations (MLOps) - Anemia Detection
Nama: M. Dwi Pratama

Username dicoding: mdpraz


| | Deskripsi |
| ----------- | ----------- |
| Dataset | [Anemia Dataset](https://www.kaggle.com/code/aronxx443/anemia-analysis-knime) |
| Masalah | Anemia adalah kondisi medis yang ditandai oleh kadar sel darah merah (hemoglobin) yang rendah dalam tubuh. Hal ini terjadi ketika tubuh tidak memiliki cukup sel darah merah yang sehat atau hemoglobin yang cukup untuk membawa oksigen ke jaringan tubuh. Anemia dapat disebabkan oleh berbagai faktor, termasuk kekurangan zat besi, kekurangan vitamin B12, kekurangan asam folat, gangguan genetik, penyakit kronis, dan kehilangan darah yang berlebihan. Pendeteksian dini dan manajemen anemia sangat penting untuk mencegah anemia semakin parah dan menyebabkan komplikasi yang lebih serius.  |
| Solusi machine learning | Dari permasalahan diatas dapat memanfaatkan suatu teknologi, teknologi yang cocok untuk membantu permasalahan tersebut adalah dengan machine learning. Dengan demikian machine learning dapat menjadi salah satu solusi untuk membantu penanganan terhadap penyakit anemia dengan mempercepat proses pendeteksian dini. Dengan suatu sistem prediksi penyakit anemia, diharapkan ahli medos maupun masyarakat dapat terbantu untuk mendeteksi penyakit anemia ini lebih awal. |
| Metode pengolahan | Pada project ini terdapat, tujuh buah feature pada dataset dimana 6 feature akan digunakan sebagai variabel independen, dan satu buah feature sebagai variable dependen yang mana berisi target data seseorang menderita *anemia* atau *tidak anemia*. Terdapat satu kolom bertipe categorical dan enam lainnya berupa numerik, yang akan dilakukan split data dengan skema 80:20 untuk data train dan eval. Proses transform dilakukan untuk me-rename feature yang ditransform dan one hot encoding untuk kelas data categorical. |
| Arsitektur model | Arsitektur model yang digunakan menggunakan *deep neural network*, yang terdiri dari beberapa lapisan Dense yaitu, Dense 256, Dense 64, Dense 16 dengan fungsi activation ReLu, kemudian pada lapisan terakhir menggunakan fungsi activation sigmoid karena akan mengklasifikasi kelas target yaitu *anemia* atau *tidak anemia*. Untuk model compile menggunakan optimizers dengan Adam dan nilai learning_rate sebesar 0.001, loss binary_crossentropy dengan metrics BinaryAccuracy. |
| Metrik evaluasi | Untuk mengukur performa dari model yang dibuat dianalisis dengan metrik evaluasi yang digunakan yaitu AUC, Precision, Recall, ExampleCount dan BinaryAccuracy. |
| Performa model | Dari performa model yang dibangun, dapat diketahui dengan melihat nilai accuracy dan loss yang didapat. Untuk accuracy didapatkan sebesar 99% dengan loss sebesar 0.0208 sedangkan untuk nilai val_accuracy didapatkan nilai sebesar 97% dengan val_loss sebesar 0.0755 dapat diketahui tidak terjadi overfitting pada model yang dibangun dan dari hasil tersebut dapat dikatakan model sudah baik dalam memprediksi target. |
| Opsi deployment | Deployment pada project ini dilakukan dengan menggunakan platform railway. |
| Web app | [anemia-prediction](https://anemia-prediction-7ac6.up.railway.app/v1/models/anemia-prediction-model/metadata)|
| Monitoring | Monitoring yang dilakukan pada project ini dilakukan dengan menggunakan layanan open-source prometheus. Dari setiap perubahan jumlah request yang dilakukan terhadap sistem ini dapat dimonitoring dengan sangat baik dan juga dapat menampilkan status dari setiap request yang diterima. |
