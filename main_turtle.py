import turtle

window = turtle.Screen() # Creates the screen
window.title("Pong by John Savard") # Creates the title for the game
window.bgcolor("black") # Changes the background color
window.setup(width=800, height=600) # Changes the resolution of the window
window.tracer(0) # Stops window from updating, always to speed up games "quite a bit". Allows game to run faster

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle() # This creates a turtle object
paddle_a.speed(0) # Speed of animation, this is set to max
paddle_a.shape("square") # Determines the shape of the paddle
paddle_a.color("white") # Color of the paddle
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #Default pixels is 20 x 20. Here we are stretching wid by 5 and len will be default
paddle_a.penup() #Turtles by def draw a line, we want the "pen up"
paddle_a.goto(-350, 0) #starting position of paddle

# Paddle B
paddle_b = turtle.Turtle() 
paddle_b.speed(0) 
paddle_b.shape("square") 
paddle_b.color("white") 
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
paddle_b.penup() 
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle() 
ball.speed(0) 
ball.shape("square") 
ball.color("white") 
ball.penup() 
ball.goto(0, 0)
ball.dx = .08 # d = Delta or change, everytime ball moves, move by value of pixels
ball.dy = .08 # d = Delta or change, everytime ball moves, move by value of pixels

# Pen
pen = turtle.Turtle()
pen.speed(0) # animation speed
pen.color("white")
pen.penup()
pen.hideturtle() # don't want to see the turtle object, just the text that it writes
pen.goto(0, 260)
pen.write("Player A :0  Player B: 0", align="center", font=("Courier", 24, "normal"))



# Functions

def paddle_a_up():
    y = paddle_a.ycor() # ycor() from turtle module, returns the y cordiante and returns to a variable
    y += 20
    paddle_a.sety(y) # sets paddle a up by 20 pixels

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
window.listen() #listen for keyboard input
window.onkeypress(paddle_a_up, "w") # when w is pressed, call the paddle_a_up function
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop (every game needs this)
while True:
    window.update() # Everytime the loop runs, it updates the screen


    # Move the ball
    ball.setx(ball.xcor() + ball.dx) # Takes the current x cordinate value and adds value of ball.dx
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor () > 290: # If the ball hits the top border
        ball.sety(290) # sets the ball to equal 290 (to avoid problems)
        ball.dy *= -1 # Reverses the direction of the ball

    if ball.ycor () < -290:
        ball.sety(-290) 
        ball.dy *= -1 

    if ball.xcor () > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1 # Raises score when ball goes off the screen
        pen.clear()
        pen.write(f"Player A :{score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


    if ball.xcor () < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1 
        pen.clear()
        pen.write(f"Player A :{score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40): # If ball hits paddle
        ball.setx(340) # Set ball cordinate
        ball.dx *= -1 # Reverse direction 
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40): # If ball hits paddle
        ball.setx(-340)
        ball.dx *= -1 
