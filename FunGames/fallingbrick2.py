import pygame
import random
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trò chơi cửa sập - Cửa sập bất thường")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# FPS và Clock
FPS = 60
clock = pygame.time.Clock()

# Nhân vật chính
player_width, player_height = 50, 50
player_x = WIDTH // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Danh sách cửa sập
trap_height = 20
traps = []
trap_speed = 4
trap_spawn_time = 1500  # Thời gian giữa các cửa sập (ms)
last_trap_spawn = pygame.time.get_ticks()

# Điểm
score = 0
font = pygame.font.Font(None, 36)

# Hàm vẽ nhân vật và cửa sập
def draw_objects():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    for trap in traps:
        pygame.draw.rect(screen, RED, trap)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

# Hàm kết thúc trò chơi
def game_over():
    over_text = font.render("Game Over! Press R to Restart or Q to Quit", True, BLACK)
    screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

# Vòng lặp chính
running = True
while running:
    clock.tick(FPS)

    # Kiểm tra sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Điều khiển nhân vật
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Tạo cửa sập mới với độ rộng ngẫu nhiên
    current_time = pygame.time.get_ticks()
    if current_time - last_trap_spawn > trap_spawn_time:
        trap_width = random.randint(50, 150)  # Độ rộng ngẫu nhiên từ 50 đến 150
        trap_x = random.randint(0, WIDTH - trap_width)
        traps.append(pygame.Rect(trap_x, 0, trap_width, trap_height))
        last_trap_spawn = current_time

    # Di chuyển cửa sập
    for trap in traps:
        trap.y += trap_speed
        if trap.colliderect((player_x, player_y, player_width, player_height)):
            game_over()
            running = False
        if trap.y > HEIGHT:
            traps.remove(trap)
            score += 1

    # Vẽ các đối tượng
    draw_objects()

# Thoát game
pygame.quit()
sys.exit()
