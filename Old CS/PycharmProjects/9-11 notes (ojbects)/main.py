import turtle


turtle.goto(0,0)
turtle.penup()
turtle.goto(100,100)
turtle.pendown()
turtle.circle(100)
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.circle(100, steps= 12)
turtle.end_fill()
turtle.penup()
turtle.goto(200,200)
turtle.pendown()
turtle.color("purple")
turtle.begin_fill()
turtle.goto(200,300)
turtle.goto(300,300)
turtle.goto(200,200)
turtle.end_fill()
turtle.done()


