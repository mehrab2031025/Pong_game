from turtle import Turtle, Screen
from bar import Bar
from ball import Ball
from score import Score




def draw_border():
    extreme_x = 490
    extreme_y = 390
    border = Turtle()
    border.color("white")
    border.hideturtle()
    border.teleport(extreme_x, -extreme_y)
    border.goto(extreme_x, extreme_y)
    border.goto(-extreme_x, extreme_y)
    border.goto(-extreme_x, -extreme_y)
    border.goto(extreme_x, -extreme_y)
    border.teleport(0, -extreme_y)
    border.pensize(5)
    border.goto(0, extreme_y)


draw_border()
screen = Screen()
screen.tracer(0)

screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.title("Let's PONG")

bar = Bar()
ball = Ball()
left_score = Score(-100, 250)
right_score = Score(100, 250)

screen.listen()
screen.onkey(key="w", fun=bar.left_up)
screen.onkey(key="s", fun=bar.left_down)
screen.onkey(key="Up", fun=bar.right_up)
screen.onkey(key="Down", fun=bar.right_down)

game_is_on = True
while game_is_on:
    screen.update()
    ball.ball_on_the_move()
    if ball.collision_with_left_side_wall():
        right_score.point()
        ball.Reset()
    elif ball.collision_with_right_side_wall():
        left_score.point()
        ball.Reset()
    elif ball.collision_with_top_bottom_wall():
        ball.top_bottom_bounce_back()
    elif ((ball.xcor() > 460 and ball.distance(bar.Right_Bar) < 60)
          or (ball.xcor() < -460 and ball.distance(bar.Left_Bar) < 60)):
        ball.side_wall_bounce_back()
        ball.speed_up()

screen.exitonclick()
