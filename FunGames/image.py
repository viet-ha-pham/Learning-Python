import pygame
import random
import sys

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

# Màu nền
BACKGROUND_COLOR = (255, 255, 255)

# Tạo màn hình
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Chạm vào thần tượng")

# Load ảnh thần tượng
idol_image = pygame.image.load("E:\GÓC TÂM LINH\idol-image.jpg")  # Thay bằng đường dẫn ảnh của bạn
idol_image = pygame.transform.scale(idol_image, (377, 500))  # Thay đổi kích thước ảnh (nếu cần)
idol_rect = idol_image.get_rect()

def get_random_position():
    """Tạo tọa độ ngẫu nhiên cho ảnh trong màn hình."""
    x = random.randint(0, SCREEN_WIDTH - idol_rect.width)
    y = random.randint(0, SCREEN_HEIGHT - idol_rect.height)
    return x, y

# Đặt ảnh ở vị trí ngẫu nhiên ban đầu
idol_rect.topleft = get_random_position()

# Vòng lặp chính
running = True
while running:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if idol_rect.collidepoint(event.pos):
                idol_rect.topleft = get_random_position()  # Cập nhật vị trí ảnh

    # Vẽ nền và ảnh thần tượng
    screen.fill(BACKGROUND_COLOR)
    screen.blit(idol_image, idol_rect)

    # Cập nhật màn hình
    pygame.display.flip()

# Thoát pygame
pygame.quit()
sys.exit()
