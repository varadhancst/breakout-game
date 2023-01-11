from turtle import Turtle


class Brick(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.dx = 10
        self.dy = 10
        self.goto(x, y)
        self.x = 1







