#P4T1 Turtle Lab
#P4Lab1: Shapes
#CTI 110
#Jessica Washington

#create turtles

import turtle
wn = turtle.Screen()
jess = turtle.Turtle()
wn.title("Square and Triangle")
jess.shape("turtle")
jess.color("hotpink")
jess.pensize(5)

ed = turtle.Turtle()
ed.color("blue")
ed.pensize(5)

#create square
for x in range(4):
    jess.forward(50)
    jess.left(90)

#create triangle

for i in range(3):
    ed.forward(60)
    ed.left(120)

wn.mainloop()





