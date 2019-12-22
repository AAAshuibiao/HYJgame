if __name__ == "__main__": raise SystemError("Incorrect starting file")

import pygame
from pygame.locals import FULLSCREEN

WINDOWED = 0

#//user config zone:
screen_size = (1920,1080)
frame_rate = 30
Game_BG_Color = (127,127,255)
screen_mode = WINDOWED  #WINDOWED or FULLSCREEN

texture_pack = "standard"
sound_pack = "standard"
font_pack = "ardestineopentype"
#font_pack = "lucidabright"

#//end user config zone

pygame.init()
font = pygame.font.SysFont(font_pack, 72)
pygame.display.set_caption("HYJ0.0.1")
screen = pygame.display.set_mode(screen_size, screen_mode, 32)

picbuf = {}

__all__ = ["menu", "UI"]
from display import *
