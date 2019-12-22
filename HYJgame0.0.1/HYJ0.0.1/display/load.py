#raise an error when starting from this file
if __name__ == "__main__": raise SystemError("Incorrect starting file")

#imports
import json

import pygame
import pygame.locals

import display

#load settings from settings.json
def settings():
    #load json file
    import sys
    print( sys.path )
    settingsFile = open("display", encoding = "utf8")
    settings = json.loads( settingsFile.read() )

    #check version
    assert settings["version"] == display.version

    #put screen_size into a tuple and convert to integers
    settings["screen_size"] = tuple( settings["screen_size"].split('*') )
    for i in range( len( settings["screen_size"] ) ):
        settings["screen_size"][i] = int( settings["screen_size"][i] )

    #convert screen_mode into pygame standard
    if settings["screen_mode"] == "windowed":
        settings["screen_mode"] = 0
    elif settings["screen_mode"] == "fullscreen":
        settings["screen_mode"] = pygame.locals.FULLSCREEN
    else:
        raise ValueError("settings.json: screen_mode invalid, use \"windowed\" or \"fullscreen\"")

    return settings
