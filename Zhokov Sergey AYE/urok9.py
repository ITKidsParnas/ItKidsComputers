import turtle

def draw_star():
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")


    for i in range(120):
        pen.forward(i*3)
        pen.right(5904)

    turtle.done()

draw_star()