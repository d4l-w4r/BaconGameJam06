#!/usr/bin/env python2.7
import sys, pygame
from pygame.locals import *

from player import *
from colors import *

pygame.init()
fpsClock = pygame.time.Clock()
fpsClock.tick()

size = [1050,500]
window = pygame.display.set_mode(size)
pygame.display.set_caption('Rainbow')
player_Image = pygame.image.load("assets/ninja_idle.png")
background = pygame.image.load("assets/Rainbow.jpg")
player = Player([500, 300], player_Image)
##debug print
print 'Player.img = ', player.image

jumped = False

while pygame.event.poll().type != QUIT:
        time = fpsClock.tick()
        keys = pygame.key.get_pressed()

        if keys[K_ESCAPE]:
            pygame.quit()

        if jumped:
            player.jump(1)
            if player.rect.y >= 300:
                player.rect.y = 300
                jumped = False

        
        if (keys[K_w] or keys[K_UP] and player.rect.y >= 185):
            player.jump(-30)
            jumped = True
        
        if keys[K_d] or keys[K_RIGHT]:
            player.move_x(1)
<<<<<<< HEAD
       
        if keys[K_a] or keys[K_LEFT]:
            player.move_x(-1)
        
=======
        if keys[K_a] or keys[K_LEFT]:
            player.move_x(-1)
>>>>>>> 51de456c0f1de922e5fa36421ccab2f8ea5a59b3


        window.fill(white)

        # pygame.draw.rect(window, red, (0, 0, 150, 500))
        # pygame.draw.rect(window, orange, (150, 0, 150, 500))
        # pygame.draw.rect(window, yellow, (300, 0, 150, 500))
        # pygame.draw.rect(window, green, (450, 0, 150, 500))
        # pygame.draw.rect(window, lightblue, (600, 0, 150, 500))
        # pygame.draw.rect(window, darkblue, (750, 0, 150, 500))
        # pygame.draw.rect(window, purple, (900, 0, 150, 500))
        # pygame.draw.rect(window, white, (0, 400, 1050, 100))
        window.blit(background, background.get_rect())
        window.blit(player.image, player.rect)

        pygame.display.update()
