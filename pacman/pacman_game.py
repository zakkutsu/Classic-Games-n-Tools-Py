import pygame
import random
import math

# Inisialisasi Pygame
pygame.init()

# --- Konstanta ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 670
BLOCK_SIZE = 20
# --- DIMODIFIKASI --- Konstanta baru untuk kecepatan berbasis waktu
INITIAL_FPS = 7.0  # Kecepatan awal (float agar presisi)
SPEED_INCREASE_INTERVAL = 3000 # Interval dalam milidetik (3 detik)
SPEED_INCREASE_FACTOR = 1.10 # Faktor kenaikan 10%

# Warna (R, G, B)
BLACK, WHITE, BLUE = (0, 0, 0), (255, 255, 255), (0, 0, 255)
YELLOW, RED, GREEN = (255, 255, 0), (255, 0, 0), (0, 255, 0)
PINK, CYAN = (255, 182, 193), (0, 255, 255)

# Setup layar
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
button_font = pygame.font.Font(None, 40)

# (Class Player, Ghost, dan fungsi lainnya tidak berubah)
# --- Layout Peta (Maze) ---
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

class Player:
    def __init__(self, x, y):
        self.start_x, self.start_y = x, y; self.x, self.y = x, y
        self.radius = BLOCK_SIZE // 2 - 2; self.speed = BLOCK_SIZE
        self.direction, self.next_direction = 'STOP', 'STOP'
        self.mouth_angle, self.mouth_change = 10, 5
        self.animation_timer, self.animation_speed = 0, 3
    def set_direction(self, direction): self.next_direction = direction
   # GANTI TOTAL FUNGSI MOVE ANDA DENGAN VERSI FINAL INI
    def move(self, maze):
        # Tentukan arah prioritas (input baru dari pemain)
        if self.next_direction != 'STOP':
            nx_temp, ny_temp = self._get_next_pos(self.next_direction)
            # Logika lorong untuk pengecekan arah
            if nx_temp < 0: nx_temp = SCREEN_WIDTH - BLOCK_SIZE
            elif nx_temp >= SCREEN_WIDTH: nx_temp = 0
            
            if not self._is_wall(nx_temp, ny_temp, maze):
                self.direction = self.next_direction
        
        # Jika tidak ada arah, jangan bergerak
        if self.direction == 'STOP':
            return

        # Dapatkan posisi berikutnya berdasarkan arah saat ini
        nx, ny = self._get_next_pos(self.direction)

        # --- LOGIKA LORONG YANG DISESUAIKAN UNTUK MAZE BARU ANDA ---
        if nx < 0:
            # Jika keluar ke kiri, muncul di kolom kedua dari kanan (kolom 28)
            self.x = SCREEN_WIDTH - (2 * BLOCK_SIZE)
            return
        elif nx >= SCREEN_WIDTH:
            # Jika keluar ke kanan, muncul di kolom kedua dari kiri (kolom 1)
            self.x = BLOCK_SIZE
            return
        # --- AKHIR PERBAIKAN ---

        # Cek tembok dan bergerak
        if not self._is_wall(nx, ny, maze):
            self.x, self.y = nx, ny
        else:
            self.direction = 'STOP'
    def update_animation(self):
        if self.direction == 'STOP': self.mouth_angle = 0; return
        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.mouth_angle += self.mouth_change
            if self.mouth_angle >= 45 or self.mouth_angle <= 0: self.mouth_change *= -1
    def draw(self, surface):
        center_x, center_y = self.x + BLOCK_SIZE // 2, self.y + BLOCK_SIZE // 2
        if self.direction == 'STOP' or self.mouth_angle <= 0:
            pygame.draw.circle(surface, YELLOW, (center_x, center_y), self.radius); return
        angle_rad = math.radians(self.mouth_angle)
        if self.direction == 'RIGHT': start_angle, end_angle = angle_rad, math.radians(360) - angle_rad
        elif self.direction == 'LEFT': start_angle, end_angle = math.radians(180) + angle_rad, math.radians(180) - angle_rad
        elif self.direction == 'UP': start_angle, end_angle = math.radians(90) + angle_rad, math.radians(90) - angle_rad
        else: start_angle, end_angle = math.radians(270) + angle_rad, math.radians(270) - angle_rad
        points = [(center_x, center_y)]; start_deg, end_deg = int(math.degrees(start_angle)), int(math.degrees(end_angle))
        if start_deg > end_deg:
            for n in range(start_deg, 360): points.append((center_x + self.radius * math.cos(math.radians(n)), center_y + self.radius * math.sin(math.radians(n))))
            for n in range(0, end_deg): points.append((center_x + self.radius * math.cos(math.radians(n)), center_y + self.radius * math.sin(math.radians(n))))
        else:
            for n in range(start_deg, end_deg): points.append((center_x + self.radius * math.cos(math.radians(n)), center_y + self.radius * math.sin(math.radians(n))))
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
        
        # Guard clause dinamis yang seharusnya mencegah error
        if map_y < 0 or map_y >= len(maze) or map_x < 0 or map_x >= len(maze[map_y]):
            return True # Anggap di luar peta sebagai tembok
            
        return maze[map_y][map_x] == '#'
    def reset(self): self.x, self.y = self.start_x, self.start_y; self.direction, self.next_direction = 'STOP', 'STOP'

class Ghost:
    def __init__(self, x, y, color):
        self.start_x, self.start_y, self.x, self.y = x, y, x, y
        self.color, self.radius, self.speed = color, BLOCK_SIZE // 2 - 2, BLOCK_SIZE
    def move(self, maze, player_pos):
        possible_moves, best_move, min_dist = [], None, float('inf')
        for direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            nx, ny = self._get_next_pos(direction)
            if not self._is_wall(nx, ny, maze): possible_moves.append((direction, nx, ny))
        if not possible_moves: return
        px, py = player_pos
        for direction, nx, ny in possible_moves:
            dist = math.sqrt((nx - px)**2 + (ny - py)**2)
            if dist < min_dist: min_dist, best_move = dist, (nx, ny)
        if best_move: self.x, self.y = best_move
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

        # --- Guard clause dinamis yang lebih aman ---
        if map_y < 0 or map_y >= len(maze) or map_x < 0 or map_x >= len(maze[map_y]):
            return True # Anggap di luar peta sebagai tembok

        return maze[map_y][map_x] in ('#', '-')
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x + BLOCK_SIZE // 2, self.y + BLOCK_SIZE // 2), self.radius)
    def reset(self): self.x, self.y = self.start_x, self.start_y

def draw_maze(surface, maze):
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == '#': pygame.draw.rect(surface, BLUE, (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
def draw_pellets(surface, pellets):
    for pellet in pellets:
        pygame.draw.circle(surface, WHITE, (pellet[0] + BLOCK_SIZE // 2, pellet[1] + BLOCK_SIZE // 2), 3)
def draw_text(surface, text, pos, color=WHITE, font_to_use=font):
    surface.blit(font_to_use.render(text, True, color), pos)
def setup_game_state():
    player, ghosts, pellets, ghost_colors = None, [], [], [RED, PINK, CYAN, GREEN]
    for y, row in enumerate(maze_map):
        for x, char in enumerate(row):
            if char == 'P': player = Player(x*BLOCK_SIZE, y*BLOCK_SIZE)
            elif char == 'G' and ghost_colors: ghosts.append(Ghost(x*BLOCK_SIZE, y*BLOCK_SIZE, ghost_colors.pop(0)))
            elif char == '.': pellets.append((x*BLOCK_SIZE, y*BLOCK_SIZE))
    return player, ghosts, pellets

# --- Fungsi Utama Game ---
def main():
    player, ghosts, pellets = setup_game_state()
    original_pellets = list(pellets)
    score = 0
    game_over = False
    win = False
    
    # --- DIMODIFIKASI --- Variabel baru untuk kecepatan berbasis waktu
    fps = INITIAL_FPS
    last_speedup_time = pygame.time.get_ticks() # Catat waktu awal
    
    button_rect = pygame.Rect(SCREEN_WIDTH//2-100, SCREEN_HEIGHT//2+40, 200, 50)
    running = True
    while running:
        # --- BARU --- Logika untuk menaikkan kecepatan berdasarkan waktu
        current_time = pygame.time.get_ticks()
        if not game_over and not win: # Hanya naikkan kecepatan jika game berjalan
            if current_time - last_speedup_time > SPEED_INCREASE_INTERVAL:
                fps *= SPEED_INCREASE_FACTOR # Naikkan FPS sebesar 10%
                last_speedup_time = current_time # Reset timer

        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if (game_over or win) and event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    score, game_over, win = 0, False, False
                    pellets = list(original_pellets)
                    player.reset()
                    for ghost in ghosts: ghost.reset()
                    
                    # --- DIMODIFIKASI --- Reset kecepatan dan timer saat game diulang
                    fps = INITIAL_FPS
                    last_speedup_time = pygame.time.get_ticks()

            if event.type == pygame.KEYDOWN and not game_over and not win:
                if event.key == pygame.K_UP: player.set_direction('UP')
                elif event.key == pygame.K_DOWN: player.set_direction('DOWN')
                elif event.key == pygame.K_LEFT: player.set_direction('LEFT')
                elif event.key == pygame.K_RIGHT: player.set_direction('RIGHT')

        if not game_over and not win:
            player.move(maze_map); player.update_animation()
            for ghost in ghosts: ghost.move(maze_map, (player.x, player.y))
            if (player.x, player.y) in pellets:
                pellets.remove((player.x, player.y)); score += 10
            for ghost in ghosts:
                if player.x == ghost.x and player.y == ghost.y: game_over = True
            if not pellets: win = True
        
        screen.fill(BLACK)
        draw_maze(screen, maze_map); draw_pellets(screen, pellets)
        player.draw(screen)
        for ghost in ghosts: ghost.draw(screen)
        draw_text(screen, f"SKOR: {score}", (10, SCREEN_HEIGHT-50))
        # --- DIMODIFIKASI --- Menampilkan FPS dengan format desimal
        draw_text(screen, f"FPS: {fps:.1f}", (SCREEN_WIDTH-120, SCREEN_HEIGHT-50))
        
        if game_over:
            draw_text(screen, "GAME OVER!", (SCREEN_WIDTH//2-100, SCREEN_HEIGHT//2-20), RED)
            pygame.draw.rect(screen, GREEN, button_rect, border_radius=10)
            draw_text(screen, "Main Lagi?", (button_rect.centerx-70, button_rect.centery-18), BLACK, button_font)
        if win:
            draw_text(screen, "KAMU MENANG!", (SCREEN_WIDTH//2-110, SCREEN_HEIGHT//2-20), GREEN)
            pygame.draw.rect(screen, BLUE, button_rect, border_radius=10)
            draw_text(screen, "Main Lagi?", (button_rect.centerx-70, button_rect.centery-18), WHITE, button_font)

        pygame.display.flip()
        
        # --- DIMODIFIKASI --- Menggunakan variabel fps yang dinamis
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()