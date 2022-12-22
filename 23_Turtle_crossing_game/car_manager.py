from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.goto(x=320, y=random.randint(-250, 250))

    def car_move(self):
        self.goto(self.xcor()-MOVE_INCREMENT, self.ycor())




