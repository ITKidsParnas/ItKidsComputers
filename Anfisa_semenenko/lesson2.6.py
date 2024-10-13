import turtle

def draw_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.speed(0)
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    for i in range(360):
        pen.color(colors[i % 6])
        pen.width(i // 100 + 1)
        pen.forward(i)
        pen.left(2222222222222222222222222222222222222222000000000000000000000000000000000000000000000)

    turtle.done()

draw_spiral()