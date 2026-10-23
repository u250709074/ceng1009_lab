import turtle

# -- setup --
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()

# -- functions --

def drawPoly(someturtle, somesides, somesize):
    angle = 360 / somesides
    for i in range(somesides):
        someturtle.fd(somesize)
        someturtle.left(angle)
def drawSpiral(someturtle, angle):
    size = 1
    for i in range(100):
        someturtle.fd(size)
        someturtle.right(angle)
        size = size + 2
def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3 , somesize)

def drawStar (someturtle, size):
    for i in range(5):
        someturtle.fd(size)
        someturtle.right(144)
def drawSprite(someturtle,legs, length):
    angle = 360 / legs
    for i in range(legs):
        someturtle.fd(length)
        someturtle.backward(length)
        someturtle.left(angle)

# -- exercises --
# Exercise 1
# tess.pencolor("hotpink")
# tess.pensize(3)
# drawPoly(tess, 8, 50)

# Exercise 2
# tess.pencolor("blue")
# for i in range(20):
#     drawPoly(tess, 4, 100)
#     tess.left(18)
#
#

# # Exercise 3
# tess.pencolor("blue")
# tess.penup()
# tess.goto(-200, 0)
# tess.pendown()
# drawSpiral(tess, 90)
# tess.penup()
# tess.goto(100, 0)
# tess.pendown()
# drawSpiral(tess, 91)

# Exercise 4
# drawEquitriangle(tess, 100)

# Exercise 5
# tess.pencolor("hotpink")
# for i in range(5):
#     drawStar(tess, 50)
#     tess.penup()
#     tess.fd(250)
#     tess.right(144)
#     tess.pendown()

# Exercise 6
# drawSprite(tess, 15, 120)

# -- finish --
wn.exitonclick()