import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw the cat's body
t.fillcolor("orange")
t.begin_fill()
t.circle(50)
t.end_fill()

# Draw the cat's ears
t.penup()
t.goto(-30, 80)
t.pendown()
t.fillcolor("pink")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(30, 80)
t.pendown()
t.fillcolor("pink")
t.begin_fill()
t.circle(20)
t.end_fill()

# Draw the cat's eyes
t.penup()
t.goto(-20, 30)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(20, 30)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(-20, 35)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(20, 35)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(5)
t.end_fill()

# Draw the cat's nose
t.penup()
t.goto(0, 10)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(5)
t.end_fill()

# Draw the cat's whiskers
t.penup()
t.goto(-20, 10)
t.pendown()
t.right(20)
t.forward(30)

t.penup()
t.goto(-20, 5)
t.pendown()
t.right(-40)
t.forward(30)

t.penup()
t.goto(20, 10)
t.pendown()
t.right(-20)
t.forward(30)

t.penup()
t.goto(20, 5)
t.pendown()
t.right(40)
t.forward(30)

# Hide the turtle cursor
t.hideturtle()

# Keep the window open until it's closed manually
turtle.done()
