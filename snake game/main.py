from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard


scoreboard = ScoreBoard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(f"My snake game")
snake = Snake()

food = Food()
screen.listen()
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")


screen.tracer(0)

gameison = True
while gameison:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 15:
        print("lol")
        food.gotopose()
        snake.extend()
        scoreboard.score += 1
        scoreboard.update_scoreboard()
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()

        snake.reset()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()














screen.exitonclick()
