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


def main_loop():
    pygame.display.set_icon(display.picbuf["Icon"])
    screen = display.screen
    flag = "press_any_key"
    
    while True:
        loop_start_time = time.time()

        screen.blit(display.picbuf["BG"], (0,0))

        if flag == "press_any_key":
            display.menu.UItools.print_text(
                "Press any key to start...", (800,1000), size = 0.3
            )

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: sys.exit()
                else:
                    if flag == "press_any_key":
                        flag = "menu"
            
            if event.type == MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

        pygame.display.update()

        while time.time()-loop_start_time < (1/30): time.sleep(0.001)


def run():
    loadpics()
    main_loop()
