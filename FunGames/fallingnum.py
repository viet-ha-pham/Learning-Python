import pygame
import random
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nhập lại thứ tự các số")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Phông chữ
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font("fonts/Roboto-VariableFont_wdth,wght.ttf", 36)

# Hàm vẽ văn bản
def draw_text(text, font, color, x, y):
    text_obj = font.render(text, True, color)
    screen.blit(text_obj, (x, y))

# Hàm tạo lại số, tốc độ và vị trí (đảm bảo không trùng bằng random.choices)
def generate_numbers():
    # Tạo danh sách các số từ 1 đến 99
    numbers = list(range(1, 100))
    random.shuffle(numbers)  # Xáo trộn danh sách số
    numbers = random.choices(numbers, k=3)  # Chọn 6 số ngẫu nhiên

    # Tạo danh sách các tốc độ từ 2 đến 12
    speeds = list(range(2, 13))
    speeds = random.choices(speeds, k=3)  # Chọn 6 tốc độ ngẫu nhiên

    # Tạo danh sách các vị trí không trùng
    positions = []
    available_x = list(range(50, WIDTH-50, 100))  # Tạo danh sách vị trí x có sẵn
    random.shuffle(available_x)  # Xáo trộn các vị trí x
    positions = random.choices(available_x, k=3)  # Chọn 6 vị trí không trùng

    return numbers, speeds, positions

# Trạng thái trò chơi
game_over = False
user_input = ""
numbers, speeds, positions = generate_numbers()
touched_order = []
result_text = ""

# Chạy vòng lặp chính
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Kiểm tra kết quả
                user_order = user_input.split()
                if user_order == list(map(str, touched_order)):
                    result_text = "Chính xác!"
                else:
                    result_text = "Sai rồi!"
                game_over = True

            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_r:
                # Chơi lại
                game_over = False
                user_input = ""
                touched_order = []
                result_text = ""
                numbers, speeds, positions = generate_numbers()

            else:
                user_input += event.unicode

    if not game_over:
        for i in range(len(numbers)):
            # Di chuyển các số xuống dưới mà không di chuyển ngang
            positions[i] += speeds[i]
            if positions[i] >= HEIGHT and numbers[i] not in touched_order:
                touched_order.append(numbers[i])

            # Vẽ số lên màn hình
            if numbers[i] not in touched_order:
                draw_text(str(numbers[i]), font, BLACK, positions[i], positions[i])

        if len(touched_order) == 3:
            game_over = True

    if game_over and len(touched_order) == 3:
        draw_text("Nhập lại thứ tự:", small_font, BLACK, 50, HEIGHT // 2 - 100)
        draw_text(user_input, small_font, RED, 50, HEIGHT // 2)

        # Vẽ thông báo kết quả và hướng dẫn chơi lại
        draw_text(result_text, small_font, RED, WIDTH // 2 - 100, HEIGHT // 2 + 50)
        draw_text("Nhấn R để chơi lại", small_font, RED, WIDTH // 2 - 150, HEIGHT // 2 + 100)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
