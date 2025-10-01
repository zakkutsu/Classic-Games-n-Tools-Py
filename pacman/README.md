# 🟡 Pac-Man Klasik

Selamat datang di implementasi **Pac-Man** klasik! Game arcade legendaris ini telah dibangun ulang menggunakan Python dan Pygame dengan fitur-fitur modern yang menarik.

## 🌟 Fitur Utama

- **Gameplay Klasik:** Bergerak di labirin, makan pellet, dan hindari hantu
- **Animasi Karakter:** Pac-Man dengan animasi mulut membuka-tutup yang dinamis
- **AI Hantu Cerdas:** Hantu yang aktif mengejar pemain di dalam labirin
- **Sistem Skor:** Dapatkan poin untuk setiap pellet yang dimakan
- **Kecepatan Dinamis:** Game bertambah cepat seiring waktu
- **Tombol Reset:** Mulai ulang permainan dengan mudah

## 🎯 Cara Bermain

**Tujuan:** Makan semua titik (pellet) putih di dalam labirin untuk memenangkan permainan.

**Kontrol:**
- **Tombol Panah Atas (↑):** Gerak ke atas
- **Tombol Panah Bawah (↓):** Gerak ke bawah  
- **Tombol Panah Kiri (←):** Gerak ke kiri
- **Tombol Panah Kanan (→):** Gerak ke kanan

**Aturan:**
- Hindari menyentuh hantu berwarna (merah, pink, cyan)
- Jika tersentuh hantu, permainan berakhir
- Makan semua pellet untuk menang
- Skor bertambah setiap pellet dimakan

## ⚙️ Instalasi dan Menjalankan

### 1. Prasyarat
Pastikan Anda sudah menginstal **Python 3** (versi 3.6 atau lebih baru).

### 2. Navigasi ke Folder
```bash
cd pacman
```

### 3. Buat Virtual Environment (Opsional tapi Disarankan)
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
pip install pygame
```

### 5. Jalankan Game
```bash
python pacman_game.py
```

## 🎮 Fitur Game

### Animasi Pac-Man
- Mulut membuka dan menutup saat bergerak
- Rotasi karakter sesuai arah pergerakan
- Animasi yang smooth dan responsif

### AI Hantu
- Hantu bergerak secara otomatis mengejar pemain
- Setiap hantu memiliki warna berbeda (merah, pink, cyan)
- Pergerakan yang realistis dalam labirin

### Sistem Kecepatan
- Game dimulai dengan kecepatan normal
- Kecepatan bertambah setiap 3 detik (10% lebih cepat)
- Memberikan tantangan yang semakin meningkat

## 🏗️ Struktur Kode

File `pacman_game.py` terdiri dari:
- **Class Player:** Logika pergerakan dan animasi Pac-Man
- **Class Ghost:** AI dan pergerakan hantu
- **Maze Layout:** Desain labirin yang dapat dikustomisasi
- **Game Loop:** Logika utama permainan dan rendering
- **Collision Detection:** Deteksi tabrakan dan interaksi

## 🎨 Customization

Anda dapat memodifikasi:
- **Layout labirin** di variable `maze_map`
- **Kecepatan game** di konstanta `INITIAL_FPS`
- **Warna karakter** di konstanta warna
- **Ukuran layar** di `SCREEN_WIDTH` dan `SCREEN_HEIGHT`

## 🔧 Pengembangan

Game ini menggunakan:
- **Pygame** untuk grafis dan input handling
- **Python OOP** untuk struktur kode yang bersih
- **Mathematical calculations** untuk AI dan collision detection

## 📝 Tips Bermain

1. **Rencanakan rute** sebelum bergerak
2. **Amati pola pergerakan hantu** untuk menghindarinya
3. **Gunakan sudut labirin** untuk bersembunyi sementara
4. **Bergerak cepat** saat hantu menjauh
5. **Jangan terjebak** di ujung jalan buntu

---

**Selamat bermain dan semoga berhasil mengalahkan hantu! 👻🟡**