import sys, pygame
from pygame.locals import *
class Player(pygame.sprite.Sprite):

    walking = 0

    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        ##debug output	
        print('Initialized to x = ', self.rect.x)
        print('Initialized to y = ', self.rect.y)

    def move_x(self, x):
        walking = 1        
        self.rect.x += x
        walking = 0

    def jump(self, y):
        self.rect.y += y
		

	
	

