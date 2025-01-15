import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
COLORS = [BLUE, GREEN, YELLOW, PURPLE]

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Ball class
class Ball:
    def __init__(self, x, y, radius, color, dx, dy):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = dx
        self.dy = dy

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off walls
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.dx = -self.dx
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.dy = -self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def is_colliding(self, other):
        distance = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return distance < self.radius + other.radius

# Square class
class Square:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def is_colliding(self, ball):
        ball_rect = pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2)
        square_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        return square_rect.colliderect(ball_rect)

# Create balls
balls = [
    Ball(
        random.randint(50, WIDTH - 50),
        random.randint(50, HEIGHT - 50),
        random.randint(10, 30),
        random.choice(COLORS),
        random.choice([-3, 3]),
        random.choice([-3, 3])
    )
    for _ in range(10)
]

# Add the special red ball
red_ball = Ball(WIDTH // 2, HEIGHT // 2, 40, RED, 4, 4)
balls.append(red_ball)

# Create a square
square = Square(WIDTH // 4, HEIGHT // 4, 50, RED)

# Game loop
running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys for square movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square.x -= 5
    if keys[pygame.K_RIGHT]:
        square.x += 5
    if keys[pygame.K_UP]:
        square.y -= 5
    if keys[pygame.K_DOWN]:
        square.y += 5

    # Update and draw balls
    for ball in balls[:]:  # Iterate over a copy of the list
        ball.move()
        ball.draw(screen)
        if red_ball.is_colliding(ball) and ball != red_ball:
            balls.remove(ball)
        elif square.is_colliding(ball):
            balls.remove(ball)

    # Draw the square
    square.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
