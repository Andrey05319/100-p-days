from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.goto(-200, 240)
        self.write(f"Level: {self.level}", align="center", font=FONT)





