####### PAINTER #######################################################

# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def rotate_counter_clockwise():
#     tim.left(10)
#
# def rotate_clockwise():
#     tim.right(10)
#
# def clear_screen():
#     tim.speed("fastest")
#     tim.setposition(0,0)
#     tim.setheading(0)
#     tim.clear()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=rotate_counter_clockwise)
# screen.onkey(key="d", fun=rotate_clockwise)
# screen.onkey(key="c", fun=clear_screen)
#
# screen.exitonclick()


####### TURTLE RACE #######################################################
import turtle
from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(width=500, height=400)
user_bet = (turtle.textinput(title="Make s bet", prompt="Which turtle will win. Type a color: red/orange/yellow/green/blue/purple")).capitalize()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

racing_turtles = []

starting_y = -100

for color in colors:
    racer = Turtle(shape="turtle")
    racer.penup()
    racer.color(color)
    racer.goto(x= -230, y= starting_y)
    racing_turtles.append(racer)
    starting_y += 40

race_is_on = True
winner = None

while race_is_on:
    for turtle_number in range(6):
        racing_turtles[turtle_number].forward(random.randint(1,10))
        if racing_turtles[turtle_number].xcor() > 230:
            winner = turtle_number
            race_is_on = False
        #print(racing_turtles[turtle_number].xcor())

print(f"{colors[turtle_number].capitalize()} is the WINNER")
if colors[turtle_number].capitalize() == user_bet:
    print("You WIN!!!")
else:
    print("You LOOSE!!!")



screen.exitonclick()

