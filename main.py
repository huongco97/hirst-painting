### Extract the color RGB from an image ###
# import colorgram
#
# k = 30
# colors = colorgram.extract('image.jpg', k)
# list = []
# for i in range(12):
#     red = colors[i].rgb.r
#     green = colors[i].rgb.g
#     blue = colors[i].rgb.b
#     list.append((red, green, blue))
# print(list)
from random import randint
import turtle as t

tim = t.Turtle()

color_list = [(202, 166, 109), (237, 240, 244), (150, 73, 49), (222, 202, 139), (167, 151, 45), (54, 92, 123),
              (133, 33, 24), (133, 163, 184), (49, 117, 88)]

screen = t.Screen()
screen.colormode(255)


def color():
    i = randint(0, len(color_list) - 1)
    return color_list[i]


tim.hideturtle()
tim.speed('fastest')
tim.penup()
tim.goto(-200, -200)
for j in range(10):
    tim.goto(-200, -200 + 50 * j)
    for i in range(10):
        tim.color(color())
        tim.begin_fill()
        tim.dot(20)
        tim.end_fill()
        tim.fd(50)
tim.pendown()

screen.exitonclick()
