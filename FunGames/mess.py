import pygame
import random
import time

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click để xóa hình chữ nhật")

# Màu sắc
WHITE = (255, 255, 255)
colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(10)]

# Khởi tạo các hình chữ nhật
rects = []
for _ in range(500):  # Số lượng hình chữ nhật
    width = random.randint(50, 150)
    height = random.randint(20, 50)
    x = random.randint(0, WIDTH - width)
    y = random.randint(0, HEIGHT - height)
    color = random.choice(colors)
    rects.append(pygame.Rect(x, y, width, height))

# Thời gian bắt đầu
start_time = time.time()

# Biến điều khiển
running = True
clicked_rects = []

# Vòng lặp chính
while running:
    screen.fill(WHITE)

    # Vẽ các hình chữ nhật
    for rect in rects:
        if rect not in clicked_rects:
            pygame.draw.rect(screen, (0,0,0), rect)

    # Kiểm tra sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for rect in rects:
                if rect.collidepoint(pos) and rect not in clicked_rects:
                    clicked_rects.append(rect)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Nhấn R để chơi lại
                rects = []
                for _ in range(10):  # Số lượng hình chữ nhật
                    width = random.randint(50, 150)
                    height = random.randint(20, 50)
                    x = random.randint(0, WIDTH - width)
                    y = random.randint(0, HEIGHT - height)
                    color = random.choice(colors)
                    rects.append(pygame.Rect(x, y, width, height, color))
                clicked_rects = []
                start_time = time.time()

    # Cập nhật màn hình
    pygame.display.flip()

pygame.quit()
