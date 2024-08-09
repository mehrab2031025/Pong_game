from turtle import Turtle
from random import choice

random_coordinate = [45, 135, 225, 315]
extreme_x = 490
extreme_y = 380


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_speed = 0.5
        self.color("white")
        self.penup()
        self.shape("circle")
        self.Reset()


    def ball_on_the_move(self):
        self.forward(self.ball_speed)

    def speed_up(self):
        self.ball_speed += 0.1

    def collision_with_left_side_wall(self):
        if self.xcor() <= -extreme_x:
            return True

    def collision_with_right_side_wall(self):
        if self.xcor() >= extreme_x:
            return True

    def collision_with_top_bottom_wall(self):
        if not -extreme_y <= self.ycor() <= extreme_y:
            return True

    def top_bottom_bounce_back(self):
        self.setheading(360 - self.heading())

    def side_wall_bounce_back(self):
        self.setheading(180 - self.heading())

    def Reset(self):
        self.ball_speed = 0.1
        self.teleport(0, 0)
        self.setheading(choice(random_coordinate))
        self.ball_on_the_move()
