# 🖼️ Image Describer - Deskripsi Gambar AI

**🌐 Languages:** [🇮🇩 Bahasa Indonesia](#bahasa-indonesia) | [🇺🇸 English](#english) | [🇯🇵 日本語](#日本語)

---

## 🇮🇩 Bahasa Indonesia

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
3. Buka file `image_describer.py`
4. Ganti baris berikut:
```python
API_KEY = "API_KEY_GEMINI_ANDA"  # Ganti dengan API key Anda
```

### 6. Jalankan Aplikasi
```bash
python image_describer.py
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

# Untuk Text Describer (AI)
cd text_describer
```

<sub><i>🔄 Ulangi langkah 3-6 untuk menjalankan tool yang baru</i></sub>

## 🏷️ Text Tags
`Python`, `Google Gemini AI`, `Computer Vision`, `Image Recognition`, `PySimpleGUI`, `PIL`, `Machine Learning`, `Artificial Intelligence`, `Visual AI`, `Image Processing`

## 🎬 Demo

### Skenario Penggunaan:
1. **Application Launch:** User membuka aplikasi dengan interface file browser
2. **Image Selection:**
   - User klik "Cari Gambar" → File dialog terbuka
   - Navigate ke folder Pictures, pilih foto sunset di pantai (beach_sunset.jpg)
   - File path muncul: "C:\Users\...\Pictures\beach_sunset.jpg"
3. **Analysis Process:**
   - User klik "Mulai Deskripsikan"
   - Status berubah: "Sedang memproses..." dengan progress indicator
   - Google Gemini Vision API menganalisis gambar (≈3-5 detik)
4. **Detailed Results:**
   ```
   "Ini adalah gambar pemandangan pantai yang menakjubkan saat matahari 
   terbenam. Langit berwarna orange dan pink yang dramatis memantulkan 
   cahaya ke permukaan air laut yang tenang. Di latar depan terlihat 
   siluet pohon kelapa yang melengkung, menciptakan frame alami. 
   Beberapa awan tipis tersebar di langit, menambah kedalaman visual. 
   Suasana terlihat sangat damai dan romantis, typical dari golden hour 
   di daerah tropis."
   ```
5. **Multiple Tests:**
   - **Pet Photo:** "Seekor kucing oren berbulu panjang sedang tidur nyenyak..."
   - **Food Image:** "Sepiring nasi goreng yang menggugah selera dengan telur mata sapi..."
   - **Architecture:** "Bangunan modern dengan desain minimalis dan kaca reflektif..."

### Capabilities Showcase:
- **Object Detection:** Identifies main subjects, backgrounds, and details
- **Color Analysis:** Recognizes color schemes and lighting conditions
- **Context Understanding:** Understands scenes, moods, and environments
- **Cultural Awareness:** Describes with Indonesian cultural context
- **Technical Details:** Notes photography aspects like composition and lighting
- **Emotion Recognition:** Captures mood and atmosphere of images

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

---

## 🇺🇸 English

Welcome to **Image Describer**! An application that uses the power of **Google Generative AI (Gemini)** to analyze and provide image content descriptions in clear and detailed Indonesian.

## 🌟 Key Features

- **AI Image Analysis:** Uses `gemini-2.5-flash` model for computer vision
- **Indonesian Descriptions:** Results analysis in natural and easy-to-understand language
- **Simple GUI:** User-friendly interface with PySimpleGUI
- **File Browser:** Easy image file selection from computer
- **Format Support:** Supports PNG, JPG, JPEG
- **Error Handling:** Informative error management

## 🎯 How to Use

1. **Select Image:** Click "Browse Image" button to open file explorer
2. **Browse File:** Select image file (PNG, JPG, JPEG) from your computer
3. **Confirm Path:** File path will appear in input box
4. **Analyze:** Click "Start Describing" to process image
5. **View Results:** Image description will appear in bottom text area

## ⚙️ Installation and Setup

### 1. Prerequisites
- Python 3.6 or newer
- Active internet connection
- Google AI Studio API Key

### 2. Navigate to Folder
```bash
cd image_describer
```

### 3. Create Virtual Environment (Recommended)
**Create virtual environment:**
```bash
python -m venv venv
```

**Activate virtual environment:**

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

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

**Or install manually if there are issues:**
```bash
pip install google-generativeai Pillow
pip install --extra-index-url https://PySimpleGUI.net/install PySimpleGUI
```

### 5. Setup API Key
1. Open [Google AI Studio](https://aistudio.google.com/)
2. Register/login and get free API Key
3. Open `image_describer.py` file
4. Replace this line:
```python
API_KEY = "API_KEY_GEMINI_ANDA"  # Replace with your API key
```

### 6. Run Application
```bash
python image_describer.py
```

### 7. Switch to Other Tools/Folders
<sub><i>💡 Guide for beginners</i></sub>

After finishing using the application, you can switch to other tools:

**Exit virtual environment:**
```bash
deactivate
```

**Return to main folder:**
```bash
cd ..
```

**Move to other tools, example:**
```bash
# For Tic-Tac-Toe game
cd tictactoe

# For Pac-Man game
cd pacman

# For Text Describer (AI)
cd text_describer
```

<sub><i>🔄 Repeat steps 3-6 to run the new tool</i></sub>

---

**Explore the world of images with AI! 📸✨**

---

## 🇯🇵 日本語

**画像記述者**へようこそ！**Google Generative AI (Gemini)**の力を使用して画像コンテンツを分析し、明確で詳細なインドネシア語での説明を提供するアプリケーションです。

## 🌟 主な機能

- **AI画像分析:** コンピュータービジョン用の`gemini-2.5-flash`モデルを使用
- **インドネシア語説明:** 自然で理解しやすい言語での結果分析
- **シンプルなGUI:** PySimpleGUIを使用したユーザーフレンドリーなインターフェース
- **ファイルブラウザ:** コンピューターから簡単に画像ファイルを選択
- **フォーマットサポート:** PNG、JPG、JPEGをサポート
- **エラーハンドリング:** 情報豊富なエラー管理

## 🎯 使用方法

1. **画像を選択:** 「画像を参照」ボタンをクリックしてファイルエクスプローラーを開く
2. **ファイルを参照:** コンピューターから画像ファイル（PNG、JPG、JPEG）を選択
3. **パスを確認:** ファイルパスが入力ボックスに表示される
4. **分析:** 「説明開始」をクリックして画像を処理
5. **結果を表示:** 画像の説明が下のテキストエリアに表示される

## ⚙️ インストールとセットアップ

### 1. 前提条件
- Python 3.6以上
- アクティブなインターネット接続
- Google AI Studio APIキー

### 2. フォルダに移動
```bash
cd image_describer
```

### 3. 仮想環境の作成（推奨）
**仮想環境を作成:**
```bash
python -m venv venv
```

**仮想環境をアクティベート:**

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

### 4. 依存関係のインストール
```bash
pip install -r requirements.txt
```

**または問題がある場合は手動でインストール:**
```bash
pip install google-generativeai Pillow
pip install --extra-index-url https://PySimpleGUI.net/install PySimpleGUI
```

### 5. APIキーのセットアップ
1. [Google AI Studio](https://aistudio.google.com/)を開く
2. 登録/ログインして無料のAPIキーを取得
3. `image_describer.py`ファイルを開く
4. この行を置き換える:
```python
API_KEY = "API_KEY_GEMINI_ANDA"  # あなたのAPIキーに置き換え
```

### 6. アプリケーション実行
```bash
python image_describer.py
```

### 7. 他のツール/フォルダへの切り替え
<sub><i>💡 初心者向けガイド</i></sub>

アプリケーションの使用終了後、他のツールに切り替えることができます：

**仮想環境を終了:**
```bash
deactivate
```

**メインフォルダに戻る:**
```bash
cd ..
```

**他のツールに移動、例:**
```bash
# 三目並べゲーム用
cd tictactoe

# パックマンゲーム用
cd pacman

# テキスト記述者（AI）用
cd text_describer
```

<sub><i>🔄 新しいツールを実行するには手順3-6を繰り返してください</i></sub>

---

**AIで画像の世界を探索してください！📸✨**