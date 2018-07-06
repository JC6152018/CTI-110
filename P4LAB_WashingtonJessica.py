#P4LAB - Nested Loop
#CTI - 110
#Jessica Washington
#July 5th, 2018


#how to make a flower shape

#create screen and turtle
import turtle
wn= turtle.Screen()
wn.bgcolor("black")
fleur = turtle.Turtle()
fleur.shape("arrow")
fleur.pensize(5)
fleur.color("white")

#create flower shape
for i in range(10):
    for x in range(2):
        fleur.forward(100)
        fleur.right(60)
        fleur.forward(100)
        fleur.right(120)
    fleur.right(36)

turtle.exitonclick()
