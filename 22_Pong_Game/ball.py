from turtle import Turtle

STARTING_COORDINATES = (0, 0)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(STARTING_COORDINATES)
        self.increment_x = 10
        self.increment_y = 10
        self.move_speed = 0.2

    def move(self):
        new_x = self.xcor() + self.increment_x
        new_y = self.ycor() + self.increment_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.increment_y *= -1

    def bounce_x(self):
        self.increment_x *= -1
        self.move_speed *= 0.9

    def refresh_ball(self):
        self.goto(STARTING_COORDINATES)
        self.bounce_x()
        self.move_speed = 0.1
