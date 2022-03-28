import turtle
import winsound
import time

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=600, height=400)
window.tracer(0, 0)

# Score
lose = 0

# Paddle AI
paddle_AI = turtle.Turtle()
paddle_AI.speed(0)
paddle_AI.shape("square")
paddle_AI.color("white")
# paddle_AI.shapesize(stretch_wid=5,stretch_len=1)
paddle_AI.penup()
paddle_AI.goto(-250, 0)

# Paddle Player
paddle_player = turtle.Turtle()
paddle_player.speed(0)
paddle_player.shape("square")
paddle_player.color("white")
paddle_player.shapesize(stretch_wid=5,stretch_len=1)
paddle_player.penup()
paddle_player.goto(250, 0)

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
pen.goto(0, 160)
pen.write("You lose : {}".format(lose), align="center", font=("Calibri", 24, "normal"))

# Functions
def paddle_AI_up():
    y = paddle_AI.ycor()
    y += 5
    paddle_AI.sety(y)

def paddle_AI_down():
    y = paddle_AI.ycor()
    y -= 5
    paddle_AI.sety(y)

def paddle_player_up():
    if paddle_player.ycor() < 150:
        y = paddle_player.ycor()
        y += 5
        paddle_player.sety(y)

def paddle_player_down():
    if paddle_player.ycor() > -140:
        y = paddle_player.ycor()
        y -= 5
        paddle_player.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(paddle_player_up, "Up")
window.onkeypress(paddle_player_down, "Down")

# Main game loop
while True:
    window.update()
    time.sleep(0.00001)

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Top and bottom
    if ball.ycor() > 190:
        ball.sety(190)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dy *= -1
        
    elif ball.ycor() < -190:
        ball.sety(-190)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dy *= -1

    # Left and right
    if ball.xcor() > 250:
        lose += 1
        pen.clear()
        pen.write("You lose : {}".format(lose), align="center", font=("Calibri", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -250:
        pen.clear()
        pen.write("You win =)))", align="center", font=("Calibri", 24, "normal"))
        time.sleep(3)
        break;

    # Paddle and ball collisions
    if (ball.xcor() <= -230 and ball.xcor() >= -250) and ball.ycor() < paddle_AI.ycor() + 50 and ball.ycor() > paddle_AI.ycor() - 50:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dx *= -1 
    
    elif (ball.xcor() >= 230 and ball.xcor() <= 250) and ball.ycor() < paddle_player.ycor() + 50 and ball.ycor() > paddle_player.ycor() - 50:
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dx *= -1

    # AI player
    if paddle_AI.ycor() < ball.ycor() and (abs(paddle_AI.ycor() - ball.ycor()) > 20):
        paddle_AI_up()

    elif paddle_AI.ycor() > ball.ycor() and (abs(paddle_AI.ycor() - ball.ycor()) > 20):
        paddle_AI_down()