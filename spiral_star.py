import turtle

spiral_star = turtle.Turtle()

for i in range(40):
    spiral_star.forward(i * 10)
    spiral_star.right(144)

turtle.done()
