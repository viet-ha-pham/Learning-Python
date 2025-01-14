import pygame
import random
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Đèn xanh, đèn đỏ")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# FPS và clock
FPS = 60
clock = pygame.time.Clock()

# Kích thước và vị trí của nhân vật
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size
player_speed = 5

# Biến trạng thái trò chơi
game_running = True
green_light = True  # Đèn xanh hoặc đỏ
light_timer = random.randint(3, 6)  # Thời gian cho mỗi trạng thái đèn

# Thời gian đếm ngược
start_time = pygame.time.get_ticks()

# Font
font = pygame.font.Font(None, 74)

# Vùng kết thúc
finish_line = 100

# Vẽ đèn báo
def draw_light():
    light_color = GREEN if green_light else RED
    pygame.draw.circle(screen, light_color, (WIDTH // 2, 50), 30)

# Vẽ nhân vật
def draw_player(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, player_size, player_size))

# Hiển thị thông báo
def show_message(text, color, y_offset=0):
    message = font.render(text, True, color)
    text_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(message, text_rect)

# Vòng lặp trò chơi chính
while game_running:
    screen.fill(WHITE)

    # Tính thời gian thay đổi đèn
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    if elapsed_time >= light_timer:
        green_light = not green_light
        light_timer = random.randint(3, 6)
        start_time = pygame.time.get_ticks()

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Lấy trạng thái phím bấm
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_speed

    # Kiểm tra người chơi di chuyển khi đèn đỏ
    if not green_light and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]):
        show_message("Bạn đã thua!", RED)
        pygame.display.flip()
        pygame.time.delay(2000)
        game_running = False

    # Kiểm tra người chơi thắng
    if player_y <= finish_line:
        show_message("You win!", GREEN)
        pygame.display.flip()
        pygame.time.delay(2000)
        game_running = False

    # Vẽ các thành phần trên màn hình
    draw_light()
    draw_player(player_x, player_y)

    # Vẽ vạch đích
    pygame.draw.line(screen, BLACK, (0, finish_line), (WIDTH, finish_line), 5)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
