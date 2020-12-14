from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        Turtle.__init__(self)
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto((0, 270))
        self.pencolor("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        