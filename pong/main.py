from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Score()

screen.listen()
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")


game_on=True
while game_on:
    time.sleep(ball.move_speed)#Tso slow the movement of the ball
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.wall_bounce()

    if ball.distance(r_paddle)<50 and ball.xcor()>325 or ball.distance(l_paddle)<50 and ball.xcor()<-325:
        ball.paddle_bounce()

    if ball.xcor()>395:
        ball.reset_position()
        score.l_point()

    if ball.xcor()<-395:
        ball.reset_position()
        score.r_point()

screen.exitonclick()



