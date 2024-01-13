from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        with open("data.txt") as data:  # Create a text file with a starting value.
            # This value is stored as a string inside the data.txt.
            self.high_score = int(data.read())  # Convert it to an integer, to be able to compare with score.

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High-Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """Resets the score and updates the high-score."""
        if self.score > self.high_score:
            self.high_score = self.score  # High_score gets reset to the current score that's higher.
            with open("data.txt", "w") as file:  # We rewrite the stored str value for high_score.
                file.write(f"{self.high_score}")
        self.score = 0

    def game_over(self):
        """Resets the snakes coordinates, writes "Game over message". """
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=("Courier", 60, "normal"))
        self.color("white")
