import sys, pygame
from pygame.locals import *
class Player(pygame.sprite.Sprite):

    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        ##debug output	
        print('Initialized to x = ', self.rect.x)
        print('Initialized to y = ', self.rect.y)

    def move_x(self, x):
        self.rect.x += x

    def jump(self, y):
        self.rect.y += y
		

	
	

