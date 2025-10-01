# ❌⭕ Tic-Tac-Toe Pro

Selamat datang di **Tic-Tac-Toe Pro**! Ini adalah implementasi modern dari game klasik Tic-Tac-Toe dengan antarmuka grafis yang menarik dan AI yang cerdas menggunakan algoritma Minimax.

## 🌟 Fitur Utama

- **Antarmuka Grafis Modern:** GUI yang responsif dan menarik menggunakan Pygame
- **Multiple Mode Game:**
  - **Player vs Player (PvP):** Dua pemain bergantian
  - **Player vs AI (Mudah):** Melawan AI dengan gerakan random
  - **Player vs AI (Sulit):** Melawan AI dengan algoritma Minimax
- **Pilihan Urutan Bermain:** Untuk mode AI, pilih apakah Anda main duluan (X) atau AI main duluan (O)
- **AI Tak Terkalahkan:** Algoritma Minimax pada level sulit
- **Notifikasi Popup:** Pengumuman pemenang yang elegan
- **Reset Game:** Mulai ulang permainan dengan mudah

## 🎯 Cara Bermain

**Tujuan:** Menyusun tiga simbol ('X' atau 'O') dalam satu baris, baik horizontal, vertikal, maupun diagonal.

**Kontrol:**
- Gunakan **Mouse** untuk mengklik kotak yang ingin diisi
- **Pilih Mode:** Klik mode permainan di menu utama
- **Pilih Urutan:** Untuk mode AI, pilih apakah Anda main duluan atau AI main duluan
- **Reset:** Klik tombol "Menu" untuk kembali atau restart permainan

## ⚙️ Instalasi dan Menjalankan

### 1. Prasyarat
Pastikan Anda sudah menginstal **Python 3** (versi 3.6 atau lebih baru).

### 2. Navigasi ke Folder
```bash
cd tictactoe
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

### 4. Instal Dependensi
```bash
pip install -r requirements.txt
```

**Atau instal manual:**
```bash
pip install pygame
```

### 5. Jalankan Game
```bash
python tictactoe.py
```

### 6. Berpindah ke Tool/Folder Lain
<sub><i>💡 Panduan untuk pengguna pemula</i></sub>

Setelah selesai bermain, Anda bisa berpindah ke tool lain:

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
# Untuk game Pac-Man
cd pacman

# Untuk Text Describer (AI)
cd text_describer

# Untuk Image Describer (AI)  
cd image_describer
```

<sub><i>🔄 Ulangi langkah 3-5 untuk menjalankan tool yang baru</i></sub>

## 🤖 Mode AI

### AI Mudah
- Bermain secara acak
- Cocok untuk pemula atau bermain santai

### AI Sulit (Minimax)
- Menggunakan algoritma Minimax untuk strategi optimal
- Hampir tidak mungkin dikalahkan
- Memberikan tantangan maksimal

## 🎨 Screenshot dan Demo

Game ini menampilkan:
- Interface yang bersih dan modern
- Animasi smooth saat bermain
- Popup notifikasi yang informatif
- Menu yang mudah digunakan

## 🔧 Pengembangan

File `tictactoe.py` terdiri dari:
- **Logika Game:** Implementasi aturan Tic-Tac-Toe
- **AI Minimax:** Algoritma AI yang optimal
- **GUI Pygame:** Antarmuka grafis yang responsif
- **Event Handling:** Penanganan input mouse dan keyboard

## 📝 Lisensi

Proyek ini dibuat untuk tujuan edukasi dan hiburan. Silakan digunakan dan dimodifikasi sesuai kebutuhan.

---

**Selamat bermain! 🎉**