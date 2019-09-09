#Simple Clock with Python3 Programming
#Coded By @sulton.exe
#Version 0.2
#TOLONG JANGAN RECODE YA :) HARGAI SI PEMBUAT TERIMA KASIH :D

import time
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Simple Clock With Python Version 0.2 by @sulton.exe")


#drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(j, m, d, pen):

    #gambar jam
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("white")
    pen.pendown()
    pen.circle(210)

    #gambar garis
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    wn.tracer(0)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    #gambar jarum jam
    pen.penup()
    pen.goto(0, 0)
    pen.color("white")
    pen.setheading(90)
    angle = (j / 12) * 360
    pen.rt(angle)
    pen.pendown()   
    pen.fd(100)

    #gambar jarum menit
    pen.penup()
    pen.goto(0, 0)
    pen.color("red")
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pendown()   
    pen.fd(170)

    #gambar jarum detik
    pen.penup()
    pen.goto(0,0)
    pen.color("green")
    pen.setheading(90)
    angle = (d / 60) * 360
    pen.rt(angle)
    pen.pendown()   
    pen.fd(50)


while True:

    j = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    d = int(time.strftime("%s"))

    draw_clock(j, m, d, pen)
    wn.update()

    time.sleep(1)
    
    pen.clear()

wn.mainloop()