#P4T1C Snowflake
#CTI 110
#Jessica Washington
#July 2nd, 2018

#create screen and turtle
import turtle
import random
wn= turtle.Screen()
wn.bgcolor("black")
snowy = turtle.Turtle()
snowy.shape("arrow")
snowy.pensize(5)
snowy.color("white")

#set up snowflake shape
snowy.penup()
snowy.forward(90)
snowy.left(45)
snowy.pendown()

#create snowflake
def branch():
    for i in range(3):
        for x in range(3):
            snowy.forward(30)
            snowy.backward(30)
            snowy.right(45)
        snowy.left(90)
        snowy.backward(30)
        snowy.left(45)
    snowy.right(90)
    snowy.forward(90)

for i in range(8):
    branch()
    snowy.left(45)

snowy.speed(1)

        



