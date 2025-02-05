import turtle
import colorsys as cs


turtle.setup(800,800)
turtle.speed(0)
turtle.width(2)
turtle.bgcolor("ivory")
for j in range(25):
    for i in range(15):
        turtle.color(cs.hsv_to_rgb(i/15,j/25,1))
        turtle.right(90)
        turtle.circle(200-j*4,90)
        turtle.left(90)
        turtle.circle(200-j*4,90)
        turtle.right(180)
        turtle.circle(50,24)
        




def draw_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.speed(0)
    colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'white', 'Gray', 'Pink', 'Brown', 'Silver', 'Ivory', 'Beige', 'Turquoise']
    for i in range(3600):
        pen.color(colors[i % 14])
        pen.width(i // 100 + 2)
        pen.forward(i)
        pen.left(59)

    turtle.hideturtle()
turtle.done()

draw_spiral()
    