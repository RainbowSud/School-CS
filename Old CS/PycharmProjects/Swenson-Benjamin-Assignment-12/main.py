# Benjamin Swenson - CS 1400 - Section 1
import turtle
import random

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        a = random.randint(-7, 10)  # Create random int
        b = random.randint(-7, 10)
        t.right(20 + a)  # Apply random int to change the angle
        tree(branchLen-15 + b, t)  # Apply random int to change the length
        t.left(40 + a)
        tree(branchLen-15 + b, t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)  # Makes the program run faster
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(120, t)
    myWin.exitonclick()

main()