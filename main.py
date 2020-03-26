import pygame 
import random
import characters

pygame.init()

# Creates game window
gameScreen = pygame.display.set_mode((1200, 800))

# Title and Logo
pygame.display.set_caption("Hero Combat")
icon = pygame.image.load('Images/superhero.png')
pygame.display.set_icon(icon)


# Player
ironMan = pygame.image.load('Images/ironman.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy 
batman = pygame.image.load('Images/batman.png')
enemyX = random.randint(0, 1200)
enemyY = 240
enemyX_change = 0
enemyY_change = 0

# Changing image size
finalPlayer = pygame.transform.scale(ironMan, (100, 100))
finalEnemy = pygame.transform.scale(batman, (150, 150))


def player(x, y):
    gameScreen.blit(finalPlayer, (x, y))

def enemy(x, y):
    gameScreen.blit(finalEnemy, (x, y))

def gravity()

# Game Loop
gameRun = True
while gameRun:
    gameScreen.fill((255, 255, 255))

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
    
    playerX += playerX_change

    # Boundries
    if playerX < 0:
        playerX = 0
    elif playerX >= 1100:
        playerX = 1100  

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    
    pygame.display.update()

