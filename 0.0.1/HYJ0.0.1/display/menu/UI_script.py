if __name__ == "__main__": raise SystemError("Incorrect starting file")

import pygame
from pygame.locals import *

import connection
import display

def load_UI():
    UI = display.menu.UItools.UI_class("start_interface", display.screen)

    press_any_key = display.menu.UItools.Page("press_any_key")

    main_menu = display.menu.UItools.Page("main_menu")

    connect_server = display.menu.UItools.Page("connect_server")

    server_menu = display.menu.UItools.Page("server_menu")

    UI.add_pages( [press_any_key, main_menu,connect_server , server_menu] )


    #PERSS_ANY_KEY
    def goto_main_menu(self, key):#key_func
        self.UI.flag = main_menu

    def scale_half(rect):#text_func
        rect.height *= 0.5
        rect.width *= 0.5
        return rect

    press_any_key.key_func = goto_main_menu

    press_any_key.add_pic(
        display.menu.UItools.Pic(
            "PAK", display.menu.UItools.print_text(
                text      = "press any key to start.." ,\
                rect_func = scale_half                 ,\
            ),  poz       = (800,1000)
        )
    )
    #PERSS_ANY_KEY


    #MAIN_MENU
    main_menu.add_button(
        display.menu.UItools.Button("start",\
            text             = "Start"                           ,\
            rect             = pygame.Rect((850,350), (300,100)) ,\
            flag             = connect_server                    ,\
            text_color       = (15,0,0)                          ,\
            background_color = (127,0,0)                         ,\
            frame_color      = (0,0,0)                           ,\
            frame_thickness  = 10
        )
    )

    main_menu.add_button(
        display.menu.UItools.Button("server",\
            text             = "Server"                          ,\
            rect             = pygame.Rect((850,500), (300,100)) ,\
            flag             = server_menu                       ,\
            text_color       = (15,0,0)                          ,\
            background_color = (127,0,0)                         ,\
            frame_color      = (0,0,0)                           ,\
            frame_thickness  = 10
        )
    )

    main_menu.add_button(
        display.menu.UItools.Button("back",\
            text             = "Back"                            ,\
            rect             = pygame.Rect((850,850), (300,100)) ,\
            flag             = press_any_key                     ,\
            text_color       = (15,0,0)                          ,\
            background_color = (127,0,0)                         ,\
            frame_color      = (0,0,0)                           ,\
            frame_thickness  = 10
        )
    )

    main_menu.add_button(
        display.menu.UItools.Button("settings",\
            text             = "Settings"                         ,\
            rect             = pygame.Rect((850, 650), (300,100)) ,\
            text_color       = (15,0,0)                           ,\
            background_color = (127,0,0)                          ,\
            frame_color      = (0,0,0)                            ,\
            frame_thickness  = 10                 
        )
    )
    #MAIN_MENU


    #CONNECT_SERVER
    def type_in(self, event):#key_func
        if event.key == K_RETURN:
            for box in self.Input_boxes:
                box.active = False
            return
        
        for box in self.Input_boxes:
            if not box.active:
                continue
            if event.key == K_BACKSPACE:
                box.text = box.text[0:-1]
            else:
                box.text += event.unicode
            box.draw_button_surface()

    def activation(self):#collide_func
        for box in self.page.Input_boxes:
            box.active = False
        self.active = True

    connect_server.key_func = type_in

    connect_server.Input_boxes = []

    for i in range(4):
        name = "Inupt_box" + str(i)

        box = display.menu.UItools.Button(name,\
            text           = ""                                         ,\
            rect           = pygame.Rect((300 + (350*i) , 350), (300,100)) ,\
            collide_func   = activation                                    ,\
            background_pic = display.picbuf["Input_box"]                   ,\
        )

        def center(rect):#text_func
            rect.height *= 1.2
            rect.width *= 1.2
            rect.centery = box.rect.height / 2
            rect.centerx = box.rect.width / 2
            return rect

        box.text_func=center

        box.active = False

        connect_server.add_button(box)
        connect_server.Input_boxes.append(box)

    connect_server.add_button(
        display.menu.UItools.Button("settings",\
            text             = "Settings"                         ,\
            rect             = pygame.Rect((850, 650), (300,100)) ,\
            text_color       = (15,0,0)                           ,\
            background_color = (127,0,0)                          ,\
            frame_color      = (0,0,0)                            ,\
            frame_thickness  = 10                 
        )
    )

    connect_server.add_button(
        display.menu.UItools.Button("back",\
            text             = "Back"                            ,\
            rect             = pygame.Rect((850,850), (300,100)) ,\
            flag             = main_menu                         ,\
            text_color       = (15,0,0)                          ,\
            background_color = (127,0,0)                         ,\
            frame_color      = (0,0,0)                           ,\
            frame_thickness  = 10
        )
    )
    #CONNECT_SERVER


    #SERVER_MENU
    server_menu.add_button(
        display.menu.UItools.Button("server_start",\
            text             = "Start Local Server"                  ,\
            rect             = pygame.Rect((600,350), (750,100))     ,\
            collide_func     = connection.connect.start_local_server ,\
            text_color       = (15,0,0)                              ,\
            background_color = (127,0,0)                             ,\
            frame_color      = (0,0,0)                               ,\
            frame_thickness  = 10
        )
    )

    server_menu.add_button(
        display.menu.UItools.Button("back",\
            text             = "Back"                            ,\
            rect             = pygame.Rect((850,650), (300,100)) ,\
            flag             = main_menu                         ,\
            text_color       = (15,0,0)                          ,\
            background_color = (127,0,0)                         ,\
            frame_color      = (0,0,0)                           ,\
            frame_thickness  = 10
        )
    )
    #SERVER_MENU


    return UI
