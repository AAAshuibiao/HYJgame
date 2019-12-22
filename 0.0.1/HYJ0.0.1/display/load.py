#raise an error when starting from this file
if __name__ == "__main__": raise SystemError("Incorrect starting file")

#imports
import json

import pygame

#load settings from settings.json
def settings():
    #load json file
    settingsFile = open("settings.json", encoding = "utf8")
    settings = json.loads( settingsFile.read() )

    
