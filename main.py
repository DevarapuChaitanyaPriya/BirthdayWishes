import turtle
from turtle import Screen
import time
from Balloon import Balloon
from cake import Cake
from Decoration import Decoration

turtle.colormode(255)
my_screen = Screen()
my_screen.setup(900, 600)
my_screen.bgcolor("MistyRose")
my_screen.tracer(0)
x = 0
g = 25
for i in range(7):
    if i % 2 != 0:
        balloon1 = Balloon(-300 + x, 125 - g)
    else:
        balloon1 = Balloon(-300 + x, 125)
    x = x + 100
    my_screen.update()
    time.sleep(0.2)
Cake()
dec = Decoration()
while True:
    time.sleep(0.3)
    dec.create_car()
    dec.move()
    my_screen.update()

my_screen.exitonclick()
