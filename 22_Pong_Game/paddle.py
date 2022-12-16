from turtle import Turtle

STARTING_COORDINATES = (350, 0)


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)





    # width = 20
    # height = 100
    # x_pos = 350
    # y_pos = 0

