__author__ = 'plaix'
try:
    import pygame
    import sys
    import os
    from pygame.locals import *
except ImportError, err:
    print "Couldnt load module %s" % (err)
    sys.exit(3)

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data/')

def load_image(name):
    """ Load image and return image object """
    fullname = DATA_PATH + name
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() == None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print "Cannot load image %s" % fullname
        raise SystemExit, message
    return image, image.get_rect()
