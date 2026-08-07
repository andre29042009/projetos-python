from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)

    def up(self):
        if self.ycor() <  255:
            new_y = self.ycor() + 20
            self.goto(self.xcor(),new_y)


    def down(self):
        if self.ycor() > -255:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)