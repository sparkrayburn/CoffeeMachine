# import turtle
#
# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon", ["Picachu", "Squirtle", "Charamander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "c"
print(table)

