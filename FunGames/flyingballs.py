import pygame
import random

# Khởi tạo pygame
pygame.init()

# Thiết lập kích thước màn hình và màu sắc
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flying balls")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Tốc độ khởi đầu
SPEED_RANGE = [-5, -4, -3, 3, 4, 5]
MAX_BALLS = 100
BALL_RADIUS = 10

# Lớp đại diện cho quả bóng
class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        # Di chuyển bóng
        self.x += self.speed_x
        self.y += self.speed_y

        # Va chạm với tường
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.speed_x = -self.speed_x
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.speed_y = -self.speed_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Hàm để kiểm tra va chạm giữa hai quả bóng
def check_collision(ball1, ball2):
    distance = ((ball1.x - ball2.x)**2 + (ball1.y - ball2.y)**2)**0.5
    return distance <= ball1.radius + ball2.radius

# Hàm để xử lý va chạm
def handle_collision(ball1, ball2, balls):
    if ball1.color == ball2.color:
        ball1.speed_x *= -2
        ball1.speed_y *= -2
        ball2.speed_x *= -2
        ball2.speed_y *= -2
    elif len(balls) < MAX_BALLS:
        new_ball = Ball(
            random.randint(20, WIDTH - 20),
            random.randint(20, HEIGHT - 20),
            BALL_RADIUS,
            random.choice(COLORS),
            random.choice(SPEED_RANGE),
            random.choice(SPEED_RANGE),
        )
        balls.append(new_ball)

# Hàm để khởi động lại trò chơi
def reset_game():
    return [
        Ball(
            random.randint(20, WIDTH - 20),
            random.randint(20, HEIGHT - 20),
            BALL_RADIUS,
            random.choice(COLORS),
            random.choice(SPEED_RANGE),
            random.choice(SPEED_RANGE),
        )
        for _ in range(5)
    ]

# Khởi tạo danh sách bóng
balls = reset_game()

# Vòng lặp chính
running = True
game_over = False
clock = pygame.time.Clock()

font = pygame.font.Font("fonts/Roboto-VariableFont_wdth,wght.ttf", 36)

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                balls = reset_game()
                game_over = False

    if not game_over:
        # Di chuyển và vẽ bóng
        for ball in balls:
            ball.move()
            ball.draw(screen)

        # Kiểm tra và xử lý va chạm
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                if check_collision(balls[i], balls[j]):
                    handle_collision(balls[i], balls[j], balls)

        # Kiểm tra trạng thái trò chơi
        if len(balls) >= MAX_BALLS:
            game_over = True

    # Hiển thị thông báo khi trò chơi kết thúc
    if game_over:
        message = f"Số lượng bóng: {len(balls)}. Nhấn R để chơi lại."
        text = font.render(message, True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    # Cập nhật màn hình
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
