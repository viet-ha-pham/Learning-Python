import pygame
import random

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Trò chơi đi ngang hàng thần tượng")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Khởi tạo nhân vật
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Khởi tạo các vật cản và thần tượng
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 3
obstacles = []

idol_width = 30
idol_height = 30
idols = []

# Khởi tạo đồng hồ
clock = pygame.time.Clock()

# Điểm số
score = 0


# Tạo vật cản và thần tượng
def create_obstacle():
    x = random.randint(0, screen_width - obstacle_width)
    y = random.randint(-150, -50)
    obstacles.append(pygame.Rect(x, y, obstacle_width, obstacle_height))


def create_idol():
    x = random.randint(0, screen_width - idol_width)
    y = random.randint(-150, -50)
    idols.append(pygame.Rect(x, y, idol_width, idol_height))


# Vẽ nhân vật
def draw_player():
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))


# Vẽ vật cản
def draw_obstacles():
    for obs in obstacles:
        pygame.draw.rect(screen, RED, obs)


# Vẽ thần tượng
def draw_idols():
    for idol in idols:
        pygame.draw.rect(screen, (255, 223, 0), idol)


# Cập nhật vị trí vật cản và thần tượng
def update_positions():
    global score
    for obs in obstacles:
        obs.y += obstacle_speed
        if obs.y > screen_height:
            obstacles.remove(obs)
    for idol in idols:
        idol.y += obstacle_speed
        if idol.y > screen_height:
            idols.remove(idol)


# Kiểm tra va chạm
def check_collisions():
    global score
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    for obs in obstacles:
        if player_rect.colliderect(obs):
            return True

    for idol in idols:
        if player_rect.colliderect(idol):
            score += 1
            idols.remove(idol)

    return False


# Chạy trò chơi
def game_loop():
    global player_x, score
    run_game = True
    while run_game:
        screen.fill(WHITE)

        # Xử lý sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        # Lấy trạng thái phím
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed

        # Tạo vật cản và thần tượng
        if random.random() < 0.02:
            create_obstacle()
        if random.random() < 0.02:
            create_idol()

        # Cập nhật vị trí vật cản và thần tượng
        update_positions()

        # Kiểm tra va chạm
        if check_collisions():
            run_game = False

        # Vẽ nhân vật và các đối tượng khác
        draw_player()
        draw_obstacles()
        draw_idols()

        # Hiển thị điểm số
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)

    # Kết thúc trò chơi
    pygame.quit()


# Chạy chương trình
game_loop()
