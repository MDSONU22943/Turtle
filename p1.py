import turtle
turtle.bgcolor("black")
turtle.pensize(0.5)
turtle.speed(10.2)

for i in range(10):
    for colours in ["red","magenta","cyan","blue","yellow","green","white","grey","brown"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(20)
turtle.hideturtle()        
