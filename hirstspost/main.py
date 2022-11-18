# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
from turtle import Turtle, Screen
import turtle as t

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]
tim = Turtle()
t.colormode(255)
tim.hideturtle()
# tim.shape("turtle")
# tim.color("red", "green")


def random_color():
    color_select = random.choice(color_list)
    return color_select


def move_up():
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.right(180)
    tim.pendown()


tim.speed(0)
tim.pensize(10)
for _ in range(10):
    for _ in range(10):
        a = random_color()
        r = a[0]
        g = a[1]
        b = a[2]
        tim.color(r, g, b)
        tim.circle(5)
        tim.penup()
        tim.forward(50)
        tim.pendown()
    move_up()















screen = Screen()
screen.exitonclick()
