import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
turtle = Player()
scoreboard = Scoreboard()
screen.onkey(turtle.up, "Up")
cars = []
game_is_on = True

def hide_cars(cars):
    for car in range(0, len(cars)):
        cars[car].ht()
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in range(0, len(cars)):
        cars[car].move()
        if turtle.distance(cars[car]) < 30:
            game_is_on = False
            scoreboard.game_over()

    if random.randint(1,6) == 1:
        if len(cars) < 30:
            car = CarManager(scoreboard.level)
            cars.append(car)

    if turtle.ycor() == 280:
        turtle.reset()
        scoreboard.next_level()
        hide_cars(cars)
        cars.clear()

screen.exitonclick()

