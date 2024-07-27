from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # moving the paddle
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # we change only the ycor because we need vertical motion alone.

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

