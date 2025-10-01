# 🖼️ Image Describer - Deskripsi Gambar AI

Selamat datang di **Image Describer**! Aplikasi yang menggunakan kekuatan **Google Generative AI (Gemini)** untuk menganalisis dan memberikan deskripsi konten gambar dalam Bahasa Indonesia yang jelas dan detail.

## 🌟 Fitur Utama

- **Analisis Gambar AI:** Menggunakan model `gemini-2.5-flash` untuk computer vision
- **Deskripsi Bahasa Indonesia:** Hasil analisis dalam bahasa yang natural dan mudah dipahami
- **GUI Sederhana:** Interface yang user-friendly dengan PySimpleGUI
- **File Browser:** Mudah memilih file gambar dari komputer
- **Format Support:** Mendukung PNG, JPG, JPEG
- **Error Handling:** Penanganan error yang informatif

## 🎯 Cara Menggunakan

1. **Pilih Gambar:** Klik tombol "Cari Gambar" untuk membuka file explorer
2. **Browse File:** Pilih file gambar (PNG, JPG, JPEG) dari komputer Anda
3. **Konfirmasi Path:** Path file akan muncul di kotak input
4. **Analisis:** Klik "Mulai Deskripsikan" untuk memproses gambar
5. **Lihat Hasil:** Deskripsi gambar akan muncul di area teks bawah

## ⚙️ Instalasi dan Setup

### 1. Prasyarat
- Python 3.6 atau lebih baru
- Koneksi internet aktif
- API Key Google AI Studio

### 2. Navigasi ke Folder
```bash
cd image_describer
```

### 3. Buat Virtual Environment (Disarankan)
```bash
# Buat virtual environment
python -m venv venv

# Aktifkan di Windows
.\venv\Scripts\activate

# Aktifkan di macOS/Linux
source venv/bin/activate
```

### 4. Instal Dependencies
```bash
pip install -r requirements.txt
```

### 5. Setup API Key
1. Buka [Google AI Studio](https://aistudio.google.com/)
2. Daftar/login dan dapatkan API Key gratis
3. Buka file `image_describer.py`
4. Ganti baris berikut:
```python
API_KEY = "API_KEY_GEMINI_ANDA"  # Ganti dengan API key Anda
```

### 6. Jalankan Aplikasi
```bash
python image_describer.py
```

## 📋 Dependencies

File `requirements.txt` berisi:
```
google-generativeai
Pillow
PySimpleGUI
```

## 🔧 Fitur Teknis

### Format Gambar Didukung
- **PNG:** Portable Network Graphics
- **JPG/JPEG:** Joint Photographic Experts Group
- **Transparansi:** Mendukung gambar dengan background transparan

### AI Model
- **Model:** gemini-2.5-flash (optimal untuk computer vision)
- **Analisis:** Deteksi objek, pemandangan, aktivitas, warna, dan konteks
- **Bahasa:** Output dalam Bahasa Indonesia yang natural

### GUI Features
- **File Browser:** Dialog pemilihan file yang mudah
- **Status Feedback:** Indikator "Sedang memproses..." saat analisis
- **Responsive Text:** Area hasil yang dapat di-scroll untuk deskripsi panjang
- **Dark Theme:** Tema gelap yang nyaman untuk mata

## 💡 Tips Penggunaan

1. **Kualitas Gambar:** Gambar dengan resolusi tinggi memberikan analisis lebih detail
2. **Pencahayaan:** Gambar dengan pencahayaan baik menghasilkan deskripsi lebih akurat
3. **Objek Jelas:** Pastikan objek utama dalam gambar terlihat jelas
4. **Context:** AI dapat mengenali konteks dan situasi dalam gambar

## 🔍 Contoh Hasil Analisis

### Foto Pemandangan
*"Ini adalah gambar pemandangan gunung yang indah dengan langit biru cerah. Terlihat puncak gunung tertutup salju putih di kejauhan, dengan pepohonan hijau di latar depan."*

### Foto Hewan
*"Gambar menunjukkan seekor kucing oranye yang sedang tidur nyenyak di atas sofa berwarna abu-abu. Kucing tersebut tampak sangat tenang dan nyaman."*

### Foto Makanan
*"Ini adalah foto sepiring nasi goreng yang terlihat lezat dengan telur mata sapi di atasnya, dilengkapi dengan irisan mentimun dan tomat sebagai garnish."*

## 🛠️ Troubleshooting

### Error File Tidak Ditemukan
- Pastikan file gambar masih ada di lokasi yang dipilih
- Coba pilih ulang file gambar
- Periksa format file (harus PNG, JPG, atau JPEG)

### Error API Key
- Pastikan API key sudah benar dan aktif
- Cek koneksi internet
- Verifikasi quota API belum habis

### Error Analisis Gambar
- Pastikan file gambar tidak corrupt
- Coba dengan gambar yang lebih kecil (< 10MB)
- Periksa format file yang didukung

### Deskripsi Tidak Akurat
- Gunakan gambar dengan kualitas lebih baik
- Pastikan objek dalam gambar terlihat jelas
- Coba dengan pencahayaan yang lebih baik

## 🔧 Pengembangan

### Struktur Kode
- **Konfigurasi API:** Setup Google Generative AI
- **Fungsi describe_image():** Core logic analisis gambar
- **GUI Layout:** Interface PySimpleGUI dengan file browser
- **Event Loop:** Handling user interaction dan file selection

### Customization
Anda dapat memodifikasi:
- **Model AI:** Ganti ke model Gemini lainnya
- **Prompt:** Customize prompt untuk analisis spesifik
- **File Types:** Tambah dukungan format file lain
- **Theme:** Ubah tema dan layout GUI

## 🚀 Pengembangan Lanjutan

### Fitur Potensial
- **Batch Processing:** Analisis multiple gambar sekaligus
- **Export Results:** Simpan hasil analisis ke file
- **Image Filters:** Pre-processing untuk meningkatkan akurasi
- **Advanced Prompts:** Analisis spesifik (objek counting, color analysis, dll)

## 📝 Lisensi

Proyek ini dibuat untuk tujuan edukasi dan pengembangan. Silakan gunakan dan modifikasi sesuai kebutuhan.

---

**Jelajahi dunia gambar dengan AI! 📸✨**