from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(x)

    def paddle_right(self):
        x = self.xcor()
        x += 20
        self.setx(x)

    def paddle_left(self):
        x = self.xcor()
        x -= 20
        self.setx(x)
