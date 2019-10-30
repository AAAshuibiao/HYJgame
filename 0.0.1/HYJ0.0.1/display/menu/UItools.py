if __name__ == "__main__": raise SystemError("Incorrect starting file")

import os
import sys
import types

import pygame

import display


def load_pic_via_names(route, namelist):
    for name in namelist:
        display.picbuf[ os.path.splitext(name)[0] ]\
        =pygame.image.load(route + name).convert_alpha()


def print_text(text,\
        rect      = None,\
        rect_func = None,\
        color     = None,\
        surface   = None):

    if type(text) != str:
        text = str(text)

    if not color:
        color = pygame.Color(0,0,0)
    elif type(color) == tuple:
        color = pygame.Color(color)
    
    text_surface = display.font.render(text, True, color)

    rect = pygame.Rect((0,0), text_surface.get_size())
    
    if rect_func:
        rect = rect_func(rect)
        text_surface = pygame.transform.scale(text_surface, rect.size)

    if not surface:
        return text_surface

    surface.blit(text_surface, rect.topleft)
    

class Pic(object):
    def __init__(self, name, surface, rect = None, poz = None):
        self.name = str( name )

        if rect:
            self.rect = rect
            self.surface = pygame.transform.scale(surface, rect.size)

        else:
            self.surface = surface
            self.rect = pygame.Rect(poz, surface.get_size())

        self.position = self.rect.topleft
        self.velocity = (0,0)
        
        self.UI = None

    def update(self):
        if self.velocity != (0,0):
            self.position = ( 
                self.position[0] + self.velocity[0] ,\
                self.position[1] + self.velocity[1]
            )
            self.rect.lefttop = self.position

        self.UI.screen.blit(self.surface, self.rect.topleft)


class Button(object):
    def __init__(self, name,\
    text             = ""                          ,\
    poz              = None                        ,\
    rect             = pygame.Rect((0,0), (0,0))   ,\
    flag             = None                        ,\
    collide_func     = None                        ,\
    surface          = None                        ,\
    background_pic   = None                        ,\
    text_func        = "Fill"                      ,\
    text_color       = pygame.Color(0,0,0)         ,\
    background_color = pygame.Color(255,255,255)   ,\
    frame_color      = pygame.Color(0,0,0)         ,\
    frame_thickness  = 0                           ):

        self.name             = str( name )
        self.text             = str( text )
        self.flag             = flag
        self.collide_func     = collide_func
        self.background_pic   = background_pic
        self.text_func        = text_func
        self.text_color       = self.color_fomatting( text_color )
        self.background_color = self.color_fomatting( background_color )
        self.frame_color      = self.color_fomatting( frame_color )
        self.frame_thickness  = frame_thickness
        self.UI               = None

        if surface:
            if rect:
                self.rect = rect
                self.surface = pygame.transform.scale(surface, rect.size)
            else:
                self.surface = surface
                self.rect = pygame.Rect(poz, surface.get_size())
        else:
            self.rect = rect
            self.surface = pygame.Surface( self.rect.size )
            self.draw_button_surface()

    @staticmethod
    def color_fomatting(color):
        if type(color) == pygame.Color: return color
        elif type(color) == tuple:
            return pygame.Color(*color)
        else: raise ValueError

    def draw_button_surface(self):
        if self.background_pic:
            self.surface.blit(
                pygame.transform.scale(
                    self.background_pic, self.rect.size
                ), (0,0)
            )
        else:
            self.surface.fill(self.background_color)

        button_frame_rect = self.rect.copy()
        button_frame_rect.topleft = (0,0)

        if self.frame_thickness != 0:
            pygame.draw.rect(self.surface, self.frame_color,\
                button_frame_rect, self.frame_thickness)
        
        if self.text != "":
            if type(self.text_func) == types.FunctionType:
                print_text(self.text           ,\
                    rect_func = self.text_func ,\
                    surface = self.surface 
                )

            elif self.text_func == "Fill":
                def fill(rect):#text_func
                    rect.height = self.rect.height
                    rect.width = self.rect.width
                    return rect

                print_text(self.text       ,\
                    rect_func = fill       ,\
                    surface = self.surface
                )
            
            elif self.text_func == "Align":
                def align_bottom(rect):#text_func
                    rect.width *= rect.height / self.rect.height
                    rect.height = self.rect.height
                    return rect
            
                print_text(self.text         ,\
                    rect_func = align_bottom ,\
                    surface = self.surface   ,\
                )
            
            else:
                raise ValueError("text_func NOT FOUND")


    def collide(self, poz):
        if self.rect.collidepoint(poz):

            if self.collide_func != None:
                self.collide_func(self)

            if self.flag != None:
                self.UI.flag = self.flag

            return True
        return False

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
        self.click_blank_func = None
    
    def add_pic(self, pic):
        pic.UI = self.UI
        pic.page = self
        self.pics[pic.name] = pic

    def add_button(self, button):
        button.UI = self.UI
        button.page = self
        self.buttons[button.name] = button

    def remove_pic(self, name):
        del self.pics[name]

    def remove_button(self, name):
        del self.buttons[name]

    def collide(self, poz):
        for buttonName in self.buttons:
            button = self.buttons[buttonName]
            if button.collide(poz):
                break
        else:
            if self.click_blank_func:
                self.click_blank_func()

    def key_down(self,key_event):
        if self.key_func != None:
            self.key_func(self, key_event)

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
        self.end = False

    def shutdown(self):
        self.flag = None
        self.end = True

    def add_page(self, page):
        page.UI = self
        self.pages[page.name] = page
        if self.flag == None:
            self.flag = page

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
