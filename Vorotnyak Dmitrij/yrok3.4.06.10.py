import turtle

def draw_star():
    screen = turtle.Screen()
    screen.bgcolor('purple')
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")

    for i in range(222):

        pen.forward(i*4)
        pen.right(144)

    turtle.done()

draw_star()