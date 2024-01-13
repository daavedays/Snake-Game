# TODO this class should know how to render itself as a small circle in the screen.
#  As soon as the snake touches this body, the body should disappear and reappear in a random location once again.

from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Should be a 10 by 10 circle.
        self.color("yellow")
        self.speed("fastest")
        self.create_new_food()

    def create_new_food(self):
        """Sends turtle object to random location."""
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))
