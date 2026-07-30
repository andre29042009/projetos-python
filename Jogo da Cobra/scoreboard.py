from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.pencolor("white")
        self.goto(0, 265)
        self.ht()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.score += 1
        self.clear()
        self.update()
