# 🤖 Text Describer - Penerjemah Teks AI

**🌐 Languages:** [🇮🇩 Bahasa Indonesia](#id) | [🇺🇸 English](#en) | [🇯🇵 日本語](#jp)

---

## 🇮🇩 Bahasa Indonesia {#id}

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

---

## 🇺🇸 English {#en}

Welcome to **Text Describer**! A text translation application that uses the power of **Google Generative AI (Gemini)** to translate text from any language to Indonesian with natural and accurate results.

## 🌟 Key Features

- **Universal Translation:** Supports translation from various languages to Indonesian
- **Google Gemini AI:** Uses advanced `gemini-2.5-flash` model
- **Simple GUI Interface:** User-friendly interface with PySimpleGUI
- **Character Counter:** Real-time input limit monitoring
- **Input Validation:** Automatic checking for empty or too long text
- **Error Handling:** Informative error management

## 🎯 How to Use

1. **Enter Text:** Type or paste text you want to translate in the top box
2. **Monitor Characters:** See character counter below (maximum 100,000 characters)
3. **Click Translate:** Press "Translate" button to process
4. **View Results:** Translation will appear in the bottom box in Indonesian

## ⚙️ Installation and Setup

### 1. Prerequisites
- Python 3.6 or newer
- Active internet connection
- Google AI Studio API Key

### 2. Navigate to Folder
```bash
cd text_describer
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
3. Open `text_describer.py` file
4. Replace this line:
```python
API_KEY = "API_KEY_GEMINI_ANDA"  # Replace with your API key
```

### 6. Run Application
```bash
python text_describer.py
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

# For Image Describer (AI)
cd image_describer
```

<sub><i>🔄 Repeat steps 3-6 to run the new tool</i></sub>

---

**Enjoy translating with AI! 🚀**

---

## 🇯🇵 日本語 {#jp}

**テキスト記述者**へようこそ！**Google Generative AI (Gemini)**の力を使用して、あらゆる言語からインドネシア語への自然で正確な翻訳を行うテキスト翻訳アプリケーションです。

## 🌟 主な機能

- **汎用翻訳:** 様々な言語からインドネシア語への翻訳をサポート
- **Google Gemini AI:** 高度な`gemini-2.5-flash`モデルを使用
- **シンプルなGUIインターフェース:** PySimpleGUIを使用したユーザーフレンドリーなインターフェース
- **文字カウンター:** リアルタイム入力制限監視
- **入力検証:** 空または長すぎるテキストの自動チェック
- **エラーハンドリング:** 情報豊富なエラー管理

## 🎯 使用方法

1. **テキスト入力:** 上のボックスに翻訳したいテキストを入力またはペースト
2. **文字数監視:** 下の文字カウンターを確認（最大100,000文字）
3. **翻訳をクリック:** 「翻訳」ボタンを押して処理
4. **結果を表示:** 翻訳が下のボックスにインドネシア語で表示

## ⚙️ インストールとセットアップ

### 1. 前提条件
- Python 3.6以上
- アクティブなインターネット接続
- Google AI Studio APIキー

### 2. フォルダに移動
```bash
cd text_describer
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
3. `text_describer.py`ファイルを開く
4. この行を置き換える:
```python
API_KEY = "API_KEY_GEMINI_ANDA"  # あなたのAPIキーに置き換え
```

### 6. アプリケーション実行
```bash
python text_describer.py
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

# 画像記述者（AI）用
cd image_describer
```

<sub><i>🔄 新しいツールを実行するには手順3-6を繰り返してください</i></sub>

---

**AIでの翻訳をお楽しみください！🚀**