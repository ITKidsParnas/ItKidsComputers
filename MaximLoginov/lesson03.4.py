import turtle

def draw_star():
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.speed(-20)
    pen.color("yellow")

    for i in range(120):
        pen.forward(i*3)
        pen.right(288)

    turtle.done()

draw_star()