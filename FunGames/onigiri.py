import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption('Onigiri Game')

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Cấu hình nhân vật
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 15

# Cấu hình onigiri
onigiri_width = 30
onigiri_height = 30
onigiri_speed = 3

# Tạo font chữ
font = pygame.font.SysFont('Arial', 36)

# Điểm số
score = 0
missed_onigiri = 0  # Số lượng cơm nắm bị rơi mà chưa thu thập
LIMIT = 10
# Thời gian trễ
clock = pygame.time.Clock()


# Hàm vẽ nhân vật
def draw_player(x, y):
    pygame.draw.rect(screen, RED, (x, y, player_width, player_height))


# Hàm vẽ onigiri
def draw_onigiri(x, y):
    pygame.draw.circle(screen, (255, 255, 0), (x, y), onigiri_width // 2)


# Hàm hiển thị điểm số
def display_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))


# Hàm hiển thị thông báo thua cuộc
def display_game_over():
    game_over_text = font.render("Game Over! Press R to Restart or Q to Quit", True, BLACK)
    screen.blit(game_over_text, (screen_width // 2 - 250, screen_height // 2))


# Chạy trò chơi
running = True
game_over = False
onigiris = []
while running:
    screen.fill(WHITE)

    # Kiểm tra sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_r and game_over:
                # Khởi tạo lại trò chơi khi nhấn R
                game_over = False
                score = 0
                missed_onigiri = 0
                player_x = screen_width // 2 - player_width // 2
                onigiris.clear()

    if game_over:
        display_game_over()
    else:
        # Lấy trạng thái phím
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed

        # Thêm onigiri mới
        if random.random() < 0.02:
            onigiri_x = random.randint(0, screen_width - onigiri_width)
            onigiri_y = 0
            onigiris.append([onigiri_x, onigiri_y])

        # Di chuyển các onigiri
        for onigiri in onigiris[:]:
            onigiri[1] += onigiri_speed
            if onigiri[1] > screen_height:
                missed_onigiri += 1
                onigiris.remove(onigiri)
                if missed_onigiri >= LIMIT:  # Nếu có 5 cơm nắm rơi xuống, thua cuộc
                    game_over = True
            elif (onigiri[0] + onigiri_width > player_x and onigiri[0] < player_x + player_width and
                  onigiri[1] + onigiri_height > player_y and onigiri[1] < player_y + player_height):
                score += 1
                onigiris.remove(onigiri)

        # Vẽ các đối tượng
        draw_player(player_x, player_y)
        for onigiri in onigiris:
            draw_onigiri(onigiri[0], onigiri[1])

        # Hiển thị điểm
        display_score(score)

    # Cập nhật màn hình
    pygame.display.update()

    # Điều chỉnh tốc độ khung hình
    clock.tick(60)

# Thoát Pygame
pygame.quit()
