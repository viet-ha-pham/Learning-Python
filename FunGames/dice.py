import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Cài đặt cửa sổ
WIDTH, HEIGHT = 400, 350
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Trò chơi Xúc Xắc')

# Cài đặt màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Cài đặt phông chữ
font = pygame.font.SysFont(None, 48)

# Hàm vẽ xúc xắc
def draw_dice(number):
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (150, 100, 100, 100), 5)  # Vẽ hình vuông

    # Vẽ các chấm trên xúc xắc
    if number == 1:
        pygame.draw.circle(screen, BLACK, (200, 150), 10)
    elif number == 2:
        pygame.draw.circle(screen, BLACK, (170, 120), 10)
        pygame.draw.circle(screen, BLACK, (230, 180), 10)
    elif number == 3:
        pygame.draw.circle(screen, BLACK, (170, 120), 10)
        pygame.draw.circle(screen, BLACK, (200, 150), 10)
        pygame.draw.circle(screen, BLACK, (230, 180), 10)
    elif number == 4:
        pygame.draw.circle(screen, BLACK, (170, 120), 10)
        pygame.draw.circle(screen, BLACK, (230, 120), 10)
        pygame.draw.circle(screen, BLACK, (170, 180), 10)
        pygame.draw.circle(screen, BLACK, (230, 180), 10)
    elif number == 5:
        pygame.draw.circle(screen, BLACK, (170, 120), 10)
        pygame.draw.circle(screen, BLACK, (230, 120), 10)
        pygame.draw.circle(screen, BLACK, (170, 180), 10)
        pygame.draw.circle(screen, BLACK, (230, 180), 10)
        pygame.draw.circle(screen, BLACK, (200, 150), 10)
    elif number == 6:
        pygame.draw.circle(screen, BLACK, (170, 120), 10)
        pygame.draw.circle(screen, BLACK, (230, 120), 10)
        pygame.draw.circle(screen, BLACK, (170, 150), 10)
        pygame.draw.circle(screen, BLACK, (230, 150), 10)
        pygame.draw.circle(screen, BLACK, (170, 180), 10)
        pygame.draw.circle(screen, BLACK, (230, 180), 10)

    pygame.display.update()


# Vòng lặp chính của trò chơi
running = True
dice_number = random.randint(1, 6)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Khi nhấn chuột
            dice_number = random.randint(1, 6)

    # Vẽ xúc xắc và kết quả
    draw_dice(dice_number)

    pygame.display.update()

# Dừng Pygame
pygame.quit()
