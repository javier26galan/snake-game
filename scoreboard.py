from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Comic Sans MS', 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.text = "Score:"
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto((0, 270))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"{self.text} {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
