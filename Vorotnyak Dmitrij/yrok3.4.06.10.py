import turtle

def draw_star():
    screen = turtle.Screen()
    screen.bgcolor('purple')
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")

    for i in range(2220):

        pen.forward(i*4)
        pen.right(145)

        screen = turtle.Screen()
    screen.bgcolor('purple')
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("red")

    for i in range(2220):

        pen.forward(i*4)
        pen.right(146)

    turtle.done()

draw_star()