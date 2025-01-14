import pygame
import random
import time

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trò chơi tính toán nhanh")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Phông chữ
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Hàm tạo phép tính ngẫu nhiên
def generate_question():
    num1 = random.randint(0, 99)
    num2 = random.randint(0, 99)
    return num1, num2, num1 + num2

# Hàm hiển thị văn bản
def display_text(text, x, y, color=BLACK, size="large"):
    if size == "large":
        text_surface = font.render(text, True, color)
    else:
        text_surface = small_font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Trò chơi chính
def main():
    running = True
    clock = pygame.time.Clock()

    # Khởi tạo câu hỏi đầu tiên
    num1, num2, correct_answer = generate_question()
    user_answer = ""
    start_time = time.time()

    while running:
        screen.fill(WHITE)

        # Kiểm tra sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Người chơi nhấn Enter
                    if user_answer.isdigit() and int(user_answer) == correct_answer:
                        # Câu trả lời đúng
                        num1, num2, correct_answer = generate_question()
                        user_answer = ""
                        start_time = time.time()
                    else:
                        # Câu trả lời sai
                        display_text("Sai! Nhấn Esc để thoát.", 150, 200, RED, "small")
                        pygame.display.flip()
                        time.sleep(2)
                        running = False
                elif event.key == pygame.K_ESCAPE:  # Thoát trò chơi
                    running = False
                elif event.key == pygame.K_BACKSPACE:  # Xóa ký tự
                    user_answer = user_answer[:-1]
                else:  # Thêm ký tự
                    user_answer += event.unicode

        # Hiển thị câu hỏi
        question = f"{num1} + {num2} = ?"
        display_text(question, 150, 100)

        # Hiển thị câu trả lời của người chơi
        display_text(user_answer, 150, 200, GREEN)

        # Tính thời gian còn lại
        elapsed_time = time.time() - start_time
        remaining_time = max(0, 5 - elapsed_time)
        display_text(f"Thời gian: {int(remaining_time)} giây", 550, 50, RED, "small")

        # Kiểm tra thời gian hết hạn
        if remaining_time <= 0:
            display_text("Hết giờ! Nhấn Esc để thoát.", 150, 200, RED, "small")
            pygame.display.flip()
            time.sleep(2)
            running = False

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
