# def GradeMark(mark):
#     if mark >= 90:
#         return "A"
#     elif mark >= 80:
#         return "B"
#     elif mark >= 70:
#         return "C"
#     elif mark >= 60:
#         return "D"
#     else:
#         return "F"
#
# marks = [95, 90, 89.9, 80, 79.9, 70, 65, 60, 59.5, 0]
# for mark in marks:
#     print("Grade is", GradeMark(mark))
#
# mark = float(input("Enter mark: "))
# print("Grade is", GradeMark(mark))
#
# import turtle
# from sysconfig import get_paths
# def chooseColor(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
#
# def drawBar(t, height, gap):
#     t.penup()
#     t.lt(90)
#     if height >= 0:
#         t.fd(height + gap)
#         t.write(" " + str(height))
#         t.bk(height + gap)
#
#     else:
#         t.fd(gap)
#         t.write(" " + str(height))
#         t.bk(gap)
#
#     t.rt(90)
#     t.pendown()
#
#     t.fillcolor(chooseColor(height))
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
#     minheight = min(data)
#     num_bars = len(data)
#     border = 10
#     gap = (maxheight - border) / 25
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#     right = 40 * num_bars + border
#     top = maxheight + 4 * border
#     bottom = minheight + 4 * border
#     wn.setworldcoordinates(-border, bottom, right, top)
#     t = turtle.Turtle()
#     t.color("blue")
#     t.fillcolor("red")
#     t.pensize(3)
#
#     for height in data:
#         drawBar(t, height, gap)
#
#     wn.exitonclick()
#     t.speed(10)
# data = [-48, 117, -48, 200, -48, 210, -48, 220]
# barChart(data)

def findHypot(side1, side2):
    return (side1**2 + side2**2)**0.5

side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))

print(findHypot(side1, side2))