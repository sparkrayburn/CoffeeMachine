import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# tim = Turtle("square")
# tim.shapesize(1, 3)


timy = Player()
screen.listen()
screen.onkey(fun=timy.tim_up, key= "Up")
scoreboard = Scoreboard()
car_manager = CarManager()
game_is_on = True


speed = 0.1
while game_is_on:
    time.sleep(speed)
    screen.update()
    car_manager.createcar()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(timy) < 20:
            scoreboard.game_over()
            game_is_on = False
            print("lol")

    if timy.ycor() == 280:
        timy.refresh()
        scoreboard.level +=1
        speed = speed/5
        scoreboard.score_keeper()



screen.exitonclick()