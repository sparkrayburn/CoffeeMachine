from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_data = screen.textinput(title="make your bet", prompt="Which turtle would win")
print(user_data)

tim = Turtle(shape="turtle")
tim.color("red")
tim.penup()
tim.goto(x=-230, y=0)

jon = Turtle(shape="turtle")
jon.color("green")
jon.penup()
jon.goto(x=-230, y=50)

tom = Turtle(shape="turtle")
tom.color("blue")
tom.penup()
tom.goto(x=-230, y=100)

jony = Turtle(shape="turtle")
jony.color("purple")
jony.penup()
jony.goto(x=-230, y=-50)

timy = Turtle(shape="turtle")
timy.color("black")
timy.penup()
timy.goto(x=-230, y=-100)

jonh = Turtle(shape="turtle")
jonh.color("pink")
jonh.penup()
jonh.goto(x=-230, y=-150)


def random_move(a):
    a.forward(10)


a = [tim, timy, jony, jonh, jon, tom]


def generate():
    c = random.choice(a)
    return c


gay = True

while gay:
    random_move(generate())
    if tim.xcor() == 200:
        print("red won")
        c = "red"
        if user_data ==c:
            print("you won ")
        else:
            print("lol")
        gay = False
    elif tom.xcor() == 200:
        print("blue won")
        c = "blue"
        if user_data == c:
            print("you won ")
        else:
            print("lol")
        gay = False
    elif timy.xcor() == 200:
        print("black won")
        c = "black"
        if user_data == c:
            print("you won ")
        else:
            print("lol")
        gay = False
    elif jonh.xcor() == 200:
        print("pink won")
        c = "pink"
        if user_data == c:
            print("you won ")
        else:
            print("lol")
        gay = False
    elif jon.xcor() == 200:
        print("green won")
        c = "green"
        if user_data == c:
            print("you won ")
        else:
            print("lol")
        gay = False
    elif jony.xcor() == 200:
        print("purple won")
        c = "purple"
        if user_data == c:
            print("you won ")
        else:
            print("lol")
        gay = False

screen.exitonclick()
