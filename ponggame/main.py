from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
screen = Screen()

screen.bgcolor("black")
screen.setup(width= 800, height= 600)
# screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


ball = Ball()
scoreboard = ScoreBoard()

# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(350, new_y)
#
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(350, new_y)



screen.listen()
#
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")


is_on = True
while is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_x()
        ball.bounce_y()
    if ball.distance(r_paddle.pos()) < 40 and ball.xcor() >340 or ball.distance(l_paddle.pos()) < 40 and ball.xcor() <-340:
        ball.bounce_x()
        ball.increase_speed()
    if ball.xcor() > 380:
        scoreboard.score1 += 1
        scoreboard.scorekeeper()
        ball.reset_position()
    if ball.xcor() < -380:
        scoreboard.score2 += 1
        scoreboard.scorekeeper()
        ball.reset_position()






































screen.exitonclick()