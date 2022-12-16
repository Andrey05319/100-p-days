from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, starting_coordinates):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.speed("fastest")
        self.goto(starting_coordinates)

    def up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -230:
            self.goto(self.xcor(), self.ycor() - 20)

