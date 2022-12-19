from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard22 import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Andrey's Pong Game")
screen.tracer(0)  # Turning off the animation of moving

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "q")
screen.onkey(l_paddle.down, "a")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()  # Works in pair with screen.tracer(0) - updating the screen in absence of animation

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 400:
        ball.refresh_ball()
        score.l_point()

    # Detect left paddle misses
    if ball.xcor() < -400:
        ball.refresh_ball()
        score.r_point()

screen.exitonclick()
