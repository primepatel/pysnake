from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def add_segment(self, position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)
    
    def create_snake(self):
        for position in INITIAL_POSITIONS:
            self.add_segment(position)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def is_tail_collision(self):
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 10:
                return True
        return False
    
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            cords = self.segments[seg_num-1].xcor(), self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(cords)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)