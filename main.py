from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)


paddle_l = Paddle((-350,0))
paddle_r = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()





screen.listen()
screen.onkey(paddle_r.go_up,"Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up,"w")
screen.onkey(paddle_l.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    #detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detecting collision with paddle_r
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # detect miss by paddle_r
    if ball.xcor()> 380:
        ball.reset_position()
        scoreboard.l_point()
    # detect miss y paddle_l
    if ball.xcor()< -380:
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()