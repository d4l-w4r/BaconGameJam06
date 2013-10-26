import sys, pygame
from pygame.locals import *

from player import *
from colors import *

pygame.init()
fpsClock = pygame.time.Clock()
fpsClock.tick()

size = [1050,500]
window = pygame.display.set_mode(size)
pygame.display.set_caption('Rainbow')
player_Image = pygame.image.load("assets/Ninja.png")
player = Player([500, 185], player_Image)
##debug print
print 'Player.img = ', player.image

jump_key_down = False

while pygame.event.poll().type != QUIT:
        time = fpsClock.tick()
        sek = float(time)/1000
        strecke = sek*50
        fall = sek*300

        keys = pygame.key.get_pressed()
        if not jump_key_down and (keys[K_w] or keys[K_UP] and player.rect.y):
            player.jump(-(fall + 50))
            jump_key_down = True
        elif jump_key_down and (keys[K_w] or keys[K_UP]):
            pass
        else:
            jump_key_down = False
        if keys[K_d] or keys[K_RIGHT]:
            player.move_x(strecke)
            print("Right", strecke)
        if keys[K_a] or keys[K_LEFT]:
            player.move_x(-strecke)
            print("Left", -strecke)

        if player.rect.y < 185:
            player.rect.y = player.rect.y+fall

        window.fill(white)

        pygame.draw.rect(window, red, (0, 0, 150, 500))
        pygame.draw.rect(window, orange, (150, 0, 150, 500))
        pygame.draw.rect(window, yellow, (300, 0, 150, 500))
        pygame.draw.rect(window, green, (450, 0, 150, 500))
        pygame.draw.rect(window, lightblue, (600, 0, 150, 500))
        pygame.draw.rect(window, darkblue, (750, 0, 150, 500))
        pygame.draw.rect(window, purple, (900, 0, 150, 500))
        pygame.draw.rect(window, white, (0, 400, 1050, 100))
        window.blit(player.image, player.rect)

        pygame.display.update()
