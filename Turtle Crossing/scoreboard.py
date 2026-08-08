from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-160, 260)
        self.write(f"Level {self.level}",align="right", font=("Courier", 24, "normal"))

    def next_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align="right", font=("Courier", 24, "normal"))
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center",  font=("Courier", 50, "normal") )