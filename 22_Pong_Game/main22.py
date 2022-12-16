from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Andrey's Pong Game")
screen.tracer(0) # Turning off the animation of moving

paddle_right = Paddle()


screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")

game_is_on = True
while game_is_on:
    screen.update() # Works in pair with screen.tracer(0) - updating the screen in absence of animation







screen.exitonclick()