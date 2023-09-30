from turtle import Turtle
import random

colors = [(255, 69, 0),
          (255, 140, 0),
          (255, 99, 71),
          (255, 0, 255),
          (128, 0, 128),
          (0, 0, 128),
          (0, 0, 255),
          (0, 128, 128),
          (0, 128, 0),
          (0, 255, 0),
          (128, 128, 0),
          (139, 69, 19),
          (128, 128, 128),
          (169, 169, 169),
          (192, 192, 192),
          (255, 255, 255),
          (255, 0, 0), (0, 128, 128),
          (0, 255, 255),
          (0, 255, 255), ]


class Decoration:
    def __init__(self):
        self.cars = []

    def create_car(self):
        my_turtle = Turtle()
        my_turtle.penup()
        my_turtle.shape("square")
        my_turtle.color(random.choice(colors))
        my_turtle.shapesize(0.5, 1.5)
        x = random.randint(-450, 450)
        my_turtle.setposition(x, 300)
        my_turtle.setheading(270)
        self.cars.append(my_turtle)

    def move(self):
        for i in self.cars:
            i.forward(50)
