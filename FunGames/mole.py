import pygame
import random
import time

# Khởi tạo pygame
pygame.init()

# Đặt kích thước màn hình và màu sắc
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trò chơi Đập Chuột Chũi Năng Động")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)

# Tạo font chữ
font = pygame.font.SysFont('Arial', 24)

# Tạo đối tượng chuột chũi
mole_radius = 30
mole_pos = [random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)]
move_timer = time.time()  # Thời gian di chuyển tiếp theo

# Tạo biến điểm số
score = 0
start_time = time.time()
game_duration = 30  # Thời gian chơi (giây)


# Chức năng vẽ chuột chũi
def draw_mole():
    pygame.draw.circle(screen, BROWN, mole_pos, mole_radius)


# Chức năng vẽ điểm số
def draw_score():
    score_text = font.render(f"Điểm số: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))


# Chức năng vẽ thời gian còn lại
def draw_time_left():
    elapsed_time = time.time() - start_time
    time_left = max(0, game_duration - int(elapsed_time))
    time_text = font.render(f"Thời gian: {time_left}s", True, BLACK)
    screen.blit(time_text, (WIDTH - 150, 10))
    return time_left


# Vòng lặp trò chơi
running = True
while running:
    screen.fill(WHITE)

    # Kiểm tra sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (mouse_x - mole_pos[0]) ** 2 + (mouse_y - mole_pos[1]) ** 2 <= mole_radius ** 2:
                score += 1
                mole_pos = [random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)]

    # Di chuyển chuột chũi sau mỗi 1 giây
    if time.time() - move_timer > 1:
        mole_pos = [random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)]
        move_timer = time.time()

    # Vẽ chuột chũi, điểm số và thời gian còn lại
    draw_mole()
    draw_score()
    time_left = draw_time_left()

    # Kết thúc trò chơi nếu hết thời gian
    if time_left == 0:
        running = False

    # Cập nhật màn hình
    pygame.display.update()

    # Giới hạn tốc độ khung hình
    pygame.time.delay(30)

# Hiển thị thông báo kết thúc
screen.fill(WHITE)
end_text = font.render(f"Trò chơi kết thúc! Điểm số của bạn: {score}", True, BLACK)
screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2))
pygame.display.update()
pygame.time.delay(3000)

pygame.quit()
