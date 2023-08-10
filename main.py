from turtle import Screen
from paddle import Paddle
from ball import Ball
from block import Block
from scoreboard import Scoreboard


def detect_collision(ball_turtle, block_turtle):
    if ball_turtle.distance(block_turtle) < 40:
        ball_turtle.bounce_y()
        block_turtle.goto(0, 600)
        scoreboard.add_point()
        scoreboard.update_scoreboard()


screen = Screen()
screen.bgcolor("black")
screen.setup(width=550, height=700)
screen.title("Breakout")
screen.tracer(0)

scoreboard = Scoreboard()
paddle = Paddle((0, -260))
ball = Ball()

block_1 = Block((-200, 50), "yellow")
block_2 = Block((-100, 50), "yellow")
block_3 = Block((0, 50), "yellow")
block_4 = Block((100, 50), "yellow")
block_5 = Block((200, 50), "yellow")

block_6 = Block((-200, 80), "yellow")
block_7 = Block((-100, 80), "yellow")
block_8 = Block((0, 80), "yellow")
block_9 = Block((100, 80), "yellow")
block_10 = Block((200, 80), "yellow")

block_11 = Block((-200, 110), "green")
block_12 = Block((-100, 110), "green")
block_13 = Block((0, 110), "green")
block_14 = Block((100, 110), "green")
block_15 = Block((200, 110), "green")

block_16 = Block((-200, 140), "green")
block_17 = Block((-100, 140), "green")
block_18 = Block((0, 140), "green")
block_19 = Block((100, 140), "green")
block_20 = Block((200, 140), "green")

block_21 = Block((-200, 170), "orange")
block_22 = Block((-100, 170), "orange")
block_23 = Block((0, 170), "orange")
block_24 = Block((100, 170), "orange")
block_25 = Block((200, 170), "orange")

block_26 = Block((-200, 200), "orange")
block_27 = Block((-100, 200), "orange")
block_28 = Block((0, 200), "orange")
block_29 = Block((100, 200), "orange")
block_30 = Block((200, 200), "orange")

block_31 = Block((-200, 230), "red")
block_32 = Block((-100, 230), "red")
block_33 = Block((0, 230), "red")
block_34 = Block((100, 230), "red")
block_35 = Block((200, 230), "red")

block_36 = Block((-200, 260), "red")
block_37 = Block((-100, 260), "red")
block_38 = Block((0, 260), "red")
block_39 = Block((100, 260), "red")
block_40 = Block((200, 260), "red")

blocks = [block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8, block_9, block_10, block_11, block_12, block_13, block_14, block_15, block_16, block_17, block_18, block_19, block_20, block_21, block_22, block_23, block_24, block_25, block_26, block_27, block_28, block_29, block_30, block_31, block_32, block_33, block_34, block_35, block_36, block_37, block_38, block_39, block_40]


screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with ceiling
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with wall
    if ball.xcor() > 260 or ball.xcor() < -260:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() == -240:
        ball.bounce_y()

    # Detect collision with blocks
    for block in blocks:
        detect_collision(ball, block)

screen.exitonclick()
