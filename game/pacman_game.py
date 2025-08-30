import pygame
import random
import math # --- BARU --- Kita butuh modul math untuk kalkulasi sudut

# Inisialisasi Pygame
pygame.init()

# --- Konstanta ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 670
BLOCK_SIZE = 20

# Warna (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PINK = (255, 182, 193)
CYAN = (0, 255, 255)

# Setup layar
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man Sederhana")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
button_font = pygame.font.Font(None, 40)

# --- Layout Peta (Maze) ---
# (Tidak ada perubahan di sini, jadi saya singkat untuk keringkasan)
maze_map = [
    "##############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.#  #.#   #.##.#   #.#  #.#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "     #.#   # ## #   #.#     ",
    "     #.# ###--### #.#     ",
    "######.# #      # #.######",
    "      .  #      #  .      ",
    "######.# #      # #.######",
    "     #.# ######## #.#     ",
    "     #.#    G     #.#     ",
    "######.# ######## #.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#...##.......P .......##...#",
    "###.##.##.########.##.##.###",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#..........................#",
    "##############################",
]


# --- Class untuk Player (Pac-Man) ---
class Player:
    # --- DIMODIFIKASI --- Menambahkan atribut untuk animasi
    def __init__(self, x, y):
        self.start_x, self.start_y = x, y
        self.x = x
        self.y = y
        self.radius = BLOCK_SIZE // 2 - 2
        self.speed = BLOCK_SIZE
        self.direction = 'STOP'
        self.next_direction = 'STOP'
        
        # --- BARU --- Atribut untuk animasi mulut
        self.mouth_angle = 10  # Sudut mulut awal
        self.mouth_change = 5    # Kecepatan buka/tutup
        self.animation_timer = 0
        self.animation_speed = 3 # Ganti frame animasi setiap 3 tick

    def set_direction(self, direction):
        self.next_direction = direction

    def move(self, maze):
        # Coba ubah arah jika memungkinkan
        if self.next_direction != 'STOP':
            nx_temp, ny_temp = self._get_next_pos(self.next_direction)
            if not self._is_wall(nx_temp, ny_temp, maze):
                self.direction = self.next_direction

        # Gerakkan Pac-Man sesuai arah saat ini
        if self.direction != 'STOP':
            nx, ny = self._get_next_pos(self.direction)
            if not self._is_wall(nx, ny, maze):
                self.x, self.y = nx, ny
            else:
                # Berhenti jika menabrak tembok
                self.direction = 'STOP'

    # --- BARU --- Metode untuk mengupdate frame animasi
    def update_animation(self):
        if self.direction == 'STOP': # Jika diam, mulut tertutup
             self.mouth_angle = 0
             return

        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.mouth_angle += self.mouth_change
            if self.mouth_angle >= 45 or self.mouth_angle <= 0:
                self.mouth_change *= -1 # Balikkan arah animasi (dari buka ke tutup, atau sebaliknya)
    
    # --- DIMODIFIKASI TOTAL --- Metode draw diganti untuk menggambar Pac-Man dengan mulut
    def draw(self, surface):
        center_x = self.x + BLOCK_SIZE // 2
        center_y = self.y + BLOCK_SIZE // 2
        
        # Jika berhenti atau sudut mulut 0, gambar lingkaran penuh
        if self.direction == 'STOP' or self.mouth_angle <= 0:
            pygame.draw.circle(surface, YELLOW, (center_x, center_y), self.radius)
            return

        # Tentukan sudut awal dan akhir berdasarkan arah
        angle_rad = math.radians(self.mouth_angle) # Ubah sudut ke radian

        if self.direction == 'RIGHT':
            start_angle = angle_rad
            end_angle = math.radians(360) - angle_rad
        elif self.direction == 'LEFT':
            start_angle = math.radians(180) + angle_rad
            end_angle = math.radians(180) - angle_rad
        elif self.direction == 'UP':
            start_angle = math.radians(90) + angle_rad
            end_angle = math.radians(90) - angle_rad
        elif self.direction == 'DOWN':
            start_angle = math.radians(270) + angle_rad
            end_angle = math.radians(270) - angle_rad
        else: # Default jika terjadi kondisi aneh
            start_angle = angle_rad
            end_angle = math.radians(360) - angle_rad

        # Buat daftar titik untuk polygon Pac-Man
        points = [(center_x, center_y)]
        # Buat titik-titik di sepanjang busur lingkaran
        for n in range(int(math.degrees(start_angle)), int(math.degrees(end_angle))):
             x = center_x + self.radius * math.cos(math.radians(n))
             y = center_y + self.radius * math.sin(math.radians(n))
             points.append((x, y))

        # Gambar Pac-Man sebagai polygon
        pygame.draw.polygon(surface, YELLOW, points)


    def _get_next_pos(self, direction):
        nx, ny = self.x, self.y
        if direction == 'UP': ny -= self.speed
        elif direction == 'DOWN': ny += self.speed
        elif direction == 'LEFT': nx -= self.speed
        elif direction == 'RIGHT': nx += self.speed
        return nx, ny

    def _is_wall(self, x, y, maze):
        map_x = x // BLOCK_SIZE
        map_y = y // BLOCK_SIZE
        return maze[map_y][map_x] == '#'
    
    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.direction = 'STOP'
        self.next_direction = 'STOP'

# --- Class Ghost dan fungsi lainnya tetap sama ---
# (Tidak ada perubahan, dilewati untuk keringkasan)
class Ghost:
    def __init__(self, x, y, color):
        self.start_x, self.start_y = x, y
        self.x = x
        self.y = y
        self.color = color
        self.radius = BLOCK_SIZE // 2 - 2
        self.speed = BLOCK_SIZE
    def move(self, maze, player_pos):
        possible_moves = []
        for direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            nx, ny = self._get_next_pos(direction)
            if not self._is_wall(nx, ny, maze):
                possible_moves.append((direction, nx, ny))
        if not possible_moves: return
        best_move, min_dist = None, float('inf')
        px, py = player_pos
        for direction, nx, ny in possible_moves:
            dist = math.sqrt((nx - px)**2 + (ny - py)**2)
            if dist < min_dist:
                min_dist, best_move = dist, (nx, ny)
        if best_move: self.x, self.y = best_move
    def _get_next_pos(self, direction):
        nx, ny = self.x, self.y
        if direction == 'UP': ny -= self.speed
        elif direction == 'DOWN': ny += self.speed
        elif direction == 'LEFT': nx -= self.speed
        elif direction == 'RIGHT': nx += self.speed
        return nx, ny
    def _is_wall(self, x, y, maze):
        map_x, map_y = x // BLOCK_SIZE, y // BLOCK_SIZE
        return maze[map_y][map_x] in ('#', '-')
    def draw(self, surface):
        center_x, center_y = self.x + BLOCK_SIZE // 2, self.y + BLOCK_SIZE // 2
        pygame.draw.circle(surface, self.color, (center_x, center_y), self.radius)
    def reset(self):
        self.x, self.y = self.start_x, self.start_y

def draw_maze(surface, maze):
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == '#': pygame.draw.rect(surface, BLUE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
def draw_pellets(surface, pellets):
    for pellet in pellets:
        center_x, center_y = pellet[0] + BLOCK_SIZE // 2, pellet[1] + BLOCK_SIZE // 2
        pygame.draw.circle(surface, WHITE, (center_x, center_y), 3)
def draw_text(surface, text, position, color=WHITE, font_to_use=font):
    text_surface = font_to_use.render(text, True, color)
    surface.blit(text_surface, position)
def setup_game_state():
    player, ghosts, pellets = None, [], []
    ghost_colors = [RED, PINK, CYAN, GREEN]
    for y, row in enumerate(maze_map):
        for x, char in enumerate(row):
            if char == 'P': player = Player(x * BLOCK_SIZE, y * BLOCK_SIZE)
            elif char == 'G':
                if ghost_colors: ghosts.append(Ghost(x * BLOCK_SIZE, y * BLOCK_SIZE, ghost_colors.pop(0)))
            elif char == '.': pellets.append((x * BLOCK_SIZE, y * BLOCK_SIZE))
    return player, ghosts, pellets
# --- Akhir dari kode yang tidak berubah ---

# --- Fungsi Utama Game ---
def main():
    player, ghosts, pellets = setup_game_state()
    original_pellets = list(pellets)
    score = 0
    game_over = False
    win = False
    button_rect = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 40, 200, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if (game_over or win) and event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    score, game_over, win = 0, False, False
                    pellets = list(original_pellets)
                    player.reset()
                    for ghost in ghosts: ghost.reset()
            if event.type == pygame.KEYDOWN and not game_over and not win:
                if event.key == pygame.K_UP: player.set_direction('UP')
                elif event.key == pygame.K_DOWN: player.set_direction('DOWN')
                elif event.key == pygame.K_LEFT: player.set_direction('LEFT')
                elif event.key == pygame.K_RIGHT: player.set_direction('RIGHT')

        if not game_over and not win:
            player.move(maze_map)
            player.update_animation() # --- BARU --- Panggil update animasi di setiap frame
            for ghost in ghosts: ghost.move(maze_map, (player.x, player.y))
            if (player.x, player.y) in pellets:
                pellets.remove((player.x, player.y))
                score += 10
            for ghost in ghosts:
                if player.x == ghost.x and player.y == ghost.y: game_over = True
            if not pellets: win = True
        
        screen.fill(BLACK)
        draw_maze(screen, maze_map)
        draw_pellets(screen, pellets)
        player.draw(screen)
        for ghost in ghosts: ghost.draw(screen)
        draw_text(screen, f"SKOR: {score}", (10, SCREEN_HEIGHT - 50))
        if game_over:
            draw_text(screen, "GAME OVER!", (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 20), RED)
            pygame.draw.rect(screen, GREEN, button_rect, border_radius=10)
            draw_text(screen, "Main Lagi?", (button_rect.centerx - 70, button_rect.centery - 18), BLACK, button_font)
        if win:
            draw_text(screen, "KAMU MENANG!", (SCREEN_WIDTH//2 - 110, SCREEN_HEIGHT//2 - 20), GREEN)
            pygame.draw.rect(screen, BLUE, button_rect, border_radius=10)
            draw_text(screen, "Main Lagi?", (button_rect.centerx - 70, button_rect.centery - 18), WHITE, button_font)

        pygame.display.flip()
        clock.tick(10)
    pygame.quit()

if __name__ == "__main__":
    main()