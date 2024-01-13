from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from obstacle import Obstacle

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game.")
screen.tracer(0)  # Turns off the screen animation.
score = 0

snake = Snake()  # Creates a snake object.
food = Food()  # Creates the food object.
scoreboard = Scoreboard()
obstacle = Obstacle(snake)

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left_turn, key="Left")
screen.onkey(fun=snake.right_turn, key="Right")


game_is_on = True
interval = 10
counter = 0
while game_is_on:
    # if counter % interval == 0:
    #     obstacle = Obstacle(snake)
    # counter += 1
    screen.update()  # Animation turns on.
    time.sleep(0.07)  # Controls the speed of the snakes motion.
    scoreboard.update_scoreboard()
    snake.color_snake()
    snake.move()
    # print(snake.head.xcor(), snake.head.ycor(), "\n" * 4)
    # print(obstacle.xcor(), obstacle.ycor())

    # Detect collision with food.
    if food.distance(snake.head) <= 20:
        food.create_new_food()
        scoreboard.increase_score()
        snake.extend()
        obstacle.create_obstacle()
        if obstacle.distance(snake.head) < 100:
            obstacle.create_obstacle()

    # Detect collision with wall & end game.
    if abs(snake.head.xcor()) >= 290:
        game_is_on = False
        scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
    elif abs(snake.head.ycor()) >= 290:
        game_is_on = False
        scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

    if obstacle.distance(snake.head) <= 50:
        game_is_on = False
        scoreboard.reset()
        snake.reset()
        scoreboard.game_over()
    elif obstacle.distance(snake.head) < 50:
        game_is_on = False
        scoreboard.reset()
        snake.reset()
        scoreboard.game_over()

    # obstacle.destroy()

screen.exitonclick()
