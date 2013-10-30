#!/usr/bin/env python2.7
import sys, pygame
from pygame.locals import *

from player import *
from obstacle import *
from colors import *

##############################
### Loading all the things ###
##############################
pygame.init()

clock = pygame.time.Clock()
size = [1050,500]
fps = 16
icon = pygame.image.load("assets/game_icon.png")
pygame.display.set_icon(icon)
window = pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.HWSURFACE)# | pygame.FULLSCREEN )
background = pygame.image.load("assets/Rainbow.jpg").convert()
pygame.display.set_caption('Rainbow Ninja')



#####################
### Set up player ###
#####################
player = Player([300, 300], walkcycle_R[0])

#########################
### Loading obstacles ###
#########################
obst_img = pygame.image.load("assets/dummy_obstacle.png").convert()
floor_img = pygame.image.load("assets/dummy_floor.png").convert()
obstacle = Obstacle([600, 343], obst_img)
floor = Obstacle([0,426], floor_img)

#################
### Game loop ###
#################
while pygame.event.poll().type != QUIT:
    clock.tick(fps)
    window.fill(white)
    player.fall(obstacle, floor)

    keys = pygame.key.get_pressed()

    if keys[K_ESCAPE]:
        print 'DEBUG: Game loop terminated by esc.\nGood Bye.'
        break

    if (keys[K_w] or keys[K_UP] or keys[K_SPACE]):
        player.jump(obstacle, floor)

    if keys[K_d] or keys[K_RIGHT]:
        player.face_right = True
        player.move_x(4, obstacle)
        player.update_walkcycl()
        print 'DEBUG: Variable face_right: ', player.face_right

    if keys[K_a] or keys[K_LEFT]:
        player.face_right = False
        player.move_x(-4, obstacle)
        player.update_walkcycl()
        print 'DEBUG: Variable face_right: ', player.face_right

    ### Draw everything
    window.blit(background, background.get_rect())
    window.blit(player.image, player.rect)
    window.blit(obstacle.image, obstacle.rect)
    window.blit(floor.image, floor.rect)

    pygame.display.update()
