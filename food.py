from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self) -> None:
        Turtle.__init__(self)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.loc = (randint(-280, 280), randint(-280, 280))
        self.goto(self.loc)
        