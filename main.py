#!/usr/bin/env python2.7
import sys, pygame
from pygame.locals import *

from player import *
from obstacle import *
from colors import *
pygame.init()

##############################
### Loading all the things ###
##############################
clock = pygame.time.Clock()
size = [1050,500]
window = pygame.display.set_mode(size)
background = pygame.image.load("assets/Rainbow.jpg")
walk1, walk2, walk1l, walk2l = pygame.image.load("assets/ninja_step1.png"), pygame.image.load("assets/ninja_step2.png"), pygame.image.load("assets/ninja_step1l.png"), pygame.image.load("assets/ninja_step2l.png")
wlkcycl = [walk1, walk2, walk1l, walk2l]
player = Player([500, 300], walk1)
pygame.display.set_caption('Rainbow')

### Obstacle trial ###
obst_img = pygame.image.load("assets/dummy_obstacle.png")
obstacle = Obstacle([600, 300], obst_img)

## Not needed right now ##
#idleImage = pygame.image.load("assets/ninja_idle.png")



#################################
### Important state variables ###
#################################  
jumped = False
face_right = True
print 'DEBUG: Variable jumped initiated to: ', jumped
print 'DEBUG: Variable face_right initiated to: ', face_right

########################
### Helper functions ###
########################
def update():
    if face_right:
        if player.image is wlkcycl[0]:
            player.image = wlkcycl[1]
        else:
            player.image = wlkcycl[0]
    else:
        if player.image is wlkcycl[3]:
            player.image = wlkcycl[2]
        else:
            player.image = wlkcycl[3]


### Game loop ###
while pygame.event.poll().type != QUIT:
        window.fill(white)
        keys = pygame.key.get_pressed()
        

        if keys[K_ESCAPE]:
            pygame.quit()

        if jumped:
            player.jump(1)
            if player.rect.y >= 300:
                player.rect.y = 300
                jumped = False

        
        if (keys[K_w] or keys[K_UP] and player.rect.y >= 174):
            clock.tick(24)            
            player.jump(-30)
            jumped = True
        
        if keys[K_d] or keys[K_RIGHT]:
            if player.rect.colliderect(obstacle.rect):
                print 'DEBUG: Collision detected.'
                pass
            else:            
                face_right = True            
                player.move_x(15)
                clock.tick(7)
                update()
                print 'DEBUG: Variable face_right: ', face_right

        if keys[K_a] or keys[K_LEFT]:
            face_right = False            
            player.move_x(-15)
            clock.tick(7)
            update()
            print 'DEBUG: Variable face_right: ', face_right
        
        window.blit(background, background.get_rect())
        window.blit(player.image, player.rect)

        pygame.display.update()
