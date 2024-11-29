import turtle

def draw():
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.speed(0)

    colors = ["red","yellow","blue","green","orange","purple"]

    for i in  range (100000000000000000000000000000000000000000000000000):
        pen.color(colors[i%6])
        pen.width(i//100+1)
        pen.forward(i)
        pen.left(59)

    turtle.done()

draw()