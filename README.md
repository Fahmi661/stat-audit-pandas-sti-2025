# 📊 Statistical Audit: Pandas GitHub Repository (STI 2025)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)

Repository ini berisi tugas pengumpulan dataset dan analisis statistika terhadap *Issues* dan *Pull Requests (PR)* dari repository open-source raksasa: **[pandas-dev/pandas](https://github.com/pandas-dev/pandas)**. 

Tujuan dari proyek ini adalah untuk melakukan audit dan analisis performa dari manajemen *Issues* serta tingkat *merge* dari *Pull Requests* dalam sebuah proyek perangkat lunak skala besar.

---

## 📁 Struktur Proyek

```text
stat-audit-pandas-sti-2025/
├── data/
│   ├── clean/
│   │   └── prs_clean.csv      # dataset bersih yang siap dianalisis
│   └── raw/                   # original data, never modified
│       ├── issues_raw.csv
│       └── prs_raw.csv
├── notebooks/
│   ├── 01_eda.ipynb           # Member A
│   ├── 02_estimation.ipynb    # Member B
│   ├── 03_confidence_interval.ipynb # Member C
│   ├── 04_hypothesis_testing.ipynb  # Member D
│   └── 05_simulation.ipynb    # Member E
├── presentation/
│   └── video_link.md
├── report/
│   └── statistika-pandas-report.pdf
├── src/
│   ├── .gitkeep               # Placeholder
│   ├── ambil_data.py          # Script ambil data GitHub API
│   ├── estimator.py           # Member B
│   ├── fix_nb2.py             # Script perbaikan notebook
│   ├── hypothesis.py          # Member D
│   ├── inference.py           # Member C
│   └── simulation.py          # Member E
├── .gitignore                 # Daftar file yang diabaikan
├── AI_USAGE_LOG.md            # required log AI
├── README.md                  # project desc, research questions, findings, how-to-run, team table
└── requirements.txt           # numpy, scipy, pandas, matplotlib, seaborn, requests
```

---

## 🛠️ Apa Saja yang Kami Lakukan?

### 1. 📡 Pengumpulan Data (Data Collection)
Kami membuat script Python (`ambil_data.py`) yang terhubung langsung dengan **GitHub REST API**. Script ini secara otomatis menarik (scraping) data terbaru dengan rincian:
- **5000 *Closed Issues***: Mengambil ID, judul, tanggal dibuat, tanggal ditutup, dan label.
- **5000 *Closed Pull Requests***: Mengambil informasi detail kapan PR dibuat, kapan ditutup, dan status apakah PR tersebut berhasil di-*merge* atau ditolak.

*(Data mentah ini kami simpan di folder `data/raw/`)*.

### 2. 🧹 Pembersihan Data (Data Cleaning)
Pemrosesan data mentah dilakukan di dalam **Jupyter Notebook (`01_eda.ipynb`)**. Proses pembersihan meliputi:
- Memilih kolom-kolom yang relevan untuk analisis.
- Menghapus data yang rusak atau memiliki nilai tanggal yang kosong (NaN).
- Mengonversi format string menjadi tipe data *Datetime* standar.
- Melakukan Feature Engineering: **Menghitung durasi penyelesaian** (*Close Time*) dengan mencari selisih hari antara waktu *Issue/PR* dibuat dengan waktu ditutupnya.
- Mengidentifikasi status integrasi PR (diberi tanda `1` jika *Merged*, `0` jika tidak).

### 3. 📈 Exploratory Data Analysis (EDA) awal
Setelah data bersih dan tersimpan di `data/clean/`, kami membuat visualisasi awal untuk mendapatkan *insight* berupa:
- **Time-Series Analysis**: Mengamati tren jumlah *Issues* yang dibuat setiap harinya.
- **Distribution Analysis**: Melihat distribusi waktu penyelesaian *Issues* (berapa hari mayoritas *Issues* bisa diselesaikan).
- **Proportion Analysis**: Menggunakan *Pie Chart* untuk melihat rasio sukses (*Merged*) dari *Pull Requests* yang dikerjakan oleh kontributor Pandas.

---

## 🚀 Cara Menjalankan Proyek Ini

Jika Anda ingin mereproduksi atau menguji proyek ini dari awal, ikuti langkah-langkah berikut:

1. **Clone repository ini**
   ```bash
   git clone https://github.com/username/stat-audit-pandas-sti-2025.git
   cd stat-audit-pandas-sti-2025
   ```

2. **Install Library yang Dibutuhkan**
   Pastikan Anda sudah menginstall library berikut:
   ```bash
   pip install pandas matplotlib seaborn requests jupyter
   ```

3. *(Opsional)* **Ambil Ulang Data dari GitHub API**
   Jika Anda ingin menarik ulang data dari GitHub, Anda harus mengatur Token terlebih dahulu.
   - Buka `ambil_data.py`
   - Masukkan *Personal Access Token* GitHub Anda pada variabel `TOKEN`.
   - Jalankan script:
     ```bash
     python ambil_data.py
     ```

4. **Jalankan Jupyter Notebook**
   Untuk melihat kode pembersihan data dan visualisasi statistik:
   ```bash
   jupyter notebook notebooks/01_eda.ipynb
   ```

---
*Dibuat untuk pemenuhan Tugas Dataset Statistika - STI 2025.*
