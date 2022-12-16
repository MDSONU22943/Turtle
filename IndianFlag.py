import turtle as t
from turtle import *

t.speed(20)

t.penup()
t.goto(-150,125)
t.pendown()

t.color("orange")
t.begin_fill()
t.fd(400)
t.rt(90)
t.fd(84)
t.rt(90)
t.fd(400)
t.end_fill()

t.lt(90)
t.fd(84)


t.color("green")
t.begin_fill()
t.fd(84)
t.lt(90)
t.fd(400)
t.lt(90)
t.fd(84)
t.end_fill()


t.penup()
t.goto(35,0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(35)
t.end_fill()



t.penup()
t.goto(30,0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(30)
t.end_fill()


t.penup()
t.goto(-27,-4)
t.pendown()
t.color("navy")

for i in range(24):
    t.begin_fill()
    t.circle(2)
    t.end_fill()
    t.penup()
    t.fd(7)
    t.rt(15)
    t.pendown()


t.color("navy")
t.penup()
t.goto(10,0)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()


t.penup()
t.goto(0,0)
t.pendown()
t.pensize()
for i in range(24):
    t.fd(30)
    t.backward(30)
    t.lt(15)


t.color("brown")
t.pensize(10)
t.penup()
t.goto(-150,125)
t.rt(180)
t.pendown()
t.fd(500)



t.mainloop()