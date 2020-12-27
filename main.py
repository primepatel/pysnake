from turtle import Screen, Turtle
from time import sleep
from snake import Snake
from food import Food
from score import Scoreboard

WIDTH, HEIGHT = 550, 550
screen = Screen()
screen.setup(width=WIDTH+90, height=HEIGHT+30)
screen.bgcolor("black")
screen.title("Snake Game")
boxer = Turtle()
boxer.hideturtle()
boxer.penup()
boxer.goto((WIDTH/2, HEIGHT/2))
boxer.pendown()
boxer.color("white")
boxer.goto((WIDTH/2, -HEIGHT/2))
boxer.goto((-WIDTH/2, -HEIGHT/2))
boxer.goto((-WIDTH/2, HEIGHT/2))
boxer.goto((WIDTH/2, HEIGHT/2))

screen.tracer(0) # used as screen update 0: PAUSE
snake = Snake()
food = Food(WIDTH, HEIGHT)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False

while not game_over:
    screen.update()
    sleep(0.05)
    snake.move()
    
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()
    
    # detect collision with wall
    if abs(snake.head.xcor()) >= (WIDTH/2-5) or abs(snake.head.ycor()) >= (HEIGHT/2-5):
        scoreboard.game_over()
        game_over = True
        
    # detect collision with tail
    if snake.is_tail_collision():
        game_over = True
        scoreboard.game_over()

screen.exitonclick()