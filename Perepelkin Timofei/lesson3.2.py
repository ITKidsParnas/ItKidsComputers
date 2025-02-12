import turtle

def draw_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.speed(0)
    colors = ["red", "purple", "black", "grey", "blue"]

    for i in range(100000):
        pen.color(colors[i % 5])
        pen.width(i // 100 + 1)
        pen.forward(i)
        pen.left(10000000000000000000000000000000000000000000000000000000000000000000000000000000000)

    turtle.done()

draw_spiral()