import pygame
import random

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Trò chơi chia hết")

# Màu sắc
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Font chữ
font = pygame.font.Font(None, 36)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Lớp đại diện cho số bay qua lại
class FlyingNumber:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.vx = random.choice([-3, 3])
        self.vy = random.choice([-3, 3])
        self.color = BLUE

    def move(self):
        self.x += self.vx
        self.y += self.vy
        # Va chạm với tường
        if self.x <= 0 or self.x >= SCREEN_WIDTH - 30:
            self.vx *= -1
        if self.y <= 0 or self.y >= SCREEN_HEIGHT - 30:
            self.vy *= -1

    def draw(self, surface):
        text = font.render(str(self.value), True, self.color)
        surface.blit(text, (self.x, self.y))

    def collide(self, other):
        return (
            self.x < other.x + 30 and
            self.x + 30 > other.x and
            self.y < other.y + 30 and
            self.y + 30 > other.y
        )

# Lớp đại diện cho kết quả phép chia
class Result:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.vx = random.choice([-2, 2])
        self.vy = random.choice([-2, 2])
        self.color = RED

    def move(self):
        self.x += self.vx
        self.y += self.vy
        # Va chạm với tường
        if self.x <= 0 or self.x >= SCREEN_WIDTH - 50:
            self.vx *= -1
        if self.y <= 0 or self.y >= SCREEN_HEIGHT - 50:
            self.vy *= -1

    def draw(self, surface):
        text = font.render(str(self.value), True, self.color)
        surface.blit(text, (self.x, self.y))

# Danh sách các số và kết quả
numbers = [FlyingNumber(random.randint(1, 10), random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 50)) for _ in range(10)]
results = []

# Vòng lặp chính
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Di chuyển và vẽ các số
    for number in numbers:
        number.move()
        number.draw(screen)

    # Di chuyển và vẽ các kết quả
    for result in results:
        result.move()
        result.draw(screen)

    # Kiểm tra va chạm và xử lý
    to_remove = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i].collide(numbers[j]) and i not in to_remove and j not in to_remove:
                if numbers[i].value % numbers[j].value == 0:
                    result_value = numbers[i].value // numbers[j].value
                    results.append(Result(result_value, numbers[i].x, numbers[i].y))
                    to_remove.add(i)
                    to_remove.add(j)
                elif numbers[j].value % numbers[i].value == 0:
                    result_value = numbers[j].value // numbers[i].value
                    results.append(Result(result_value, numbers[j].x, numbers[j].y))
                    to_remove.add(i)
                    to_remove.add(j)

    # Xóa các số bị va chạm
    numbers = [number for index, number in enumerate(numbers) if index not in to_remove]

    # Cập nhật màn hình
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
