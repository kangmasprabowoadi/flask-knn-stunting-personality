# 🚀 Super AI Predictor - PSAS MP1

Super AI Predictor adalah aplikasi web cerdas terintegrasi yang memanfaatkan algoritma **Machine Learning (K-Nearest Neighbors)** untuk melakukan prediksi pada dua domain yang berbeda: medis dan psikologis. Proyek ini dibangun sebagai bagian dari Penilaian Sumatif Akhir Semester (PSAS).

Aplikasi ini dibalut dengan antarmuka **Glassmorphism** yang modern, responsif, dan estetik menggunakan Tailwind CSS.

## ✨ Fitur Utama

1. **🩺 Deteksi Dini Stunting (AI Medika)**
   * Memprediksi status gizi dan tumbuh kembang balita.
   * Input: Umur (Bulan), Jenis Kelamin, dan Tinggi Badan (cm).
   * Output: Klasifikasi status gizi (Normal, Sangat Pendek, Pendek, Tinggi) beserta saran medis preventif.
   
2. **🧠 Analisis Kepribadian (AI Personality)**
   * Memetakan tipe kepribadian pengguna (Ekstrovert/Introvert) berdasarkan data kebiasaan sosial sehari-hari.
   * Input: Waktu sendirian, kehadiran acara sosial, jumlah teman, frekuensi posting sosmed, dll.
   * Output: Visualisasi tipe kepribadian beserta deskripsi analitis.

3. **🎨 Modern UI/UX**
   * Desain *Glassmorphism* tembus pandang yang dinamis.
   * *Loading screen* interaktif dan transisi halaman yang mulus.
   * Latar belakang pemandangan Indonesia yang estetik (Gunung Bromo, Jakarta, Tegalalang Bali).

## 🛠️ Teknologi yang Digunakan

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-Learn (K-Nearest Neighbors), Pandas, Numpy, Joblib
* **Frontend:** HTML5, Tailwind CSS, Lucide Icons

## 📸 Tangkapan Layar (Screenshots)

*(Catatan: Jangan lupa unggah screenshot web kamu ke folder repo, lalu ganti link gambar di bawah ini dengan nama file screenshot kamu)*

* **Menu Utama:** ![Menu Utama](link-gambar-menu-utama.png)
* **Prediksi Stunting:** ![Stunting](link-gambar-stunting.png)
* **Analisis Kepribadian:** ![Personality](link-gambar-personality.png)

## 🚀 Cara Menjalankan Aplikasi di Komputer Lokal

1. Pastikan Python sudah terinstal di komputer Anda.
2. Buka terminal (atau Command Prompt / VS Code Terminal).
3. _Clone_ repositori ini atau ekstrak file proyek ke dalam satu folder.
4. Instal semua *library* yang dibutuhkan dengan menjalankan perintah berikut:
   ```bash
   pip install flask joblib numpy scikit-learn pandas

👨‍💻 Penulis
Prabowo Adi Sanjaya
Kelas: XI PPLG 5
Instansi: SMK Telkom Purwokerto
Proyek Penilaian Sumatif Akhir Semester (PSAS) Mata Pelajaran 1 (MP1)
Dibuat dengan ❤️ dan ☕ untuk menjelajahi potensi Kecerdasan Buatan.
