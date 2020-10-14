## Python3 Pong game built using turtle module
## Following a tutorial with link in the README
## Doesn't follow OOP too much just a brute-force method
## Also set up for mac rather than windows/linux

# turtle module that is built in to allow for games
import turtle
# specifically for mac to interact with the sounds
import os

## this is what creates the window for the game
window = turtle.Screen()
window.title("Python Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# keep and modify the score
score_a = 0
score_b = 0


## left paddle
# small turtle for module, Turtle for object 
paddle_a = turtle.Turtle()
# speed of animation
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
# .goto(x-coordinate, y coordinate)
paddle_a.goto(-350, 0)


## right paddle
paddle_b = turtle.Turtle()
# speed of animation
paddle_b.speed(0)
# creates the shape of the paddle
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
# .goto(x-coordinate, y coordinate)
paddle_b.goto(350, 0)


## ball
ball = turtle.Turtle()
# speed of animation
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
# .goto(x-coordinate, y coordinate)
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# creating the score card (pen)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white");
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  |  Player 2: 0", align="center", font=("Courier", 20, "normal"))

# functions to allow the pieces to move
def paddle_a_up():
    # need to first get the y-coordinate from the turtle module
    y = paddle_a.ycor()
    y += 20
    # updates y to be the new coordinate set
    paddle_a.sety(y)

def paddle_a_down():
    # need to first get the y-coordinate from the turtle module
    y = paddle_a.ycor()
    y -= 20
    # updates y to be the new coordinate set
    paddle_a.sety(y)

def paddle_b_up():
    # need to first get the y-coordinate from the turtle module
    y = paddle_b.ycor()
    y += 20
    # updates y to be the new coordinate set
    paddle_b.sety(y)

def paddle_b_down():
    # need to first get the y-coordinate from the turtle module
    y = paddle_b.ycor()
    y -= 20
    # updates y to be the new coordinate set
    paddle_b.sety(y)

# listens for the keyboard input
window.listen()
# listens specifically for lowercase "w" input
window.onkeypress(paddle_a_up, "w")
# listens specifically for lowercase "s" input
window.onkeypress(paddle_a_down, "s")
# listens specifically for up arrow input
window.onkeypress(paddle_b_up, "Up")
# listens specifically for down arrow input
window.onkeypress(paddle_b_down, "Down")

## main game loop
# this is what runs the game continuously
while True:
    window.update()


    # move the ball
    # this controls and moves the x-coordinate to update and move
    ball.setx(ball.xcor() + ball.dx)
    # this controls and moves the y-coordinate to update and move
    ball.sety(ball.ycor() + ball.dy)

    
    # controls the ball to move off the top and bottom border
    if ball.ycor() > 280:
        ball.sety(280)
        # this is specifically what reverses the direction when it gets to the border
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.ycor() < -280:
        ball.sety(-280)
        # this is specifically what reverses the direction when it gets to the border
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # controls the ball reset the ball once it reaches the outer x borders
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        # since it goes off the right side of screen, player A has gotten a score
        score_a += 1
        # this clears what's on the screen prior to writing the new score
        pen.clear()
        pen.write("Player A: {}  |  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        # since it goes off the right side of screen, player B has gotten a score
        score_b += 1
        # this clears what's on the screen prior to writing the new score
        pen.clear()
        pen.write("Player A: {}  |  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))


    # set up the collision for the paddle and the ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")