from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(2, 1)
        self.setheading(90)
        self.pensize(5)
        self.hideturtle()
        self.penup()
        self.dis = -30
        self.goto(0, 600)

        for n in range(15):
            self.pendown()
            self.forward(self.dis)
            self.penup()
            self.forward(self.dis)
