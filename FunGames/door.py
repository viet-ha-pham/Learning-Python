import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trò chơi gõ cửa")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

# Phông chữ
font = pygame.font.Font(None, 36)

# Vị trí và kích thước của các cửa
door_width = 100
door_height = 200
door_positions = [
    (100, HEIGHT // 2 - door_height // 2),
    (250, HEIGHT // 2 - door_height // 2),
    (400, HEIGHT // 2 - door_height // 2),
]

# Cửa đúng
correct_door = random.randint(0, 2)

# Biến trò chơi
attempts = 7
correct_hits = 0
game_over = False
message = "CLICK TO KNOCK"

# Hàm vẽ cửa
def draw_doors():
    for i, pos in enumerate(door_positions):
        color = GREEN if game_over and i == correct_door else GRAY
        pygame.draw.rect(screen, color, (*pos, door_width, door_height))
        text = font.render(f"Door {i + 1}", True, BLACK)
        screen.blit(text, (pos[0] + 10, pos[1] + door_height + 10))

# Vòng lặp trò chơi
running = True
while running:
    screen.fill(WHITE)

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            for i, pos in enumerate(door_positions):
                rect = pygame.Rect(*pos, door_width, door_height)
                if rect.collidepoint(x, y):
                    if i == correct_door:
                        correct_hits += 1

                        if correct_hits == 3:
                            game_over = True
                            message = "You Win!"

                    attempts -= 1

                    if attempts == 0 and not game_over:
                        game_over = True
                        message = "You Lose!"

    # Vẽ cửa
    draw_doors()

    # Hiển thị thông báo và số lần gõ còn lại
    msg_text = font.render(message, True, BLACK)
    attempts_text = font.render(f"Attempts: {attempts}", True, BLACK)
    screen.blit(msg_text, (20, 20))
    screen.blit(attempts_text, (20, 60))

    # Cập nhật màn hình
    pygame.display.flip()

# Thoát Pygame
pygame.quit()
