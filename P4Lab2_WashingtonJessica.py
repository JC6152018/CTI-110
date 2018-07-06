#P4T1 Turtle Lab
#P4Lab2: Initials
#CTI 110
#Jessica Washington

#create turtle

import turtle
wn = turtle.Screen()
jess = turtle.Turtle()
wn.title("Initals")
jess.shape("arrow")
jess.color("hotpink")
jess.pensize(5)

#create first initial
jess.right(90)
jess.forward(70)
for i in range(2):
    jess.right(90)
    jess.forward(30)

#move turtle
jess.penup()
jess.right(90)
jess.forward(50)
jess.left(90)
jess.forward(40)
jess.pendown()

#create last initial
jess.left(180)
jess.forward(70)
jess.left(135)
jess.forward(35)
jess.right(90)
jess.forward(35)
jess.left(135)
jess.forward(70)

wn.mainloop()





