import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Square Race Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Square properties
SQUARE_SIZE = 40
PLAYER_COLOR = RED
AUTO_COLOR_1 = GREEN
AUTO_COLOR_2 = BLUE

# Speeds
PLAYER_SPEED = 5
AUTO_SPEED_RANGE = (3, 6)

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 48)

# Function to reset game variables
def reset_game():
    global player_pos, auto_pos_1, auto_pos_2, winner_order, game_over, end_message
    player_pos = [50, HEIGHT // 4 - SQUARE_SIZE // 2]
    auto_pos_1 = [50, HEIGHT // 2 - SQUARE_SIZE // 2]
    auto_pos_2 = [50, 3 * HEIGHT // 4 - SQUARE_SIZE // 2]
    winner_order = []
    game_over = False
    end_message = ""

# Initialize game variables
reset_game()

# Finish line
FINISH_X = WIDTH - 100

# Helper functions
def draw_squares():
    pygame.draw.rect(screen, PLAYER_COLOR, (*player_pos, SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.rect(screen, AUTO_COLOR_1, (*auto_pos_1, SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.rect(screen, AUTO_COLOR_2, (*auto_pos_2, SQUARE_SIZE, SQUARE_SIZE))

def display_message(text):
    message = font.render(text, True, BLACK)
    text_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(message, text_rect)

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_game()

    if not game_over:
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_pos[1] > 0:
            player_pos[1] -= PLAYER_SPEED
        if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - SQUARE_SIZE:
            player_pos[1] += PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - SQUARE_SIZE:
            player_pos[0] += PLAYER_SPEED
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= PLAYER_SPEED

        # Automatic square movement
        if auto_pos_1[0] < FINISH_X:
            auto_pos_1[0] += random.randint(*AUTO_SPEED_RANGE)
        elif "Auto1" not in winner_order:
            winner_order.append("Auto1")

        if auto_pos_2[0] < FINISH_X:
            auto_pos_2[0] += random.randint(*AUTO_SPEED_RANGE)
        elif "Auto2" not in winner_order:
            winner_order.append("Auto2")

        if player_pos[0] >= FINISH_X and "Player" not in winner_order:
            winner_order.append("Player")

        # Check for game end
        if len(winner_order) == 3:
            if winner_order.index("Player") == 1:
                end_message = "You Win! Finished Second!"
            else:
                end_message = "You Lose!"
            game_over = True

    else:
        display_message(f"{end_message} Press R to Restart")

    # Draw everything
    draw_squares()
    pygame.draw.line(screen, BLACK, (FINISH_X, 0), (FINISH_X, HEIGHT), 5)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

pygame.quit()
