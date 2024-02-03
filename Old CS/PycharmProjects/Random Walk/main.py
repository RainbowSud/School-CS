import turtle
import random

turtle.goto(0, 0)
turtle.pendown()
turtle.width(2)

while True:

    if turtle.xcor() <= -500:
        break
    if turtle.xcor() >= 500:
        break
    if turtle.ycor() >= 500:
        break
    if turtle.ycor() <= -500:
        break

    direction = random.randint(1, 4)

    if direction == 1:
        turtle.goto(turtle.xcor()+10, turtle.ycor())
    if direction == 2:
        turtle.goto(turtle.xcor()-10, turtle.ycor())
    if direction == 3:
        turtle.goto(turtle.xcor(), turtle.ycor()+10)
    if direction == 4:
        turtle.goto(turtle.xcor(), turtle.ycor()-10)

turtle.done()
