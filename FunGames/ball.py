import pygame
import random
import sys
import time

# Khởi tạo Pygame
pygame.init()

# Cài đặt màn hình và màu sắc
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Trò chơi hình tròn")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Font chữ để hiển thị kích thước cuối cùng
font = pygame.font.Font(None, 48)

# Các thông số của hình tròn
circle_color = RED
circle_radius = 50
circle_position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Biến thời gian
start_time = time.time()
duration = 60  # Trò chơi kéo dài 1 phút
final_message = None  # Biến lưu tin nhắn cuối cùng

# Vòng lặp trò chơi
running = True
while running:
    screen.fill(WHITE)

    # Vẽ hình tròn
    pygame.draw.circle(screen, circle_color, circle_position, circle_radius)

    # Kiểm tra sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            distance = ((mouse_x - circle_position[0]) ** 2 + (mouse_y - circle_position[1]) ** 2) ** 0.5
            if distance <= circle_radius:
                # Phóng to hoặc thu nhỏ ngẫu nhiên
                change = random.randint(-10, 10)
                new_radius = circle_radius + change
                # Đảm bảo bán kính không quá to hoặc quá nhỏ
                if 20 <= new_radius <= 100:
                    circle_radius = new_radius

    # Hiển thị thời gian
    elapsed_time = time.time() - start_time
    if elapsed_time >= duration:
        # Dừng trò chơi sau 1 phút
        final_message = f"Score: {circle_radius}"
        running = False

    # Cập nhật màn hình
    pygame.display.flip()

# Hiển thị kích thước cuối cùng trên màn hình
screen.fill(WHITE)
if final_message:
    text = font.render(final_message, True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

# Chờ một lúc trước khi thoát
pygame.time.wait(5000)

# Thoát Pygame
pygame.quit()
sys.exit()
