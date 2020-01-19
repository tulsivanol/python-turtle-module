import turtle

t = turtle.Turtle()
t.speed(0)
t.color("red")


def draw_circle(length):
    for side in range(4):
        t.forward(100)
        t.right(90)
        for side in range(4):
            t.forward(50)
            t.right(90)


t.penup()
t.back(5)
t.pendown()


for circle in range(80):
    draw_circle(5)
    t.forward(5)
    t.left(5)

turtle.done()
