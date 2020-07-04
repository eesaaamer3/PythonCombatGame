import pygame
import sys
from characters import IronMan, Batman
import time

class GameScreen:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((700,400))

        self.icon = pygame.image.load('Images/superhero.png')

        self.icon_transformed = pygame.transform.scale(self.icon, (100, 100))

        self.background = pygame.image.load('Images/background.png')

        pygame.display.set_icon(self.icon_transformed)      

        pygame.display.set_caption("Hero Combat")  
        
    def update_screen(self, player, enemy):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0,0))
        self.screen.blit(player.finalPlayer, (player.x, player.y))
        self.screen.blit(enemy.finalEnemy, (enemy.x, enemy.y))

    def run_game(self, player, enemy):
        while True:

            # Checks to see if game has been quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
            
            # Player controls for Iron Man 
            if event.type == pygame.KEYDOWN:
                #Iron Man moving to the left 
                if event.key == pygame.K_LEFT:
                    player.x_change = -2
                    player.finalPlayer = player.reverseFlyingAnimation
                    player.flying = True
                # Iron man moving to the right
                if event.key == pygame.K_RIGHT:
                    player.finalPlayer = player.flyingAnimation
                    player.flying = True
                    player.x_change = 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.x_change = 0
                    player.flying = False
                    player.finalPlayer = player.playerImg

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player.y = 290
                    player.finalPlayer = player.shootingAnimation

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player.y = 280
                    player.finalPlayer = player.playerImg
            
            # Iron man stays on the map
            if player.x < 0:
                player.x = 0
            elif player.x >= 600:
                player.x = 600 

            # Iron man jumping
            if player.standing == True and player.flying == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        # Gravity on Iron man
                        player.velocity = -14
                        player.jumping = True
                        player.standing = False
                        player.finalPlayer = player.JumpingAnimation
            # Ensures iron man doesn't fly away/go past the roof when he is jumping
            elif player.jumping == True:
                if player.flying == False:
                    player.velocity += 0.41
                elif player.flying == True:
                    player.velocity += 0.1
                if player.y > 280:
                    player.velocity = 0
                    player.y = 280
                    player.jumping = False
                    player.standing = True
                    player.finalPlayer = player.playerImg

            player.y += player.velocity
            player.x += player.x_change

            # Player controls for Batman 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    enemy.x_change = -2
                if event.key == pygame.K_d:
                    enemy.x_change = 2
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    enemy.x_change = 0
             
            if enemy.x < 0:
                enemy.x  = 0
            elif enemy.x  >= 600:
                enemy.x = 600
            
            if enemy.standing == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        enemy.velocity = -14
                        enemy.jumping = True
                        enemy.standing = False
            elif enemy.jumping == True:
                enemy.velocity += 0.5
                if enemy.y > 240:
                    enemy.velocity = 0
                    enemy.y = 240
                    enemy.jumping = False
                    enemy.standing = True

            enemy.y += enemy.velocity
            enemy.x += enemy.x_change

            self.update_screen(player, enemy)
            pygame.display.update()

if __name__ == "__main__":
    game = GameScreen()
    ironMan = IronMan(20, 275, 0, 0, True, False, False)
    batman = Batman(550, 240, 0, 0, True, False)
    game.run_game(ironMan, batman)
