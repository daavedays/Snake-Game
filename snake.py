from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 12



class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()  # calls the create_snake method and adds it to segments.
        self.head = self.segments[0]  # first segment of the snake.

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake = Turtle(shape="square")  # Creating the first 3 segments of the snake.
            snake.penup()
            snake.goto(position)
            self.segments.append(snake)

    def color_snake(self):
        """Colors the segments of the snake, in 2 different colors"""
        for segment in self.segments[0::2]:
            segment.color("gray")
        for segment in self.segments[1::2]:
            segment.color("white")

    def move(self):
        """Starting from the last segment, this for loop makes the last segment follow the one before it.
           This way the body of the snake can be controlled."""

        for seg_num in range(len(self.segments) - 1, 0, -1):  # Iteration starts from the last segment of the turtle
            # instance and goes backwards until the first segment.
            new_x = self.segments[seg_num - 1].xcor()  # New x co-ordinate is set to equal x co-ordinate of
            # second to last segment.
            new_y = self.segments[seg_num - 1].ycor()  # Same for new y co-ordinate.
            self.segments[seg_num].goto(new_x, new_y)  # seg_num iterating is always the last segment piece.
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        for i in range(3):
            self.add_segment((self.segments[-1].position()))

    def up(self):
        if self.head.heading() == 270:  # if snake moving down doesn't allow to move up.
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)

    def left_turn(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180)

    def right_turn(self):
        if self.head.heading() == 180:
            pass
        else:
            self.head.setheading(0)

    def reset(self):
        """Clear the list of segments create a new 3 segment snake and set the head as [0]-th element in list."""
        for seg in self.segments:
            seg.goto(1000, 1000)  # Makes the dead snakes disappear off-screen.
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
