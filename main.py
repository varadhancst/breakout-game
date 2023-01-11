from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from wall import Brick
import time

screen = Screen()
screen.tracer(0)
screen.title("Breakout game")
screen.bgcolor("black")
screen.setup(width=800, height=600)

paddle_bottom = Paddle((0, -250))

screen.listen()

screen.onkeypress(paddle_bottom.paddle_left, "Left")
screen.onkeypress(paddle_bottom.paddle_right, "Right")

ball = Ball()

bricks = []
x_position = -360
y_position = 150
for i in range(15):
    brick = Brick(x_position, y_position)
    bricks.append(brick)
    x_position += 50

lives = Scoreboard((-100, 200))
points = Scoreboard((100, 200))
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    if ball.distance(paddle_bottom) < 25 and ball.ycor() > -280:
        ball.bounce_y()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.ycor() < - 280:
        lives.update_lives()
        ball.reset_position()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    for brick in bricks:
        if ball.distance(brick) < 15:
            brick.hideturtle()
            bricks.remove(brick)
            points.update_points()

    if lives.lives >= 10:
        points.game_over()
        game_is_on = False

screen.exitonclick()
