from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.delay = 0.15

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def next_level(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.delay *= 0.8
