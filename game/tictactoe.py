import pygame
import sys
import math
import random

# --- Inisialisasi Pygame ---
pygame.init()

# --- Konstanta ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600 # Diubah agar fokus ke papan, status dipindah ke popup
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = SCREEN_WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# --- Warna ---
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (84, 84, 84)
BUTTON_HOVER_COLOR = (120, 120, 120)
POPUP_BG_COLOR = (44, 44, 44)

# --- Layar ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tic Tac Toe Pro')

# --- Font ---
font = pygame.font.Font(None, 70)
medium_font = pygame.font.Font(None, 40)
small_font = pygame.font.Font(None, 30)

# --- Variabel Game ---
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
player = 1  # 1-X, 2-O
game_over = False
winner = None
game_mode = 'menu'  # menu, pvp, pve_easy, pve_hard

def draw_lines():
    """Menggambar garis papan permainan."""
    # Garis Horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (SCREEN_WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (SCREEN_WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Garis Vertikal
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, SCREEN_HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, SCREEN_HEIGHT), LINE_WIDTH)

def draw_figures():
    """Menggambar simbol X dan O di papan."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)

def mark_square(row, col, player):
    """Menandai kotak pada papan."""
    if board[row][col] is None:
        board[row][col] = player
        return True
    return False

def check_win(player):
    """Memeriksa apakah pemain menang."""
    # Cek vertikal
    for col in range(BOARD_COLS):
        if all(board[row][col] == player for row in range(BOARD_ROWS)): return True
    # Cek horizontal
    for row in range(BOARD_ROWS):
        if all(board[row][col] == player for col in range(BOARD_COLS)): return True
    # Cek diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player: return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player: return True
    return False

def check_draw():
    """Memeriksa apakah permainan seri."""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True

def restart_game():
    """Mereset permainan ke kondisi awal."""
    global board, player, game_over, winner
    board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = 1
    game_over = False
    winner = None

def draw_button(text, x, y, width, height, active_color, inactive_color, action=None, font_size=small_font):
    """Menggambar tombol interaktif."""
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    is_hovered = x + width > mouse[0] > x and y + height > mouse[1] > y
    
    if is_hovered:
        pygame.draw.rect(screen, active_color, (x, y, width, height), border_radius=8)
        if click[0] == 1 and action is not None:
            pygame.time.delay(200) # Mencegah klik ganda
            action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height), border_radius=8)

    text_surf = font_size.render(text, True, TEXT_COLOR)
    text_rect = text_surf.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surf, text_rect)

def set_game_mode(mode):
    """Mengatur mode permainan dan merestart."""
    global game_mode, SCREEN_HEIGHT
    if mode == 'menu':
        SCREEN_HEIGHT = 600
    else:
        SCREEN_HEIGHT = 700 # Tambah ruang untuk status giliran
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_mode = mode
    restart_game()

def show_menu():
    """Menampilkan menu utama."""
    screen.fill(BG_COLOR)
    title_text = font.render("Tic Tac Toe", True, TEXT_COLOR)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))

    draw_button("Player vs Player", 150, 220, 300, 50, BUTTON_HOVER_COLOR, BUTTON_COLOR, lambda: set_game_mode('pvp'), medium_font)
    draw_button("Player vs AI (Mudah)", 150, 290, 300, 50, BUTTON_HOVER_COLOR, BUTTON_COLOR, lambda: set_game_mode('pve_easy'), medium_font)
    draw_button("Player vs AI (Sulit)", 150, 360, 300, 50, BUTTON_HOVER_COLOR, BUTTON_COLOR, lambda: set_game_mode('pve_hard'), medium_font)

def draw_turn_indicator():
    """Menampilkan giliran siapa di bawah papan."""
    if not game_over:
        message = f"Giliran Pemain: {'X' if player == 1 else 'O'}"
        text = medium_font.render(message, True, TEXT_COLOR)
        pygame.draw.rect(screen, LINE_COLOR, (0, 600, SCREEN_WIDTH, 100))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 635))

# --- FUNGSI BARU UNTUK POPUP ---
def draw_winner_popup():
    """Menggambar popup saat permainan berakhir."""
    # Lapisan semi-transparan
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180)) # Warna hitam dengan 180 alpha (transparansi)
    screen.blit(overlay, (0, 0))

    # Kotak popup
    popup_rect = pygame.Rect(100, 200, 400, 250)
    pygame.draw.rect(screen, POPUP_BG_COLOR, popup_rect, border_radius=15)

    # Pesan Pemenang
    if winner:
        message = f"Pemain '{'X' if winner == 1 else 'O'}' Menang!"
    else:
        message = "Permainan Berakhir Seri!"
    
    text = font.render(message, True, TEXT_COLOR)
    screen.blit(text, (popup_rect.centerx - text.get_width() // 2, popup_rect.y + 30))

    # Tombol di dalam popup
    draw_button("Restart", 150, 350, 140, 50, BUTTON_HOVER_COLOR, BUTTON_COLOR, restart_game)
    draw_button("Menu", 310, 350, 140, 50, BUTTON_HOVER_COLOR, BUTTON_COLOR, lambda: set_game_mode('menu'))

# --- Logika AI (Sama seperti sebelumnya) ---
def get_available_moves():
    moves = []
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                moves.append((row, col))
    return moves

def ai_easy():
    moves = get_available_moves()
    return random.choice(moves) if moves else None

def minimax(is_maximizing):
    if check_win(2): return 1
    if check_win(1): return -1
    if check_draw(): return 0

    scores = []
    for row, col in get_available_moves():
        if is_maximizing:
            board[row][col] = 2
            scores.append(minimax(False))
            board[row][col] = None
        else:
            board[row][col] = 1
            scores.append(minimax(True))
            board[row][col] = None
    
    return max(scores) if is_maximizing else min(scores)

def ai_hard():
    best_score = -math.inf
    best_move = None
    for row, col in get_available_moves():
        board[row][col] = 2
        score = minimax(False)
        board[row][col] = None
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move

# --- Loop Utama Game ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_over and game_mode != 'menu':
                mouseX, mouseY = event.pos
                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)

                if clicked_row < 3: # Memastikan klik di dalam papan
                    # Giliran Pemain
                    if (game_mode == 'pvp' or (game_mode in ['pve_easy', 'pve_hard'] and player == 1)):
                        if mark_square(clicked_row, clicked_col, player):
                            if check_win(player):
                                winner = player
                                game_over = True
                            elif check_draw():
                                game_over = True
                            else:
                                player = 2 if player == 1 else 1

    # --- Bagian Render ---
    if game_mode == 'menu':
        show_menu()
    else:
        screen.fill(BG_COLOR)
        draw_lines()
        draw_figures()
        draw_turn_indicator() # Tampilkan giliran di bawah

        # Giliran AI (setelah giliran pemain selesai)
        if not game_over and game_mode in ['pve_easy', 'pve_hard'] and player == 2:
            pygame.time.wait(400) # Jeda agar AI tidak instan
            move = ai_easy() if game_mode == 'pve_easy' else ai_hard()
            if move:
                mark_square(move[0], move[1], player)
                if check_win(player):
                    winner = player
                    game_over = True
                elif check_draw():
                    game_over = True
                else:
                    player = 1
        
        # --- MENAMPILKAN POPUP JIKA GAME BERAKHIR ---
        if game_over:
            draw_winner_popup()

    pygame.display.update()