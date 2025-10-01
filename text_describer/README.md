# 🤖 Text Describer - Penerjemah Teks AI

Selamat datang di **Text Describer**! Aplikasi penerjemah teks yang menggunakan kekuatan **Google Generative AI (Gemini)** untuk menerjemahkan teks dari bahasa apa pun ke Bahasa Indonesia dengan hasil yang natural dan akurat.

## 🌟 Fitur Utama

- **Penerjemahan Universal:** Mendukung terjemahan dari berbagai bahasa ke Bahasa Indonesia
- **AI Google Gemini:** Menggunakan model `gemini-2.5-flash` yang canggih
- **Antarmuka GUI Sederhana:** Interface yang user-friendly dengan PySimpleGUI
- **Penghitung Karakter:** Monitor batas input secara real-time
- **Validasi Input:** Pengecekan otomatis untuk teks kosong atau terlalu panjang
- **Error Handling:** Penanganan error yang informatif

## 🎯 Cara Menggunakan

1. **Masukkan Teks:** Ketik atau paste teks yang ingin diterjemahkan di kotak atas
2. **Monitor Karakter:** Lihat penghitung karakter di bawah (maksimal 100.000 karakter)
3. **Klik Terjemahkan:** Tekan tombol "Terjemahkan" untuk memproses
4. **Lihat Hasil:** Terjemahan akan muncul di kotak bawah dalam Bahasa Indonesia

## ⚙️ Instalasi dan Setup

### 1. Prasyarat
- Python 3.6 atau lebih baru
- Koneksi internet aktif
- API Key Google AI Studio

### 2. Navigasi ke Folder
```bash
cd text_describer
```

### 3. Buat Virtual Environment (Disarankan)
**Buat virtual environment:**
```bash
python -m venv venv
```

**Aktifkan virtual environment:**

*PowerShell:*
```powershell
.\venv\Scripts\Activate.ps1
```

*Command Prompt:*
```cmd
venv\Scripts\activate.bat
```

*Git Bash:*
```bash
source venv/Scripts/activate
```

### 4. Instal Dependencies
```bash
pip install -r requirements.txt
```

**Atau instal manual jika ada masalah:**
```bash
pip install google-generativeai Pillow
pip install --extra-index-url https://PySimpleGUI.net/install PySimpleGUI
```

### 5. Setup API Key
1. Buka [Google AI Studio](https://aistudio.google.com/)
2. Daftar/login dan dapatkan API Key gratis
3. Buka file `text_describer.py`
4. Ganti baris berikut:
```python
API_KEY = "API_KEY_GEMINI_ANDA"  # Ganti dengan API key Anda
```

### 6. Jalankan Aplikasi
```bash
python text_describer.py
```

### 7. Berpindah ke Tool/Folder Lain
<sub><i>💡 Panduan untuk pengguna pemula</i></sub>

Setelah selesai menggunakan aplikasi, Anda bisa berpindah ke tool lain:

**Keluar dari virtual environment:**
```bash
deactivate
```

**Kembali ke folder utama:**
```bash
cd ..
```

**Pindah ke tool lain, contoh:**
```bash
# Untuk game Tic-Tac-Toe
cd tictactoe

# Untuk game Pac-Man
cd pacman

# Untuk Image Describer (AI)
cd image_describer
```

<sub><i>🔄 Ulangi langkah 3-6 untuk menjalankan tool yang baru</i></sub>

## 📋 Dependencies

File `requirements.txt` berisi:
```
google-generativeai
PySimpleGUI
```

## 🔧 Fitur Teknis

### Validasi Input
- **Batas Karakter:** Maksimal 100.000 karakter per terjemahan
- **Teks Kosong:** Validasi otomatis untuk input kosong
- **Real-time Counter:** Penghitung karakter berubah warna jadi merah jika melebihi batas

### AI Model
- **Model:** gemini-2.5-flash (cepat dan efisien)
- **Prompt Engineering:** Optimized untuk hasil terjemahan terbaik
- **Error Handling:** Penanganan error API yang komprehensif

### GUI Features
- **Responsive Layout:** Interface yang responsif dan mudah digunakan
- **Status Feedback:** Indikator "Sedang menerjemahkan..." saat proses
- **Dark Theme:** Tema gelap yang nyaman untuk mata

## 💡 Tips Penggunaan

1. **Teks Panjang:** Untuk teks sangat panjang, pertimbangkan membagi menjadi beberapa bagian
2. **Bahasa Khusus:** AI dapat menangani bahasa teknis, slang, dan idiom
3. **Format:** Aplikasi mempertahankan struktur paragraf asli
4. **Akurasi:** Hasil terjemahan semakin baik dengan konteks yang jelas

## 🛠️ Troubleshooting

### Error API Key
- Pastikan API key sudah benar dan aktif
- Cek koneksi internet
- Verifikasi quota API belum habis

### Error Koneksi
- Pastikan koneksi internet stabil
- Coba restart aplikasi
- Periksa firewall/antivirus

### Terjemahan Tidak Akurat
- Berikan konteks yang lebih jelas
- Periksa ejaan teks asli
- Coba dengan kalimat yang lebih pendek

## 🔧 Pengembangan

### Struktur Kode
- **Konfigurasi API:** Setup Google Generative AI
- **Fungsi translate_text():** Core logic penerjemahan
- **GUI Layout:** Interface PySimpleGUI
- **Event Loop:** Handling user interaction

### Customization
Anda dapat memodifikasi:
- **Model AI:** Ganti ke model Gemini lainnya
- **Batas Karakter:** Sesuaikan `MAX_CHARS`
- **Prompt:** Customize prompt untuk hasil spesifik
- **Theme:** Ubah tema GUI

## 📝 Lisensi

Proyek ini dibuat untuk tujuan edukasi dan pengembangan. Silakan gunakan dan modifikasi sesuai kebutuhan.

---

**Nikmati pengalaman menerjemahkan dengan AI! 🚀**