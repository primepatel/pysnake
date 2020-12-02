from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
        for position in INITIAL_POSITIONS:
            new_seg = Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(position)
            self.segments.append(new_seg)
    
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            cords = self.segments[seg_num-1].xcor(), self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(cords)
        self.segments[0].forward(MOVE_DISTANCE)