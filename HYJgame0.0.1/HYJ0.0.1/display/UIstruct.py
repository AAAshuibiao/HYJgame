#raise an error when starting from this file
if __name__ == "__main__": raise SystemError("Incorrect starting file")


#imports
import pygame


#define the "Pic" class, used to hold a picLayer with it's kinetics
class Pic(object):
    #initialize the object with necessary information
    def __init__(self, name, surface ,\
            poz       = None     ,\
            rect      = None     ,\
            kinetics  = [[0,0]]  ,\
            eventFunc = None     ):

        #initialize the rect of this object
        if rect:
            self.rect = rect
            self.surface = pygame.transform.scale(surface, rect.size)
        elif poz:
            self.rect = pygame.Rect(poz, surface.size)
            self.surface = surface
        else:
            raise ValueError("both argument poz and rect is not given")

        #declare the name attibute
        self.name = name

        #decalre the attibute for kinetics calculation
        self.kinetics = kinetics

        #declare the attibute for event processing
        self.eventFunc = eventFunc
    
        #declare the attibute for owner indication
        self.page = None

    def event(self, event):
        if self.eventFunc:
            self.eventFunc(self, event)

    #update the velocity and the acceleration of the picLayer
    def update(self, blit = True):
        #do the kinetics calculation ( integration )
        for d in range( len(self.kinetics), 1, -1 ):
            for axis in [0,1]:
                self.kinetics[d-2][axis] += self.kinetics[d-1][axis]
        self.rect.top  += self.kinetics[0][0]
        self.rect.left += self.kinetics[0][1]

        #blit the picture
        if blit:
            self.blit()

    #blit the picLayer
    def blit(self):
        self.page.surface.blit( self.surface, self.rect.topleft )


#define the "Page" class, used to hold and use some picLayers
class Page(object):
    #initialize the object with necessary information
    def __init__(self, name):
        self.name = name
        self.picLayers = {}
