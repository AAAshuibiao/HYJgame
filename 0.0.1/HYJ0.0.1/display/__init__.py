if __name__ == "__main__": raise SystemError("Incorrect starting file")

import pygame
from pygame.locals import FULLSCREEN

WINDOWED = 0

#//user config zone:
screen_size = (1920,1080)
texture_pack = "standard"
screen_mode = WINDOWED
#//end user config zone

pygame.init()
pygame.display.set_caption("HYJ0.0.1")
screen = pygame.display.set_mode(screen_size, screen_mode, 32)

picbuf = {}

__all__ = ["menu","game"]
from display import *
