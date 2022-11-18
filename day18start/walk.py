from turtle import Turtle, Screen
import random


tim = Turtle()
tim.shape("turtle")
tim.color("red", "green")


colors = ["royal blue", "dark red", "chocolate", "medium orchid", "medium slate blue"]
list = [0, 90, 180, 270]

for _ in range(200):
    tim.pensize(15)
    tim.speed(9)
    tim.color(random.choice(colors))
    tim.forward(50)

    tim.setheading(random.choice(list))

















screen = Screen()
screen.exitonclick()
