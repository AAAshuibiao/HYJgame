if __name__ == "__main__": raise SystemError("Incorrect starting file")

import sys
import pygame

import display

def loadpics(route, namelist):
    for name in namelist:
        display.picbuf[name] =\
            pygame.image.load(route + name).convert_alpha()
