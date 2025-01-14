import pygame
import random
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trò chơi cửa sập")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# FPS
FPS = 60
clock = pygame.time.Clock()

# Nhân vật
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 8

# Cửa sập
trap_width = 100
trap_height = 20
traps = []  # Danh sách cửa sập
trap_speed = 6
spawn_interval = 1500  # Thời gian giữa các lần tạo cửa sập (ms)

# Điểm số
score = 0
font = pygame.font.Font(None, 36)

# Thời gian
last_spawn_time = pygame.time.get_ticks()


def draw_text(text, x, y, color=WHITE):
    """Hàm vẽ văn bản lên màn hình."""
    label = font.render(text, True, color)
    screen.blit(label, (x, y))


# Vòng lặp trò chơi
running = True
while running:
    screen.fill(BLACK)

    # Kiểm tra sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Điều khiển nhân vật
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Tạo cửa sập mới
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time > spawn_interval:
        trap_x = random.randint(0, WIDTH - trap_width)
        traps.append([trap_x, 0])  # Thêm cửa sập mới
        last_spawn_time = current_time

    # Di chuyển cửa sập
    for trap in traps:
        trap[1] += trap_speed

    # Xóa cửa sập khi ra khỏi màn hình
    traps = [trap for trap in traps if trap[1] < HEIGHT]

    # Kiểm tra va chạm
    for trap in traps:
        if (
            player_x < trap[0] + trap_width
            and player_x + player_size > trap[0]
            and player_y < trap[1] + trap_height
            and player_y + player_size > trap[1]
        ):
            running = False

    # Vẽ nhân vật
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    # Vẽ cửa sập
    for trap in traps:
        pygame.draw.rect(screen, RED, (trap[0], trap[1], trap_width, trap_height))

    # Hiển thị điểm
    score += 1
    draw_text(f"Điểm: {score}", 10, 10)

    # Cập nhật màn hình
    pygame.display.flip()
    clock.tick(FPS)

# Hiển thị màn hình kết thúc
screen.fill(BLACK)
draw_text("Game Over", WIDTH // 2 - 70, HEIGHT // 2 - 20, RED)
draw_text(f"Điểm của bạn: {score}", WIDTH // 2 - 100, HEIGHT // 2 + 20, WHITE)
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
