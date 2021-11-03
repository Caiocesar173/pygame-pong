import pygame,sys

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if( ball.top <= 0 or ball.bottom >= screen_height ):
        ball_speed_y *= -1
    if( ball.right <= 0 or ball.left >= screen_width ):
        ball_speed_x *= -1

    if( ball.colliderect(player) or ball.colliderect(opponent)):
        ball_speed_x *= -1

#General Setup
pygame.init()
clock = pygame.time.Clock()

#Setting up the main Window
screen_width = 900
screen_height = 600

ball_speed_x = 7
ball_speed_y = 7

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')


ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
ligth_grey = pygame.Color(200,200,200)



while True:
    #Handling Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball_animation()


    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, ligth_grey, player)
    pygame.draw.rect(screen, ligth_grey, opponent)
    pygame.draw.ellipse(screen, ligth_grey, ball)

    pygame.draw.aaline(screen, ligth_grey, (screen_width/2, 0), (screen_width/2, screen_height))


    #Updating the Window
    pygame.display.flip()
    clock.tick(60)