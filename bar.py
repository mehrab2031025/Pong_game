from turtle import Turtle

bar_speed = 60
extreme_y = 335


class Bar(Turtle):
    def __init__(self):
        super().__init__()
        self.bars = []
        for i in range(2):
            bar = Turtle()
            bar.shape("square")
            bar.shapesize(stretch_wid=1, stretch_len=5)
            bar.setheading(90)
            bar.color("white")
            bar.penup()
            self.bars.append(bar)
        self.Left_Bar = self.bars[0]
        self.Right_Bar = self.bars[1]

        self.Left_Bar.teleport(-480, 0)
        self.Right_Bar.teleport(480, 0)

    def left_up(self):
        if self.Left_Bar.ycor() >= extreme_y:
            pass
        else:
            self.Left_Bar.forward(bar_speed)

    def left_down(self):
        if self.Left_Bar.ycor() <= -extreme_y:
            pass
        else:
            self.Left_Bar.backward(bar_speed)

    def right_up(self):
        if self.Right_Bar.ycor() >= extreme_y:
            pass
        else:
            self.Right_Bar.forward(bar_speed)

    def right_down(self):
        if self.Right_Bar.ycor() <= -extreme_y:
            pass
        else:
            self.Right_Bar.backward(bar_speed)
