from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()
turtle.hideturtle()
turtle.penup()
turtle.color("black")
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
states = data["state"]
state_list = states.to_list()
is_on = True
states_guessed = []
while len(states_guessed) < 50:
    user_data = screen.textinput(title="US States", prompt="Enter the States").title()
    if user_data == "Exit":
        break
    for pos in state_list:
        if user_data == pos:
            states_guessed.append(user_data)
            x_cords = data[data.state == pos].x
            y_cords = data[data.state == pos].y
            turtle.goto(int(x_cords), int(y_cords))
            turtle.write(user_data, font=("Arial", 7, "normal"))

states_missed = [missed for missed in state_list if missed not in states_guessed ]
# for miss in states_guessed:
#     for stat in state_list:
#         if miss != stat:
#             states_missed.append(stat)


file = pandas.DataFrame(states_missed)
print(file)
# file.to_csv("oops_you_missed these.csv")