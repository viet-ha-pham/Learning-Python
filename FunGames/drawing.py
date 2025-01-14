import turtle
import random

# Thiết lập màn hình
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Hình vẽ thú vị với Turtle")

# Hàm vẽ ngôi sao
def draw_star(t, size, color):
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

# Hàm vẽ bông hoa
def draw_flower(t, size, color):
    t.color(color)
    for _ in range(36):  # Vẽ 36 cánh hoa
        t.circle(size)
        t.left(10)

# Hàm vẽ hình xoắn ốc màu sắc
def draw_spiral(t):
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    for i in range(100):
        t.color(random.choice(colors))
        t.forward(i * 2)
        t.right(59)

# Hàm chính
def main():
    # Tạo turtle
    star_turtle = turtle.Turtle()
    flower_turtle = turtle.Turtle()
    spiral_turtle = turtle.Turtle()

    # Tăng tốc độ vẽ
    star_turtle.speed(10)
    flower_turtle.speed(10)
    spiral_turtle.speed(0)

    # Vẽ ngôi sao
    star_turtle.penup()
    star_turtle.goto(-200, 100)
    star_turtle.pendown()
    draw_star(star_turtle, 100, "gold")

    # Vẽ bông hoa
    flower_turtle.penup()
    flower_turtle.goto(200, 100)
    flower_turtle.pendown()
    draw_flower(flower_turtle, 50, "red")

    # Vẽ hình xoắn ốc
    spiral_turtle.penup()
    spiral_turtle.goto(0, -200)
    spiral_turtle.pendown()
    draw_spiral(spiral_turtle)

    # Ẩn turtle
    star_turtle.hideturtle()
    flower_turtle.hideturtle()
    spiral_turtle.hideturtle()

    # Giữ màn hình
    screen.mainloop()

if __name__ == "__main__":
    main()
