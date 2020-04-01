import pygame 
import random
import characters

pygame.init()

# Creates game window
gameScreen = pygame.display.set_mode((700, 400))

# Title and Logo
pygame.display.set_caption("Hero Combat")
icon = pygame.image.load('Images/superhero.png')
pygame.display.set_icon(icon)


# Background
background = pygame.image.load('Images/background.png')

# Player
ironMan = pygame.image.load('Images/ironman.png')
playerX = 20
playerY = 275
playerX_change = 0
player_velocity = 0
playerStanding = True
playerJumping = False

# Enemy 
batman = pygame.image.load('Images/batman.png')
enemyX = 550
enemyY = 240
enemyX_change = 0
enemy_velocity = 0
enemyStanding = True
enemyJumping = False


# Changing image size
finalPlayer = pygame.transform.scale(ironMan, (100, 100))
finalEnemy = pygame.transform.scale(batman, (150, 150))


def player(x, y):
    gameScreen.blit(finalPlayer, (x, y))

def enemy(x, y):
    gameScreen.blit(finalEnemy, (x, y))



# Game Loop
gameRun = True
while gameRun:
    gameScreen.fill((255, 255, 255))

    gameScreen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False
    
    # if keystroke is pressed, check whether it is right or left

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -4
        if event.key == pygame.K_RIGHT:
            playerX_change = 4

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            enemyX_change = -4
        if event.key == pygame.K_d:
            enemyX_change = 4
        
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a or event.key == pygame.K_d:
            enemyX_change = 0


    # Iron Man Jumping
    if playerStanding == True:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_velocity = -14
                playerJumping = True
                playerStanding = False
    elif playerJumping == True:
        player_velocity += 0.5
        if playerY > 275:
            player_velocity = 0
            playerY = 275
            playerJumping = False
            playerStanding = True

    playerY += player_velocity

    # Batman Jumping
    if enemyStanding == True:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                enemy_velocity = -14
                enemyJumping = True
                enemyStanding = False
    elif enemyJumping == True:
        enemy_velocity += 0.5
        if enemyY > 240:
            enemy_velocity = 0
            enemyY = 240
            enemyJumping = False
            enemyStanding = True

   
    enemyY += enemy_velocity

    playerX += playerX_change
    enemyX += enemyX_change


    # Boundries on the side walls
    if playerX < 0:
        playerX = 0
    elif playerX >= 600:
        playerX = 600 
    
    if enemyX < 0:
        enemyX = 0
    elif enemyX >= 600:
        enemyX = 600

    
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()

