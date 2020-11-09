import turtle
from turtle import Turtle, Screen
import random as rand

turtle.colormode(255)
screen = Screen()
columns = 10
rows = 10
loc_x = 0
loc_y = 0
dir = -1
color_list = [(45, 95, 143), (213, 214, 205), (126, 159, 205), (221, 225, 223), (169, 78, 26), (168, 189, 219), (187, 150, 163), (202, 165, 34), (18, 58, 82)]

class Painter():
    def __init__(self):
        self.id = Turtle()
        paint = self.id
        paint.color(color_list[0])
        paint.hideturtle()


painter = Painter()
painter.id.penup()


for row in range(rows):

    for col in range(columns):
        painter.id.dot(15, color_list[rand.randint(0, len(color_list)-1)])
        loc_x += 30 * dir
        painter.id.setx(loc_x)

    if dir == -1:
        dir = 1
    else:
        dir = -1
    painter.id.dot(15, color_list[rand.randint(0, len(color_list)-1)])
    loc_y -= 30
    painter.id.sety(loc_y)


screen.exitonclick()
