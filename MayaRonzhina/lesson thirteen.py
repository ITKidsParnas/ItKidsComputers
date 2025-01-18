import turtle

def draw():
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.speed(0)

    colors = ["red", "pink"]

    for i in range(750):
        pen.color(colors[i%2])
        pen.width(i//100+1)
        pen.forward(i)
        pen.left(59)

    turtle.done()

draw()