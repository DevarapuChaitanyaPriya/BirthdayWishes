from turtle import Turtle
import math


class Cake(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.rectangle()

    def rectangle(self):
        self.penup()
        self.goto(-100, -260)
        self.drawing(300, "#FFFFFF", 10)
        self.penup()
        self.goto(-70, -250)
        self.drawing(240, "#FFE838", 40)
        self.penup()
        self.goto(-70, -210)
        self.drawing(240, "#BF671F", 15)
        self.penup()
        self.goto(-70, -195)
        self.drawing(240, "#67F55F", 15)
        self.penup()
        self.goto(-70, -180)
        self.drawing(240, "#FFFA5C", 30)
        self.penup()
        self.goto(-70, -150)
        self.drawing(240, "#e30b5d", 45)
        self.addIcing("#FFFFFF", -70, -105, 240)
        self.addCherry()
        self.writeBirthdayWishes()

    def drawing(self, x, color, width):
        self.begin_fill()
        self.pencolor(color)
        self.color(color)
        self.pendown()
        self.forward(x)
        self.setheading(90)
        self.forward(width)
        self.setheading(180)
        self.forward(x)
        self.setheading(270)
        self.forward(width)
        self.end_fill()
        self.penup()
        self.setposition(0, 0)
        self.setheading(0)

    def addIcing(turtle, color, x, y, size):
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x, y + 10)
        turtle.pendown()
        turtle.begin_fill()

        for i in range(x, x + size):
            angle = (i - x) / size * 5 * math.pi  # Adjusted the angle for two complete waves
            y_offset = 10 * math.cos(angle)
            turtle.goto(i, y - 10 - y_offset)

        turtle.goto(x + size, y + 10)
        turtle.goto(x, y + 10)
        turtle.end_fill()

    def addCherry(self):
        self.penup()
        self.color("#C20067")
        self.goto(50, -95)
        self.begin_fill()
        self.pendown()
        self.circle(15)
        self.end_fill()

    def writeBirthdayWishes(self):
        self.penup()
        self.goto(50, 0)
        self.color("darkblue")  # Set text color to dark blue
        self.hideturtle()
        self.write("Happy Birthday!", align="center", font=("Arial", 40, "bold"))
