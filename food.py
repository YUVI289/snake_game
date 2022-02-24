from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.3,0.3)
        self.penup()
        self.color("red")
        self.reassign()
    
    def reassign(self):
        xc = randint(-350,90)
        yc = randint(-100,250)
        self.goto(xc,yc)