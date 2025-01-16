import pygame
import random

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Số bay qua lại - đổi dấu khi va tường")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Font chữ
font = pygame.font.Font(None, 50)

# Tạo số di chuyển
class MovingNumber:
    def __init__(self, number, x, y, dx, dy):
        self.number = number
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = RED if number < 0 else WHITE

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Đổi hướng khi va chạm tường
        if self.x <= 0 or self.x >= WIDTH - 50:  # Trừ 50 vì kích thước số
            self.dx = -self.dx
            self.number = -self.number
            self.color = RED if self.number < 0 else WHITE

        if self.y <= 0 or self.y >= HEIGHT - 50:
            self.dy = -self.dy
            self.number = -self.number
            self.color = RED if self.number < 0 else WHITE

    def draw(self, screen):
        text = font.render(str(self.number), True, self.color)
        screen.blit(text, (self.x, self.y))


# Tạo danh sách các số
numbers = []
for i in range(10):  # Tạo 10 số ngẫu nhiên
    num = random.randint(-10, 10)
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    dx = random.choice([-3, 3])
    dy = random.choice([-3, 3])
    numbers.append(MovingNumber(num, x, y, dx, dy))

# Vòng lặp chính
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cập nhật vị trí
    for number in numbers:
        number.move()

    # Vẽ màn hình
    screen.fill(BLACK)
    for number in numbers:
        number.draw(screen)

    pygame.display.flip()
    clock.tick(30)  # Giới hạn FPS

pygame.quit()
