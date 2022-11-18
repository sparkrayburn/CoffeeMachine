FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-150, 250)
        self.level = 1
        self.write(f"Level = {self.level}", font=FONT)

    def score_keeper(self):
        self.clear()
        self.write(f"Level = {self.level}", font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT)

