# Digital Scene
# Angelo, Nathan, Jazmin
# 10/04/24

# digital scene of Bikini Bottom from Spongebob

# initialize
import turtle
import random

nja = turtle.Turtle() # our group's initials
nja.speed(20)
turtle.colormode(255)

# Functions

# coded by: Nathan
# draws the roads, sand, and sky
def road():
    nja.dot(20000,"#66ccff")
    nja.left(90)
    nja.forward(40)
    nja.left(90)
    nja.color("#fff1cc")
    nja.begin_fill()
    for i in range(4):
        nja.forward(500)
        nja.left(90)
        nja.forward(500)
    nja.end_fill()
    nja.pencolor("gray")
    nja.penup()
    nja.left(90)
    nja.forward(340)
    nja.pendown()
    nja.right(120)
    nja.forward(560)
    nja.backward(560)
    nja.left(120)
    nja.penup()
    nja.backward(340)
    nja.forward(440)
    nja.pendown()
    nja.right(120)
    nja.forward(560)
    nja.color("#7c837e")
    nja.begin_fill()
    nja.right(120) # start of first hall
    nja.forward(250)
    nja.right(60)
    nja.forward(40)
    nja.right(120)
    nja.forward(250) # end of first hall
    nja.end_fill()
    nja.left(120)
    nja.forward(150)
    nja.left(60) # start of second hall
    nja.forward(100)
    for i in range(4):
        nja.penup()
        nja.forward(20)
        nja.pendown()
        nja.color("#7c837e")
        nja.begin_fill()
        nja.right(60)
        nja.forward(40)
        nja.left(60)
        nja.forward(20)
        nja.left(120)
        nja.forward(40)
        nja.left(60)
        nja.forward(20)
        nja.left(180)
        nja.forward(20)
        nja.end_fill()
    nja.penup()
    nja.backward(260)
    nja.pendown()
    nja.right(60)
    nja.forward(200)
    nja.left(60)
    nja.color("#7c837e")
    nja.begin_fill()
    nja.forward(250)
    nja.right(60)
    nja.forward(50)
    nja.right(120)
    nja.forward(150) # end of last hall
    nja.end_fill()
    nja.left(120)
    nja.forward(40)
    nja.color("#7c837e")
    nja.begin_fill()
    nja.left(30) # start of color
    nja.forward(470)
    nja.right(90)
    nja.forward(85)
    nja.right(90)
    nja.forward(500)
    nja.right(90)
    nja.left(60)
    nja.forward(650)
    nja.right(120)
    nja.forward(106)
    nja.right(60)
    nja.forward(585)
    nja.end_fill()
    nja.backward(60)
    nja.left(60)
    nja.color("green")
    nja.penup()
    nja.dot(20) # dots outside spongebob's house
    nja.forward(25)
    nja.dot(10)
    nja.forward(30)
    nja.dot(25)
    nja.forward(30)
    nja.dot(20)
    nja.forward(35)
    nja.dot(22)
    nja.forward(10)
    nja.left(90)
    nja.forward(20)
    nja.left(90)
    nja.forward(8)
    nja.dot(15)
    nja.forward(25)
    nja.dot(13)
    nja.forward(20)
    nja.dot(10)
    nja.forward(40)
    nja.dot(16)
    nja.forward(30)
    nja.dot(17)
    nja.seth(0)

# coded by: Jazmin
# draws patrick's house
# x = integer
# y = integer
def patrick(x,y):
  nja.goto(x,y)
  nja.left(90)
  nja.color("#660033")
  nja.begin_fill()
  nja.circle(100,180) # draws a semi-circle and fills it in
  nja.left(90)
  nja.forward(200)
  nja.end_fill()
  nja.goto(x-100,y+100)
  nja.width(3)
  nja.color("#e6e600")
  nja.left(90)
  nja.pendown()
  nja.forward(40)
  nja.penup()
  nja.goto(x-120,y+130)
  nja.penup()
  nja.right(90)
  nja.pendown()
  nja.forward(40)
  nja.penup()  
  nja.goto(x-130,y+120)
  nja.pendown()
  nja.forward(60)
  nja.width(1)

# coded by: Jazmin
# draws the base shape of Squidward's house (trapezoid)
# x = integer
# y = integer
def squidwardBase(x,y): 
    nja.penup()
    nja.goto(x,y)
    nja.pendown()
    nja.color("#2d5986")
    nja.begin_fill()
    nja.left(85) # draws the house shape
    nja.forward(260)
    nja.right(85)
    nja.forward(90)
    nja.right(85)
    nja.forward(260)
    nja.right(95)
    nja.forward(135)
    nja.end_fill()

# coded by: Jazmin
# functions for the rectangles on the side of the house
# x = integer
# y = integer
def squidwardEar(x,y): 
    nja.penup()
    nja.goto(x,y)
    nja.pendown()
    nja.color("#336699")
    nja.begin_fill()
    for i in range(2): # to draw a vertical rectangle
        nja.right(90)
        nja.forward(90)
        nja.right(90)
        nja.forward(30)
    nja.end_fill()

# coded by: Jazmin
# draws the door
# x = integer
# y = integer
def squidwardDoor(x,y): 
    nja.penup()
    nja.goto(x,y)
    nja.pendown()
    nja.color("#cc7a00")
    nja.begin_fill()
    nja.left(180)
    nja.forward(20)
    nja.left(90)
    nja.forward(30)
    nja.circle(20,180)
    nja.forward(31)
    nja.end_fill()
    nja.goto(x+10,y+20)
    nja.color("yellow")
    nja.dot(10) # draws the door handle

# coded by: Jazmin
# draws the nose of the house (trapezoid)
# x = integer
# y = integer
def squidwardNose(x,y): 
    nja.penup()
    nja.goto(x,y)
    nja.pendown()
    nja.color("#4080bf")
    nja.begin_fill()
    nja.left(90)
    nja.forward(62)
    nja.left(105)
    nja.forward(110)
    nja.left(75)
    nja.forward(5)
    nja.left(75)
    nja.forward(110)
    nja.seth(0)
    nja.end_fill()

# coded by: Jazmin
# draws the eyebrow
# x = integer
# y = integer
def squidwardEyebrow(x,y): 
    nja.penup()
    nja.goto(x,y)
    nja.pendown()
    nja.color("#4080bf")
    nja.begin_fill()
    for i in range(2): # to draw a horizontal rectangle
        nja.forward(95)
        nja.left(90)
        nja.forward(15)
        nja.left(90)
    nja.end_fill()

# coded by: Jazmin
# draws the eyes (windows)
# x = integer
# y = integer
def squidwardEye(x,y): 
    nja.penup()
    nja.goto(x,y)
    nja.pendown()
    nja.color("#80dfff")
    nja.dot(38) # for the glass of the window
    nja.goto(x, y-19)
    nja.color("#008ae6")
    nja.width(10)
    nja.circle(19) # for the border around the window
    nja.width(1)

# coded by: Jazmin
# draws squidward's house
def squidward():
    squidwardBase(-100,-80) 
    squidwardEar(-115,0) # left ear
    squidwardEar(20,0) # right ear
    squidwardDoor(-30,-75)
    squidwardNose(-63,-20)
    squidwardEye(-62,70) # left eye
    squidwardEye(-2,70) # right eye
    squidwardEyebrow(-80,90)

# coded by: Jazmin
# draws the flowers in the sky with different colors and locations
# color = string
# x = integer
# y = integer
def flower(color,x,y):
    nja.width(2)
    nja.penup()
    nja.color(color)
    nja.goto(x,y)
    nja.pendown()
    nja.circle(7) # draws the center of the flower
    nja.penup()
    nja.goto(x-40,y-75)
    nja.pendown()
    nja.circle(20,-90) # begins drawing the flower
    nja.circle(25,-90)
    nja.circle(-10,-90)
    nja.circle(-15,-90)
    nja.circle(-75,-30)
    nja.circle(25,-100)
    nja.circle(35,-170)
    nja.circle(-25,-210)
    nja.circle(30,-290)
    nja.circle(-20,-90)
    nja.circle(-60,-30)
    nja.circle(-30,-70)
    nja.circle(25,-160)
    nja.circle(30,-120)
    nja.circle(-45,-40)
    nja.circle(-20,-50)
    nja.circle(-10,-155)
    nja.circle(45,-100)
    nja.circle(35,-200)
    nja.circle(-30,-70)
    nja.circle(-10,-100)
    nja.circle(-20,-70)
    nja.circle(35,-25)
    nja.circle(15,-65)
    nja.circle(37,-70)
    nja.penup()
    nja.width(1) # resets the size of the turtle
    nja.seth(0) # resets the angle

# coded by: Angelo
# a function for positioning the turtle to other locations without showing the pen markings
# x = integer
# y = integer
def goto(x,y):
  nja.pu()
  nja.goto(x,y)
  nja.pd()

# coded by: Angelo
# creates a vertical oval
# r = integer
def talloval(r):               # Vertical Oval

    for loop in range(2):      # Draws 2 halves of ellipse
        nja.circle(r,90)    # Long curved part
        nja.circle(r/2,90)  # Short curved part

# coded by: Angelo
# creates a horizontal oval
# r = integer
def flatoval(r):               # Horizontal Oval
  nja.right(45)
  for loop in range(2):
    nja.circle(r,90)
    nja.circle(r/2,90)

# coded by: Angelo
# Draws spongebob's house
def spongebob():
  nja.color("orange")
  goto(190,-170)
  nja.left(90)
  nja.begin_fill()
  flatoval(150)
  goto(50,-120)
  nja.seth(0)
  nja.end_fill()
  nja.forward(175)
  nja.pensize(55)
  nja.color("#fff1cc")
  goto(215,-165)
  nja.bk(170)
  nja.pensize(1)
  nja.color("black")
  goto(100,50)
  nja.seth(180)
  nja.pensize(25)
  nja.color("green")
  nja.circle(-45,90)
  nja.seth(0)
  nja.goto(110,55)
  goto(100,60)
  nja.seth(90)
  nja.circle(-130,45)
  nja.goto(125,50)
  nja.circle(90,45)
  nja.seth(0)
  nja.goto(160,50)
  nja.circle(35,130)
  nja.goto(160,50)
  goto(190,5)
  nja.seth(0)
  nja.color("#d1e0e0")
  nja.pensize(10)
  nja.forward(50)
  nja.left(90)
  nja.forward(30)
  nja.pensize(15)
  nja.begin_fill()
  goto(150,-145)
  nja.seth(0)
  nja.left(45)
  nja.pu()
  talloval(60)
  nja.pd()
  nja.end_fill()
  nja.color("black")
  goto(80,-15)
  nja.dot(40,"#d1e0e0")
  goto(50,-120)
  nja.seth(0)
  nja.pensize(55)
  nja.color("#fff1cc")
  goto(215,-165)
  nja.bk(170)
  nja.pensize(1)
  nja.color("black")
  goto(80,-15)
  nja.dot(50/2,"#80bfff")
  goto(190,-75)
  nja.dot(40,"#d1e0e0")
  nja.dot(50/2,"#80bfff")

# coded by: Angelo
# makes a bubble
def bubble():
  nja.penup()
  nja.goto(random.randint(-300,300), random.randint(200,300))
  nja.pendown()
  nja.circle(random.randint(10,35))

# coded by: Angelo
# makes multiple bubbles
def bubbles(x,y):
  for i in range(5):
    bubble()

# draws the final digital scene
def digitalScene(): 
  road()
  for i in range(3):
      flower((random.randint(0,255),random.randint(0,255),random.randint(0,255)),random.randint(-300,300),random.randint(150,300))
  patrick(-150,-20)
  squidward()
  spongebob()
  bubbles(random.randint(-300,300), random.randint(-200,300))

# main
digitalScene()
