import turtle as t

t.color("violet")
t.width("3")
t.speed(4)

for i in range(4):
    t.fd(150)
    t.lt(90)

t.penup()
t.goto(0,50)
t.pendown()

t.fd(150)

t.penup()
t.goto(0,100)
t.pendown()

t.fd(150)

t.penup()
t.goto(50,0)
t.pendown()

t.lt(90)
t.fd(150)

t.penup()
t.goto(100,0)
t.pendown()

t.fd(150)

t.mainloop()