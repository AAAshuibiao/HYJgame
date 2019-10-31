if __name__ == "__main__": raise SystemError("Incorrect starting file")

import display

# to do:
#   change UI structure, combine "Pic" and "Button", REDO update logic, seperate display and update
#   change "UI_Script" design, stucturelize it as like JSON or Java class define or something better
#   or change the "UI_Script" design to 100% program_generate

#bug_fix:
#   text_color may not working

__all__ = ["UItools", "start_interface", "game_interface", "UI_script", "PLtools"]
from display.menu import *
