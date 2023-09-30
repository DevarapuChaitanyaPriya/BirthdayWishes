from turtle import Turtle
import random

colors = [(246, 246, 244), (224, 158, 62), (147, 173, 42), (232, 212, 84), (56, 100, 173), (198, 7, 48), (237, 69, 50),
          (189, 66, 27), (204, 15, 11), (212, 62, 127), (165, 47, 126), (98, 154, 226), (81, 120, 199), (222, 230, 246),
          (19, 148, 61), (230, 117, 176), (237, 250, 245), (43, 180, 72), (242, 173, 194), (245, 157, 148)]


class Balloon:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.a = random.choice(colors)
        self.create_balloon()

    def create_balloon(self):
        my_turtle1 = Turtle()
        my_turtle1.speed("fastest")
        my_turtle1.penup()
        my_turtle1.setposition(self.x, self.y)
        my_turtle1.hideturtle()
        my_turtle1.pendown()
        my_turtle1.color(self.a)
        my_turtle1.begin_fill()
        my_turtle1.left(45)
        for i in range(7):
            my_turtle1.left(1)
            my_turtle1.forward(10)
        my_turtle1.left(10)
        i = 0
        for j in range(12):
            my_turtle1.left(2 + i)
            my_turtle1.forward(5)
            i = i + 0.5

        my_turtle1.forward(5)
        my_turtle1.left(2)
        my_turtle1.forward(5)
        j = 0
        for i in range(12):
            my_turtle1.left(2 + i)
            my_turtle1.forward(5)
            i = j + 0.5
        my_turtle1.end_fill()
        my_turtle2 = Turtle()
        my_turtle2.color(self.a)
        my_turtle2.speed("fastest")
        my_turtle2.penup()
        my_turtle2.setposition(self.x, self.y)
        my_turtle2.pendown()
        my_turtle2.hideturtle()
        my_turtle2.begin_fill()
        my_turtle2.right(235)
        for i in range(7):
            my_turtle2.right(1)
            my_turtle2.forward(10)
        my_turtle2.right(10)
        i = 0
        for j in range(12):
            my_turtle2.right(2 + i)
            my_turtle2.forward(5)
            i = i + 0.5
        my_turtle2.forward(5)
        my_turtle2.right(2)
        my_turtle2.forward(5)
        j = 0
        for i in range(12):
            my_turtle2.right(2 + i)
            my_turtle2.forward(5)
            i = j + 0.5
        my_turtle2.end_fill()

        self.ball()
        self.hanging()

    def ball(self):
        my_turtle = Turtle()
        my_turtle.speed("fastest")
        my_turtle.hideturtle()
        my_turtle.right(180)
        my_turtle.penup()
        my_turtle.begin_fill()
        my_turtle.color(self.a)
        my_turtle.setposition(self.x, self.y)
        my_turtle.begin_fill()
        my_turtle.pendown()
        my_turtle.circle(4)
        my_turtle.end_fill()

    def hanging(self):
        my_turtle = Turtle()
        my_turtle.speed("fastest")
        my_turtle.hideturtle()
        my_turtle.penup()
        my_turtle.right(90)
        my_turtle.setposition(self.x, self.y - 8)
        my_turtle.pendown()
        for i in range(2):
            for i in range(5):
                my_turtle.right(10)
                my_turtle.forward(5)
                my_turtle.left(10)
            for i in range(5):
                my_turtle.left(10)
                my_turtle.forward(5)
                my_turtle.right(10)
