import turtle

def draw_star():
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("yellow", "white")

    for i in range(1000):
        pen.forward(i*3)
        pen.left(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

    turtle.done()

draw_star()