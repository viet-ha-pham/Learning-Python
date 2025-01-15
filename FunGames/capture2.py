import pygame
import random
import time

# Khởi tạo Pygame
pygame.init()

# Cài đặt cửa sổ
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Từ Tiếng Anh Bay Qua Bay Lại")

# Các màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Phông chữ
font = pygame.font.Font(None, 40)

# Các từ tiếng Anh
words = ["hello", "world", "computer", "science", "programming", "pygame", "python", "artificial", "intelligence"]


# Tạo các đối tượng từ tiếng Anh
class Word:
    def __init__(self, text, x, y, speed_x, speed_y):
        self.text = text
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Nếu từ ra ngoài màn hình, quay lại từ đối diện
        if self.x < 0 or self.x > screen_width:
            self.speed_x = -self.speed_x
        if self.y < 0 or self.y > screen_height:
            self.speed_y = -self.speed_y

    def draw(self):
        text_surface = font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.x, self.y))


# Hàm kiểm tra xem điểm có nằm trong đường bao không
def point_in_polygon(x, y, polygon):
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


# Các biến quan trọng
running = True
words_list = [Word(word, random.randint(0, screen_width), random.randint(0, screen_height),
                   random.choice([-5, 5]), random.choice([-5, 5])) for word in words]
drawing_polygon = False
polygon_points = []

# Vòng lặp trò chơi
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not drawing_polygon:
                polygon_points = [pygame.mouse.get_pos()]
                drawing_polygon = True
            else:
                polygon_points.append(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing_polygon:
                polygon_points.append(pygame.mouse.get_pos())
                drawing_polygon = False

    # Di chuyển và vẽ các từ
    for word in words_list:
        word.move()
        word.draw()

        # Kiểm tra xem từ có nằm trong đường bao không
        if point_in_polygon(word.x, word.y, polygon_points):
            pygame.draw.rect(screen, RED, (word.x - 5, word.y - 5, 100, 40), 2)  # Vẽ khung dừng lại

    # Vẽ đường bao nếu có
    if len(polygon_points) > 1:
        pygame.draw.polygon(screen, RED, polygon_points, 2)

    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
