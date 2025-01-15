import pygame
import random
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Thiết lập màn hình
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Trò chơi đoán số")

# Font chữ
font = pygame.font.Font("fonts/Roboto-VariableFont_wdth,wght.ttf", 36)
small_font = pygame.font.Font("fonts/Roboto-VariableFont_wdth,wght.ttf", 28)

# Biến trò chơi
target_number = random.randint(1, 100)
guess = ""
message = "Nhập số từ 1 đến 100:"
attempts = 0
game_over = False

# Vòng lặp chính
running = True
while running:
    screen.fill(WHITE)

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_RETURN:  # Nhấn Enter để đoán
                if guess.isdigit():
                    attempts += 1
                    user_guess = int(guess)
                    if user_guess < target_number:
                        message = "Số lớn hơn!"
                    elif user_guess > target_number:
                        message = "Số nhỏ hơn!"
                    else:
                        message = f"Chúc mừng! cBạn đoán đúng sau {attempts} lần."
                        game_over = True
                    guess = ""
            elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự cuối
                guess = guess[:-1]
            elif event.unicode.isdigit():  # Nhập số
                guess += event.unicode

    # Vẽ thông báo và số đoán
    title_text = font.render("Trò chơi đoán số", True, BLUE)
    message_text = font.render(message, True, BLACK)
    guess_text = font.render(guess, True, RED)
    attempts_text = small_font.render(f"Lần đoán: {attempts}", True, BLACK)

    # Hiển thị lên màn hình
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))
    screen.blit(message_text, (50, 150))
    screen.blit(guess_text, (50, 250))
    screen.blit(attempts_text, (50, 350))

    if game_over:
        restart_text = small_font.render("Nhấn R để chơi lại hoặc ESC để thoát.", True, GREEN)
        screen.blit(restart_text, (50, 450))
        # Kiểm tra phím chơi lại hoặc thoát
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            target_number = random.randint(1, 100)
            guess = ""
            message = "Nhập số từ 1 đến 100:"
            attempts = 0
            game_over = False
        elif keys[pygame.K_ESCAPE]:
            running = False

    # Cập nhật màn hình
    pygame.display.flip()

# Thoát Pygame
pygame.quit()
sys.exit()
