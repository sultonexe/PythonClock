#Simple Clock with Python3 Programming
#Coded By @sulton.exe
#Version 0.1
#TOLONG JANGAN RECODE YA :) HARGAI SI PEMBUAT TERIMA KASIH :D

import time
import turtle

wn = turtle.Screen()
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.title("Simple Clock By @sulton.exe")

#Drawing Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)
wn.tracer(0)

def draw_clock(h, m, s, pen):
    
    #Drawing Clock
    pen.up()
    pen.goto(0 ,210)
    pen.setheading(180)
    pen.color("black")
    pen.pendown()
    pen.circle(210)

    #Draw The Lines
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30) 

    #Draw Clock Hour Hands
    pen.penup()
    pen.goto(0,0)
    pen.color("black")
    pen.setheading(90)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.pendown() 
    pen.fd(100)

    #Draw Clock Minute Hand
    pen.penup()
    pen.goto(0,0)
    pen.color("red")
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

    #Draw Clock Second Hand
    pen.penup()
    pen.goto(0,0)
    pen.color("yellow")
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(50)

while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%s"))

    draw_clock(h, m, s, pen)
    wn.update()

    time.sleep(1)

    pen.clear()

wn.mainloop()