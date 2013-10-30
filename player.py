import sys, pygame
from pygame.locals import *
from obstacle import *
from player_assets import *

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-10,0)
        self.rect.topleft = pos
        self.face_right = True
        self.jumped = False
        ##debug output
        print 'DEBUG: Variable jumped initiated to: ', self.jumped
        print 'DEBUG: Variable face_right initiated to: ', self.face_right
        print('Initialized to x = ', self.rect.x)
        print('Initialized to y = ', self.rect.y)

    def touching(self, obj):
        return self.rect.colliderect(obj.rect)

    def jump(self, obstacle, floor):
        if not self.jumped:
            self.jumped = True
            self.rect.y += -95

    def fall(self, obstacle, floor):
        bounds = boundsRaw = self.rect.copy()
        boundsRaw.y += 6
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

    def move_x(self, x, obstacle):
        bounds = self.rect.copy()

        i = x
        if i != 0:
            if i >= 0:
                bounds.x += i/i
                print 'DEBUG: i has value: ', i
                if not bounds.colliderect(obstacle.rect):
                    self.rect.x = bounds.x
                    self.move_x(x-1, obstacle)
            elif i <= 0:
                bounds.x += i/-i
                print 'DEBUG: i has value: ', i
                if not bounds.colliderect(obstacle.rect):
                    self.rect.x = bounds.x
                    self.move_x(x+1, obstacle)
        else:
            print 'DEBUG: i is 0'

    def update_walkcycl(self):
        if self.face_right:
            if self.image is walkcycle_R[0]:
                self.image = walkcycle_R[1]
            elif self.image is walkcycle_R[1]:
                self.image = walkcycle_R[2]
            elif self.image is walkcycle_R[2]:
                self.image = walkcycle_R[3]
            elif self.image is walkcycle_R[3]:
                self.image = walkcycle_R[4]
            else:
                self.image = walkcycle_R[0]
        else:
            if self.image is walkcycle_L[0]:
                self.image = walkcycle_L[1]
            elif self.image is walkcycle_L[1]:
                self.image = walkcycle_L[2]
            elif self.image is walkcycle_L[2]:
                self.image = walkcycle_L[3]
            elif self.image is walkcycle_L[3]:
                self.image = walkcycle_L[4]
            else:
                self.image = walkcycle_L[0]
