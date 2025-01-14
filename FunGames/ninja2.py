import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sợi chỉ giữa những bóng vàng")

# Màu sắc
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Tốc độ trò chơi
clock = pygame.time.Clock()
FPS = 60

# Kích thước đối tượng
thread_width = 20
thread_height = 20
ball_radius = 15

# Vị trí bắt đầu của sợi chỉ
thread_x = screen_width // 2
thread_y = screen_height // 2

# Tốc độ di chuyển của sợi chỉ
thread_speed = 5

# Danh sách bóng vàng
balls = []


# Hàm tạo bóng vàng mới
def create_ball():
    ball_x = random.randint(ball_radius, screen_width - ball_radius)
    ball_y = random.randint(ball_radius, screen_height - ball_radius)
    balls.append([ball_x, ball_y])


# Hàm vẽ sợi chỉ
def draw_thread(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, thread_width, thread_height))


# Hàm vẽ bóng vàng
def draw_balls():
    for ball in balls:
        pygame.draw.circle(screen, YELLOW, (ball[0], ball[1]), ball_radius)


# Hàm kiểm tra va chạm
def check_collision(thread_x, thread_y, balls):
    for ball in balls:
        dist = ((thread_x + thread_width // 2 - ball[0]) ** 2 + (thread_y + thread_height // 2 - ball[1]) ** 2) ** 0.5
        if dist < ball_radius + thread_width // 2:
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
        thread_x -= thread_speed
    if keys[pygame.K_RIGHT]:
        thread_x += thread_speed
    if keys[pygame.K_UP]:
        thread_y -= thread_speed
    if keys[pygame.K_DOWN]:
        thread_y += thread_speed

    # Giới hạn sợi chỉ không ra ngoài màn hình
    thread_x = max(0, min(thread_x, screen_width - thread_width))
    thread_y = max(0, min(thread_y, screen_height - thread_height))

    # Tạo bóng vàng ngẫu nhiên sau mỗi vài giây
    if random.random() < 0.02:
        create_ball()

    # Vẽ các đối tượng
    draw_thread(thread_x, thread_y)
    draw_balls()

    # Kiểm tra va chạm
    if check_collision(thread_x, thread_y, balls):
        print("Bạn đã thua!")
        running = False

    # Cập nhật màn hình
    pygame.display.flip()

    # Điều chỉnh tốc độ trò chơi
    clock.tick(FPS)

# Thoát Pygame
pygame.quit()
