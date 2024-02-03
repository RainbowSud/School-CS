import turtle
#Benjamin Swenson Cs-1400-MW1

#Head
turtle.penup()
turtle.goto(0,-150)
turtle.color("yellow")
turtle.pendown()
turtle.begin_fill()
turtle.circle(150)
turtle.end_fill()

#Main Mask
turtle.color("light blue")
turtle.begin_fill()
turtle.penup()
turtle.goto(0,-125)
turtle.pendown()
turtle.circle(125, 91)
turtle.goto(-125,0)
turtle.right(180)
turtle.circle(125,91)
turtle.end_fill()
turtle.penup()

#Left upper Strap
turtle.color("black")
turtle.goto(-122,-27.221)
turtle.pendown()
turtle.goto(-150,0)
turtle.penup()
#Right upper Strap
turtle.goto(122,-27.221)
turtle.pendown()
turtle.goto(150,0)
turtle.penup()
#Left lower strap
turtle.goto(-75,-100)
turtle.pendown()
turtle.goto(-120,-90)
turtle.penup()
#Right lower strap
turtle.goto(75,-100)
turtle.pendown()
turtle.goto(120,-90)
turtle.penup()

#Mask Polkadots
turtle.color("pink")
turtle.goto(-100,-25)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()

turtle.goto(-80,-40)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()

turtle.goto(-40,-80)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()

turtle.goto(-20,-40)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()

turtle.goto(0,-80)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()

turtle.goto(30,-85)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()

turtle.goto(-20,-105)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()

turtle.goto(-80,-75)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()

turtle.goto(20,-25)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()

turtle.goto(40,-40)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()

turtle.goto(80, -30)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()

turtle.goto(60, -80)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()

#Left eye
turtle.color("black")
turtle.goto(-60,35)
turtle.begin_fill()
turtle.pendown()
turtle.circle(30, steps = 5)
turtle.end_fill()
turtle.penup()
#Right eye
turtle.goto(60,35)
turtle.begin_fill()
turtle.pendown()
turtle.circle(30, steps = 5)
turtle.end_fill()
turtle.penup()

#Text
turtle.goto(150,100)
turtle.write("Hi, My name is Steve, I have a very nice Mask, also Covid Sucks")

#Ending
turtle.hideturtle()
turtle.done()
