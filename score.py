from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        Turtle.__init__(self)
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto((0, 280))
        self.pencolor("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
    
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
    
    def game_over(self):
        self.goto((0, 0))
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
