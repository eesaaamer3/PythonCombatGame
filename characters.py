import pygame
import sys

class IronMan:
    def __init__(self, x, y, x_change, velocity, standing, jumping):
        super().__init__()
        self.x = x
        self.y = y
        self.x_change = x_change 
        self.velocity = velocity 
        self.standing = standing
        self.jumping = jumping

        self.playerImg = pygame.image.load("Images/ironman.png")
        self.finalPlayer = pygame.transform.scale(self.playerImg, (100, 100))

class Batman:
    def __init__(self, x, y, x_change, velocity, standing, jumping):
        super().__init__()
        self.x = x
        self.y = y
        self.x_change = x_change 
        self.velocity = velocity 
        self.standing = standing
        self.jumping = jumping

        self.enemyImg = pygame.image.load("Images/batman.png")
        self.finalEnemy = pygame.transform.scale(self.enemyImg, (150, 150))

    
        



        