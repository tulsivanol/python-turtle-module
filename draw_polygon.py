import turtle


def draw_polygon(sides, trun, color, width):

    t = turtle.Turtle()
    t.color(color)
    t.width(width)
    t.speed(0)
    for n in range(sides):
        t.forward(n)
        t.right(trun)
        t.penup()
        t.left(60)
        t.forward(10)
        t.right(60)
        t.pendown()

        t.hideturtle()


draw_polygon(130, 60, "dark green", 5)
