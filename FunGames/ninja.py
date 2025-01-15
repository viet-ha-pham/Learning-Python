import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bao Vây Thần Tượng')

# Màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Các thông số
player_radius = 10
idol_radius = 30
player_speed = 5
idol_pos = (WIDTH // 2, HEIGHT // 2)
enemy_speed = 1
clock = pygame.time.Clock()

# Khởi tạo nhân vật người chơi
player = pygame.Rect(WIDTH // 2, HEIGHT - 50, player_radius * 2, player_radius * 2)

# Khởi tạo đối thủ
enemies = []
for _ in range(50):
    enemy = pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 20, 20)
    enemies.append(enemy)

# Hàm vẽ
def draw():
    screen.fill(WHITE)
    pygame.draw.circle(screen, GREEN, idol_pos, idol_radius)  # Thần tượng
    pygame.draw.circle(screen, BLUE, player.center, player_radius)  # Người chơi
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)  # Đối thủ
    pygame.display.update()

# Hàm kiểm tra va chạm
def check_collision(rect, circle_center, radius):
    circle_rect = pygame.Rect(circle_center[0] - radius, circle_center[1] - radius, radius * 2, radius * 2)
    return rect.colliderect(circle_rect)

# Main game loop
running = True
while running:
    clock.tick(60)  # 60 FPS

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Điều khiển nhân vật
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Di chuyển đối thủ
    for enemy in enemies:
        enemy.x += random.choice([-1, 1]) * enemy_speed
        enemy.y += random.choice([-1, 1]) * enemy_speed

    # Kiểm tra va chạm giữa người chơi và thần tượng
    if check_collision(player, idol_pos, idol_radius):
        print("Bạn đã đến đích thành công!")
        running = False

    # Kiểm tra va chạm với đối thủ
    for enemy in enemies:
        if check_collision(player, enemy.center, 10):
            print("Game Over! Bạn đã bị đối thủ bắt.")
            running = False

    # Vẽ lại tất cả các đối tượng
    draw()

pygame.quit()
