import pygame
from pygame.locals import *

class Obstacle(pygame.sprite.Sprite):
    
    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-9.5,0)
        self.rect.topleft = pos
        
        
        
