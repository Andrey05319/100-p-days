import turtle
import random

#### Getting colors from a picture

# import colorgram
#
# colors = colorgram.extract('dots.jpg', 20)
#
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

##### Colours_extracted_from_picture:
list_of_colors = [(198, 13, 32), (250, 238, 17), (39, 76, 189), (39, 217, 69), (238, 226, 5), (229, 159, 46),
                  (27, 40, 156), (215, 75, 13), (198, 15, 11), (15, 154, 15), (242, 35, 166), (229, 17, 121),
                  (70, 10, 31), (61, 15, 8), (224, 141, 209), (11, 97, 62)]

turtle.colormode(255)
dotter = turtle.Turtle()
dotter.penup()
dotter.hideturtle()
dotter.speed("fastest")
starting_y = (-50 * 9) / 2


def dot_painting():
    dotter.dot(20, random.choice(list_of_colors))


def drawning_a_line_of_dots(y_coord):
    starting_x = (-50 * 9) / 2
    dotter.setx(starting_x)
    dotter.sety(starting_y)
    for _ in range(10):
        dot_painting()
        dotter.forward(50)


for _ in range(10):
    drawning_a_line_of_dots(starting_y)
    starting_y += 50

screen = turtle.Screen()
screen.exitonclick()
