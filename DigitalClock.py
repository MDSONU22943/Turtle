import turtle
import time
import datetime as dte
# displaying time
tt1=turtle.Turtle() 
# creating rectangle 
tt2=turtle.Turtle()   

screen=turtle.Screen()
screen.bgcolor("pink")

secs=dte.datetime.now().second
mins=dte.datetime.now().minute
hrs=dte.datetime.now().hour

tt2.pensize(3)
tt2.color("white")

for j in range(2):
    tt2.fd(200)
    tt2.lt(90)
    tt2.fd(70)
    tt2.lt(90)


# displaying the generated time
tt1.write(str(hrs).zfill(2) + ":" +str(mins).zfill(2)+":"+str(secs).zfill(2),font=("callibri Narrow",37,"bold"))
time.sleep(1)
secs=secs+1
if secs==60:
    secs=0
    mins=mins+1
if mins==60:
    mins=0
    hrs=hrs+1
if hrs==13:
    hrs=1


turtle.mainloop()
