# Convolutional Neural Network (CNN) Model

## Deskripsi Proyek

Proyek ini mencakup implementasi model Convolutional Neural Network (CNN) untuk Klasifikasi Aksara Jawa. Model ini telah dilatih pada dataset berisi kumpulan aksara jawa dan dapat digunakan untuk mengetahui aksara jawa.

## Daftar Isi

- [Deskripsi Proyek](#deskripsi-proyek)
- [Daftar Isi](#daftar-isi)
- [Persyaratan](#persyaratan)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Struktur File](#struktur-file)
- [Contoh](#contoh)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)
- [Kontak](#kontak)

## Persyaratan

Untuk menjalankan proyek ini, Anda memerlukan:

- Python 3.9 - 3.11
- Library Python berikut:
  - TensorFlow 2.15.0
  - NumPy
  - Pandas
  - Matplotlib
  - scikit-learn
- Jupyter Notebook (opsional, untuk eksplorasi dan pelatihan interaktif)

## Instalasi

1. Clone repository ini:
    ```sh
    git clone https://github.com/rfahur11/aksara_jawa.git
    cd repository
    ```

2. Buat dan aktifkan environment virtual (opsional tetapi direkomendasikan):
    ```sh
    python -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`
    ```

3. Instal dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Penggunaan

### Pelatihan Model

1. Jalankan notebook `train_model.ipynb` untuk melatih model:
    ```sh
    jupyter notebook.ipynb
    ```
   - Atur parameter pelatihan seperti jumlah epoch, ukuran batch, dsb., di dalam notebook.

2. Model terlatih akan disimpan di direktori `models/`.

### Inferensi/Pengujian Model

1. Gunakan skrip `predict.py` untuk melakukan prediksi menggunakan model terlatih:
    ```sh
    python predict.py --input path/to/input_image --model path/to/model
    ```

   - Gantilah `path/to/input_image` dengan path ke gambar input dan `path/to/model` dengan path ke model terlatih.

## Struktur File

Berikut adalah struktur direktori proyek ini:

repository/
├── data/
│   ├── raw/                   # Direktori untuk dataset mentah \n
│   └── README.md              # Dokumentasi tentang data
├── models/                    # Direktori untuk menyimpan model terlatih
│   └── modelC.keras           # model yang tersimpan untuk diuji coba
│   └── modelC.tflite          # model yang telah dideploy untuk diintegrasikan ke aplikasi android
├── notebooks/                 # Jupyter Notebooks
    └── notebook.ipynb         # Notebook untuk pelatihan model
    └── notebook_coolab.ipynb  # Notebook untuk pelatihan model di Coolab
    └── load_model.ipynb       # Notebook untuk ppengujian model
├── .gitignore                 # File untuk mengabaikan file/direktori tertentu dalam Git
├── README.md                  # Dokumentasi proyek
└── requirements.txt           # Daftar dependencies



## Contoh

Berikut adalah contoh penggunaan model untuk melakukan prediksi:

```sh
python scripts/predict.py --input data/test_image.jpg --model model/modelC.keras


