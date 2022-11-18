from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()



def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)

def move_right():
    tim.right(5)

def move_left():
    tim.left(5)

def clear():
    tim.home()
    tim.clear()


tim.speed(0)
screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun= move_backwards)
screen.onkeypress(key="d", fun= move_right)
screen.onkeypress(key="a", fun= move_left)
screen.onkeypress(key="c", fun= clear)

screen.exitonclick()








