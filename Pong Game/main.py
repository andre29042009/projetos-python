from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from divide import Line
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
line = Line()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move_up()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.x_move > 0 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 and ball.x_move < 0:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()
screen.exitonclick()