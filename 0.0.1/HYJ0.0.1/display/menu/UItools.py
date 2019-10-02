if __name__ == "__main__": raise SystemError("Incorrect starting file")

import os
import sys
import pygame

import display


def loadpics(route, namelist):
    for name in namelist:
        display.picbuf[ os.path.splitext(name)[0] ]\
        =pygame.image.load(route + name).convert_alpha()


def print_text(text, poz = None, color = pygame.Color(0,0,0), size = None, surface = "Not_given"):
    if type(text) != str: text = str(text)

    FS = display.font.render(text, True, color)

    if type(size) == int or type(size) == float:
        size = ( int(size*FS.get_size()[0]) , int(size*FS.get_size()[1]) )

    if size: FS = pygame.transform.scale(FS, size)

    if surface == "Not_given":
        return FS
    else: surface.blit(FS, poz)


class Pic(object):
    def __init__(self, name, surface, rect = None, poz = None):
        self.name = str( name )

        if rect: surface = pygame.transform.scale(surface, rect.size)
        self.surface = surface

        if not rect: rect = pygame.Rect(poz, surface.get_size())
        self.rect = rect
        
        self.UI = None

    def update(self):
        self.UI.screen.blit(self.surface, self.rect.topleft)


class Button(object):
    def __init__(self, name, text, rect            ,\
    flag             = None                        ,\
    collide_func     = None                        ,\
    text_color       = pygame.Color(0,0,0)         ,\
    background_color = pygame.Color(255,255,255)   ,\
    frame_color      = pygame.Color(0,0,0)         ,\
    frame_thickness  = 0                           ):

        self.name             = str( name )
        self.rect             = pygame.Rect( rect )
        self.text             = str( text )
        self.flag             = flag
        self.collide_func     = collide_func
        self.surface          = pygame.Surface( self.rect.size )
        self.text_color       = self.color_fomatting( text_color )
        self.background_color = self.color_fomatting( background_color )
        self.frame_color      = self.color_fomatting( frame_color )
        self.frame_thickness  = frame_thickness
        self.UI               = None

        self.init_button_surface()

    @staticmethod
    def color_fomatting(color):
        if type(color) == pygame.Color: return color
        elif type(color) == tuple:
            return pygame.Color(*color)
        else: raise ValueError

    def init_button_surface(self):
        surface = self.surface

        surface.fill(self.background_color)

        button_frame_rect = self.rect.copy()
        button_frame_rect.topleft = (0,0)

        pygame.draw.rect(surface, self.frame_color,\
            button_frame_rect, self.frame_thickness)

        print_text(self.text, (0,0), self.text_color,\
            self.rect.size, surface)

    def collide(self, poz):
        if self.rect.collidepoint(poz):

            if self.collide_func != None:
                self.collide_func(self)

            if self.flag != None:
                self.UI.flag = self.flag

    def update(self):
        self.UI.screen.blit(self.surface, self.rect.topleft)


class Page(object):
    def __init__(self, name):
        self.name = str( name )
        self.pics = {}
        self.buttons = {}
        self.UI = None
        self.update_func = None
        self.key_func = None
    
    def add_pic(self, pic):
        pic.UI = self.UI
        self.pics[pic.name] = pic

    def add_button(self, button):
        button.UI = self.UI
        self.buttons[button.name] = button

    def remove_pic(self, name):
        del self.pics[name]

    def remove_button(self, name):
        del self.buttons[name]

    def collide(self, poz):
        for buttonName in self.buttons:
            button = self.buttons[buttonName]
            button.collide(poz)

    def key_down(self,key):
        if self.key_func != None:
            self.key_func(self, key)

    def update(self):
        if self.update_func != None:
            self.update_func(self)

        for picName in self.pics:
            self.pics[picName].update()
        
        for buttonName in self.buttons:
            self.buttons[buttonName].update()


class UI_class(object):
    def __init__(self, name, screen):
        self.name = str( name )
        self.screen = screen
        self.flag = None
        self.pages = {}

    def add_page(self, page):
        page.UI = self
        self.pages[page.name] = page
        if self.flag == None: self.flag = page

    def remove_page(self, name):
        del self.pages[name]

    def add_pages(self, pages):
        for page in pages:
            self.add_page(page)

    def remove_pages(self, pages):
        for page in pages:
            self.remove_page(page)

    def update(self):
        if self.flag != None:
            self.flag.update()
