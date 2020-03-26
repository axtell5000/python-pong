import turtle

wn = turtle.Screen()
wn.title('Pong by Stephen Axtell')
wn.bgcolor('black')
wn.setup(width=800, height=800)
wn.tracer(0) # stops window auto updating

# paddle left
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('white')
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# paddle right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.color('white')
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# functions
def padddle_left_up():
  y = paddle_left.ycor()
  y += 20
  paddle_left.sety(y)

def padddle_left_down():
  y = paddle_left.ycor()
  y -= 20
  paddle_left.sety(y)

def padddle_right_up():
  y = paddle_right.ycor()
  y += 20
  paddle_right.sety(y)

def padddle_right_down():
  y = paddle_right.ycor()
  y -= 20
  paddle_right.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(padddle_left_up, "w")
wn.onkeypress(padddle_left_down, "s")

wn.onkeypress(padddle_right_up, "o")
wn.onkeypress(padddle_right_down, "l")

# Main game loop
while True:
  wn.update()
  # Move the ball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  # Border checking
  if ball.ycor() > 390:
    ball.sety(390)
    ball.dy *= -1

  if ball.ycor() < -390:
    ball.sety(-390)
    ball.dy *= -1

  if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1

  if ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
