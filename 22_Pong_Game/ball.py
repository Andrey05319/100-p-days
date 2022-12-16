from turtle import Turtle
import time

STARTING_COORDINATES = (0, 0)
increment_x = 10
increment_y = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(STARTING_COORDINATES)

    def move(self):
        new_x = self.xcor() + increment_x
        new_y = self.ycor() + increment_y
        if (new_y > 290) or (new_y < -290):
            print("hehehe")
            increment_y = increment_y * (-1)
            new_y = self.ycor() + increment_y


        time.sleep(0.1)
        self.goto(new_x, new_y)