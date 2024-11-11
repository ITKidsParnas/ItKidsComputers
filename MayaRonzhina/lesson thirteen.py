import turtle

def draw():
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.speed(0)

    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

    for i in range(720):
        pen.color(colors[i%6])
        pen.width(i//100+1)
        pen.forward(i)
        pen.left(59)

    turtle.done()

draw()