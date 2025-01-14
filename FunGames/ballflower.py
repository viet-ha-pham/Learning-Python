import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click Bóng Ăn Hoa")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Tạo đối tượng bóng và hoa
ball_radius = 20
flower_radius = 10

# Khởi tạo vị trí ngẫu nhiên của bóng và hoa
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = random.randint(ball_radius, HEIGHT - ball_radius)
flower_x = random.randint(flower_radius, WIDTH - flower_radius)
flower_y = random.randint(flower_radius, HEIGHT - flower_radius)

# Tốc độ di chuyển của bóng
ball_speed_x = random.choice([-5, 5])
ball_speed_y = random.choice([-5, 5])

# Điểm
score = 0
font = pygame.font.SysFont(None, 36)

# Hàm vẽ bóng
def draw_ball(x, y):
    pygame.draw.circle(screen, RED, (x, y), ball_radius)

# Hàm vẽ hoa
def draw_flower(x, y):
    pygame.draw.circle(screen, YELLOW, (x, y), flower_radius)

# Hàm vẽ điểm số
def draw_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Vòng lặp trò chơi
running = True
while running:
    screen.fill(WHITE)

    # Kiểm tra sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Kiểm tra nếu click vào hoa
            if (flower_x - mouse_x)**2 + (flower_y - mouse_y)**2 <= flower_radius**2:
                # Tăng điểm và tạo hoa mới ở vị trí ngẫu nhiên
                score += 1
                flower_x = random.randint(flower_radius, WIDTH - flower_radius)
                flower_y = random.randint(flower_radius, HEIGHT - flower_radius)
            # Kiểm tra nếu click vào bóng
            elif (ball_x - mouse_x)**2 + (ball_y - mouse_y)**2 <= ball_radius**2:
                # Tăng 5 điểm
                score += 5

    # Di chuyển bóng
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Đổi hướng bóng khi va chạm với biên
    if ball_x <= ball_radius or ball_x >= WIDTH - ball_radius:
        ball_speed_x = -ball_speed_x
    if ball_y <= ball_radius or ball_y >= HEIGHT - ball_radius:
        ball_speed_y = -ball_speed_y

    # Vẽ bóng và hoa lên màn hình
    draw_ball(ball_x, ball_y)
    draw_flower(flower_x, flower_y)
    draw_score(score)

    # Cập nhật màn hình
    pygame.display.flip()

    # Đặt tốc độ khung hình
    pygame.time.Clock().tick(60)

# Thoát trò chơi
pygame.quit()
