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

<<<<<<< HEAD
=======
    def touching(self, obj):
        return self.rect.colliderect(obj.rect)

    def jump(self, obstacle, floor):
        if not self.jumped:
            self.jumped = True
            self.rect.y += -95

    def fall(self, obstacle, floor):
        bounds = boundsRaw = self.rect.copy()
        boundsRaw.y += 8
        if boundsRaw.colliderect(obstacle.rect) or boundsRaw.colliderect(floor.rect):
            boundsFine = bounds = self.rect.copy()
            boundsFine.y += 1
            if boundsFine.colliderect(obstacle.rect) or boundsFine.colliderect(floor.rect):
                self.jumped = False
            else:
                self.rect.y = boundsFine.y
            #self.jumped = False
        else:
            self.rect.y = bounds.y

>>>>>>> 8b27334ad5b6ed104326427a733fbd3da8f10231
    def move_x(self, x, obstacle):
        bounds = self.rect.copy()
        bounds.x += x
        if not bounds.colliderect(obstacle.rect):
            self.rect = bounds
        else:
<<<<<<< HEAD
            print 'DEBUG: Collision detected.'
=======
            print 'DEBUG: i has value: 0'
>>>>>>> 8b27334ad5b6ed104326427a733fbd3da8f10231

    def jump(self, y, obstacle):
        bounds = self.rect.copy()
        bounds.y += y
        if not bounds.colliderect(obstacle.rect):
            self.rect.y += y
        else:
            print 'DEBUG: Collision detected.'

    def touching(self, obj):
        return self.rect.colliderect(obj.rect)
