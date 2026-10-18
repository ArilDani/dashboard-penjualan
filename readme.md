# 📊 DigiMart Sales Dashboard

**From Raw Data to Business Insight**

DigiMart Sales Dashboard adalah proyek simulasi analisis data penjualan menggunakan Python yang dikembangkan dengan Streamlit, Pandas, dan Plotly. Dashboard ini membantu pengguna memahami performa penjualan melalui KPI, visualisasi interaktif, serta eksplorasi data transaksi berdasarkan kota dan kategori produk.

Proyek ini merupakan bagian dari simulasi praktik **Data Bridge: From Code to Insight**, yang memperkenalkan alur kerja Data Analyst mulai dari pengolahan data hingga penyajian insight melalui dashboard interaktif.

## 🔗 Live Dashboard

**Dashboard Online:** [https://digimart.streamlit.app/]


## ✨ Features

- **Interactive Filters** — memfilter data berdasarkan kota dan kategori produk.
- **Total Revenue** — menampilkan total pendapatan berdasarkan filter aktif.
- **Units Sold** — menampilkan total unit produk yang terjual.
- **Transactions** — menghitung jumlah transaksi unik berdasarkan `order_id`.
- **Revenue by Category** — membandingkan total pendapatan setiap kategori produk.
- **Units Sold by Product** — membandingkan jumlah unit terjual untuk setiap produk.
- **Daily Revenue Trend** — memvisualisasikan perubahan pendapatan harian.
- **Transaction Details** — menampilkan detail data transaksi sesuai filter.
- **Download Filtered Data** — mengunduh data yang telah difilter dalam format CSV.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Bahasa pemrograman utama |
| Streamlit | Membangun dashboard interaktif |
| Pandas | Pengolahan dan analisis data |
| Plotly Express | Membuat visualisasi data interaktif |

## 📁 Project Structure

```text
dashboard-penjualan/
├── app.py
├── digimart_clean.csv
├── requirements.txt
├── README.md
└── .gitignore
```

**File description:**

- `app.py` — kode utama dashboard.
- `digimart_clean.csv` — dataset penjualan yang digunakan dashboard.
- `requirements.txt` — daftar library Python yang dibutuhkan.
- `README.md` — dokumentasi proyek.
- `.gitignore` — menentukan file atau folder yang tidak perlu dilacak Git.

## 📊 Dataset

Dashboard menggunakan dataset `digimart_clean.csv` yang telah melalui proses pembersihan data.

Kolom yang dibutuhkan oleh aplikasi:

| Column | Description |
|---|---|
| `order_id` | ID transaksi |
| `order_date` | Tanggal transaksi |
| `product` | Nama produk |
| `category` | Kategori produk |
| `quantity` | Jumlah unit terjual |
| `revenue` | Pendapatan transaksi atau baris data |
| `city` | Kota transaksi |

Pastikan dataset memiliki seluruh kolom tersebut dan kolom `revenue` berisi nilai numerik.

## ⚙️ Installation & Setup

### 1. Clone repository

```bash
git clone https://github.com/ArilDani/dashboard-penjualan
cd dashboard-penjualan
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv env
env\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

Pastikan file `requirements.txt` berisi:

```text
streamlit
pandas
plotly
```

Kemudian instal dependensi:

```bash
python -m pip install -r requirements.txt
```

### 4. Run the dashboard

```bash
streamlit run app.py
```

Dashboard akan berjalan secara lokal dan dapat diakses melalui alamat yang ditampilkan di terminal, biasanya `http://localhost:8501`.

## ☁️ Deployment

Dashboard dapat dipublikasikan menggunakan Streamlit Community Cloud.

1. Push seluruh file yang diperlukan ke GitHub.
2. Buka [Streamlit Community Cloud](https://share.streamlit.io/).
3. Buat aplikasi baru dan hubungkan repositori GitHub.
4. Pilih branch dan file utama `app.py`.
5. Klik **Deploy**.
6. Periksa logs jika terjadi error saat proses deployment.
7. Setelah berhasil, tambahkan URL dashboard ke bagian **Live Dashboard** di README ini.

Pastikan `requirements.txt` tersedia di lokasi yang dikenali oleh konfigurasi deployment dan dataset dapat ditemukan menggunakan path yang ditentukan dalam kode.

## 🔍 How to Use

1. Buka dashboard melalui tautan online atau jalankan secara lokal.
2. Pilih kota melalui filter **Select City**.
3. Pilih kategori produk melalui filter **Select Category**.
4. Amati perubahan KPI sesuai filter yang dipilih.
5. Analisis grafik pendapatan berdasarkan kategori, unit terjual berdasarkan produk, dan tren pendapatan harian.
6. Periksa tabel **Transaction Details** untuk melihat data transaksi.
7. Klik **Download Filtered Data** untuk mengunduh data sesuai filter aktif.

## 💡 Business Questions

Dashboard ini dapat digunakan untuk mengeksplorasi pertanyaan bisnis seperti:

- Kategori produk mana yang menghasilkan pendapatan terbesar?
- Produk mana yang memiliki jumlah unit terjual paling tinggi?
- Bagaimana tren pendapatan harian?
- Bagaimana perbedaan penjualan berdasarkan kota?
- Bagaimana komposisi penjualan berubah ketika kategori atau kota difilter?

Hasil visualisasi dapat digunakan untuk menyusun insight awal. Interpretasi tetap perlu mempertimbangkan kualitas data dan konteks bisnis yang tersedia.

## 📌 Notes

- Filter kota dan kategori diterapkan secara bersamaan.
- Total transaksi dihitung berdasarkan jumlah `order_id` unik pada data yang telah difilter.
- Total pendapatan dihitung dari penjumlahan kolom `revenue`.
- Tren harian menggunakan agregasi pendapatan berdasarkan `order_date`.
- Dashboard ini merupakan proyek simulasi pembelajaran dan bukan sistem pelaporan keuangan yang telah diaudit.
- Jangan mengunggah kredensial, token API, atau data sensitif ke repositori publik.

## 👨‍💻 Author

**M. Aril Ardani**

Data Bridge — From Code to Insight

---

*Turning cleaned data into meaningful business insights.*
