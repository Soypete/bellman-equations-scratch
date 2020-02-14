import turtle

win = turtle.Screen()
win.title('Paddle')
win.bgcolor('black')
win.tracer(0)
win.setup(width=600, height=600)

paddle = turtle.Turtle()
paddle.shape('square')
paddle.speed(0)
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.color('white')
paddle.goto(0, -275)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0, 100)
ball.dx = 3
ball.dy = -3


def paddle_right():
    x = paddle.xcor()
    if x < 255:
        paddle.setx(x+20)


def paddle_left():
    x = paddle.xcor()
    if x > -255:
        paddle.setx(x-20)


# Ball-Walls collision
if ball.xcor() > 290:
    ball.setx(290)
    ball.dx *= -1


if ball.xcor() < -290:
    ball.setx(-290)
    ball.dx *= -1


if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1


# Ball-Paddle collision
if abs(ball.ycor() + 250) < 2 and abs(paddle.xcor() - ball.xcor()) < 55:
    ball.dy *= -1


# Ball-Ground collison
if ball.ycor() < -290:
    ball.goto(0, 100)


win.listen()
win.onkey(paddle_right, 'Right')
win.onkey(paddle_left, 'Left')


while True:
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
