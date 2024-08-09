from turtle import Turtle


class Score(Turtle):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.teleport(self.x, self.y)
        self.write(self.score, align="center", font=("Courier", 80, "normal"))

    def point(self):
        self.score += 1
        self.clear()
        self.write(self.score, align="center", font=("Courier", 80, "normal"))
