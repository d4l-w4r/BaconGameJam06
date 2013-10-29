import sys, pygame
from pygame.locals import *
from obstacle import *

class Player(pygame.sprite.Sprite):


    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-10,0)
        self.rect.topleft = pos

        ##debug output
        print('Initialized to x = ', self.rect.x)
        print('Initialized to y = ', self.rect.y)

    def move_x(self, x, obstacle):
        bounds = self.rect.copy()
        bounds.x += x
        if not bounds.colliderect(obstacle.rect):
            self.rect = bounds
        else:
            print 'DEBUG: Collision detected.'

    def jump(self, y, obstacle):
        bounds = self.rect.copy()
        bounds.y += y
        if not bounds.colliderect(obstacle.rect):
            self.rect.y += y
        else:
            print 'DEBUG: Collision detected.'

    def touching(self, obj):
        return self.rect.colliderect(obj.rect)

    def movex(self, x, obstacle):
        bounds = self.rect.copy()

        i = x
        if i != 0:
            if i >= 0:
                bounds.x += i/i
                print 'DEBUG: i has value: ', i
                if not bounds.colliderect(obstacle.rect):
                    self.rect.x = bounds.x
                    self.movex(x-1, obstacle)
            elif i <= 0:
                bounds.x += i/i
                if not bounds.colliderect(obstacle.rect):
                    self.rect.x = bounds.x
                    self.movex(x+1, obstacle)
        else:
            print 'DEBUG: x is 0'
