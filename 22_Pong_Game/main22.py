from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Andrey's Pong Game")
screen.tracer(0)  # Turning off the animation of moving

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "q")
screen.onkey(l_paddle.down, "a")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()  # Works in pair with screen.tracer(0) - updating the screen in absence of animation

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


screen.exitonclick()
