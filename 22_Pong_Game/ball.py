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


    def move(self):
        new_x = self.xcor() + self.increment_x
        new_y = self.ycor() + self.increment_y
        # if (new_y > 290) or (new_y < -290):
        #     print("hehehe")
        #     increment_y = increment_y * (-1)
        #     new_y = self.ycor() + increment_y
        self.goto(new_x, new_y)


    def bounce(self):
        self.increment_y *= -1
