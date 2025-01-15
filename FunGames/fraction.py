import pygame
import random
import math
from fractions import Fraction

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simplify the Fraction")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Phông chữ
font = pygame.font.Font(None, 74)

# Tốc độ rơi
fall_speed = 5

# Hàm kiểm tra tối giản
def is_simplified(numerator, denominator):
    return math.gcd(numerator, denominator) == 1

# Tạo phân số ngẫu nhiên
def generate_fraction():
    numerator = random.randint(1, 20)
    denominator = random.randint(1, 20)
    return numerator, denominator

# Lớp FractionObject
class FractionObject:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.x = WIDTH // 2
        self.y = HEIGHT // 4
        self.color = RED if not is_simplified(numerator, denominator) else BLACK

    def draw(self):
        fraction_text = f"{self.numerator}/{self.denominator}"
        text = font.render(fraction_text, True, self.color)
        text_rect = text.get_rect(center=(self.x, self.y))
        screen.blit(text, text_rect)

    def update_position(self):
        self.y += fall_speed

    def simplify(self):
        fraction = Fraction(self.numerator, self.denominator)
        self.numerator, self.denominator = fraction.numerator, fraction.denominator
        self.color = BLACK

# Main loop
def main():
    clock = pygame.time.Clock()
    running = True
    fractions = []
    spawn_timer = 0

    while running:
        screen.fill(WHITE)
        dt = clock.tick(60) / 1000  # Thời gian mỗi khung hình (giây)
        spawn_timer += dt

        # Sinh phân số mỗi giây
        if spawn_timer >= 1:
            numerator, denominator = generate_fraction()
            fractions.append(FractionObject(numerator, denominator))
            spawn_timer = 0

        # Sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for fraction in fractions:
                    text_width, text_height = font.size(f"{fraction.numerator}/{fraction.denominator}")
                    if fraction.x - text_width // 2 < mouse_x < fraction.x + text_width // 2 and \
                       fraction.y - text_height // 2 < mouse_y < fraction.y + text_height // 2:
                        if not is_simplified(fraction.numerator, fraction.denominator):
                            fraction.simplify()

        # Cập nhật trạng thái và vẽ các phần tử
        for fraction in fractions:
            fraction.draw()
            fraction.update_position()

        # Xóa phân số rơi xuống khỏi màn hình
        fractions = [fraction for fraction in fractions if fraction.y < HEIGHT]

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
