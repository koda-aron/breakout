from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 25
        if new_x > -250:
            self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 25
        if new_x < 250:
            self.goto(new_x, self.ycor())
