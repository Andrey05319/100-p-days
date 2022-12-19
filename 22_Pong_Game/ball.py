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
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.increment_x
        new_y = self.ycor() + self.increment_y
        # if (new_y > 290) or (new_y < -290):
        #     print("hehehe")
        #     increment_y = increment_y * (-1)
        #     new_y = self.ycor() + increment_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.increment_y *= -1


    def bounce_x(self):
        self.increment_x *= -1
        self.move_speed *= 0.9

    def refresh_ball(self):
        # if self.xcor() > 0:
        #     self.increment_x = ((self.increment_x ** 2) ** (1/2)) * -1
        # else:
        #     self.increment_x = ((self.increment_x ** 2) ** (1 / 2))
        self.goto(STARTING_COORDINATES)
        self.bounce_x()
        self.move_speed = 0.1
