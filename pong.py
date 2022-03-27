import turtle
import winsound
import time

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=1000, height=600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-450, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(450, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center", font=("Calibri", 24, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(paddle_a_up, "f")
window.onkeypress(paddle_a_down, "v")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    window.update()
    time.sleep(0.00001)
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dy *= -1
        
    elif ball.ycor() < -290:
        ball.sety(-290)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dy *= -1

    # Left and right
    if ball.xcor() > 450:
        score_a += 1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center", font=("Calibri", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -450:
        score_b += 1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center", font=("Calibri", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if (ball.xcor() < -430 and ball.xcor() > -450) and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dx *= -1 
    
    elif (ball.xcor() > 430 and ball.xcor() < 450) and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dx *= -1