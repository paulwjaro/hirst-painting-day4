import turtle
from turtle import Turtle as t, Screen
import random as rand

screen = Screen()
turtle.colormode(255)
directions = [0, 90, 180, 270]
run_time = 100


class Player:
    def __init__(self):
        self.id = t()
        player = self.id
        player.width(4)
        player.speed(1)

    def move(self):
        player = self.id
        player.forward(25)
        player.color(rand_color())
        player.setheading(rand.choice(directions))



def rand_color():
    r = rand.randint(0, 255)
    b = rand.randint(0, 255)
    g = rand.randint(0, 255)

    colors = (r, b, g)

    return colors

Tammy = Player()

while run_time > 0:
    Tammy.move()
    run_time -= 1


screen.exitonclick()

