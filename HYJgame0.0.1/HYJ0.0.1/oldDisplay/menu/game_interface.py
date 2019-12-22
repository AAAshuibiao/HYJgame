if __name__ == "__main__": raise SystemError("Incorrect starting file")

import sys
import time

import pygame
from pygame.locals import *

import command
import connection
import display


def main_loop():
    pics = display.menu.PLtools.PicPool()
    screen = display.screen

    while True:
        loop_start_time = time.time()

        connection.connect.dog_check()

        command.execute.all()

        screen.fill( display.Game_BG_Color )

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return 0

        pygame.display.update()

        while time.time()-loop_start_time < (1/display.frame_rate):
            time.sleep(0.001)


def run():
    main_loop()
