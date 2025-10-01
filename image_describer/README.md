# 🖼️ Image Describer - Analisis Gambar AI Modern

**🌐 Languages:** [🇮🇩 Bahasa Indonesia](#bahasa-indonesia) | [🇺🇸 English](#english) | [🇯🇵 日本語](#日本語)

---

## 🇮🇩 Bahasa Indonesia

Selamat datang di **Image Describer**! Aplikasi analisis gambar modern yang menggunakan kekuatan **Google Generative AI (Gemini Vision)** dengan interface **Flet** yang elegan untuk menganalisis dan memberikan deskripsi detail konten gambar dalam Bahasa Indonesia.

## 🌟 Fitur Utama

### 🎨 **Modern UI & UX**
- **Dark theme elegan** yang nyaman untuk mata
- **Responsive design** dengan layout yang adaptive  
- **Color-coded interface:** Purple untuk file picker, Green untuk analisis
- **Modern typography** dengan emoji dan proper spacing

### 🚀 **AI Vision & Performance**
- **Google Gemini Vision AI** menggunakan model `gemini-2.5-flash` untuk computer vision
- **Advanced image analysis** dengan deskripsi detail dan informatif
- **Smart error handling** dengan feedback yang informatif
- **Fast rendering** dan smooth animations

### 📊 **Enhanced Features**
- **File picker modern:** Dialog file picker yang user-friendly
- **Real-time file info:** Monitor nama file, ukuran, dan format
- **Progress indicator:** Visual feedback dengan progress ring
- **Status tracking:** Real-time status dengan emoji dan warna
- **File validation:** Validasi format dan ukuran file otomatis
- **Clear function:** Reset semua field dengan satu klik
- **Modern notifications:** Snackbar notifications yang tidak mengganggu

### ✅ **Smart Validation**
- **Format support:** PNG, JPG, JPEG, GIF, WebP
- **File size limit:** Maksimal 10MB dengan warning visual
- **Path validation:** Pengecekan otomatis untuk file yang valid
- **Error feedback:** Pesan error yang jelas dan actionable

## 🚀 Quick Start

### 1. **Instalasi Cepat**
```bash
pip install flet google-generativeai Pillow requests
```

### 2. **Setup API Key**
1. Buka [Google AI Studio](https://aistudio.google.com/)
2. Daftar/login dan dapatkan API Key gratis
3. Buka file `image_describer.py`
4. Ganti baris berikut:
```python
API_KEY = "API_KEY_GEMINI_ANDA"  # Ganti dengan API key Anda
```

### 3. **Jalankan Aplikasi**
```bash
python image_describer.py
```

## ⚙️ Instalasi dan Setup Lengkap

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

**Atau instal manual:**
```bash
pip install flet google-generativeai Pillow requests
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
# Untuk Text Describer (AI)
cd text_describer

# Untuk game Tic-Tac-Toe
cd tictactoe

# Untuk game Pac-Man
cd pacman
```

<sub><i>🔄 Ulangi langkah 3-6 untuk menjalankan tool yang baru</i></sub>

## 🎯 Cara Menggunakan

### **Interface Modern**
1. **Header Section:** Title dan info aplikasi dengan styling elegan
2. **File Section:** Path display dan file picker dengan validasi real-time
3. **Action Section:** Tombol analisis dengan progress indicator
4. **Statistics Panel:** Real-time monitoring file info dan status
5. **Output Section:** Text field untuk hasil analisis detail
6. **Control Section:** Tombol clear dan info panel

### **Workflow Penggunaan**
1. **Pilih Gambar:** Klik tombol "📂 Pilih Gambar" untuk membuka file picker
2. **Validasi File:** Sistem otomatis validasi format dan ukuran file
3. **Monitor Info:** Lihat informasi file (nama, ukuran, format) di panel
4. **Analisis:** Klik tombol "🔍 Analisis Gambar"
5. **Visual Feedback:** Progress ring muncul, status berubah ke "Memproses..."
6. **Hasil:** Deskripsi detail muncul dengan notification sukses
7. **Clear (Optional):** Gunakan tombol "🗑️ Bersihkan" untuk reset

## 🏷️ Text Tags
`Python`, `Flet`, `Google Gemini Vision AI`, `Computer Vision`, `Image Analysis`, `Modern UI`, `Dark Theme`, `AI`, `Machine Learning`, `Image Processing`, `OCR`, `Visual Recognition`, `Responsive Design`

## 🎬 Demo

### **Skenario Penggunaan Lengkap:**

#### 1. **Modern App Launch**
- User membuka aplikasi dan melihat interface dark theme yang elegan
- Header menampilkan "🖼️ Image Describer AI - Modern Edition"
- Layout responsif dengan file picker yang modern

#### 2. **File Selection Process**
- User klik tombol "📂 Pilih Gambar" dengan styling purple yang menarik
- Dialog file picker muncul dengan filter untuk format gambar
- User memilih foto landscape pemandangan gunung (landscape.jpg, 2.3MB)

#### 3. **Real-time File Validation**
- File path ditampilkan di text field: `C:\Users\Photos\landscape.jpg`
- File info update: "📄 landscape.jpg | 📏 2.30 MB | 🔧 .JPG"
- Statistics panel update: "Format: .JPG | 2.3MB"
- Tombol "🔍 Analisis Gambar" menjadi aktif (hijau)

#### 4. **Modern Analysis Process**
- User klik tombol "🔍 Analisis Gambar" dengan hover effects
- Progress ring muncul dengan smooth animation
- Text berubah: "Sedang menganalisis gambar..."
- Status panel: "Memproses..." dengan warna orange
- UI tetap responsive, tidak freeze

#### 5. **Detailed AI Analysis Results**
- Green snackbar notification: "✅ Analisis gambar berhasil!"
- Hasil analisis detail muncul:
```
"Gambar ini menampilkan pemandangan gunung yang menakjubkan dengan puncak yang tertutup salju. 
Di latar depan terdapat danau yang tenang dengan permukaan air yang memantulkan bayangan gunung. 
Langit berwarna biru cerah dengan awan putih yang bergerak, menciptakan kontras yang indah 
dengan warna hijau pepohonan di sekitar danau. Komposisi foto ini sangat seimbang dengan 
penggunaan rule of thirds yang baik. Pencahayaan alami memberikan nuansa yang hangat dan 
menenangkan, menghadirkan suasana yang damai dan menyegarkan mata."
```

#### 6. **Enhanced Result Display**
- Status panel: "✅ Berhasil" dengan warna hijau
- Output info: "✅ Analisis selesai | 487 karakter"
- Result length monitoring untuk tracking productivity
- Hasil deskripsi yang natural dengan detail yang komprehensif

#### 7. **Advanced Features Demo**
- **File Validation:** User coba upload file .txt → error message "Format file tidak didukung"
- **Size Validation:** User coba upload file 15MB → warning "Ukuran file terlalu besar"
- **Clear Function:** User klik "🗑️ Bersihkan" → semua field reset dengan smooth transition
- **Error Recovery:** Jika API error → red snackbar dengan troubleshooting tips

### **Fitur Interaktif:**
- **Smart File Picker:** Filter otomatis untuk format gambar yang didukung
- **Real-time Validation:** Validasi file format dan size dengan visual feedback
- **Progressive Enhancement:** UI yang merespons setiap tahap proses
- **Error Recovery:** Actionable error messages dengan solusi yang jelas
- **Detailed Analysis:** Deskripsi yang comprehensive dan informatif
- **Responsive Design:** Adaptive layout untuk berbagai screen size

## 📋 Dependencies

File `requirements.txt` berisi:
```
flet>=0.21.0
google-generativeai>=0.3.0
Pillow>=10.0.0
requests>=2.31.0
```

## 🔧 Fitur Teknis

### **Modern Architecture**
- **Flet Framework:** Cross-platform modern UI framework
- **Event-driven:** Reactive programming dengan callback functions
- **Component-based:** Modular UI components dengan proper separation
- **State Management:** Efficient state updates dengan page.update()

### **Computer Vision Integration**
- **Model:** gemini-2.5-flash dengan vision capabilities
- **Image Processing:** PIL/Pillow untuk preprocessing dan validation
- **Format Support:** PNG, JPG, JPEG, GIF, WebP
- **Size Optimization:** Smart file size validation (max 10MB)

### **AI Analysis Features**
- **Detailed Description:** Comprehensive object dan scene analysis
- **Color Analysis:** Color composition dan visual elements
- **Activity Recognition:** Scene context dan situation analysis
- **Technical Details:** Format, composition, dan artistic elements

### **Performance Optimizations**
- **Lazy Loading:** Components dimuat sesuai kebutuhan
- **Efficient Image Handling:** Optimized image loading dan processing
- **Memory Management:** Proper cleanup dan resource management
- **Responsive File Operations:** Non-blocking file operations

### **UI/UX Features**
- **Dark Theme:** Modern dark theme yang konsisten
- **Color System:** Systematic color coding (Purple: files, Green: analysis)
- **File Picker Integration:** Native file picker dengan proper filtering
- **Progress Feedback:** Real-time progress indicators
- **Error Visualization:** Color-coded error states dan recovery

## 💡 Tips Penggunaan

### **Optimal Usage**
1. **File Quality:** Gunakan gambar dengan resolusi yang baik untuk analisis terbaik
2. **Format Preference:** JPG/PNG memberikan hasil analisis yang optimal
3. **File Size:** Gambar 1-5MB memberikan balance antara quality dan speed
4. **Content Types:** AI dapat menganalisis landscape, objects, people, text dalam gambar

### **Advanced Features**
1. **Batch Analysis:** Gunakan clear function untuk workflow yang efficient
2. **Error Recovery:** Perhatikan color-coded feedback untuk troubleshooting
3. **Performance:** Monitor file size untuk optimal processing speed
4. **Quality:** Gambar yang clear dan well-lit memberikan analisis yang lebih detail

## 🛠️ Troubleshooting

### **Common Issues**

#### **API Key Errors**
- **Symptom:** Error dialog saat launch
- **Solution:** Verify API key di Google AI Studio, check internet connection
- **Prevention:** Test API key sebelum deployment

#### **File Format Issues**
- **Symptom:** "Format file tidak didukung" message
- **Solution:** Gunakan format PNG, JPG, JPEG, GIF, atau WebP
- **Recovery:** Convert file ke format yang didukung

#### **File Size Issues**
- **Symptom:** "Ukuran file terlalu besar" warning
- **Solution:** Compress image atau gunakan file < 10MB
- **Optimization:** Resize image maintain aspect ratio

#### **Analysis Quality**
- **Symptom:** Deskripsi yang kurang detail
- **Solution:** Gunakan gambar dengan resolusi dan lighting yang baik
- **Enhancement:** Pilih gambar dengan content yang jelas dan fokus

### **Advanced Debugging**
- **UI Issues:** Check Flet version compatibility
- **API Issues:** Monitor API quotas dan rate limits  
- **Performance:** Use system monitor untuk resource usage
- **Image Issues:** Validate image integrity dengan image viewers

## 🔧 Customization & Development

### **Theme Customization**
```python
# Ubah theme mode
page.theme_mode = ft.ThemeMode.LIGHT  # atau DARK, SYSTEM

# Custom colors
page.bgcolor = ft.colors.GREY_900
```

### **Window Customization**
```python
# Ukuran window
page.window_width = 800
page.window_height = 1000

# Window properties
page.window_resizable = True
page.window_maximizable = True
```

### **Analysis Customization**
```python
# Custom prompt untuk analisis
custom_prompt = """
Analisis gambar ini secara detail dalam Bahasa Indonesia.
Fokus pada: objek utama, komposisi warna, aktivitas yang terjadi.
"""

# File size limit
MAX_FILE_SIZE = 15 * 1024 * 1024  # 15MB
```

## � Pengembangan Lanjutan

### **Fitur Potensial**
- **Batch Processing:** Analisis multiple gambar sekaligus dengan queue system
- **Export Results:** Simpan hasil analisis ke file (TXT, PDF, JSON)
- **Image Filters:** Pre-processing untuk meningkatkan akurasi (contrast, brightness, noise reduction)
- **Advanced Prompts:** Analisis spesifik (object counting, color analysis, text recognition, scene understanding)
- **Comparison Mode:** Bandingkan analisis dari multiple gambar
- **Image History:** Database lokal untuk menyimpan hasil analisis sebelumnya
- **Custom Templates:** Template prompt yang bisa disesuaikan untuk kebutuhan spesifik
- **OCR Integration:** Extract dan translate text dari gambar
- **Image Enhancement:** Auto-enhance gambar sebelum analisis
- **Multi-language Output:** Hasil analisis dalam berbagai bahasa

### **Improvements yang Direncanakan**
- **Performance Optimization:** Image compression dan caching untuk file besar
- **Cloud Storage Integration:** Upload dan analisis dari cloud services (Google Drive, Dropbox)
- **AI Model Selection:** Pilihan multiple AI models untuk analisis berbeda
- **Annotation Tools:** Markup tools untuk highlight area specific dalam gambar
- **Report Generation:** Generate comprehensive reports dengan charts dan statistics
- **API Integration:** RESTful API untuk integration dengan aplikasi lain
- **Mobile Companion:** Companion mobile app untuk capture dan sync
- **Real-time Camera:** Live camera feed analysis dengan real-time description

### **Technical Roadmap**
- **Database Integration:** SQLite untuk menyimpan metadata dan results
- **Image Processing Pipeline:** Advanced preprocessing dengan OpenCV
- **Machine Learning Enhancement:** Custom model training untuk domain-specific analysis
- **Microservices Architecture:** Scalable backend dengan containerization
- **WebSocket Integration:** Real-time updates untuk collaborative analysis
- **Testing Framework:** Automated testing dengan pytest dan image fixtures
- **Documentation Generator:** Auto-generate API docs dan user guides

## �📝 Lisensi

Proyek ini dibuat untuk tujuan edukasi dan pengembangan. Silakan gunakan dan modifikasi sesuai kebutuhan dengan tetap mencantumkan credit yang appropriate.

---

**Nikmati pengalaman analisis gambar dengan AI modern! 🚀**

---

## 🇺🇸 English

Welcome to **Image Describer**! A modern image analysis application that uses the power of **Google Generative AI (Gemini Vision)** with an elegant **Flet** interface to analyze and provide detailed descriptions of image content in Indonesian.

## 🌟 Key Features

### 🎨 **Modern UI & UX**
- **Elegant dark theme** that's comfortable for the eyes
- **Responsive design** with adaptive layout
- **Color-coded interface:** Purple for file picker, Green for analysis
- **Modern typography** with emojis and proper spacing

### 🚀 **AI Vision & Performance**
- **Google Gemini Vision AI** using `gemini-2.5-flash` model for computer vision
- **Advanced image analysis** with detailed and informative descriptions
- **Smart error handling** with informative feedback
- **Fast rendering** and smooth animations

### 📊 **Enhanced Features**
- **Modern file picker:** User-friendly file picker dialog
- **Real-time file info:** Monitor file name, size, and format
- **Progress indicator:** Visual feedback with progress ring
- **Status tracking:** Real-time status with emojis and colors
- **File validation:** Automatic format and size validation
- **Clear function:** Reset all fields with one click
- **Modern notifications:** Non-intrusive snackbar notifications

## 🚀 Quick Start

### 1. **Quick Installation**
```bash
pip install flet google-generativeai Pillow requests
```

### 2. **Setup API Key**
1. Open [Google AI Studio](https://aistudio.google.com/)
2. Register/login and get free API Key
3. Open `image_describer.py` file
4. Replace this line:
```python
API_KEY = "YOUR_GEMINI_API_KEY"  # Replace with your API key
```

### 3. **Run Application**
```bash
python image_describer.py
```

## 🎯 How to Use

### **Modern Interface**
1. **Header Section:** Title and app info with elegant styling
2. **File Section:** Path display and file picker with real-time validation
3. **Action Section:** Analysis button with progress indicator
4. **Statistics Panel:** Real-time file info and status monitoring
5. **Output Section:** Text field for detailed analysis results
6. **Control Section:** Clear button and info panel

### **Usage Workflow**
1. **Select Image:** Click "📂 Select Image" to open file picker
2. **File Validation:** System automatically validates format and file size
3. **Monitor Info:** See file information (name, size, format) in panel
4. **Analyze:** Click "🔍 Analyze Image" button
5. **Visual Feedback:** Progress ring appears, status changes to "Processing..."
6. **Results:** Detailed description appears with success notification
7. **Clear (Optional):** Use "🗑️ Clear" button to reset

## 🚀 **Advanced Development**

### **Potential Features**
- **Batch Processing:** Analyze multiple images simultaneously with queue system
- **Export Results:** Save analysis results to files (TXT, PDF, JSON)
- **Image Filters:** Pre-processing to improve accuracy (contrast, brightness, noise reduction)
- **Advanced Prompts:** Specific analysis (object counting, color analysis, text recognition, scene understanding)
- **Comparison Mode:** Compare analysis from multiple images
- **Image History:** Local database to store previous analysis results
- **Custom Templates:** Customizable prompt templates for specific needs
- **OCR Integration:** Extract and translate text from images
- **Image Enhancement:** Auto-enhance images before analysis
- **Multi-language Output:** Analysis results in various languages

### **Planned Improvements**
- **Performance Optimization:** Image compression and caching for large files
- **Cloud Storage Integration:** Upload and analyze from cloud services (Google Drive, Dropbox)
- **AI Model Selection:** Multiple AI models selection for different analysis
- **Annotation Tools:** Markup tools to highlight specific areas in images
- **Report Generation:** Generate comprehensive reports with charts and statistics
- **API Integration:** RESTful API for integration with other applications
- **Mobile Companion:** Companion mobile app for capture and sync
- **Real-time Camera:** Live camera feed analysis with real-time description

---

**Enjoy analyzing images with modern AI! 🚀**

---

## 🇯🇵 日本語

**画像記述者**へようこそ！**Google Generative AI (Gemini Vision)**の力とエレガントな**Flet**インターフェースを使用して、画像内容を詳細に分析し、インドネシア語で説明を提供するモダンな画像分析アプリケーションです。

## 🌟 主な機能

### 🎨 **モダンUI & UX**
- **エレガントなダークテーマ** - 目に優しい
- **レスポンシブデザイン** - 適応的なレイアウト
- **カラーコード化されたインターフェース:** ファイルピッカー（紫）、分析（緑）
- **モダンタイポグラフィ** - 絵文字と適切なスペーシング

### 🚀 **AI Vision & パフォーマンス**
- **Google Gemini Vision AI** - コンピュータビジョン用`gemini-2.5-flash`モデルを使用
- **高度な画像分析** - 詳細で情報豊富な説明
- **スマートエラーハンドリング** - 情報豊富なフィードバック
- **高速レンダリング** - スムーズなアニメーション

## 🚀 クイックスタート

### 1. **クイックインストール**
```bash
pip install flet google-generativeai Pillow requests
```

### 2. **APIキーセットアップ**
1. [Google AI Studio](https://aistudio.google.com/)を開く
2. 登録/ログインして無料のAPIキーを取得
3. `image_describer.py`ファイルを開く
4. この行を置き換える:
```python
API_KEY = "YOUR_GEMINI_API_KEY"  # あなたのAPIキーに置き換え
```

### 3. **アプリケーション実行**
```bash
python image_describer.py
```

## 🎯 使用方法

### **モダンインターフェース**
1. **ヘッダーセクション:** エレガントなスタイリングのタイトルとアプリ情報
2. **ファイルセクション:** リアルタイム検証付きのパス表示とファイルピッカー
3. **アクションセクション:** プログレスインジケータ付き分析ボタン
4. **統計パネル:** リアルタイムファイル情報とステータス監視
5. **出力セクション:** 詳細分析結果用のテキストフィールド
6. **コントロールセクション:** クリアボタンと情報パネル

### **使用ワークフロー**
1. **画像選択:** 「📂 画像を選択」をクリックしてファイルピッカーを開く
2. **ファイル検証:** システムが自動的に形式とファイルサイズを検証
3. **情報監視:** パネルでファイル情報（名前、サイズ、形式）を確認
4. **分析:** 「🔍 画像分析」ボタンをクリック
5. **視覚的フィードバック:** プログレスリングが表示され、ステータスが「処理中...」に変更
6. **結果:** 成功通知と共に詳細な説明が表示
7. **クリア（オプション）:** 「🗑️ クリア」ボタンを使用してリセット

## 🚀 **高度な開発**

### **潜在的な機能**
- **バッチ処理:** キューシステムによる複数画像の同時分析
- **結果エクスポート:** 分析結果をファイル（TXT、PDF、JSON）に保存
- **画像フィルター:** 精度向上のための前処理（コントラスト、明度、ノイズ除去）
- **高度なプロンプト:** 特定分析（オブジェクト計数、色分析、テキスト認識、シーン理解）
- **比較モード:** 複数画像からの分析比較
- **画像履歴:** 以前の分析結果を保存するローカルデータベース
- **カスタムテンプレート:** 特定ニーズ用のカスタマイズ可能なプロンプトテンプレート
- **OCR統合:** 画像からのテキスト抽出と翻訳
- **画像強化:** 分析前の自動画像強化
- **多言語出力:** 様々な言語での分析結果

### **計画された改善**
- **パフォーマンス最適化:** 大きなファイル用の画像圧縮とキャッシュ
- **クラウドストレージ統合:** クラウドサービス（Google Drive、Dropbox）からのアップロードと分析
- **AIモデル選択:** 異なる分析用の複数AIモデル選択
- **注釈ツール:** 画像内の特定エリアをハイライトするマークアップツール
- **レポート生成:** チャートと統計を含む包括的レポートの生成
- **API統合:** 他のアプリケーションとの統合用RESTful API
- **モバイルコンパニオン:** キャプチャと同期用のコンパニオンモバイルアプリ
- **リアルタイムカメラ:** リアルタイム説明付きライブカメラフィード分析

---

**モダンなAIでの画像分析をお楽しみください！🚀**