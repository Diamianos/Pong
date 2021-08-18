import pygame

pygame.init()
pygame.font.init()

# Globals for width and height
WIDTH = 800
HEIGHT = 600
WHITE = (255,255,255)

# Drawing the initial surface
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Setting the caption
pygame.display.set_caption("Pong")

# Setting up the font style for the game
myFont = pygame.font.SysFont('couriernew', 30)


# Variable to hold the score
player1 = 0
player2 = 0

# Creating the text surface
textSurface = myFont.render(f"Player 1: {player1}    Player2: {player2}", True, (WHITE))
text_rect = textSurface.get_rect(center=(WIDTH/2, 0 + 30))

# Setting the speed of the paddles and ball
vel = 5

# Paddle 1
pad_1_x = 50
pad_1_y = 250
pad_1_width = 10
pad_1_height = 100

# Paddle 2
pad_2_x = 750
pad_2_y = 250
pad_2_width = 10
pad_2_height = 100

# Ball
ball_x = 400
ball_y = 300

ball_dx = 3
ball_dy = 3

run = True
while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Setting up a variable for the key presses  
    keys = pygame.key.get_pressed()

    # Binding the key presses to move the paddles
    if keys[pygame.K_UP] and pad_2_y > 0 + vel:
        pad_2_y -= vel
    if keys[pygame.K_DOWN] and pad_2_y < HEIGHT - pad_2_height:
        pad_2_y += vel
    if keys[pygame.K_w] and pad_1_y > 0 + vel:
        pad_1_y -= vel
    if keys[pygame.K_s] and pad_1_y < HEIGHT - pad_2_height:
        pad_1_y += vel

    # Starts the initial movement of the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Setting the boundaries for the ball and reversing direction if hitting the bounds
    if ball_y > HEIGHT - 15 or ball_y < 0 + 15:
        ball_dy *= -1
    # if ball_x > WIDTH - 15 or ball_x < 0 + 15:
    #     ball_dx *= -1

    # Ball and Paddle collisions 
    if (ball_x >= pad_2_x - 10 and ball_x < pad_2_x + 10) and ball_y >= pad_2_y and ball_y <= pad_2_y + 100:
        ball_dx *= -1
    if (ball_x <= pad_1_x + 20 and ball_x > pad_1_x) and ball_y >= pad_1_y and ball_y <= pad_1_y + 100:
        ball_dx *= -1

    # If the ball goes out of bounds, set it back in the middle of the screen
    if ball_x > WIDTH + 20:
        player1 += 1 # Incrementing the score count
        textSurface = myFont.render(f"Player 1: {player1}    Player2: {player2}", True, (WHITE))
        ball_x = 400
        ball_y = 300
        ball_dx *= -1
        

    if ball_x < 0 - 20:
        player2 += 1 # Incrementing the score count
        textSurface = myFont.render(f"Player 1: {player1}    Player2: {player2}", True, (WHITE))
        ball_x = 400
        ball_y = 300
        ball_dx *= -1
        
    
    
    window.fill((0,0,0))
    window.blit(textSurface, text_rect)
    pygame.draw.rect(window, WHITE, (pad_1_x, pad_1_y, pad_1_width, pad_1_height))
    pygame.draw.rect(window, WHITE, (pad_2_x, pad_2_y, pad_2_width, pad_2_height))
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), 15)
    pygame.display.update()

pygame.quit()