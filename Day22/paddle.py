from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos1):
        super().__init__()
        self.create_paddle(pos1)


    def create_paddle(self,pos1):
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)