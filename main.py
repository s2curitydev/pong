from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < - 330:
        ball.bounce_x()

    if ball.xcor() > 380:
        time.sleep(0.5)
        scoreboard.l_point()
        ball.reset_ball()

    if ball.xcor() < - 380:
        time.sleep(0.5)
        scoreboard.r_point()
        ball.reset_ball()

    if scoreboard.l_score > 10 or scoreboard.r_score > 10:
        scoreboard.end_game()
        game_is_on = False


screen.exitonclick()
