import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Số chẵn và số lẻ")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Phông chữ
font = pygame.font.Font(None, 36)

# Tạo đối tượng số
class Number:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.vx = random.choice([-2, -1, 1, 2])
        self.vy = random.choice([-2, -1, 1, 2])

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Va chạm biên
        if self.x < 0 or self.x > WIDTH:
            self.vx = -self.vx
        if self.y < 0 or self.y > HEIGHT:
            self.vy = -self.vy

    def draw(self, screen):
        text = font.render(str(self.value), True, BLACK)
        screen.blit(text, (self.x, self.y))

    def get_rect(self):
        text = font.render(str(self.value), True, BLACK)
        return text.get_rect(topleft=(self.x, self.y))

# Kiểm tra va chạm
def check_collision(num1, num2):
    rect1 = num1.get_rect()
    rect2 = num2.get_rect()
    return rect1.colliderect(rect2)

# Tạo danh sách các số
numbers = [Number(random.randint(1, 10), random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50)) for _ in range(10)]

# Vòng lặp chính
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Di chuyển và vẽ các số
    for number in numbers:
        number.move()
        number.draw(screen)

    # Kiểm tra va chạm
    for i in range(len(numbers) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if check_collision(numbers[i], numbers[j]):
                if (numbers[i].value % 2 == 0 and numbers[j].value % 2 == 0) or \
                   (numbers[i].value % 2 != 0 and numbers[j].value % 2 != 0):
                    # Tạo số mới
                    new_value = numbers[i].value + numbers[j].value
                    new_x = random.randint(0, WIDTH - 50)
                    new_y = random.randint(0, HEIGHT - 50)
                    numbers.append(Number(new_value, new_x, new_y))

                    # Xóa hai số đã va chạm
                    del numbers[i]
                    del numbers[j]
                    break

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
