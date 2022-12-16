from turtle import Turtle
import time

STARTING_COORDINATES = (0, 0)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(STARTING_COORDINATES)

    def move(self):
        increment_x = 1
        increment_y = 1
        new_x = self.xcor() + increment_x
        new_y = self.ycor() + increment_y
        time.sleep(0.1)
        self.goto(new_x, new_y)