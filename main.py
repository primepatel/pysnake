from turtle import Screen, Turtle
from time import sleep
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # used as screen update 0: PAUSE
snake = Snake()

while True:
    screen.update()
    sleep(0.1)
    snake.move()


screen.exitonclick()