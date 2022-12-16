import turtle as t

t.bgcolor("black")
t.pensize(2)
t.speed(0)

for i in range(6):
    for colors in ["red","blue","magenta","green","yellow","white"]:
        t.pencolor(colors)
        t.circle(100)
        t.lt(10)

t.mainloop()





