__author__ = 'plaix'
import sys

try:
    import pygame
    import os
    from pygame.locals import *
except ImportError as err:
    print("Couldnt load module %s" % (err))
    sys.exit(3)

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data/')


def load_image(name):
    """ Load image and return image object """
    fullname = DATA_PATH + name
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print("Cannot load image %s" % fullname)
        raise SystemExit(message)
    return image, image.get_rect()
