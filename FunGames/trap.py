import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Trò chơi Cửa Sập")

# Màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Tốc độ khung hình
FPS = 60
clock = pygame.time.Clock()

# Kích thước người chơi
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20

# Khởi tạo người chơi (bắt đầu từ cạnh dưới)
player = pygame.Rect(SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2, SCREEN_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
player_speed = 5

# Kích thước cửa
DOOR_WIDTH = 20
door_left = pygame.Rect(0, 0, DOOR_WIDTH, SCREEN_HEIGHT)
door_right = pygame.Rect(SCREEN_WIDTH - DOOR_WIDTH, 0, DOOR_WIDTH, SCREEN_HEIGHT)

# Tốc độ đóng cửa
door_speed = 2
closing = True

# Trạng thái trò chơi
game_over = False
win = False
font = pygame.font.Font("fonts/Roboto-VariableFont_wdth,wght.ttf", 36)

def draw_game():
    screen.fill(WHITE)

    # Vẽ cửa
    pygame.draw.rect(screen, BLUE, door_left)
    pygame.draw.rect(screen, BLUE, door_right)

    # Vẽ người chơi
    pygame.draw.rect(screen, RED, player)

    # Hiển thị trạng thái trò chơi
    if game_over:
        text = font.render("Game Over! Nhấn R để chơi lại.", True, GREEN)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 20))
    elif win:
        text = font.render("You Win! Nhấn R để chơi lại.", True, GREEN)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 20))
    pygame.display.flip()

# Hàm kiểm tra va chạm
def check_collision():
    if player.colliderect(door_left) or player.colliderect(door_right):
        return True
    return False

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (game_over or win) and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Khởi động lại trò chơi
                player.x = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
                player.y = SCREEN_HEIGHT - PLAYER_HEIGHT
                door_left.width = DOOR_WIDTH
                door_right.x = SCREEN_WIDTH - DOOR_WIDTH
                closing = True
                game_over = False
                win = False

    # Điều khiển người chơi
    keys = pygame.key.get_pressed()
    if not game_over and not win:
        if keys[pygame.K_UP] and player.top > 0:
            player.y -= player_speed
        if keys[pygame.K_DOWN] and player.bottom < SCREEN_HEIGHT:
            player.y += player_speed
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < SCREEN_WIDTH:
            player.x += player_speed

    # Di chuyển cửa nếu chưa thắng hoặc thua
    if closing and not (game_over or win):
        door_left.width += door_speed
        door_right.x -= door_speed
        door_right.width += door_speed  # Đảm bảo cửa phải đóng từ phải sang trái

        if door_left.width >= SCREEN_WIDTH // 2 or door_right.x <= SCREEN_WIDTH // 2:
            closing = False

    # Kiểm tra thắng
    if player.top <= 0 and not game_over:
        win = True
        closing = False  # Dừng cửa lại khi thắng

    # Kiểm tra va chạm
    if check_collision():
        game_over = True

    # Vẽ trò chơi
    draw_game()

    # Điều chỉnh tốc độ khung hình
    clock.tick(FPS)

pygame.quit()
sys.exit()
