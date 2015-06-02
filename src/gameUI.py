__author__ = 'plaix'
import pygame
import sys
from pygame.locals import *

#Window Conf
WIDTH = 640
HEIGHT = 480
BEGIN = 10

#Initialization
pygame.init()
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tower of Hanoi')

#Settings
FPS = 30
fpsClock = pygame.time.Clock()

#Colors
BLACK = pygame.Color(0, 0, 0)
PINK = pygame.Color(255, 192, 192)
WHITE = pygame.Color(255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

DISPLAYSURF.fill(BLACK)

#Write Text
fontObj = pygame.font.Font('freesansbold.ttf', 20)
textSurfaceObj = fontObj.render('Tower of Hanoi Level: 1', True, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (320, 20)

#pygame.draw.circle(DISPLAYSURF, PINK, (x, y), 10)
while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.quit()

    pygame.display.update()
    fpsClock.tick(FPS)
