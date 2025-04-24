# PEMROGRAMAN_WEB_ITERA_122140080

# Pertemuan Ke-2


# 📘 JKu (Jadwal Kuliah)
Aplikasi ini merupakan dashboard pribadi sederhana untuk mahasiswa, yang berfungsi untuk mencatat, mengelola, dan melihat **jadwal kuliah** secara interaktif. Dibuat menggunakan HTML5, Tailwind CSS, dan JavaScript ES6+ dengan penyimpanan data berbasis `localStorage`.
**Link Deploy**

https://jadwalkuy.vercel.app/
---

## 🎯 Deskripsi Singkat

Aplikasi ini mempermudah mahasiswa dalam:
- Menambah jadwal kuliah
- Melihat daftar jadwal mingguan
- Mengedit dan menghapus jadwal yang sudah ada
- Menyaring daftar berdasarkan hari

Semua data disimpan secara **lokal di browser** tanpa memerlukan backend, sehingga aplikasi tetap berfungsi meskipun offline.

---

## ✨ Fitur Utama

- ✅ Tambah jadwal kuliah dengan form input
- ✅ Edit jadwal melalui halaman tampilan daftar
- ✅ Hapus jadwal langsung dari daftar
- ✅ Filter jadwal berdasarkan hari (contoh: “Senin”)
- ✅ Simpan data ke `localStorage` agar tidak hilang saat refresh
- ✅ Navigasi antar halaman (Beranda & Jadwal)
- ✅ Antarmuka menggunakan **Tailwind CSS** yang modern dan responsif

---

## 🧠 Fitur ES6+ yang Diimplementasikan

| Fitur ES6+               | Implementasi                                                |
|--------------------------|-------------------------------------------------------------|
| `let` & `const`          | Digunakan di seluruh modul JS                               |
| Arrow Functions (`=>`)   | `renderSchedules`, `setupFilter`, `delay`, dan lainnya     |
| Template Literals        | Untuk render HTML dinamis di `createScheduleItem()`        |
| Async/Await              | `await delay(200)` untuk simulasi proses async             |
| Classes                  | `class Schedule` digunakan untuk struktur data jadwal       |
| Modularisasi             | Menggunakan `import/export` antara file utils dan data      |

### Penjelasan Singkat:
- **`let` dan `const`**: digunakan sesuai fungsinya untuk variabel tetap dan variabel yang berubah.
- **Arrow Functions**: membuat kode lebih ringkas, digunakan untuk callback, event listener, dan render data.
- **Template Literals**: digunakan untuk menampilkan elemen HTML dengan data dinamis secara efisien.
- **Async/Await**: digunakan untuk menunggu simulasi delay sebelum render awal.
- **Class**: digunakan untuk mendefinisikan struktur data `Schedule`.

---

## 🖼️ Screenshot


![Screenshot (83)](https://github.com/user-attachments/assets/6a468eab-5d73-4d8b-b04f-156e6d812c0a)
![Screenshot (85)](https://github.com/user-attachments/assets/9a2094b1-8927-4585-91da-34486250cc8a)
![Screenshot (87)](https://github.com/user-attachments/assets/08e6bbbc-63a5-4d2c-82b9-e57c7c754471)
![Screenshot (88)](https://github.com/user-attachments/assets/3c729faa-1a2e-400e-96c8-1f6f0b883116)

# Pertemuan 3
# Pustakaku 📚

Pustakaku adalah aplikasi pengelolaan koleksi buku yang dibangun menggunakan React. Aplikasi ini memungkinkan pengguna untuk menambahkan, mengedit, dan menghapus daftar buku berdasarkan status seperti dimiliki, sedang dibaca, dan ingin dibeli.
# Link Deploy
 ## https://pustakaku.vercel.app/
 
## Fitur Utama

- Tambah, edit, dan hapus buku
- Filter berdasarkan status (dimiliki, dibaca, ingin dibeli)
- Pencarian buku berdasarkan judul atau penulis
- Statistik buku
- Penyimpanan data menggunakan Firebase Realtime Database
- Penggunaan `localStorage` untuk pencarian dan filter
- Testing unit menggunakan React Testing Library
- Validasi input form
- Menggunakan PropTypes dan React Hooks

## Struktur Proyek

```
pustakaku-app/
  pustakaku-app/
    .gitignore
    package-lock.json
    package.json
    README.md
    node_module
```

> Hanya sebagian struktur folder yang ditampilkan di atas.

## Instalasi

1. Clone repositori atau ekstrak file zip:
   ```bash
   git clone https://github.com/nama-kamu/pustakaku.git
   ```

2. Masuk ke direktori proyek:
   ```bash
   cd pustakaku-app
   ```

3. Install dependensi:
   ```bash
   npm install
   ```

4. Jalankan aplikasi:
   ```bash
   npm start
   ```

5. Jalankan testing:
   ```bash
   npm test
   ```

## Teknologi yang Digunakan

- React
- React Router DOM
- Firebase Realtime Database
- TailwindCSS atau styling CSS biasa
- React Testing Library
- PropTypes
  
## 🖼️ Screenshot
![Screenshot (149)](https://github.com/user-attachments/assets/aa5015ae-350e-4c1b-8e09-032e25fc71bc)
![Screenshot (150)](https://github.com/user-attachments/assets/a507e41e-01c2-425c-a5aa-a6527cd34890)
![Screenshot 2025-04-20 110421](https://github.com/user-attachments/assets/af21a78d-448a-44eb-9c6a-c6d516cfeea8)
![Screenshot (151)](https://github.com/user-attachments/assets/df4b47df-31a0-44e6-b1df-8bab9f64c061)
![Screenshot (155)](https://github.com/user-attachments/assets/b6a4a2ad-e303-4b9a-a922-bc3c123b727e)
![Screenshot (148)](https://github.com/user-attachments/assets/3214b08b-3971-40c5-87e0-42b964f05d1a)
![Screenshot (153)](https://github.com/user-attachments/assets/3788b5c2-009d-4998-895e-d03afc7fc9f1)




# 📘 Prakitum Pertemuan 4

# Kumpulan program Python sederhana untuk menyelesaikan berbagai permasalahan umum seperti kalkulasi BMI,
# penghitungan nilai mahasiswa, dan perhitungan luas & keliling bangun datar.

# 📁 Daftar File

## 1. bmi_no1.py
 Program untuk menghitung Body Mass Index (BMI) berdasarkan input berat dan tinggi badan.
 Otomatis menyesuaikan jika tinggi dimasukkan dalam satuan cm.
 - BMI < 18.5: Berat badan kurang
 - 18.5 ≤ BMI < 25: Berat badan normal
 - 25 ≤ BMI < 30: Berat badan berlebih
 - BMI ≥ 30: Obesitas

## 2. nilai_mahasiswa_no2.py
- Menghitung dan merekap nilai akhir mahasiswa dari UTS, UAS, dan Tugas.
- Menampilkan grade, serta mahasiswa dengan nilai tertinggi dan terendah.

## 3. main_no3.py & mtk_no3.py
### Program kalkulator bangun datar interaktif:
 - Persegi
 - Persegi panjang
 - Lingkaran
 - Konversi suhu (Celsius ke Fahrenheit dan Kelvin)
 - Bonus: Belah ketupat, Segitiga

# Struktur Penggunaan:
Program utama: main_no3.py
Modul fungsi matematika: mtk_no3.py

# 🚀 Cara Menjalankan
python bmi_no1.py              : Kalkulasi BMI
python nilai_mahasiswa_no2.py  : Nilai mahasiswa
python main_no3.py             : Kalkulator bangun datar

# ✅ Requirement
- Python 3.x
- Tidak membutuhkan library eksternal

## Kontributor

- Nama: Maulina Ayu S
- Mata Kuliah: Praktikum Pemrograman Web




