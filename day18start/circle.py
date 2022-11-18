from turtle import Turtle, Screen
import random
import turtle as t

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.color("red", "green")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color



tim.speed(0)
for _ in range(int(360/8)):
    tim.pencolor(random_color())
    tim.circle(70)
    tim.left(8)






#
#
# lists = [0, 90, 180, 270]
#
# for _ in range(200):
#     random_color()
#     tim.pensize(15)
#     tim.speed(9)
#     tim.color(random_color())
#     tim.forward(50)
#
#     tim.setheading(random.choice(lists))

















screen = Screen()
screen.exitonclick()
