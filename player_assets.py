import pygame
from pygame.locals import *
from player import *

## importing all the player assets

walk_r1, walk_r2, walk_r3, walk_r4, walk_r5 = pygame.image.load("assets/walkcycle_R/ninja_step1.png"), pygame.image.load("assets/walkcycle_R/ninja_step2.png"), pygame.image.load("assets/walkcycle_R/ninja_step3.png"), pygame.image.load("assets/walkcycle_R/ninja_step4.png"), pygame.image.load("assets/walkcycle_R/ninja_step5.png")

walk_l1, walk_l2, walk_l3, walk_l4, walk_l5 = pygame.image.load("assets/walkcycle_L/ninja_step1.png"), pygame.image.load("assets/walkcycle_L/ninja_step2.png"), pygame.image.load("assets/walkcycle_L/ninja_step3.png"), pygame.image.load("assets/walkcycle_L/ninja_step4.png"), pygame.image.load("assets/walkcycle_L/ninja_step5.png")

walkcycle_R = [walk_r1, walk_r2, walk_r3, walk_r4, walk_r5]
walkcycle_L = [walk_l1, walk_l2, walk_l3, walk_l4, walk_l5]