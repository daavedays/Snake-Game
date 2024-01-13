import random
from turtle import Turtle


class Obstacle(Turtle):

    def __init__(self, snake):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.color("gray")
        self.penup()
        self.shapesize(stretch_wid=4, stretch_len=4)
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))
        self.snake = snake  # snake instance from main.py to fetch its head coordinates.

    def create_obstacle(self):
        """ """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        if -20 <= random_x <= 20 or -20 <= random_y <= 20:
            self.goto(x=-90, y=100)
        elif (random_x - 50 < self.snake.head.xcor() < random_x + 50 or
                random_y - 50 < self.snake.head.ycor() < random_x + 50):
            self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))
        else:
            self.goto(random_x, random_y)

    def destroy(self):
        self.goto(1000, 1000)
