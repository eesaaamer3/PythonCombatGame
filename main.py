import pygame 

pygame.init()

# Creates game window
gameScreen = pygame.display.set_mode((1200, 800))

# Title and Logo
pygame.display.set_caption("Hero Combat")
icon = pygame.image.load('Images/superhero.png')
pygame.display.set_icon(icon)



# Game Loop
gameRun = True
while gameRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False
    
    # Game screen colour (RGB Value)
    gameScreen.fill((0, 0, 0))
    
    pygame.display.update()

