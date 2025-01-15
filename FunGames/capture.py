import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Capture the Numbers")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 10, 255)

# Font
font = pygame.font.SysFont(None, 36)

# Clock
clock = pygame.time.Clock()

# Number class
class Number:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.dx = random.choice([-2, -1, 1, 2])
        self.dy = random.choice([-2, -1, 1, 2])
        self.stopped = False

    def move(self):
        if not self.stopped:
            self.x += self.dx
            self.y += self.dy

            # Bounce off walls
            if self.x < 0 or self.x > WIDTH:
                self.dx *= -1
            if self.y < 0 or self.y > HEIGHT:
                self.dy *= -1

    def draw(self):
        color = BLUE if self.stopped else RED
        text = font.render(str(self.value), True, color)
        screen.blit(text, (self.x, self.y))

# Create numbers
numbers = [Number(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), random.randint(0, 99)) for _ in range(20)]

# Variables for drawing the bounding box
is_drawing = False
start_pos = None
end_pos = None

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Start drawing the bounding box
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            is_drawing = True
            start_pos = event.pos

        # Finish drawing the bounding box
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            is_drawing = False
            end_pos = event.pos

            # Calculate the bounding box
            if start_pos and end_pos:
                x1, y1 = start_pos
                x2, y2 = end_pos
                left = min(x1, x2)
                right = max(x1, x2)
                top = min(y1, y2)
                bottom = max(y1, y2)

                # Stop numbers within the bounding box
                for number in numbers:
                    if left <= number.x <= right and top <= number.y <= bottom:
                        number.stopped = True

    # Draw and move numbers
    for number in numbers:
        number.move()
        number.draw()

    # Draw the bounding box
    if is_drawing and start_pos:
        current_pos = pygame.mouse.get_pos()
        rect = pygame.Rect(min(start_pos[0], current_pos[0]), min(start_pos[1], current_pos[1]),
                           abs(start_pos[0] - current_pos[0]), abs(start_pos[1] - current_pos[1]))
        pygame.draw.rect(screen, BLACK, rect, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
