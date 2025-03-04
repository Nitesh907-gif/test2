import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('yellow')

t = turtle.Turtle()
t.speed(1)


t.penup()
t.goto(0,0)
t.pendown()
t.pencolor('cyan')
t.fillcolor('cyan')
t.begin_fill()

t.setheading(45)
t.forward(70)

t.setheading(135)
t.forward(70)

t.setheading(225)
t.forward(70)

t.setheading(315)
t.forward(70)



t.end_fill()

t.penup()
t.goto(100,0)
t.pendown()

t.pencolor('brown')
t.fillcolor('brown')
t.begin_fill()

t.setheading(45)
t.forward(70)

t.setheading(135)
t.forward(70)

t.setheading(225)
t.forward(70)

t.setheading(315)
t.forward(70)
t.end_fill()
t.hideturtle()





#this is the last line of code
turtle.done()