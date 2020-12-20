from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # used as screen update 0: PAUSE
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False

while not game_over:
    screen.update()
    sleep(0.1)
    snake.move()
    
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
    
    # detect collision with wall
    if abs(snake.head.xcor()) >= 280 or abs(snake.head.ycor()) >= 280:
        scoreboard.game_over()
        game_over = True

screen.exitonclick()