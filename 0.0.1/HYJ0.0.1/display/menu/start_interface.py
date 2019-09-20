if __name__ == "__main__": raise SystemError("Incorrect starting file")

import time
import sys
import pygame
from pygame.locals import *

import display

def loadpics():
    route = sys.path[0] + "\\display\\texture\\" + display.texture_pack + "\\"
    piclist = ["BG.jpg", "Icon.png"]
    display.menu.UItools.loadpics(route, piclist)

def mainloop():
    pygame.display.set_icon(display.picbuf["Icon"])
    screen = display.screen
    
    while True:
        loop_start_time = time.time()

        screen.blit(display.picbuf["BG"], (0,0))

        for event in pygame.event.get():
            if event.type == QUIT: sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: sys.exit()


        pygame.display.update()

        while time.time()-loop_start_time < (1/30): time.sleep(0.001)

def run():
    loadpics()
    mainloop()
