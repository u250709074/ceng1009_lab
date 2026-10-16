# import random
# for i in range(10):
#     print(random.random())
#

# import random
# for i in range(10):
#     print(random.randint(25,35))

# import math
# a = int(input("enter length:"))
# b = int(input("enter width:"))
# hypotenuse = math.sqrt(a**2 + b**2)
# print(hypotenuse)

# import math
# def areaofcircle(r):
#     return math.pi * r**2
# print(areaofcircle(5))

# import turtle
# def  drawstar(t, side):
#     for i in range(5):
#         t.fd(side)
#         t.right(144)
#
# screen = turtle.Screen()
# tess = turtle.Turtle()
# drawstar(tess, 100)
# screen.exitonclick()

# def drawsquare(t, side):
#     for i in range(4):
#         t.fd(side)
#         t.left(90)
#
# import turtle
# tess = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# tess.pensize(3)
# tess.pencolor("hotpink")
# for i in range(5):
#     drawsquare(tess, 20)
#     tess.penup()
#     tess.fd(40)
#     tess.pendown()
#
#
# screen.exitonclick()
#
# def drawsquare(t, side):
#     for i in range(4):
#         t.fd(side)
#         t.left(90)
#
# import turtle
# tess = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# tess.pensize(3)
# tess.pencolor("hotpink")
# for i in range(20, 120, 20):
#     drawsquare(tess, i)
#     tess.penup()
#     tess.bk(10)
#     tess.right(90)
#     tess.forward(10)
#     tess.left(90)
#     tess.pendown()
# screen.exitonclick()