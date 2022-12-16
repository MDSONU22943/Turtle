import turtle as t

t.bgcolor("black")
t.pencolor("red")

a=0
b=0

''' 0 -> fastest
    10 -> fast
    6 -> normal
    3 -> slow
    1 -> slowest '''
t.speed(10)
t.penup()
t.goto(0,200)
t.pendown()

while(True):
    t.fd(a)
    t.rt(b)
    a=a+3
    b=b+1
    if b==210:
        break


t.mainloop()