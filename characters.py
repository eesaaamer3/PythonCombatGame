import pygame
import sys

class IronMan:
    def __init__(self, x, y, x_change, velocity, standing, jumping, flying):
        super().__init__()
        self.x = x
        self.y = y
        self.x_change = x_change 
        self.velocity = velocity 
        self.standing = standing
        self.jumping = jumping
        self.flying = flying

        self.playerImg = pygame.image.load("Images/IronMan-Standing.png")
        self.finalPlayer = pygame.transform.scale(self.playerImg, (75, 100))

        self.flyingAnimation = pygame.image.load("Images/IronMan-Flying.png")
        self.JumpingAnimation = pygame.image.load("Images/IronMan-Jumping.png")

        self.shootingAnimation = pygame.image.load("Images/Iron-man-shooting.png")
        

        self.reverseFlyingAnimation = pygame.transform.flip(self.flyingAnimation, True, False)
        
        #self.PunchAnimation = pygame.image.load()

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
        self.finalEnemy = pygame.transform.scale(self.enemyImg, (100, 100))


        
        



        