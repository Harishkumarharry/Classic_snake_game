from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", 'r') as file:
            self.high_score = int(file.read())
        self.goto(0, 280)
        self.color("red")
        self.hideturtle()
        self.score_increase()

    def score_increase(self):
        self.update_scoreboard()
        self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

