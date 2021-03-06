__author__ = 'plaix'
# Version 0.1
# Tower of Hanoi by Sotaya
# __________________________________________________________
import sys

try:
    import pygame
    import os
    from lib import load_image
    from pygame.locals import *
except ImportError as err:
    print("Couldnt load module %s" % err)
    sys.exit(3)

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data/')

# Window Conf
WIDTH = 540
HEIGHT = 380
BEGIN = 10

# Initialization
pygame.init()
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tower of Hanoi')

# ___________________________________________________________

# Settings
FPS = 30
fpsClock = pygame.time.Clock()

# ___________________________________________________________

# Colors
BLACK = pygame.Color(0, 0, 0)
PINK = pygame.Color(255, 192, 192)
WHITE = pygame.Color(255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

# DISPLAYSURF.fill(BLACK)

# Write Text
fontObj = pygame.font.Font('freesansbold.ttf', 15)
textSurfaceObj = fontObj.render('Tower of Hanoi Level: 1', True, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (WIDTH / 2, 20)

# ---------------------------------------------------------------
# Objects and variables
towers_x = 20
towers_y = 200
disks_x = 15
disks_y = 320
TOWER_1 = load_image('tower.png')
TOWER_2 = load_image('tower.png')
TOWER_3 = load_image('tower.png')
DISK_1 = load_image('disk.png')
TOWER_1[1].y = towers_y
TOWER_2[1].y = towers_y
TOWER_3[1].y = towers_y
TOWER_1[1].x = towers_x
TOWER_2[1].x = towers_x + 200
TOWER_3[1].x = towers_x + 400
DISK_1[1].x = disks_x
DISK_1[1].y = disks_y


# ------------------------------------------------------------
# Game Loop
# pygame.draw.circle(DISPLAYSURF, PINK, (x, y), 10)
disk = None
tower1 = None
tower2 = None
tower3 = None
held = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if disk.collidepoint(pygame.mouse.get_pos()):
                held = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if DISK_1[1].colliderect(TOWER_2[1]):
                disks_x = TOWER_2[1].x
            elif DISK_1[1].colliderect(TOWER_3[1]):
                disks_x = TOWER_3[1].x
            elif DISK_1[1].colliderect(TOWER_1[1]):
                disks_x = TOWER_1[1].x
            DISK_1[1].x = disks_x
            DISK_1[1].y = disks_y
            held = False
        if held:
            DISK_1[1].x, DISK_1[1].y = pygame.mouse.get_pos()

    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    tower1 = DISPLAYSURF.blit(TOWER_1[0], TOWER_1[1])
    tower2 = DISPLAYSURF.blit(TOWER_2[0], TOWER_2[1])
    tower3 = DISPLAYSURF.blit(TOWER_3[0], TOWER_3[1])
    disk = DISPLAYSURF.blit(DISK_1[0], DISK_1[1])
    pygame.display.update()
    fpsClock.tick(FPS)
