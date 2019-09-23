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

    UI = display.menu.UItools.UI("start_interface", display.screen)

    press_any_key = display.menu.UItools.Page("press_any_key")

    main_menu = display.menu.UItools.Page("main_menu")

    UI.add_pages( [press_any_key, main_menu] )

    press_any_key.add_pic(
        display.menu.UItools.Pic(
            "Unnamed", display.menu.UItools.print_text(
                "press any key to start..", size = 0.5
            ), poz = (800,1000)
        )
    )

    main_menu.add_button(
        display.menu.UItools.Button(
            "back", "Back", pygame.Rect((500,500), (200,100)), press_any_key
        )
    )

    while True:
        loop_start_time = time.time()

        screen.blit(display.picbuf["BG"], (0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    UI.flag = main_menu
            
            if event.type == MOUSEBUTTONDOWN:
                mouse_poz = pygame.mouse.get_pos()
                UI.flag.collide(mouse_poz)
                #print(mouse_poz) #temp

        UI.update()
        
        pygame.display.update()

        while time.time()-loop_start_time < (1/30): time.sleep(0.001)


def run():
    loadpics()
    main_loop()
