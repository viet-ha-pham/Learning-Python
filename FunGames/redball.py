import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Trò chơi bắt bóng đỏ")

# Màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
COLORS = [(255, 255, 0), (0, 255, 0), (0, 255, 255), (255, 0, 255)]

# FPS
FPS = 60
clock = pygame.time.Clock()

# Nhân vật
player_size = 50
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player_speed = 5

# Quả bóng
balls = []
for _ in range(10):
    ball = {
        "pos": [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)],
        "radius": random.randint(10, 30),
        "color": random.choice(COLORS),
        "speed": [random.choice([-2, -1, 1, 2]), random.choice([-2, -1, 1, 2])],
    }
    balls.append(ball)

# Quả bóng đỏ lớn
red_ball = {
    "pos": [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)],
    "radius": 40,
    "color": RED,
    "speed": [random.choice([-2, -1, 1, 2]), random.choice([-2, -1, 1, 2])],
}

# Hàm vẽ quả bóng
def draw_ball(ball):
    pygame.draw.circle(screen, ball["color"], (int(ball["pos"][0]), int(ball["pos"][1])), ball["radius"])

# Hàm kiểm tra va chạm
def is_collision(pos1, size1, pos2, radius2):
    distance = ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5
    return distance < size1 / 2 + radius2

# Vòng lặp chính
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Di chuyển nhân vật
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed

    # Giới hạn nhân vật trong màn hình
    player_pos[0] = max(0, min(SCREEN_WIDTH, player_pos[0]))
    player_pos[1] = max(0, min(SCREEN_HEIGHT, player_pos[1]))

    # Di chuyển các quả bóng
    for ball in balls + [red_ball]:
        ball["pos"][0] += ball["speed"][0]
        ball["pos"][1] += ball["speed"][1]

        # Đảo chiều nếu chạm tường
        if ball["pos"][0] - ball["radius"] <= 0 or ball["pos"][0] + ball["radius"] >= SCREEN_WIDTH:
            ball["speed"][0] *= -1
        if ball["pos"][1] - ball["radius"] <= 0 or ball["pos"][1] + ball["radius"] >= SCREEN_HEIGHT:
            ball["speed"][1] *= -1

    # Vẽ các quả bóng
    for ball in balls:
        draw_ball(ball)

    # Vẽ quả bóng đỏ
    draw_ball(red_ball)

    # Vẽ nhân vật
    pygame.draw.rect(screen, BLUE, (player_pos[0] - player_size // 2, player_pos[1] - player_size // 2, player_size, player_size))

    # Kiểm tra va chạm với quả bóng đỏ
    if is_collision(player_pos, player_size, red_ball["pos"], red_ball["radius"]):
        print("Bạn đã chạm vào quả bóng đỏ! Chiến thắng!")
        running = False

    # Cập nhật màn hình
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
