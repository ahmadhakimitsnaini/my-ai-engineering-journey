# 100-Day AI Engineering Roadmap: Dari Nol Hingga Produksi Skala Besar

Dokumen ini adalah kurikulum harian eksklusif yang dibangun dengan menerapkan 4 prinsip utama:
1. **Code-First Math**: Mengimplementasikan rumus murni tanpa library sebelum beralih ke *framework*.
2. **Zig-Zag Learning**: Berpindah dinamis antara Matematika (Teori) -> Kode (Praktik) -> Aplikasi (Proyek) -> Matematika Lanjutan.
3. **Project-Driven Progression**: Integrasi harian yang bermuara pada mini-project setiap akhir bagian.
4. **Systems Thinking**: Tidak hanya melatih model, tetapi merekayasa server infrastrukturnya di fase akhir.

---

## Bagian 1: Fondasi Data & Aljabar (Hari 1 - 20)

### Minggu 1: Setup & Python Dasar
- [ ] **Hari 1:** **[Systems]** *Setup Environment* (Python 3.10+, VS Code, Git, Jupyter Notebook). Memahami terminal.
- [ ] **Hari 2:** **[Code]** Review Python Fundamentals (Variabel, Tipe Data, Loop Bersarang, Function).
- [ ] **Hari 3:** **[Code]** Python Fungsional (*List Comprehension*, `lambda`, `map`, `filter`).
- [ ] **Hari 4:** **[Code]** Object-Oriented Programming (OOP) Dasar. Memahami `class`, `object`, dan `__init__` (pondasi library ML).
- [ ] **Hari 5:** **[Code]** Eksplorasi struktur data bawaan Python (`collections`, `math`, `itertools`).

### Minggu 2: Aljabar Linear (Code-First)
- [ ] **Hari 6:** **[Math]** Konsep Skalar, Vektor, dan Operasi Vektor matematis (Penjumlahan, Pengurangan).
- [ ] **Hari 7:** **[Code]** Membuat `class Vector` manual dan fungsi `dot_product` murni Python.
- [ ] **Hari 8:** **[Math]** Konsep Matriks, Dimensi (Shape), dan Operasi Matriks (Transposisi).
- [ ] **Hari 9:** **[Code]** Menulis fungsi perkalian matriks (*Matrix Multiplication*) secara manual dengan loop bersarang.
```python
# Contoh Code-First: Matmul Manual
def matmul(A, B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
```
- [ ] **Hari 10:** **[Code]** Migrasi total dari kode manual ke `NumPy`. Membuktikan perbedaan performa drastis antara loop Python vs Vektorisasi C di backend `NumPy`.

### Minggu 3: Manipulasi Data
- [ ] **Hari 11:** **[ML]** Pengenalan `Pandas`: Series dan DataFrame (Analoginya seperti tabel Excel bertenaga roket).
- [ ] **Hari 12:** **[ML]** Data Wrangling 1: *Filtering*, *Slicing*, dan *Sorting* dataset E-Commerce mentah.
- [ ] **Hari 13:** **[ML]** Data Wrangling 2: Mendeteksi dan menangani *Missing Values* (Imputasi) serta anomali *Outliers*.
- [ ] **Hari 14:** **[ML]** Data Aggregation: Menggunakan *Groupby*, *Pivot Table*, dan menggabungkan DataFrame.
- [ ] **Hari 15:** **[ML]** Visualisasi Data (*Exploratory Data Analysis*) menggunakan `Matplotlib` & `Seaborn` untuk mencari korelasi fitur.

### Minggu 4: Micro-Project 1 (Sistem Rekomendasi)
- [ ] **Hari 16:** **[Math]** Mempelajari Jarak Euclidean & Cosine Similarity secara visual dan matematis.
- [ ] **Hari 17:** **[Code]** Mengimplementasikan algoritma Cosine Similarity buatan sendiri di atas data riil Pandas.
- [ ] **Hari 18:** **[App]** Menggabungkan logika di atas untuk membuat rekomendasi item berdasarkan riwayat pencarian pengguna.
- [ ] **Hari 19:** **[App]** Merancang antarmuka CLI (*Command Line Interface*) yang bisa menerima *input* teks dari user.
- [ ] **Hari 20:** **[App]** Uji coba sistem, *refactoring* kode agar modular, dan komit hasil ke Git.

---

## Bagian 2: Probabilitas & Machine Learning Tabular (Hari 21 - 40)

### Minggu 5: Probabilitas Dasar
- [ ] **Hari 21:** **[Math]** Mempelajari metrik pusat: Mean, Median, Mode, Variance, dan Standard Deviation.
- [ ] **Hari 22:** **[Code]** Menulis kode Python murni tanpa `stats` library untuk menghitung semua metrik di atas.
- [ ] **Hari 23:** **[Math]** Konsep Kurva Lonceng (Distribusi Normal), Z-Score, dan dasar Teorema Bayes.
- [ ] **Hari 24:** **[Code]** Melakukan normalisasi skala data (Pembuatan fungsi `StandardScaler` dan `MinMaxScaler` secara manual).
- [ ] **Hari 25:** **[ML]** Transisi menggunakan pipeline *Preprocessing* siap pakai dari `Scikit-Learn`.

### Minggu 6: Regresi & Gradient Descent (Zig-Zag Math)
- [ ] **Hari 26:** **[Math]** Membedah persamaan garis linear ($y = mx + c$) & *Cost Function* (MSE).
- [ ] **Hari 27:** **[Code]** Menulis fungsi evaluasi `Mean Squared Error` murni dengan Python.
- [ ] **Hari 28:** **[ML]** Intuisi *Gradient Descent*: Bagaimana mesin mengubah angka bobot ($m$ dan $c$) sedikit demi sedikit agar eror menurun.
- [ ] **Hari 29:** **[Code]** Menulis *Loop Gradient Descent* manual untuk regresi linear sederhana (tanpa model!).
- [ ] **Hari 30:** **[ML]** Penerapan Regresi Linear menggunakan ekosistem produksi di `Scikit-Learn`.

### Minggu 7: Klasifikasi Tabular
- [ ] **Hari 31:** **[Math]** Konsep Fungsi Sigmoid dan *Log Loss* (Biner 0 dan 1).
- [ ] **Hari 32:** **[ML]** Implementasi Regresi Logistik untuk prediksi klasifikasi ya/tidak.
- [ ] **Hari 33:** **[ML]** Arsitektur berbasis pohon (*Decision Trees*): Mempelajari *Entropy* dan *Information Gain*.
- [ ] **Hari 34:** **[ML]** Memahami *Ensemble Learning* (Bagging) dan menerapkan model *Random Forest*.
- [ ] **Hari 35:** **[ML]** Evaluasi matriks Klasifikasi secara matematis: *Confusion Matrix*, *Precision*, *Recall*, *F1-Score*.

### Minggu 8: Micro-Project 2 (Prediksi Pelanggan/Churn)
- [ ] **Hari 36:** **[ML]** Membersihkan dataset pelanggan riil (*Churn Dataset*).
- [ ] **Hari 37:** **[ML]** Melakukan *Feature Engineering* dan melatih model klasifikasi *Random Forest*.
- [ ] **Hari 38:** **[ML]** Optimalisasi model menggunakan *Hyperparameter Tuning* (GridSearchCV).
- [ ] **Hari 39:** **[App]** Berkenalan dengan framework UI web cepat: **Streamlit**.
- [ ] **Hari 40:** **[App]** Menggabungkan model `Scikit-Learn` ke dalam UI interaktif Streamlit di mana parameter dapat digeser secara visual.

---

## Bagian 3: Kalkulus & Deep Learning Dasar (Hari 41 - 60)

### Minggu 9: Kalkulus Lanjut (Persiapan Deep Learning)
- [ ] **Hari 41:** **[Math]** Konsep dasar Derivatif (Turunan numerik) dan Power Rule.
- [ ] **Hari 42:** **[Code]** Menulis skrip Python turunan limit: `(f(x+h) - f(x))/h`.
- [ ] **Hari 43:** **[Math]** Konsep Mutlak: **Chain Rule** (Aturan Rantai) untuk menghitung turunan dari fungsi bersarang.
- [ ] **Hari 44:** **[Code]** Menulis implementasi *Chain Rule* berlapis di kode murni.
- [ ] **Hari 45:** **[Math]** Pengenalan *Partial Derivatives* untuk model dengan banyak variabel.

### Minggu 10: Saraf Tiruan (Neural Network) Manual
- [ ] **Hari 46:** **[ML]** Anatomi Perceptron & Fungsi Aktivasi non-linear (ReLU, Tanh, Sigmoid).
- [ ] **Hari 47:** **[Code]** Menulis proses **Forward Pass** menggunakan matriks perkalian `NumPy` dari nol.
- [ ] **Hari 48:** **[Code]** Menulis proses **Backward Pass** (Backpropagation) murni menggunakan turunan dari Hari 44.
- [ ] **Hari 49:** **[Code]** Menyatukan alur maju mundur menjadi *Training Loop* yang utuh untuk Neural Network manual.
- [ ] **Hari 50:** **[ML]** Pembuktian model manual berhasil menurunkan *Loss* seiring naiknya iterasi (*Epoch*).

### Minggu 11: Framework Produksi (PyTorch)
- [ ] **Hari 51:** **[ML]** Memulai **PyTorch**: Perbedaan `Tensor` vs `NumPy array` dan pemindahan data ke GPU.
- [ ] **Hari 52:** **[Code]** Paradigma modern: Menjelajahi `torch.autograd` yang menghancurkan kebutuhan menulis turunan manual.
- [ ] **Hari 53:** **[ML]** Struktur kelas dataset kustom melalui `torch.utils.data.Dataset` dan `DataLoader`.
- [ ] **Hari 54:** **[ML]** Mendefinisikan lapisan *Neural Network* menggunakan rancangan kelas `nn.Module`.
- [ ] **Hari 55:** **[ML]** Pola standar PyTorch Training Loop: `optimizer.zero_grad()`, `loss.backward()`, `optimizer.step()`.

### Minggu 12: Micro-Project 3 (Time-Series Neural Net)
- [ ] **Hari 56:** **[ML]** Mempersiapkan dataset historis (runtun waktu / penjualan produk).
- [ ] **Hari 57:** **[ML]** Merancang teknik *Sliding Window* pada Pandas untuk menyiapkan label masa depan (X hari ke belakang prediksi Y besok).
- [ ] **Hari 58:** **[ML]** Membangun Multi-Layer Perceptron (MLP) dengan arsitektur regresi di PyTorch.
- [ ] **Hari 59:** **[ML]** Menjalankan *Training Loop* dan mencatat pergerakan indikator RMSE secara langsung.
- [ ] **Hari 60:** **[App]** Menggunakan *Matplotlib* untuk menggambar garis prediksi (*Model Output*) vs garis aktual.

---

## Bagian 4: Arsitektur Modern & Generative AI (Hari 61 - 80)

### Minggu 13: NLP Dasar & Embeddings
- [ ] **Hari 61:** **[Math]** Paradigma Teks ke Angka: TF-IDF vs *One-Hot Encoding*.
- [ ] **Hari 62:** **[Code]** Membangun matriks TF-IDF (Pembobotan frekuensi dokumen) tanpa library ML.
- [ ] **Hari 63:** **[Math]** Konsep *Embeddings* dan Vektor Ruang Semantik (Kedekatan jarak melambangkan kedekatan arti).
- [ ] **Hari 64:** **[ML]** Pemrosesan teks (Tokenisasi dasar, *Stopwords*, dan *Stemming*).
- [ ] **Hari 65:** **[ML]** Membangun klasifikasi opini teks/sentimen tradisional menggunakan Regresi Logistik di atas matriks kata.

### Minggu 14: Anatomi Transformer & LLM
- [ ] **Hari 66:** **[ML]** Titik Lemah Arsitektur Sequence (RNN/LSTM) dan era Paralelisasi.
- [ ] **Hari 67:** **[Math]** Mekanisme **Self-Attention** (Konsep Vektor Query, Key, Value).
- [ ] **Hari 68:** **[Code]** Implementasi manual *Scaled Dot-Product Attention* (Matriks inti Transformer).
- [ ] **Hari 69:** **[ML]** Peta makro arsitektur Encoder-Decoder (BERT vs GPT).
- [ ] **Hari 70:** **[ML]** Pengenalan ekosistem perpustakaan terbesar AI: Hugging Face `transformers` dan `datasets`.

### Minggu 15: Prompting & Interaksi LLM
- [ ] **Hari 71:** **[Code]** *Loading* Model LLM Ringan (*Pre-trained*) menggunakan pipeline Hugging Face secara lokal.
- [ ] **Hari 72:** **[ML]** Pola desain *Prompt Engineering* (Zero-Shot, Few-Shot, Chain-of-Thought).
- [ ] **Hari 73:** **[ML]** Penyesuaian hyperparameter output model (Temperature, Top-K, Top-P, Repetition Penalty).
- [ ] **Hari 74:** **[Code]** Memaksa LLM untuk selalu meng-output struktur JSON yang valid (*Structured Outputs*).
- [ ] **Hari 75:** **[ML]** Teori Efisiensi Pelatihan Lanjut: Membedah konsep LoRA (*Low-Rank Adaptation*) untuk Fine-Tuning murah.

### Minggu 16: Micro-Project 4 (AI Auto-Writer)
- [ ] **Hari 76:** **[App]** Menulis pipeline Python untuk menelan file input `katalog_spesifikasi.json`.
- [ ] **Hari 77:** **[App]** Mendesain *System Prompt* tegar dan *User Prompt* dinamis dari input file.
- [ ] **Hari 78:** **[Code]** Membangun Loop *Batch Processing* agar AI tidak putus saat men-generate data berjumlah ratusan teks.
- [ ] **Hari 79:** **[App]** Mengarahkan hasil teks LLM ke format siap publikasi (Blog Post berformat HTML/Markdown yang ramah SEO).
- [ ] **Hari 80:** **[App]** Menyisipkan blok *Exception Handling* / Try-Catch untuk mengatasi momen LLM error atau berhalusinasi.

---

## Bagian 5: MLOps, Produksi, & Sistem Skala Besar (Hari 81 - 100)

### Minggu 17: Microservices & API Wrapping
- [ ] **Hari 81:** **[Systems]** Pengenalan **FastAPI**, framework asinkron super cepat pengganti Flask.
- [ ] **Hari 82:** **[Code]** Membuat *route endpoint* dasar GET `/health` untuk mengecek status nyala server.
- [ ] **Hari 83:** **[Systems]** Integrasi *Pydantic Models* untuk menjaga keamanan validasi *Request Body*.
- [ ] **Hari 84:** **[Systems]** Membungkus fungsi *inference* (Prediksi) Model dari Fase 4 ke dalam *endpoint* POST `/predict`.
- [ ] **Hari 85:** **[Systems]** Strategi aman melacak variabel sensitif (*Environment Variables* / `.env`) dan isolasi konfigurasi.

### Minggu 18: Containerization (Docker)
- [ ] **Hari 86:** **[Systems]** Paradigma Virtualisasi: Mengapa model ML rentan *crash* ("Works on my machine!") dan perlunya **Docker**.
- [ ] **Hari 87:** **[Code]** Menulis deklarasi `Dockerfile` spesifik untuk proyek Python, memahami *Layer Caching* untuk `pip install`.
- [ ] **Hari 88:** **[Systems]** Eksperimen Build Images (`docker build`) dan Expose / Mapping Server Ports (`docker run`).
- [ ] **Hari 89:** **[Systems]** Pola Desain Pemisahan (*Decoupling*): Mengapa UI, API Model, dan Database harus dipisah menjadi *container* berbeda.
- [ ] **Hari 90:** **[Code]** Menyusun deklarasi yaml `docker-compose.yml` untuk membangkitkan semua kontainer secara berbarengan.

### Minggu 19: Infrastruktur Skala Enterprise & Antrian
- [ ] **Hari 91:** **[Systems]** Pengenalan **NGINX** (Reverse Proxy) sebagai tameng utama lalu lintas data menuju API AI kita.
- [ ] **Hari 92:** **[Systems]** Membuat pengaman dinding *Rate Limiting* di NGINX (Misal: maksimal 5 *request* per detik per IP).
- [ ] **Hari 93:** **[Systems]** Paradigma asinkronisasi proses ML: Pengenalan Broker Pesan seperti **Redis**.
- [ ] **Hari 94:** **[Code]** Mengonfigurasi arsitektur **Celery** sebagai agen *Worker* yang secara perlahan menjemput antrian job AI dari Redis.
- [ ] **Hari 95:** **[Systems]** Uji Gempuran (*Stress-Test*): Menggunakan modul `Locust` untuk mensimulasikan ribuan klik massal pengguna palsu (*Load Testing*).

### Minggu 20: Capstone Project (End-to-End Production)
- [ ] **Hari 96:** **[App]** Orkestrasi Gabungan Total: Mengonfigurasi `docker-compose` berisi 4 *services* terikat (NGINX, FastAPI UI, FastAPI AI Model, Redis, Celery).
- [ ] **Hari 97:** **[App]** Menyalakan ekosistem produksi. Melakukan pengujian NGINX untuk membuktikan *traffic bot* jahat berhasil ditolak oleh *Rate Limit*.
- [ ] **Hari 98:** **[App]** Mengirimkan data CSV E-commerce massal via UI dan melihat sistem *Worker* sukses menyicil ratusan teks konten menggunakan GPU secara paralel tanpa *downtime*.
- [ ] **Hari 99:** **[App]** Menerapkan strategi pencatatan Log (Logging module) tingkat produksi agar mudah di- *debug* jika AI gagal (*Silent Failure*).
- [ ] **Hari 100:** **[App]** Evaluasi arsitektur utuh, penyempurnaan `README.md` pada repositori Git, dan Anda resmi mencetak gelar **Full-Stack AI Engineer!**
