if __name__ == "__main__": raise SystemError("Incorrect starting file")

import sys
import pygame

import display

def loadpics(route, namelist):
    for name in namelist:
        display.picbuf[name.split(".")[0]] =\
            pygame.image.load(route + name).convert_alpha()

def print_text(text, poz, color = pygame.Color(0,0,0), size = None):
    if type(text) != str: text = str(text)

    FS = display.font.render(text, True, color)

    if type(size) == int or type(size) == float:
        size = ( int(size*FS.get_size()[0]) , int(size*FS.get_size()[1]) )

    if size: FS = pygame.transform.scale(FS, size)

    display.screen.blit(FS, poz)
