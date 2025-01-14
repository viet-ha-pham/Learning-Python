import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ trò chơi
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Trò chơi Theo Đuổi Thần Tượng')

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Tải hình ảnh cho nhân vật và thần tượng
player_image = pygame.Surface((50, 50))
player_image.fill(RED)
idol_image = pygame.Surface((50, 50))
idol_image.fill((0, 0, 255))

# Khởi tạo đối tượng nhân vật và thần tượng
player_rect = player_image.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT - 50)

idol_rect = idol_image.get_rect()
idol_rect.center = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT // 2))

# Tốc độ di chuyển của nhân vật
player_speed = 5

# Đồng hồ để kiểm soát tốc độ cập nhật màn hình
clock = pygame.time.Clock()

# Biến đếm điểm
score = 0
font = pygame.font.SysFont('Arial', 30)


# Hàm vẽ điểm số
def draw_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))


# Vòng lặp chính của trò chơi
running = True
while running:
    screen.fill(WHITE)

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Điều khiển di chuyển nhân vật
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += player_speed
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect.y += player_speed

    # Kiểm tra xem nhân vật có đến được thần tượng không
    if player_rect.colliderect(idol_rect):
        score += 1
        idol_rect.center = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT // 2))  # Đổi vị trí thần tượng

    # Vẽ nhân vật và thần tượng
    screen.blit(player_image, player_rect)
    screen.blit(idol_image, idol_rect)

    # Vẽ điểm số
    draw_score()

    # Cập nhật màn hình
    pygame.display.flip()

    # Điều khiển tốc độ trò chơi
    clock.tick(30)

# Thoát trò chơi
pygame.quit()
