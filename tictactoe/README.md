**🌐 Languages:** [🇮🇩 Bahasa Indonesia](#bahasa-indonesia) | [🇺🇸 English](#english) | [🇯🇵 日本語](#日本語)

---

# ❌⭕ Tic-Tac-Toe Pro

---

## 🇮🇩 Bahasa Indonesia

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

## 🏷️ Text Tags
`Python`, `Pygame`, `Tic-Tac-Toe`, `Minimax Algorithm`, `Artificial Intelligence`, `Game Development`, `GUI`, `Strategy Game`, `Computer Science`, `Algorithm Implementation`

## 🎬 Demo

### Skenario Permainan:
1. **Startup:** Pemain membuka aplikasi dan melihat menu utama dengan 3 opsi mode
2. **Mode Selection:** Pemain memilih "Player vs AI (Sulit)" untuk tantangan maksimal
3. **Turn Order:** Aplikasi menampilkan menu pemilihan - pemain memilih "Saya Main Duluan (X)"
4. **Gameplay:** 
   - Pemain mengklik kotak tengah (strategi optimal)
   - AI merespons dalam 400ms dengan gerakan counter-strategy
   - Pemain mencoba membuat fork (dua peluang menang)
   - AI memblokir dengan sempurna menggunakan algoritma Minimax
5. **Endgame:** Setelah 9 gerakan, hasil seri dengan popup elegant "Draw!"
6. **Reset:** Pemain klik "Menu" untuk kembali atau mencoba mode lain

### Fitur Visual:
- **Hover Effects:** Tombol berubah warna saat mouse hover
- **Turn Indicator:** Status giliran ditampilkan di bawah board
- **Popup Animation:** Winner announcement dengan overlay semi-transparan
- **Responsive Design:** Interface menyesuaikan dengan interaksi mouse

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

---

## 🇺🇸 English

Welcome to **Tic-Tac-Toe Pro**! This is a modern implementation of the classic Tic-Tac-Toe game with an attractive graphical interface and smart AI using the Minimax algorithm.

## 🌟 Key Features

- **Modern Graphical Interface:** Responsive and attractive GUI using Pygame
- **Multiple Game Modes:**
  - **Player vs Player (PvP):** Two players take turns
  - **Player vs AI (Easy):** Against AI with random moves
  - **Player vs AI (Hard):** Against AI with Minimax algorithm
- **Turn Order Selection:** For AI mode, choose whether you go first (X) or AI goes first (O)
- **Unbeatable AI:** Minimax algorithm on hard level
- **Popup Notifications:** Elegant winner announcements
- **Reset Game:** Easily restart the game

## 🎯 How to Play

**Objective:** Arrange three symbols ('X' or 'O') in a row, either horizontal, vertical, or diagonal.

**Controls:**
- Use **Mouse** to click on the square you want to fill
- **Select Mode:** Click game mode in the main menu
- **Select Order:** For AI mode, choose whether you go first or AI goes first
- **Reset:** Click "Menu" button to return or restart game

## ⚙️ Installation and Running

### 1. Prerequisites
Make sure you have **Python 3** (version 3.6 or newer) installed.

### 2. Navigate to Folder
```bash
cd tictactoe
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

**Or install manually:**
```bash
pip install pygame
```

### 5. Run Game
```bash
python tictactoe.py
```

### 6. Switch to Other Tools/Folders
<sub><i>💡 Guide for beginners</i></sub>

After finishing playing, you can switch to other tools:

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
# For Pac-Man game
cd pacman

# For Text Describer (AI)
cd text_describer

# For Image Describer (AI)  
cd image_describer
```

<sub><i>🔄 Repeat steps 3-5 to run the new tool</i></sub>

## 🏷️ Text Tags
`Python`, `Pygame`, `Tic-Tac-Toe`, `Minimax Algorithm`, `Artificial Intelligence`, `Game Development`, `GUI`, `Strategy Game`, `Computer Science`, `Algorithm Implementation`

## 🎬 Demo

### Game Scenario:
1. **Startup:** Player opens application and sees main menu with 3 mode options
2. **Mode Selection:** Player selects "Player vs AI (Hard)" for maximum challenge
3. **Turn Order:** Application displays selection menu - player chooses "I Go First (X)"
4. **Gameplay:** 
   - Player clicks center square (optimal strategy)
   - AI responds in 400ms with counter-strategy move
   - Player attempts to create fork (two winning opportunities)
   - AI blocks perfectly using Minimax algorithm
5. **Endgame:** After 9 moves, draw result with elegant "Draw!" popup
6. **Reset:** Player clicks "Menu" to return or try other modes

### Visual Features:
- **Hover Effects:** Buttons change color on mouse hover
- **Turn Indicator:** Turn status displayed below board
- **Popup Animation:** Winner announcement with semi-transparent overlay
- **Responsive Design:** Interface adapts to mouse interactions

---

**Happy playing! 🎉**

---

## 🇯🇵 日本語

**三目並べプロ**へようこそ！これは、魅力的なグラフィカルインターフェースとMinimaxアルゴリズムを使用したスマートAIを備えたクラシック三目並べゲームのモダンな実装です。

## 🌟 主な機能

- **モダンなグラフィカルインターフェース:** Pygameを使用したレスポンシブで魅力的なGUI
- **複数のゲームモード:**
  - **プレイヤー対プレイヤー（PvP）:** 二人のプレイヤーが交代
  - **プレイヤー対AI（簡単）:** ランダムな動きのAIと対戦
  - **プレイヤー対AI（難しい）:** Minimaxアルゴリズムを使用したAIと対戦
- **ターン順序選択:** AIモードでは、あなたが先手（X）かAIが先手（O）かを選択
- **無敗のAI:** ハードレベルでのMinimaxアルゴリズム
- **ポップアップ通知:** エレガントな勝者発表
- **ゲームリセット:** 簡単にゲームを再開

## 🎯 プレイ方法

**目標:** 3つのシンボル（'X'または'O'）を一列に並べる（水平、垂直、対角線）。

**操作:**
- **マウス**を使って塗りつぶしたいマスをクリック
- **モード選択:** メインメニューでゲームモードをクリック
- **順序選択:** AIモードでは、あなたが先手かAIが先手かを選択
- **リセット:** 「メニュー」ボタンをクリックして戻るかゲームを再開

## ⚙️ インストールと実行

### 1. 前提条件
**Python 3**（バージョン3.6以上）がインストールされていることを確認してください。

### 2. フォルダに移動
```bash
cd tictactoe
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

**または手動でインストール:**
```bash
pip install pygame
```

### 5. ゲーム実行
```bash
python tictactoe.py
```

### 6. 他のツール/フォルダへの切り替え
<sub><i>💡 初心者向けガイド</i></sub>

プレイ終了後、他のツールに切り替えることができます：

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
# パックマンゲーム用
cd pacman

# テキスト記述者（AI）用
cd text_describer

# 画像記述者（AI）用
cd image_describer
```

<sub><i>🔄 新しいツールを実行するには手順3-5を繰り返してください</i></sub>

## 🏷️ テキストタグ
`Python`, `Pygame`, `三目並べ`, `Minimaxアルゴリズム`, `人工知能`, `ゲーム開発`, `GUI`, `戦略ゲーム`, `コンピューターサイエンス`, `アルゴリズム実装`

## 🎬 デモ

### ゲームシナリオ:
1. **起動:** プレイヤーがアプリケーションを開き、3つのモードオプションがあるメインメニューを表示
2. **モード選択:** 最大の挑戦のため「プレイヤー対AI（難しい）」を選択
3. **ターン順序:** アプリケーションが選択メニューを表示 - プレイヤーが「私が先手（X）」を選択
4. **ゲームプレイ:** 
   - プレイヤーが中央マスをクリック（最適戦略）
   - AIが400msでカウンター戦略の手で応答
   - プレイヤーがフォーク（2つの勝利機会）を作ろうと試みる
   - AIがMinimaxアルゴリズムを使用して完璧にブロック
5. **エンドゲーム:** 9手後、エレガントな「引き分け！」ポップアップで引き分け結果
6. **リセット:** プレイヤーが「メニュー」をクリックして戻るか他のモードを試す

### ビジュアル機能:
- **ホバー効果:** マウスホバー時にボタンの色が変わる
- **ターン表示:** ボード下部にターン状況を表示
- **ポップアップアニメーション:** 半透明オーバーレイ付きの勝者発表
- **レスポンシブデザイン:** マウスインタラクションに適応するインターフェース

---

**楽しくプレイしてください！🎉**