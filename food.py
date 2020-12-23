from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self, xrange, yrange) -> None:
        self.xrange, self.yrange = xrange//2 - 10, yrange//2 - 10
        Turtle.__init__(self)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        self.loc = (randint(-self.xrange, self.xrange), randint(-self.yrange, self.yrange))
        self.goto(self.loc)