from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 2

class CarManager(Turtle):
    def __init__(self, level):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.penup()
        self.x = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (level - 1))
        self.shapesize(1, 2)
        self.goto(290 , random.randint(-210, 290))

    def move(self):
        if self.xcor() == -280:
            self.goto(290 , random.randint(-210, 290))
        new_x = self.xcor() - self.x
        self.goto(new_x, self.ycor())
