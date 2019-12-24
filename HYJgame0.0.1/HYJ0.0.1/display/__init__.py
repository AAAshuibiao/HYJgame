#raise an error when starting from this file
if __name__ == "__main__": raise SystemError("Incorrect starting file")

# to do:
#   change UI structure, combine "Pic" and "Button", REDO update logic, seperate display and update   //doing
#   change "UI_Script" design, stucturelize it as like JSON or Java class define or something better   //doing

#   try using pygame.sprite.Sprite to do the class PicLayer   //not sure

#   make the UI.json design to 100% program_generate   // waiting
#   implicitly do draw_button_surface   //not sure
#   make a git_ignored, local saved setting system   //waiting

#bug_fix:
#   text_color may not working

#imports
import pygame

import display

#load submodules
__all__ = ["load"]
from display import *

#version
version = "0.0.1"

#load settings
settings = display.load.settings()

#initialize screen
screen = display.load.screen()
