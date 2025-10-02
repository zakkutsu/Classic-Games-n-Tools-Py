**🌐 Languages:** [🇮🇩 Bahasa Indonesia](#bahasa-indonesia) | [🇺🇸 English](#english) | [🇯🇵 日本語](#日本語)

---

# 🟡 Pac-Man Klasik

---

## 🇮🇩 Bahasa Indonesia

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

## 🇺🇸 English

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

## 🏷️ Text Tags
`Python`, `Pygame`, `Pac-Man`, `Arcade Game`, `Game Development`, `Animation`, `AI Pathfinding`, `Classic Games`, `Retro Gaming`, `Computer Graphics`

## 🎬 Demo

### Game Scenario:
1. **Game Start:** Player starts with Pac-Man at initial position (center bottom of maze)
2. **Initial Movement:** 
   - Pac-Man moves right with mouth opening-closing animation
   - Red, pink, and cyan ghosts start patrolling their respective areas
3. **Pellet Collection:**
   - Player navigates through narrow corridors, eating white pellets
   - Each pellet gives +10 points, score increases in real-time
   - Ghost AI starts detecting Pac-Man's position and moves closer
4. **Chase Sequence:**
   - Red ghost actively chases, player must use maze corners to avoid
   - Game speed increases 10% every 3 seconds - gameplay becomes more intense
5. **Near Miss:** Pac-Man almost gets caught in narrow corridor, successfully escapes to left tunnel
6. **Tunnel Mechanic:** Exit from left side of screen, appear on right side (wraparound)
7. **Victory/Defeat:** 
   - **Win:** All pellets consumed → "You Win!" with final score
   - **Lose:** Caught by ghost → "Game Over!" with restart option

### Technical Features:
- **Smooth Animation:** 60 FPS with smooth movement interpolation
- **Dynamic Speed:** Progressive difficulty with FPS scaling
- **Collision Detection:** Pixel-perfect detection for walls and ghosts
- **Audio-Visual Feedback:** Screen flash on game over, victory celebration

## 🎮 Game Features

### Pac-Man Animation
- Mouth opens and closes while moving
- Character rotation according to movement direction
- Smooth and responsive animation

### Ghost AI
- Ghosts automatically move to chase the player
- Each ghost has different colors (red, pink, cyan)
- Realistic movement within the maze

### Speed System
- Game starts at normal speed
- Speed increases every 3 seconds (10% faster)
- Provides increasingly challenging gameplay

## 🏗️ Code Structure

The `pacman_game.py` file consists of:
- **Player Class:** Pac-Man movement logic and animation
- **Ghost Class:** AI and ghost movement
- **Maze Layout:** Customizable maze design
- **Game Loop:** Main game logic and rendering
- **Collision Detection:** Collision detection and interactions

## 🎨 Customization

You can modify:
- **Maze layout** in the `maze_map` variable
- **Game speed** in the `INITIAL_FPS` constant
- **Character colors** in the color constants
- **Screen size** in `SCREEN_WIDTH` and `SCREEN_HEIGHT`

## 🔧 Development

This game uses:
- **Pygame** for graphics and input handling
- **Python OOP** for clean code structure
- **Mathematical calculations** for AI and collision detection

## 📝 Playing Tips

1. **Plan your route** before moving
2. **Observe ghost movement patterns** to avoid them
3. **Use maze corners** to hide temporarily
4. **Move quickly** when ghosts are moving away
5. **Don't get trapped** in dead ends

---

**Happy playing and good luck defeating the ghosts! 👻🟡**

---

## 🇯🇵 日本語

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

## 🏷️ テキストタグ
`Python`, `Pygame`, `パックマン`, `アーケードゲーム`, `ゲーム開発`, `アニメーション`, `AI経路探索`, `クラシックゲーム`, `レトロゲーミング`, `コンピューターグラフィックス`

## 🎬 デモ

### ゲームシナリオ:
1. **ゲーム開始:** プレイヤーは迷路の初期位置（中央下部）でパックマンを開始
2. **初期移動:** 
   - パックマンが口の開閉アニメーションで右に移動
   - 赤、ピンク、シアンのゴーストがそれぞれのエリアでパトロール開始
3. **ペレット収集:**
   - プレイヤーが狭い廊下を移動し、白いペレットを食べる
   - 各ペレットで+10ポイント、スコアがリアルタイムで増加
   - ゴーストAIがパックマンの位置を検出し、近づき始める
4. **追跡シーケンス:**
   - 赤いゴーストが積極的に追跡、プレイヤーは迷路の角を使って回避
   - 3秒ごとにゲーム速度が10%増加 - ゲームプレイがより激しくなる
5. **ニアミス:** パックマンが狭い廊下でほぼ捕まりそうになるが、左のトンネルへの脱出に成功
6. **トンネルメカニクス:** 画面左側から出て右側に現れる（ラップアラウンド）
7. **勝利/敗北:** 
   - **勝利:** すべてのペレット消費 → 最終スコアで「勝利！」
   - **敗北:** ゴーストに捕まる → 再開オプション付き「ゲームオーバー！」

### 技術的特徴:
- **スムーズアニメーション:** スムーズな移動補間での60 FPS
- **ダイナミックスピード:** FPSスケーリングによる段階的難易度
- **衝突検出:** 壁とゴーストのピクセル完璧な検出
- **オーディオビジュアルフィードバック:** ゲームオーバー時の画面フラッシュ、勝利祝賀

## 🎮 ゲーム機能

### パックマンアニメーション
- 移動中に口が開閉
- 移動方向に応じたキャラクター回転
- スムーズで反応の良いアニメーション

### ゴーストAI
- ゴーストが自動的にプレイヤーを追跡するように移動
- 各ゴーストは異なる色（赤、ピンク、シアン）
- 迷路内での現実的な移動

### スピードシステム
- ゲームは通常速度で開始
- 3秒ごとに速度が増加（10%高速化）
- ますます挑戦的なゲームプレイを提供

## 🏗️ コード構造

`pacman_game.py`ファイルの構成:
- **Playerクラス:** パックマンの移動ロジックとアニメーション
- **Ghostクラス:** AIとゴーストの移動
- **迷路レイアウト:** カスタマイズ可能な迷路設計
- **ゲームループ:** メインゲームロジックとレンダリング
- **衝突検出:** 衝突検出と相互作用

## 🎨 カスタマイゼーション

変更可能項目:
- `maze_map`変数の**迷路レイアウト**
- `INITIAL_FPS`定数の**ゲーム速度**
- 色定数の**キャラクター色**
- `SCREEN_WIDTH`と`SCREEN_HEIGHT`の**画面サイズ**

## 🔧 開発

このゲームは以下を使用:
- **Pygame** - グラフィックスと入力処理用
- **Python OOP** - クリーンなコード構造用
- **数学計算** - AIと衝突検出用

## 📝 プレイのコツ

1. **移動前にルートを計画**
2. **ゴーストの移動パターンを観察**して回避
3. **迷路の角を使用**して一時的に隠れる
4. **ゴーストが離れる時に素早く移動**
5. **行き止まりで罠にかからない**

---

**楽しくプレイして、ゴーストを倒せるよう頑張ってください！👻🟡**