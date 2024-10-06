import turtle

def draw_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.speed(0)
    colors= ["red", "yellow", "blue", "green", "orange", "purple"]

    for i in range(360):
        pen.color(colors[i % 6])
        pen.width(i // 100 +1 )
        pen.forward(i)
        pen.left(5904)

    turtle.done()

draw_spiral()