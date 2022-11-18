from turtle import Turtle, Screen



tim = Turtle()
tim.shape("turtle")
tim.color("red", "green")


sides = 3
g = 0
pen = ["blue", "green", "black", "pink", "red", "brown"]
for _ in range (6):
    a = pen[g]
    tim.pencolor(a)
    g += 1
    angle = 360 / sides
    for _ in range(sides):

        tim.forward(100)
        tim.right(angle)
    # tim.home()
    sides += 1


















screen = Screen()
screen.exitonclick()
