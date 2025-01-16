import pygame
import random
import string

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trò chơi chữ cái")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Tốc độ khung hình
FPS = 60

# Các biến
font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()

# Danh sách nguyên âm và phụ âm
VOWELS = set("AEIOU")
CONSONANTS = set(string.ascii_uppercase) - VOWELS

# Danh sách các chữ cái bay
letters = []

for _ in range(20):  # Tạo 20 chữ cái ban đầu
    letter = random.choice(string.ascii_uppercase)
    x = random.randint(0, WIDTH - 40)
    y = random.randint(0, HEIGHT - 40)
    dx = random.choice([-3, 3])  # Hướng di chuyển ngang
    dy = random.choice([-3, 3])  # Hướng di chuyển dọc
    letters.append({"char": letter, "x": x, "y": y, "dx": dx, "dy": dy})

# Danh sách chuỗi đứng yên
static_pairs = []

# Hàm kiểm tra va chạm giữa 2 chữ cái
def is_collision(letter1, letter2):
    return abs(letter1["x"] - letter2["x"]) < 40 and abs(letter1["y"] - letter2["y"]) < 40

# Vòng lặp chính
running = True
while running:
    screen.fill(WHITE)

    # Kiểm tra sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Di chuyển các chữ cái
    for letter in letters:
        letter["x"] += letter["dx"]
        letter["y"] += letter["dy"]

        # Bật tường
        if letter["x"] <= 0 or letter["x"] >= WIDTH - 40:
            letter["dx"] *= -1
        if letter["y"] <= 0 or letter["y"] >= HEIGHT - 40:
            letter["dy"] *= -1

    # Kiểm tra va chạm giữa các chữ cái
    for i in range(len(letters) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if is_collision(letters[i], letters[j]):
                char1, char2 = letters[i]["char"], letters[j]["char"]

                # Kiểm tra điều kiện phụ âm + nguyên âm
                if (char1 in CONSONANTS and char2 in VOWELS) or (char2 in CONSONANTS and char1 in VOWELS):
                    static_pairs.append(char1 + char2)
                    letters.pop(i)
                    letters.pop(j)
                    break

    # Vẽ các chữ cái bay
    for letter in letters:
        text = font.render(letter["char"], True, RED if letter["char"] in VOWELS else BLUE)
        screen.blit(text, (letter["x"], letter["y"]))

    # Vẽ các chuỗi đứng yên
    for idx, pair in enumerate(static_pairs):
        text = font.render(pair, True, BLACK)
        screen.blit(text, (10, 10 + idx * 30))

    # Cập nhật màn hình
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
