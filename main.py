#!/usr/bin/env python2.7
import sys, pygame
from pygame.locals import *

from player import *
from obstacle import *
from colors import *
from player_assets import *
pygame.init()

##############################
### Loading all the things ###
##############################
clock = pygame.time.Clock()
size = [1050,500]
fps = 16
window = pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.HWSURFACE)## | pygame.FULLSCREEN )
background = pygame.image.load("assets/Rainbow.jpg").convert()
pygame.display.set_caption('Rainbow')

#####################
### Set up player ###
#####################
#Loading player images is done in player_assets
player = Player([300, 300], walkcycle_R[0])

#########################
### Loading obstacles ###
#########################
obst_img = pygame.image.load("assets/dummy_obstacle.png").convert()
floor_img = pygame.image.load("assets/dummy_floor.png").convert()
obstacle = Obstacle([600, 343], obst_img)
floor = Obstacle([0,426], floor_img)

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
        if player.image is walkcycle_R[0]:
            player.image = walkcycle_R[1]
        elif player.image is walkcycle_R[1]:
            player.image = walkcycle_R[2]
        elif player.image is walkcycle_R[2]:
            player.image = walkcycle_R[3]
        elif player.image is walkcycle_R[3]:
            player.image = walkcycle_R[4]
        else:
            player.image = walkcycle_R[0]
    else:
        if player.image is walkcycle_L[0]:
            player.image = walkcycle_L[1]
        elif player.image is walkcycle_L[1]:
            player.image = walkcycle_L[2]
        elif player.image is walkcycle_L[2]:
            player.image = walkcycle_L[3]
        elif player.image is walkcycle_L[3]:
            player.image = walkcycle_L[4]
        elif player.image is walkcycle_L[4]:
            player.image = walkcycle_L[0]
        else:
            player.image = walkcycle_L[0]

#################
### Game loop ###
#################
while pygame.event.poll().type != QUIT:
    clock.tick(fps)
    window.fill(white)
    keys = pygame.key.get_pressed()
    #print 'DEBUG: Jumped = ', jumped

    if keys[K_ESCAPE]:
        #pygame.quit()
        print 'DEBUG: Game loop terminated by esc.\nGood Bye.'
        break

<<<<<<< HEAD
    if jumped:
        player.jump(fps/2.5, obstacle)
    if player.touching(floor) or player.touching(obstacle):
            jumped = False

    if (keys[K_w] or keys[K_UP] and not jumped):
        player.jump(-fps*6, obstacle)
        jumped = True
=======
    if (keys[K_w] or keys[K_UP] or keys[K_SPACE]):
        player.jump(obstacle, floor)
>>>>>>> 8b27334ad5b6ed104326427a733fbd3da8f10231

    if keys[K_d] or keys[K_RIGHT]:
        face_right = True
        player.move_x(fps/4, obstacle)
        update()
        print 'DEBUG: Player image is: ', player.image
        print 'DEBUG: Variable face_right: ', face_right

    if keys[K_a] or keys[K_LEFT]:
        face_right = False
        player.move_x(fps/-4, obstacle)
        update()
        print 'DEBUG: Player image is: ', player.image
        print 'DEBUG: Variable face_right: ', face_right

    window.blit(background, background.get_rect())
    window.blit(player.image, player.rect)
    window.blit(obstacle.image, obstacle.rect)
    window.blit(floor.image, floor.rect)

    pygame.display.update()
