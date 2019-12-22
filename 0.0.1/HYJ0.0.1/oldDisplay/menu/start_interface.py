if __name__ == "__main__": raise SystemError("Incorrect starting file")

import os
import time
import sys

import pygame
from pygame.locals import *

import display


def loadpics(piclist = []):
    directory = sys.path[0] + "\\display\\texture\\"\
    +  display.texture_pack + "\\"

    if not piclist:
        for filename in os.listdir(directory):
            if os.path.isfile( directory + filename )\
            and os.path.splitext(filename)[1] == ".jpg"\
            or  os.path.splitext(filename)[1] == ".png":
                piclist.append(filename)
    
    display.menu.UItools.load_pic_via_names(directory, piclist)


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
