import turtle as t

timmy_the_turtle = t.Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

## Drawning a square ---------------------------
# angle = 90
# distance = 100
# for sides in range(1, 5):
#     timmy_the_turtle.right(angle)
#     timmy_the_turtle.forward(distance)
#     #print(f"side - {sides}, angle - {angle}")
#
## Draw a Dashed line ______________________________

# for _ in range(12):
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)

## Draw multi-angle geometric figures ______________________________

# import random
# distance = 100
# color_list = ["red", "green", "blue", "coral", "gold"]
#
# for number_of_angles in range(3, 9):
#     print(f"Number of angles = {number_of_angles}")
#     timmy_the_turtle.color(random.choice(color_list))
#     for sides in range(1, number_of_angles+1):
#         timmy_the_turtle.forward(distance)
#         timmy_the_turtle.right(360/number_of_angles)

## Draw a random walk -------------------------------------------

# import random
#
# t.colormode(255)
# number_of_steps = 300
# possible_angles_of_turn = [0, 90, 180, 270]
# step_distance = 25
# line_thickness = 4
# timmy_the_turtle.pensize(10)
# timmy_the_turtle.speed(10)
#
# for step in range(0, number_of_steps):
#     angle_of_turn = random.choice(possible_angles_of_turn)
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     timmy_the_turtle.color((r, g, b))
#     timmy_the_turtle.setheading(angle_of_turn)
#     timmy_the_turtle.forward(step_distance)

## Draw a spilogram -------------------------------------------

import random

t.colormode(255)
timmy_the_turtle.speed(10)

for direction in range(0, 360, 20):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy_the_turtle.color((r, g, b))
    timmy_the_turtle.setheading(direction)

    timmy_the_turtle.circle(100)


# ----------------------------------------------------------------

screen = t.Screen()
screen.exitonclick()
