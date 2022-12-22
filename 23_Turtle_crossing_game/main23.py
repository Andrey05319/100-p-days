import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

screen.listen()
screen.onkey(player.move, "Up")

counter = 1
game_is_on = True
cars = []

while game_is_on:
    counter += 1

    if counter == 5:
        cars.append(CarManager())
        counter = 1

    for car in cars:
        if player.distance(car) < 20:
            print("Game Over")
            game_is_on = False
        car.car_move()

    if player.ycor() > 250:
        player.next_level()

    time.sleep(player.delay)
    screen.update()

screen.exitonclick()

# 1. A turtle moves forwards when you press the "Up" key.
# It can only move forwards, not back, left or right.

# 2. Cars are randomly generated along the y-axis and
# will move from the right edge of the screen to the
# left edge.

# 3. When the turtle hits the top edge of the screen,
# it moves back to the original position and the player
# levels up. On the next level, the car speed increases.

# 4. When the turtle collides with a car, it's game over
# and everything stops.
