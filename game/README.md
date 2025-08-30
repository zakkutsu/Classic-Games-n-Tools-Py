# Proyek Game Tic-Tac-Toe

Repositori ini berisi dua implementasi game Tic-Tac-Toe menggunakan Python: versi klasik berbasis konsol dan versi modern dengan antarmuka grafis (GUI) yang kaya fitur.

-----

## 📜 **Tic-Tac-Toe Pro (GUI)**

### **Tujuan**

Aplikasi ini bertujuan untuk menghadirkan pengalaman bermain Tic-Tac-Toe yang lengkap dan modern. Dibangun dengan `Pygame`, game ini menyediakan antarmuka visual yang interaktif, beberapa mode permainan (Player vs Player dan Player vs AI), serta lawan AI dengan tingkat kesulitan yang dapat diatur, termasuk AI yang tak terkalahkan menggunakan algoritma Minimax.

### **Dokumentasi**

Skrip `tic_tac_toe_gui.py` terdiri dari beberapa bagian utama:

1.  **Konfigurasi Pygame**: Menginisialisasi library Pygame, mengatur konstanta seperti ukuran layar, warna, dan font yang akan digunakan di seluruh aplikasi.
2.  **Fungsi-Fungsi Game**: Berisi logika inti permainan seperti `draw_lines` untuk menggambar papan, `draw_figures` untuk menampilkan 'X' dan 'O', `check_win` untuk mendeteksi kemenangan, dan `restart_game` untuk memulai ulang.
3.  **Logika AI (Kecerdasan Buatan)**: Terdapat dua level AI. Level **"Mudah"** akan memilih langkah secara acak, sedangkan level **"Sulit"** mengimplementasikan **algoritma Minimax** untuk menganalisis semua kemungkinan langkah dan memilih yang paling optimal, membuatnya tidak mungkin untuk dikalahkan.
4.  **Antarmuka GUI**: Dibangun dengan `Pygame`, antarmuka ini mengelola semua elemen visual, mulai dari menu utama untuk pemilihan mode, papan permainan interaktif, hingga *popup window* yang muncul saat permainan berakhir untuk menampilkan pemenang atau hasil seri.

### **Preview Singkat**

Versi canggih dari Tic-Tac-Toe dengan antarmuka grafis, mode permainan yang fleksibel, dan AI yang sangat menantang untuk dilawan.

### **Tampilan Aplikasi**

Aplikasi ini adalah game desktop mandiri. Pengguna akan disambut oleh menu utama untuk memilih mode permainan. Layar permainan utama menampilkan papan 3x3 di mana pemain dapat mengklik untuk menempatkan simbol mereka. Saat permainan selesai, sebuah popup akan muncul di tengah layar yang mengumumkan hasilnya dan menawarkan opsi untuk bermain lagi atau kembali ke menu.

### **Text Tag**

`Python`, `Pygame`, `AI`, `Game Development`, `Minimax Algorithm`, `GUI`

### **Demo**

Pengguna menjalankan aplikasi dan disambut oleh menu utama. Ia memilih mode "Player vs AI (Sulit)". Permainan dimulai, menampilkan papan 3x3 yang kosong. Pengguna (sebagai 'X') mengklik sebuah kotak, dan AI (sebagai 'O') secara otomatis merespons dengan langkah terbaiknya. Setelah beberapa giliran, AI berhasil menyusun tiga 'O' dalam satu baris. Seketika, sebuah popup muncul di layar dengan pesan "Pemain 'O' Menang\!" beserta tombol "Restart" dan "Menu".

-----

## Console **Tic-Tac-Toe Klasik (Konsol)**

### **Tujuan**

Aplikasi ini bertujuan untuk menyediakan implementasi dasar dari game Tic-Tac-Toe yang berjalan sepenuhnya di dalam terminal atau konsol. Fokus utamanya adalah pada logika inti permainan tanpa ketergantungan pada library grafis eksternal, menjadikannya proyek yang bagus untuk memahami dasar-dasar algoritma game.

### **Dokumentasi**

Skrip `tic_tac_toe_konsol.py` memiliki struktur berikut:

1.  **Representasi Papan**: Papan permainan direpresentasikan sebagai struktur data sederhana, seperti list dua dimensi, yang menyimpan status setiap kotak ('X', 'O', atau kosong).
2.  **Fungsi Inti**: Terdiri dari fungsi-fungsi esensial seperti `print_board()` untuk menampilkan kondisi papan saat ini di konsol, `check_win()` untuk memvalidasi kondisi kemenangan setelah setiap langkah, dan `check_draw()` untuk mendeteksi permainan seri.
3.  **Loop Permainan Utama**: Sebuah `while loop` menjadi mesin utama game. Loop ini secara terus-menerus menampilkan papan, meminta input dari pemain saat ini, memvalidasi input tersebut, memperbarui papan, dan memeriksa apakah permainan telah berakhir.

### **Preview Singkat**

Pengalaman bermain Tic-Tac-Toe klasik berbasis teks, langsung di dalam terminal Anda, sempurna untuk nostalgia dan pembelajaran.

### **Tampilan Aplikasi**

Aplikasi ini berjalan di terminal. Papan permainan ditampilkan menggunakan karakter teks (misalnya, `| X | O | |`). Pemain berinteraksi dengan memasukkan koordinat baris dan kolom melalui keyboard. Setiap status, giliran, dan hasil permainan akan dicetak sebagai output teks di konsol.

### **Text Tag**

`Python`, `Console Game`, `Terminal`, `Game Logic`, `Beginner Project`

### **Demo**

Pengguna menjalankan skrip dari terminal. Papan kosong 3x3 langsung tercetak. Sebuah prompt muncul: `Giliran Pemain X. Masukkan baris dan kolom (0-2):`. Pemain mengetik `0 0` dan menekan Enter. Layar dibersihkan dan papan yang diperbarui muncul dengan 'X' di pojok kiri atas. Prompt berikutnya muncul untuk Pemain O. Permainan ini berlanjut hingga terminal mencetak pesan "Selamat, Pemain X menang\!" atau "Permainan Seri\!".

-----

## ⚙️ **Cara Instalasi dan Menjalankan**

Ikuti langkah-langkah berikut untuk menginstal dependensi yang diperlukan dan menjalankan kedua aplikasi.

### **0. Prasyarat**

Pastikan Anda sudah menginstal **Python** (versi 3.6 atau lebih baru) di sistem Anda.

### **1. Buka Folder Proyek**

Buka Command Prompt atau Terminal, lalu navigasikan ke folder tempat Anda menyimpan file `tic_tac_toe_gui.py` dan `tic_tac_toe_konsol.py`.

  * **Navigasi ke Folder:**
    ```bash
    cd path/ke/folder/proyek
    ```

### **2. Instalasi Library (Hanya untuk Versi GUI)**

Versi konsol tidak memerlukan instalasi apa pun. Untuk versi GUI, disarankan untuk menggunakan *virtual environment*.

  * **Buat Virtual Environment:**

    ```bash
    python -m venv venv
    ```

  * **Aktifkan Virtual Environment:**

      * Di Windows:
        ```bash
        venv\Scripts\activate
        ```
      * Di MacOS/Linux:
        ```bash
        source venv/bin/activate
        ```

  * **Install library Pygame:**

    ```bash
    pip install pygame
    ```

    *(Ini adalah satu-satunya library yang dibutuhkan untuk menjalankan versi GUI).*

### **3. Jalankan Aplikasi**

Pastikan Anda berada di direktori yang benar dan virtual environment (jika digunakan) sudah aktif.

  * **Untuk menjalankan versi konsol:**

    ```bash
    python tic_tac_toe_konsol.py
    ```

  * **Untuk menjalankan versi GUI:**

    ```bash
    python tic_tac_toe_gui.py
    ```

Sebuah jendela aplikasi (untuk versi GUI) atau output di terminal (untuk versi konsol) akan muncul sesuai dengan skrip yang Anda jalankan.