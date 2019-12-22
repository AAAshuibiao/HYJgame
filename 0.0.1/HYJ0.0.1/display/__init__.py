#raise an error when starting from this file
if __name__ == "__main__": raise SystemError("Incorrect starting file")

# to do:
#   change UI structure, combine "Pic" and "Button", REDO update logic, seperate display and update
#   change "UI_Script" design, stucturelize it as like JSON or Java class define or something better
#   or change the "UI_Script" design to 100% program_generate
#   implicitly do draw_button_surface
#   make a git_ignored, local saved setting system

#bug_fix:
#   text_color may not working

#imports
import pygame

#version
version = "0.0.1"

__all__ = ["loader"]
from display import *
