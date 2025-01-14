import pygame
import random
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Phản xạ số lớn hơn")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Phông chữ
font = pygame.font.Font(None, 74)

# Thời gian giới hạn (ms)
TIME_LIMIT = 3000

# Tạo số ngẫu nhiên
def generate_numbers():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    while num1 == num2:  # Đảm bảo 2 số không bằng nhau
        num2 = random.randint(1, 99)
    return num1, num2

# Tạo hình vuông và số
def draw_numbers(num1, num2):
    square1 = pygame.Rect(WIDTH // 4 - 50, HEIGHT // 2 - 50, 100, 100)
    square2 = pygame.Rect(3 * WIDTH // 4 - 50, HEIGHT // 2 - 50, 100, 100)
    pygame.draw.rect(screen, BLUE, square1)
    pygame.draw.rect(screen, RED, square2)

    text1 = font.render(str(num1), True, WHITE)
    text2 = font.render(str(num2), True, WHITE)

    screen.blit(text1, (square1.x + 25, square1.y + 25))
    screen.blit(text2, (square2.x + 25, square2.y + 25))

    return square1, square2

# Main game loop
def main():
    running = True
    clock = pygame.time.Clock()
    num1, num2 = generate_numbers()
    last_time = pygame.time.get_ticks()

    while running:
        screen.fill(WHITE)
        square1, square2 = draw_numbers(num1, num2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if square1.collidepoint(mouse_pos) and num1 > num2:
                    num1, num2 = generate_numbers()
                    last_time = pygame.time.get_ticks()
                elif square2.collidepoint(mouse_pos) and num2 > num1:
                    num1, num2 = generate_numbers()
                    last_time = pygame.time.get_ticks()
                else:
                    print("Thua cuộc! Số bạn chọn không lớn hơn.")
                    running = False

        # Kiểm tra thời gian phản xạ
        if pygame.time.get_ticks() - last_time > TIME_LIMIT:
            print("Thua cuộc! Bạn không phản xạ kịp thời.")
            running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
