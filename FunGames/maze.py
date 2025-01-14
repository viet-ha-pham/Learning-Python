import pygame
import time
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 40
COLS, ROWS =15, 15

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Mê cung (1: Tường, 0: Đường đi)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Vị trí người chơi
player_pos = [1, 1]
exit_pos = [13, 13]

# Cửa sổ game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Đồng hồ đo thời gian
clock = pygame.time.Clock()

# Bắt đầu thời gian
start_time = time.time()

def draw_maze():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if maze[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_player():
    pygame.draw.rect(screen, BLUE, (player_pos[1] * CELL_SIZE, player_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_exit():
    pygame.draw.rect(screen, GREEN, (exit_pos[1] * CELL_SIZE, exit_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    global player_pos

    while True:
        screen.fill(BLACK)

        # Vẽ mê cung, người chơi và mục tiêu
        draw_maze()
        draw_exit()
        draw_player()

        # Kiểm tra sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Nhận phím di chuyển
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and maze[player_pos[0] - 1][player_pos[1]] == 0:
            player_pos[0] -= 1
        if keys[pygame.K_DOWN] and maze[player_pos[0] + 1][player_pos[1]] == 0:
            player_pos[0] += 1
        if keys[pygame.K_LEFT] and maze[player_pos[0]][player_pos[1] - 1] == 0:
            player_pos[1] -= 1
        if keys[pygame.K_RIGHT] and maze[player_pos[0]][player_pos[1] + 1] == 0:
            player_pos[1] += 1

        # Kiểm tra thắng
        if player_pos == exit_pos:
            end_time = time.time()
            total_time = round(end_time - start_time, 2)
            print(f"Congratulations! You escaped the maze in {total_time} seconds.")
            pygame.quit()
            sys.exit()

        # Cập nhật màn hình
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
