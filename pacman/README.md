# 🟡 Pac-Man Klasik

**🌐 Languages:** [🇮🇩 Bahasa Indonesia](#id) | [🇺🇸 English](#en) | [🇯🇵 日本語](#jp)

---

## 🇮🇩 Bahasa Indonesia {#id}

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
pip install -r requirements.txt
```

**Atau instal manual:**
```bash
pip install pygame
```

### 5. Jalankan Game
```bash
python pacman_game.py
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
# Untuk game Tic-Tac-Toe
cd tictactoe

# Untuk Text Describer (AI)
cd text_describer

# Untuk Image Describer (AI)
cd image_describer
```

<sub><i>🔄 Ulangi langkah 3-5 untuk menjalankan tool yang baru</i></sub>

## 🏷️ Text Tags
`Python`, `Pygame`, `Pac-Man`, `Arcade Game`, `Game Development`, `Animation`, `AI Pathfinding`, `Classic Games`, `Retro Gaming`, `Computer Graphics`

## 🎬 Demo

### Skenario Permainan:
1. **Game Start:** Pemain memulai dengan Pac-Man di posisi awal (tengah bawah maze)
2. **Initial Movement:** 
   - Pac-Man bergerak ke kanan dengan animasi mulut membuka-tutup
   - Hantu merah, pink, dan cyan mulai berpatroli di area masing-masing
3. **Pellet Collection:**
   - Pemain navigasi melalui lorong sempit, memakan pellet putih
   - Setiap pellet memberikan +10 poin, skor bertambah real-time
   - Ghost AI mulai mendeteksi posisi Pac-Man dan bergerak mendekat
4. **Chase Sequence:**
   - Hantu merah aktif mengejar, pemain harus menggunakan sudut maze untuk menghindari
   - Kecepatan game bertambah 10% setiap 3 detik - gameplay semakin intens
5. **Near Miss:** Pac-Man hampir tertangkap di lorong sempit, berhasil kabur ke tunnel kiri
6. **Tunnel Mechanic:** Keluar dari sisi kiri layar, muncul di sisi kanan (wraparound)
7. **Victory/Defeat:** 
   - **Win:** Semua pellet habis → "You Win!" dengan skor final
   - **Lose:** Tertangkap hantu → "Game Over!" dengan opsi restart

### Fitur Teknis:
- **Smooth Animation:** 60 FPS dengan interpolasi gerakan yang halus
- **Dynamic Speed:** Progressive difficulty dengan FPS scaling
- **Collision Detection:** Pixel-perfect detection untuk walls dan ghosts
- **Audio-Visual Feedback:** Screen flash saat game over, victory celebration

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

---

## 🇺🇸 English {#en}

Welcome to the classic **Pac-Man** implementation! This legendary arcade game has been rebuilt using Python and Pygame with exciting modern features.

## 🌟 Key Features

- **Classic Gameplay:** Move through maze, eat pellets, and avoid ghosts
- **Character Animation:** Pac-Man with dynamic mouth opening-closing animation
- **Smart Ghost AI:** Ghosts actively chase the player in the maze
- **Scoring System:** Get points for every pellet eaten
- **Dynamic Speed:** Game gets faster over time
- **Reset Button:** Easily restart the game

## 🎯 How to Play

**Objective:** Eat all the white dots (pellets) in the maze to win the game.

**Controls:**
- **Up Arrow (↑):** Move up
- **Down Arrow (↓):** Move down  
- **Left Arrow (←):** Move left
- **Right Arrow (→):** Move right

**Rules:**
- Avoid touching colored ghosts (red, pink, cyan)
- If touched by ghost, game ends
- Eat all pellets to win
- Score increases for each pellet eaten

## ⚙️ Installation and Running

### 1. Prerequisites
Make sure you have **Python 3** (version 3.6 or newer) installed.

### 2. Navigate to Folder
```bash
cd pacman
```

### 3. Create Virtual Environment (Optional but Recommended)
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
python pacman_game.py
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
# For Tic-Tac-Toe game
cd tictactoe

# For Text Describer (AI)
cd text_describer

# For Image Describer (AI)
cd image_describer
```

<sub><i>🔄 Repeat steps 3-5 to run the new tool</i></sub>

---

**Happy playing and good luck defeating the ghosts! 👻🟡**

---

## 🇯🇵 日本語 {#jp}

クラシック**パックマン**の実装へようこそ！この伝説的なアーケードゲームは、エキサイティングなモダン機能でPythonとPygameを使用して再構築されました。

## 🌟 主な機能

- **クラシックゲームプレイ:** 迷路を移動し、ペレットを食べ、ゴーストを避ける
- **キャラクターアニメーション:** 口の開閉ダイナミックアニメーション付きパックマン
- **スマートゴーストAI:** ゴーストが迷路内でプレイヤーを積極的に追跡
- **スコアリングシステム:** 食べたペレットごとにポイント獲得
- **ダイナミックスピード:** 時間とともにゲームが高速化
- **リセットボタン:** 簡単にゲームを再開

## 🎯 プレイ方法

**目標:** 迷路内のすべての白い点（ペレット）を食べてゲームに勝利。

**操作:**
- **上矢印キー（↑）:** 上に移動
- **下矢印キー（↓）:** 下に移動  
- **左矢印キー（←）:** 左に移動
- **右矢印キー（→）:** 右に移動

**ルール:**
- 色付きゴースト（赤、ピンク、シアン）に触れないよう避ける
- ゴーストに触れるとゲーム終了
- すべてのペレットを食べると勝利
- 食べたペレットごとにスコア増加

## ⚙️ インストールと実行

### 1. 前提条件
**Python 3**（バージョン3.6以上）がインストールされていることを確認してください。

### 2. フォルダに移動
```bash
cd pacman
```

### 3. 仮想環境の作成（オプションだが推奨）
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
python pacman_game.py
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
# 三目並べゲーム用
cd tictactoe

# テキスト記述者（AI）用
cd text_describer

# 画像記述者（AI）用
cd image_describer
```

<sub><i>🔄 新しいツールを実行するには手順3-5を繰り返してください</i></sub>

---

**楽しくプレイして、ゴーストを倒せるよう頑張ってください！👻🟡**