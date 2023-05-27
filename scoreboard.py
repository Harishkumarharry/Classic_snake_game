from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.color("red")
        self.hideturtle()
        self.score_increase()

    def score_increase(self):
        self.clear()
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
