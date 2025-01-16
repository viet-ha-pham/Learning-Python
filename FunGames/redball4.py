import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trò chơi quả bóng")

# Màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)


# Tạo lớp quả bóng
class Ball:
    def __init__(self, color, radius, x, y, dx, dy):
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # Đảm bảo quả bóng không ra ngoài màn hình
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.dx = -self.dx
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.dy = -self.dy

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def check_collision(self, other):
        distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return distance < self.radius + other.radius

    def bounce(self, other):
        # Đổi hướng khi va chạm
        self.dx = -self.dx
        self.dy = -self.dy


# Tạo hình vuông
class Square:
    def __init__(self, color, size, x, y, dx, dy):
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # Đảm bảo hình vuông không ra ngoài màn hình
        if self.x < 0:
            self.x = 0
        if self.x + self.size > WIDTH:
            self.x = WIDTH - self.size
        if self.y < 0:
            self.y = 0
        if self.y + self.size > HEIGHT:
            self.y = HEIGHT - self.size

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def check_collision(self, ball):
        ball_rect = pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2)
        square_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        return ball_rect.colliderect(square_rect)

    def bounce(self, ball):
        # Đổi hướng khi va chạm
        self.dx = -self.dx
        self.dy = -self.dy


# Tạo danh sách quả bóng và hình vuông
balls = []
for _ in range(5):  # Tạo 5 quả bóng nhỏ ngẫu nhiên
    radius = random.randint(15, 30)
    color = random.choice([BLUE, GREEN, YELLOW])
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    dx = random.choice([-3, 3])
    dy = random.choice([-3, 3])
    balls.append(Ball(color, radius, x, y, dx, dy))

# Tạo quả bóng đỏ lớn
big_ball = Ball(RED, 50, WIDTH // 2, HEIGHT // 2, 2, 2)

# Tạo hình vuông
square = Square(RED, 40, WIDTH // 2, HEIGHT // 2 + 100, 0, 0)

# Vòng lặp trò chơi
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lấy thông tin bàn phím để điều khiển hình vuông
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        square.dx = -5
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        square.dx = 5
    else:
        square.dx = 0

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        square.dy = -5
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        square.dy = 5
    else:
        square.dy = 0

    # Di chuyển quả bóng và hình vuông
    big_ball.move()
    square.move()

    # Kiểm tra va chạm giữa quả bóng đỏ và các quả bóng nhỏ
    for ball in balls:
        if big_ball.check_collision(ball):
            big_ball.bounce(ball)  # Nảy ra khi va chạm
            ball.bounce(big_ball)  # Quả bóng nhỏ cũng nảy ra

    # Kiểm tra va chạm giữa hình vuông và các quả bóng nhỏ
    for ball in balls:
        if square.check_collision(ball):
            square.bounce(ball)  # Nảy ra khi va chạm
            ball.bounce(square)  # Quả bóng nhỏ cũng nảy ra

    # Vẽ quả bóng và hình vuông
    big_ball.draw()
    square.draw()

    # Vẽ các quả bóng nhỏ còn lại
    for ball in balls:
        ball.move()
        ball.draw()

    pygame.display.update()
    pygame.time.delay(10)

pygame.quit()
