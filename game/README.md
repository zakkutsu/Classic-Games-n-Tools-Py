# 🎮 Proyek Game 🎮

Selamat datang di folder proyek game! Folder ini berisi koleksi game yang dibuat menggunakan **Python** dan library **Pygame**.

---

### ⚙️ Instalasi dan Cara Menjalankan (Untuk Semua Game)

Ikuti langkah-langkah ini untuk menyiapkan environment dan menjalankan semua game di dalam folder ini.

**1. Prasyarat**
Pastikan Anda sudah menginstal **Python 3** (versi 3.6 atau lebih baru) di sistem Anda.

**2. Navigasi ke Folder Game**
Dari direktori utama proyek, masuklah ke folder `game`.
```bash
cd game
```

**3. Buat dan Aktifkan Virtual Environment** (Opsional, tapi disarankan)
Sangat disarankan untuk menggunakan *virtual environment* agar library game tidak tercampur dengan instalasi Python sistem Anda.

```bash
# Buat virtual environment
python -m venv venv

# Aktifkan di Windows
.\venv\Scripts\activate

# Aktifkan di macOS/Linux
source venv/bin/activate
```

**4. Instal Dependensi**
Instal library **Pygame** yang dibutuhkan untuk menjalankan semua game.
```bash
pip install pygame
```
> ✅ Setelah langkah-langkah ini selesai, Anda siap untuk menjalankan game di bawah ini.

---

## 🕹️ Daftar Game

### 1. Pac-Man Sederhana 🟡

Ini adalah implementasi sederhana dari game klasik **Pac-Man** yang dibuat menggunakan Python dan library Pygame. Proyek ini mencakup mekanik dasar permainan, animasi karakter, dan beberapa fitur modern.

**Fitur Utama:**
-   **Gameplay Klasik:** Bergerak di dalam labirin, memakan *pellet*, dan menghindari hantu.
-   **Animasi Karakter:** Pac-Man memiliki animasi mulut membuka dan menutup yang dinamis.
-   **AI Hantu Sederhana:** Hantu akan secara aktif mengejar pemain di dalam labirin.
-   **Sistem Skor:** Dapatkan poin untuk setiap *pellet* yang dimakan.
-   **Tombol Reset:** Memulai ulang permainan dengan mudah setelah menang atau kalah.

**Cara Bermain:**
-   **Tujuan:** Makan semua titik (*pellet*) putih di dalam labirin untuk menang.
-   **Kontrol:** Gunakan **Tombol Panah** (Atas, Bawah, Kiri, Kanan) untuk menggerakkan Pac-Man.
-   **Hindari Hantu:** Jangan sampai menyentuh hantu. Jika tersentuh, permainan akan berakhir.

**Menjalankan Game:**
```bash
python pacman_game.py
```

---

### 2. Tic-Tac-Toe ❌⭕

Aplikasi ini adalah implementasi modern dari game **Tic-Tac-Toe** dengan antarmuka visual yang interaktif, beberapa mode permainan, serta lawan AI yang tak terkalahkan menggunakan **algoritma Minimax**.

**Fitur Utama:**
-   **Antarmuka Grafis (GUI)** menggunakan Pygame.
-   **Mode Permainan:** Player vs Player dan Player vs AI (Mudah & Sulit).
-   **AI Cerdas:** Termasuk AI level "Sulit" yang menggunakan algoritma **Minimax**.
-   **Notifikasi Popup** untuk mengumumkan pemenang atau hasil seri.

**Cara Bermain:**
-   **Tujuan:** Menyusun tiga simbol ('X' atau 'O') dalam satu baris (horizontal, vertikal, atau diagonal).
-   **Kontrol:** Gunakan **Mouse** untuk mengklik kotak yang ingin diisi.

**Menjalankan Game:**
```bash
python tictactoe.py
```