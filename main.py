import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Setting up the screen for the game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Calling the snake class and the food class
snake = Snake()
food = Food()
score = ScoreBoard()

# Taking keyboard input
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food.
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.score_increase()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with Tail.
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
