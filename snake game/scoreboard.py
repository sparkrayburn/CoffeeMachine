

from turtle import Turtle

with open("highscore.txt", mode="r") as file:
    contents = file.read()
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.high_score = 0

        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.hideturtle()
        self.clear()
        self.write(arg=f"Your score = {self.score}  {contents}", align="center", font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"Highscore = {self.score}")
        self.score = 0
        self.update_scoreboard()






