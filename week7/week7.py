# def sumTo(n):
#     return n * (n + 1) / 2
#     return total
# print(sumTo(10))
# n = int(input("Please enter a number: "))
# print("Sum is", sumTo(n))
import math


# import turtle
#
# def drawStar(t, n, size):
#     angle = 180 - 180/n
#     for i in range(n):
#         turtle.fd(size)
#         turtle.right(angle)
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.pensize(3)
#
# drawStar(t, 7, 200)
#
# wn.exitonclick()

# def sumTo(n):
#     total = 0
#     for i in range(1, n+1):
#         total = total + i
#     return total
# n = int(input("Enter a number: "))
# print("Sum is", sumTo(n))

# def mySqrt(x):
#     guess = x/2
#     for i in range(20):
#         guess = (1/2) * (guess + x / guess)
#     return guess
# n = int(input("Enter a positive integer: "))
# print("the result is",mySqrt(n))
# print("the result is",math.sqrt(n))

# import turtle
#
# def drawSprite(someturtle, legs, length):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.fd(length)
#         someturtle.backward(length)
#         someturtle.left(angle)
# def fancySquare(t, size):
#     for corner in range(4):
#         drawSprite(t, 8, 20)
#         t.fd(size)
#         t.left(90)
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.color("purple")
# t.speed(100)
# t.pensize(2)
# fancySquare(t, 100)
# wn.exitonclick()

# import turtle
#
# def drawTip(t, size):
#     t.begin_fill()
#     t.lt(90)
#     t.fd(size / 2)
#     t.rt(120)
#     t.fd(size)
#     t.rt(120)
#     t.fd(size)
#     t.rt(120)
#     t.fd(size / 2)
#     t.rt(90)
#     t.end_fill()
#
# def drawSpriteWithTips(someturtle, legs, length):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.fd(length)
#         drawTip(someturtle, 10)
#         someturtle.bk(length)
#         someturtle.lt(angle)
# def fancySquare(t, size):
#     for corner in range(4):
#         drawSpriteWithTips(t, 8 , 20)
#         t.fd(size)
#         t.lt(90)
# wn = turtle.Screen()
# wn.bgcolor("lightgray")
# t = turtle.Turtle()
# t.speed(100)
# t.pensize(3)
# fancySquare(t, 100)
# wn.exitonclick()

# def checkSign(x):
#     if x >= 0:
#         return "the number is positive"
#     elif x < 0:
#         return "the number is negative"
#     else:
#         return "the number is zero"
# numbers = [-7, 5, 0]
# for number in numbers:
#     print(number, checkSign(number))
# n = int(input("enter a number: "))
# print(checkSign(n))

# import turtle
# from sysconfig import get_paths
#
#
# def drawBar(t, height, gap):
#     t.penup()
#     t.lt(90)
#     t.fd(height + gap)
#     t.write(" " + str(height))
#     t.bk(height + gap)
#     t.rt(90)
#     t.pendown()
#
#     t.begin_fill()
#     t.lt(90)
#     t.fd(height)
#     t.rt(90)
#     t.fd(40)
#     t.rt(90)
#     t.fd(height)
#     t.lt(90)
#     t.end_fill()
#
# def barChart(data):
#     maxheight = max(data)
#     num_bars = len(data)
#     border = 10
#     gap = (maxheight - border) / 25
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#     right = 40 * num_bars + border
#     top = maxheight + 4 * border
#     wn.setworldcoordinates(-border, -border, right, top)
#     t = turtle.Turtle()
#     t.color("blue")
#     t.fillcolor("red")
#     t.pensize(3)
#
#     for height in data:
#         drawBar(t, height, gap)
#
#     wn.exitonclick()
# data = [48, 117, 200, 240, 160, 260, 220]
# barChart(data)