import turtle

amy = turtle.Turtle()
amy.color("cyan")
amy.speed(0)


def draw_square():
    for side in range(4):
        amy.forward(100)
        amy.right(90)
        for side in range(4):
            amy.forward(50)
            amy.right(90)


amy.penup()
amy.back(20)
amy.pendown()


for square in range(80):
    draw_square
    amy.forward(5)
    amy.left(5)
amy.hideturtle()
