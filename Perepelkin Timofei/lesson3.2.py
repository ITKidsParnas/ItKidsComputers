import turtle

def draw_triangle():
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.speed(0)
    colors = ["yellow", "purple", "green", "red", "blue"]

    for i in range(360):
        pen.color(colors[i % 5])
        pen.width(i // 100 + 1)
        pen.forward(i)
        pen.left(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

    turtle.done()

draw_triangle()