# 🎮 Tic-Tac-Toe Pro

Selamat datang di **Tic-Tac-Toe Pro**! Ini adalah implementasi modern dari game klasik Tic-Tac-Toe dengan antarmuka grafis yang menarik dan AI yang cerdas menggunakan algoritma Minimax.

## 🌟 Fitur Utama

- **Antarmuka Grafis (GUI)** yang modern menggunakan Pygame
- **Mode Permainan Beragam:**
  - Player vs Player (PvP)
  - Player vs AI Mudah
  - Player vs AI Sulit (menggunakan algoritma Minimax)
- **AI Tak Terkalahkan** pada mode sulit
- **Notifikasi Popup** untuk mengumumkan pemenang atau hasil seri
- **Animasi dan Efek Visual** yang halus

## 🎯 Cara Bermain

**Tujuan:** Menyusun tiga simbol ('X' atau 'O') dalam satu baris, baik horizontal, vertikal, maupun diagonal.

**Kontrol:**
- Gunakan **Mouse** untuk mengklik kotak yang ingin diisi
- Pilih mode permainan di menu utama
- Klik "Reset" untuk memulai permainan baru

## ⚙️ Instalasi dan Menjalankan

### 1. Prasyarat
Pastikan Anda sudah menginstal **Python 3** (versi 3.6 atau lebih baru).

### 2. Navigasi ke Folder
```bash
cd tictactoe
```

### 3. Buat Virtual Environment (Opsional tapi Disarankan)
```bash
# Buat virtual environment
python -m venv venv

# Aktifkan di Windows
.\venv\Scripts\activate

# Aktifkan di macOS/Linux
source venv/bin/activate
```

### 4. Instal Dependensi
```bash
pip install pygame
```

### 5. Jalankan Game
```bash
python tictactoe.py
```

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