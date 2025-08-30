# README.md-----

# Proyek AI Deskripsi Gambar & Teks

Repositori ini berisi dua aplikasi Python sederhana yang memanfaatkan Google Generative AI untuk melakukan tugas-tugas spesifik: mendeskripsikan gambar dan menerjemahkan teks. Keduanya dibangun dengan antarmuka pengguna grafis (GUI) yang simpel menggunakan PySimpleGUI.

-----

## 📜 **Text Describer (Penerjemah Teks)**

### **Tujuan**

Aplikasi ini bertujuan untuk menyediakan alat penerjemah teks yang mudah digunakan. Pengguna dapat memasukkan teks dalam bahasa apa pun, dan aplikasi akan menggunakan model `gemini-1.5-flash` dari Google AI untuk menerjemahkannya ke dalam Bahasa Indonesia yang alami dan jelas.

### **Dokumentasi**

Skrip `text_describer.py` terdiri dari tiga bagian utama:

1.  **Konfigurasi AI**: Menginisialisasi model `gemini-1.5-flash` dengan kunci API yang disediakan. Terdapat penanganan error jika kunci API tidak valid atau koneksi internet bermasalah.
2.  **Fungsi `translate_text`**: Mengirim teks input dari pengguna ke Google AI dengan *prompt* yang spesifik untuk meminta hasil terjemahan saja, tanpa tambahan lain. Fungsi ini juga menangani validasi input seperti teks kosong atau teks yang melebihi batas 50.000 karakter.
3.  **Antarmuka GUI**: Dibangun dengan `PySimpleGUI`, jendela aplikasi menyediakan dua area teks (untuk input dan output), tombol "Terjemahkan" dan "Keluar", serta penghitung karakter dinamis yang berubah warna menjadi merah jika input melebihi batas.

### **Preview Singkat**

Aplikasi ini memiliki jendela sederhana di mana Anda bisa mengetik atau menempelkan teks, menekan tombol, dan melihat hasilnya langsung di bawahnya.

### **Isi Web**

Aplikasi ini dirancang sebagai *desktop tool* mandiri. Ia memiliki dua kolom utama: satu untuk memasukkan teks yang ingin diterjemahkan dan satu lagi untuk menampilkan hasil terjemahan dari AI. Terdapat juga penghitung karakter untuk memantau batas input.

### **Text Tag**

`Python`, `Google Gemini`, `AI`, `Text Translation`, `PySimpleGUI`, `API`

### **Demo**

Pengguna membuka aplikasi, memasukkan paragraf dalam Bahasa Inggris ke dalam kotak teks atas. Saat mereka mengetik, penghitung karakter di bawahnya akan bertambah. Setelah selesai, mereka mengklik tombol "Terjemahkan". Kotak teks bawah yang tadinya kosong akan menampilkan status "Sedang menerjemahkan..." sejenak, lalu digantikan dengan hasil terjemahan paragraf tersebut dalam Bahasa Indonesia.

-----

## 🖼️ **Image Describer (Deskripsi Gambar)**

### **Tujuan**

Aplikasi ini berfungsi sebagai alat untuk menganalisis dan mendeskripsikan konten sebuah gambar. Pengguna dapat memilih file gambar dari komputer mereka, dan aplikasi akan menggunakan model `gemini-2.5-flash` untuk menghasilkan deskripsi singkat dan jelas tentang apa yang ada di dalam gambar tersebut dalam Bahasa Indonesia.

### **Dokumentasi**

Skrip `image_describer.py` memiliki struktur berikut:

1.  **Konfigurasi AI**: Sama seperti penerjemah teks, skrip ini mengonfigurasi akses ke Google AI menggunakan kunci API.
2.  **Fungsi `describe_image`**: Membuka file gambar yang dipilih pengguna menggunakan library `Pillow`, kemudian mengirimkannya bersama *prompt* ke model AI untuk meminta deskripsi. Fungsi ini juga melakukan validasi untuk memastikan file gambar benar-benar ada.
3.  **Antarmuka GUI**: Jendela aplikasi berisi input teks untuk menampilkan path file, tombol "Cari Gambar" untuk membuka file explorer, tombol "Mulai Deskripsikan", dan area teks untuk menampilkan hasil deskripsi dari AI.

### **Preview Singkat**

Aplikasi ini memungkinkan Anda memilih sebuah file gambar, dan AI akan memberitahu Anda apa yang ada di dalam gambar tersebut.

### **Isi Web**

Aplikasi ini adalah utilitas desktop. Tampilan utamanya memiliki tombol untuk memilih file gambar dari komputer. Setelah gambar dipilih, path file akan muncul di kotak input. Dengan menekan tombol proses, deskripsi yang dihasilkan AI akan muncul di area teks di bagian bawah jendela.

### **Text Tag**

`Python`, `Google Gemini`, `AI`, `Image Recognition`, `Computer Vision`, `PySimpleGUI`

### **Demo**

Pengguna mengklik tombol "Cari Gambar" dan memilih foto seekor kucing yang sedang tidur di sofa. Path file gambar tersebut muncul di aplikasi. Pengguna kemudian menekan "Mulai Deskripsikan". Setelah beberapa saat, teks di bawahnya akan berubah dari "Sedang memproses..." menjadi deskripsi seperti, "Ini adalah gambar seekor kucing oranye yang sedang tidur nyenyak di atas sofa berwarna abu-abu."

-----

## ⚙️ **Cara Instalasi dan Menjalankan**

Ikuti langkah-langkah berikut untuk menginstal dependensi yang diperlukan dan menjalankan kedua aplikasi.

### **0. Buka Folder dari file yang akan dijalankan**

Buka folder tempat Anda menyimpan file `text_describer.py` dan `image_describer.py`.

  * **Navigasi ke Folder:**
    ```bash
    cd belajar-python/translate
    ```

### **1. Instalasi Library**

Buka Command Prompt atau Terminal dan jalankan perintah berikut satu per satu:

  * **Install Virtual Environment:**
  
    ```bash
    python -m venv venv
    ```

    *(Ini adalah langkah pertama untuk menginstall virtual environment).*

  * **Buka Virtual Environment:**

    ```bash
    source venv/Scripts/activate
    ```

    *(Ini adalah langkah untuk menggunakan virtual environment).*

  * **Install library Google Generative AI:**

    ```bash
    pip install google-generativeai
    ```

    *(Ini adalah library resmi untuk berkomunikasi dengan AI Google).*

  * **Install library Pillow:**

    ```bash
    pip install Pillow
    ```

    *(Ini digunakan untuk membuka dan memanipulasi file gambar untuk `image_describer.py`).*

  * **Install library PySimpleGUI:**

    ```bash
    python -m pip install --upgrade --extra-index-url https://PySimpleGUI.net/install PySimpleGUI
    ```

    *(Ini digunakan untuk membuat jendela aplikasi yang simpel dengan tombol dan teks).*

  * **Jika salah install, gunakan perintah berikut:**
    ```bash
    python -m pip install --force-reinstall --extra-index-url https://PySimpleGUI.net/install PySimpleGUI
    ```

     *(Ini digunakan jika instalasi sebelumnya salah).*

### **2. Ganti Kunci API**

Dapatkan kunci API Anda dari **Google AI Studio**. Setelah itu, buka kedua file (`text_describer.py` dan `image_describer.py`) dan cari baris berikut:

```python
API_KEY = "ENTER YOUR API KEY HERE" # Ganti dengan kunci Anda
```

Ganti nilai string di dalam tanda kutip dengan kunci API yang sudah Anda miliki.

### **3. Jalankan Aplikasi**

Buka Command Prompt atau Terminal, lalu navigasikan ke folder tempat Anda menyimpan file-file ini menggunakan perintah `cd`.

  * **Untuk menjalankan penerjemah teks:**

    ```bash
    python text_describer.py
    ```

  * **Untuk menjalankan pendeskripsi gambar:**

    ```bash
    python image_describer.py
    ```

Sebuah jendela aplikasi akan muncul sesuai dengan skrip yang Anda jalankan.