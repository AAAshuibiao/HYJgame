#raise an error when starting from this file
if __name__ == "__main__": raise SystemError("Incorrect starting file")

#imports
import os
import time
import sys

import pygame
from pygame.locals import *

import display


def main_loop():
    pygame.display.set_icon(display.picbuf["Icon"])
    screen = display.screen

    UI = display.menu.UI_script.load_UI()

    while True:
        loop_start_time = time.time()

        screen.blit(display.picbuf["BG"], (0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                else:
                    UI.flag.key_down(event)
            
            if event.type == MOUSEBUTTONDOWN:
                mouse_poz = pygame.mouse.get_pos()
                UI.flag.collide(mouse_poz)

        UI.update()
        
        pygame.display.update()

        if UI.end:
            break

        while time.time()-loop_start_time < (1/display.frame_rate):
            time.sleep(0.001)


def run():
    loadpics()
    main_loop()
