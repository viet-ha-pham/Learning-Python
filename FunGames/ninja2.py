import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Square")

# Màu sắc
BLACK = (0, 0, 0)
YELLOW = (200, 255, 10)
RED = (255, 0, 0)

# Tốc độ trò chơi
clock = pygame.time.Clock()
FPS = 60

# Kích thước đối tượng
square_width = 20
square_height = 20
ball_radius = 15

# Vị trí bắt đầu của hình vuông
square_x = screen_width // 2
square_y = screen_height // 2

# Tốc độ di chuyển của hình vuông
square_speed = 5

# Danh sách bóng vàng
balls = []


# Hàm tạo bóng vàng mới
def create_ball():
    ball_x = random.randint(ball_radius, screen_width - ball_radius)
    ball_y = random.randint(ball_radius, screen_height - ball_radius)
    balls.append([ball_x, ball_y])


# Hàm vẽ hình vuông
def draw_square(x, y):
    pygame.draw.rect(screen, RED, (x, y, square_width, square_height))


# Hàm vẽ bóng vàng
def draw_balls():
    for ball in balls:
        pygame.draw.circle(screen, YELLOW, (ball[0], ball[1]), ball_radius)


# Hàm kiểm tra va chạm
def check_collision(thread_x, thread_y, balls):
    for ball in balls:
        dist = ((thread_x + square_width // 2 - ball[0]) ** 2 + (thread_y + square_height // 2 - ball[1]) ** 2) ** 0.5
        if dist < ball_radius + square_width // 2:
            return True
    return False


# Chạy trò chơi
running = True
while running:
    screen.fill(BLACK)

    # Kiểm tra các sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lấy các phím bấm
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        square_x -= square_speed
    if keys[pygame.K_RIGHT]:
        square_x += square_speed
    if keys[pygame.K_UP]:
        square_y -= square_speed
    if keys[pygame.K_DOWN]:
        square_y += square_speed

    # Giới hạn sợi chỉ không ra ngoài màn hình
    square_x = max(0, min(square_x, screen_width - square_width))
    square_y = max(0, min(square_y, screen_height - square_height))

    # Tạo bóng vàng ngẫu nhiên sau mỗi vài giây
    if random.random() < 0.02:
        create_ball()

    # Vẽ các đối tượng
    draw_square(square_x, square_y)
    draw_balls()

    # Kiểm tra va chạm
    if check_collision(square_x, square_y, balls):
        print("Bạn đã thua!")
        running = False

    # Cập nhật màn hình
    pygame.display.flip()

    # Điều chỉnh tốc độ trò chơi
    clock.tick(FPS)

# Thoát Pygame
pygame.quit()
