from turtle import Turtle
from paddle import Paddle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()


        self.scorekeeper()

    def scorekeeper(self):
        self.hideturtle()
        self.clear()
        self.goto(-390, 260)
        self.write(f"Player 1  = {self.score1}  ", font=("arial", 18, "normal"))
        self.goto(250, 260)
        self.write(f"Player 2  = {self.score2}  ", font=("arial", 18, "normal"))
