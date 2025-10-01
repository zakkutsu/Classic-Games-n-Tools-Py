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
3. Buka file `API-KEY.txt` di folder root project
4. Ganti API key dengan yang baru:
```
API key details

API Key: PASTE_API_KEY_ANDA_DI_SINI
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
3. Buka file `API-KEY.txt` di folder root project (`c:\project\Classic-Games-And-Tools-Py\API-KEY.txt`)
4. Ganti API key dengan yang baru:
```
API key details

API Key: PASTE_API_KEY_ANDA_DI_SINI
```

**Catatan:** API key disimpan di file terpisah untuk keamanan dan kemudahan update. Satu API key digunakan untuk semua aplikasi dalam project ini.

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
3. Open `API-KEY.txt` file in the project root folder
4. Replace the API key with your new one:
```
API key details

API Key: PASTE_YOUR_API_KEY_HERE
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

## 📝 Dependencies

The `requirements.txt` file contains:
```
flet>=0.21.0
google-generativeai>=0.3.0
Pillow>=10.0.0
requests>=2.31.0
```

## 🔧 Technical Features

### **Modern Architecture**
- **Flet Framework:** Cross-platform modern UI framework
- **Event-driven:** Reactive programming with callback functions
- **Component-based:** Modular UI components with proper separation
- **State Management:** Efficient state updates with page.update()

### **Computer Vision Integration**
- **Model:** gemini-2.5-flash with vision capabilities
- **Image Processing:** PIL/Pillow for preprocessing and validation
- **Format Support:** PNG, JPG, JPEG, GIF, WebP
- **Size Optimization:** Smart file size validation (max 10MB)

### **AI Analysis Features**
- **Detailed Description:** Comprehensive object and scene analysis
- **Color Analysis:** Color composition and visual elements
- **Activity Recognition:** Scene context and situation analysis
- **Technical Details:** Format, composition, and artistic elements

### **Performance Optimizations**
- **Lazy Loading:** Components loaded as needed
- **Efficient Image Handling:** Optimized image loading and processing
- **Memory Management:** Proper cleanup and resource management
- **Responsive File Operations:** Non-blocking file operations

### **UI/UX Features**
- **Dark Theme:** Consistent modern dark theme
- **Color System:** Systematic color coding (Purple: files, Green: analysis)
- **File Picker Integration:** Native file picker with proper filtering
- **Progress Feedback:** Real-time progress indicators
- **Error Visualization:** Color-coded error states and recovery

## 💡 Usage Tips

### **Optimal Usage**
1. **File Quality:** Use images with good resolution for best analysis results
2. **Format Preference:** JPG/PNG provide optimal analysis results
3. **File Size:** Images 1-5MB provide balance between quality and speed
4. **Content Types:** AI can analyze landscapes, objects, people, text in images

### **Advanced Features**
1. **Batch Analysis:** Use clear function for efficient workflow
2. **Error Recovery:** Pay attention to color-coded feedback for troubleshooting
3. **Performance:** Monitor file size for optimal processing speed
4. **Quality:** Clear and well-lit images provide more detailed analysis

## 🛠️ Troubleshooting

### **Common Issues**

#### **API Key Errors**
- **Symptom:** Error dialog at launch
- **Solution:** Verify API key in Google AI Studio, check internet connection
- **Prevention:** Test API key before deployment

#### **File Format Issues**
- **Symptom:** "Unsupported file format" message
- **Solution:** Use PNG, JPG, JPEG, GIF, or WebP formats
- **Recovery:** Convert file to supported format

#### **File Size Issues**
- **Symptom:** "File size too large" warning
- **Solution:** Compress image or use file < 10MB
- **Optimization:** Resize image maintaining aspect ratio

#### **Analysis Quality**
- **Symptom:** Less detailed descriptions
- **Solution:** Use images with good resolution and lighting
- **Enhancement:** Choose images with clear and focused content

### **Advanced Debugging**
- **UI Issues:** Check Flet version compatibility
- **API Issues:** Monitor API quotas and rate limits  
- **Performance:** Use system monitor for resource usage
- **Image Issues:** Validate image integrity with image viewers

## 🔧 Customization & Development

### **Theme Customization**
```python
# Change theme mode
page.theme_mode = ft.ThemeMode.LIGHT  # or DARK, SYSTEM

# Custom colors
page.bgcolor = ft.colors.GREY_900
```

### **Window Customization**
```python
# Window size
page.window_width = 800
page.window_height = 1000

# Window properties
page.window_resizable = True
page.window_maximizable = True
```

### **Analysis Customization**
```python
# Custom prompt for analysis
custom_prompt = """
Analyze this image in detail in Indonesian.
Focus on: main objects, color composition, activities occurring.
"""

# File size limit
MAX_FILE_SIZE = 15 * 1024 * 1024  # 15MB
```

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

### **Technical Roadmap**
- **Database Integration:** SQLite for storing metadata and results
- **Image Processing Pipeline:** Advanced preprocessing with OpenCV
- **Machine Learning Enhancement:** Custom model training for domain-specific analysis
- **Microservices Architecture:** Scalable backend with containerization
- **WebSocket Integration:** Real-time updates for collaborative analysis
- **Testing Framework:** Automated testing with pytest and image fixtures
- **Documentation Generator:** Auto-generate API docs and user guides

## 📝 License

This project is created for educational and development purposes. Please use and modify as needed while maintaining appropriate credits.

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
3. プロジェクトルートフォルダの`API-KEY.txt`ファイルを開く
4. 新しいAPIキーに置き換える:
```
API key details

API Key: ここにAPIキーを貼り付け
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

## 📝 依存関係

`requirements.txt`ファイルに含まれる内容:
```
flet>=0.21.0
google-generativeai>=0.3.0
Pillow>=10.0.0
requests>=2.31.0
```

## 🔧 技術的機能

### **モダンアーキテクチャ**
- **Fletフレームワーク:** クロスプラットフォームのモダンUIフレームワーク
- **イベント駆動:** コールバック関数でのリアクティブプログラミング
- **コンポーネントベース:** 適切な分離を持つモジュラーUIコンポーネント
- **状態管理:** page.update()での効率的な状態更新

### **コンピュータービジョン統合**
- **モデル:** ビジョン機能付きgemini-2.5-flash
- **画像処理:** 前処理と検証用PIL/Pillow
- **フォーマットサポート:** PNG、JPG、JPEG、GIF、WebP
- **サイズ最適化:** スマートなファイルサイズ検証（最大10MB）

### **AI分析機能**
- **詳細説明:** 包括的なオブジェクトとシーン分析
- **色分析:** 色構成と視覚的要素
- **アクティビティ認識:** シーンコンテキストと状況分析
- **技術的詳細:** フォーマット、構成、芸術的要素

### **パフォーマンス最適化**
- **遅延読み込み:** 必要に応じてコンポーネントを読み込み
- **効率的画像処理:** 最適化された画像読み込みと処理
- **メモリ管理:** 適切なクリーンアップとリソース管理
- **レスポンシブファイル操作:** ノンブロッキングファイル操作

### **UI/UX機能**
- **ダークテーマ:** 一貫したモダンダークテーマ
- **カラーシステム:** 体系的カラーコーディング（紫：ファイル、緑：分析）
- **ファイルピッカー統合:** 適切なフィルタリング付きネイティブファイルピッカー
- **プログレスフィードバック:** リアルタイムプログレスインジケーター
- **エラー視覚化:** カラーコード化されたエラー状態と復旧

## 💡 使用のコツ

### **最適な使用方法**
1. **ファイル品質:** 最適な分析結果のために高品質な解像度の画像を使用
2. **フォーマットの優先:** JPG/PNGが最適な分析結果を提供
3. **ファイルサイズ:** 1-5MBの画像が品質と速度のバランスを提供
4. **コンテンツタイプ:** AIは景観、オブジェクト、人、画像内のテキストを分析可能

### **高度な機能**
1. **バッチ分析:** 効率的なワークフローのためにクリア機能を使用
2. **エラー復旧:** トラブルシューティングのためにカラーコード化されたフィードバックに注意
3. **パフォーマンス:** 最適な処理速度のためにファイルサイズを監視
4. **品質:** 明確で適切な照明の画像がより詳細な分析を提供

## 🛠️ トラブルシューティング

### **一般的な問題**

#### **APIキーエラー**
- **症状:** 起動時のエラーダイアログ
- **解決方法:** Google AI StudioでAPIキーを確認、インターネット接続をチェック
- **予防:** デプロイ前にAPIキーをテスト

#### **ファイルフォーマットの問題**
- **症状:** 「サポートされていないファイルフォーマット」メッセージ
- **解決方法:** PNG、JPG、JPEG、GIF、WebPフォーマットを使用
- **復旧:** サポートされているフォーマットにファイルを変換

#### **ファイルサイズの問題**
- **症状:** 「ファイルサイズが大きすぎます」警告
- **解決方法:** 画像を圧縮するか10MB未満のファイルを使用
- **最適化:** アスペクト比を維持して画像をリサイズ

#### **分析品質**
- **症状:** 詳細さの低い説明
- **解決方法:** 高解像度と良い照明の画像を使用
- **改善:** 明確でフォーカスのあるコンテンツの画像を選択

### **高度なデバッグ**
- **UIの問題:** Fletバージョンの互換性をチェック
- **APIの問題:** APIクォータとレート制限を監視  
- **パフォーマンス:** リソース使用量のためにシステムモニターを使用
- **画像の問題:** 画像ビューアーで画像の整合性を検証

## 🔧 カスタマイゼーションと開発

### **テーマカスタマイズ**
```python
# テーマモードの変更
page.theme_mode = ft.ThemeMode.LIGHT  # またはDARK、SYSTEM

# カスタムカラー
page.bgcolor = ft.colors.GREY_900
```

### **ウィンドウカスタマイズ**
```python
# ウィンドウサイズ
page.window_width = 800
page.window_height = 1000

# ウィンドウプロパティ
page.window_resizable = True
page.window_maximizable = True
```

### **分析カスタマイズ**
```python
# 分析用カスタムプロンプト
custom_prompt = """
この画像をインドネシア語で詳細に分析してください。
主要オブジェクト、色構成、発生しているアクティビティに焦点を当ててください。
"""

# ファイルサイズ制限
MAX_FILE_SIZE = 15 * 1024 * 1024  # 15MB
```

## 🚀 **高度な開発**

### **潜在的な機能**
- **バッチ処理:** キューシステムで複数の画像を同時分析
- **結果エクスポート:** 分析結果をファイルに保存（TXT、PDF、JSON）
- **画像フィルター:** 精度向上のための前処理（コントラスト、明度、ノイズ除去）
- **高度なプロンプト:** 特定分析（オブジェクトカウント、色分析、テキスト認識、シーン理解）
- **比較モード:** 複数の画像からの分析比較
- **画像履歴:** 以前の分析結果を保存するローカルデータベース
- **カスタムテンプレート:** 特定ニーズ用のカスタマイズ可能プロンプトテンプレート
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
- **モバイルコンパニオン:** キャプチャと同期用コンパニオンモバイルアプリ
- **リアルタイムカメラ:** リアルタイム説明付きライブカメラフィード分析

### **技術ロードマップ**
- **データベース統合:** メタデータと結果を保存するSQLite
- **画像処理パイプライン:** OpenCVでの高度前処理
- **機械学習強化:** ドメイン固有分析用カスタムモデルトレーニング
- **マイクロサービスアーキテクチャ:** コンテナ化でのスケーラブルバックエンド
- **WebSocket統合:** コラボレーティブ分析用リアルタイム更新
- **テストフレームワーク:** pytestと画像フィクスチャでの自動テスト
- **ドキュメントジェネレーター:** APIドキュメントとユーザーガイドの自動生成

## 📝 ライセンス

このプロジェクトは教育および開発目的で作成されています。適切なクレジットを維持しながら、必要に応じて使用および変更してください。

---