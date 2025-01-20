import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
FONT_SIZE = 32
TARGET_SUM = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize screen and font
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Number Collector")
font = pygame.font.Font(None, FONT_SIZE)

# Classes
class Number:
    def __init__(self):
        self.value = random.randint(1, 10)
        self.x = random.randint(0, SCREEN_WIDTH - FONT_SIZE)
        self.y = random.randint(0, SCREEN_HEIGHT - FONT_SIZE)
        self.speed = random.choice([-2, -1, 1, 2])

    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > SCREEN_WIDTH - FONT_SIZE:
            self.speed = -self.speed

    def draw(self):
        text = font.render(str(self.value), True, BLUE)
        screen.blit(text, (self.x, self.y))

class Player:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 50, 50)
        self.color = GREEN
        self.speed = 5
        self.score = 0

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

# Functions
def check_collision(player, numbers):
    for number in numbers:
        num_rect = pygame.Rect(number.x, number.y, FONT_SIZE, FONT_SIZE)
        if player.rect.colliderect(num_rect):
            player.score += number.value
            numbers.remove(number)
            numbers.append(Number())

def display_text(text, color, y_offset=0):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
    screen.blit(text_surface, text_rect)

# Main game function
def main():
    clock = pygame.time.Clock()
    running = True

    player = Player()
    numbers = [Number() for _ in range(5)]

    game_over = False
    win = False

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if game_over and keys[pygame.K_r]:
            main()  # Restart the game
            return

        if not game_over:
            player.move(keys)
            check_collision(player, numbers)

            if player.score == TARGET_SUM:
                win = True
                game_over = True
            elif player.score > TARGET_SUM:
                win = False
                game_over = True

        for number in numbers:
            number.move()
            number.draw()

        player.draw()

        # Display score
        score_text = f"Score: {player.score}"
        score_surface = font.render(score_text, True, BLACK)
        screen.blit(score_surface, (10, 10))

        if game_over:
            if win:
                display_text("You Win! Press R to Restart", GREEN)
            else:
                display_text("You Lose! Press R to Restart", RED)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
