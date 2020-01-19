import turtle

t = turtle.Turtle()
t.color("green")
t.speed(0)


def draw_circle(length):
    for side in range(4):
        t.forward(100)
        t.right(90)
        for side in range(4):
            t.forward(50)
            t.right(90)


t.penup()
t.back(20)
t.pendown()


for circle in range(80):
    draw_circle(5)
    t.forward(5)
    t.left(5)

t.hideturtle()
