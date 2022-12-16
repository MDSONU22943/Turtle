import turtle as t
t.bgcolor("black")
t.pensize(2)

def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)
t.speed(3)
t.color("red","pink")

t.begin_fill()
t.left(140)
t.forward(111.65)
curve()

t.lt(120)
curve()
t.fd(111.65)
t.end_fill()

t.mainloop()