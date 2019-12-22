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

    error_addrInvalid = display.menu.UItools.Page("_error__addrInvalid")

    set_success = display.menu.UItools.Page("_set__success")

    server_menu = display.menu.UItools.Page("server_menu")

    UI.add_pages( [press_any_key, main_menu,connect_server , server_menu,\
        error_addrInvalid, set_success] )


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
    def de_activation(Input_boxes):#static_method
        for box in Input_boxes:
            box.active = False
            box.frame_thickness = 0
            box.draw_button_surface()

    def type_in(self, event):#key_func
        if event.key == K_RETURN:
            de_activation(self.Input_boxes)
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
        de_activation(self.page.Input_boxes)
        self.active = True
        self.text = ""
        self.frame_thickness = 20
        self.draw_button_surface()

    def set_addr(self):#collide_func
        self.addr = ""
        for box in self.page.Input_boxes:
            self.addr += ('.' + box.text)
        self.addr = self.addr[1:]
        try:
            connection.connect.set_server_addr(self.addr)
            self.UI.flag = self.UI.pages["_set__success"]
        except ValueError:
            self.UI.flag = self.UI.pages["_error__addrInvalid"]

    def UI_quit(self):
        self.UI.shutdown()


    connect_server.key_func = type_in

    connect_server.Input_boxes = []

    for i in range(4):
        name = "Inupt_box" + str(i)

        box = display.menu.UItools.Button(name,\
            text           = ""                                            ,\
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
        display.menu.UItools.Button("set",\
            text             = "Set Server Address"              ,\
            rect             = pygame.Rect((650,500), (700,100)) ,\
            collide_func     = set_addr                          ,\
            text_color       = (15,0,0)                          ,\
            background_color = (127,0,0)                         ,\
            frame_color      = (0,0,0)                           ,\
            frame_thickness  = 10                 
        )
    )

    connect_server.add_button(
        display.menu.UItools.Button("start",\
            text             = "Start Game"                      ,\
            rect             = pygame.Rect((750,650), (500,100)) ,\
            collide_func     = UI_quit                           ,\
            text_color       = (15,0,0)                          ,\
            background_color = (127,0,0)                         ,\
            frame_color      = (0,0,0)                           ,\
            frame_thickness  = 10                 
        )
    )

    connect_server.add_button(
        display.menu.UItools.Button("back",\
            text             = "Back"                            ,\
            rect             = pygame.Rect((850,800), (300,100)) ,\
            flag             = main_menu                         ,\
            text_color       = (15,0,0)                          ,\
            background_color = (127,0,0)                         ,\
            frame_color      = (0,0,0)                           ,\
            frame_thickness  = 10
        )
    )
    #CONNECT_SERVER


    #_ERROR__ADDRINVALID
    def loadBufAddr(self):#update_func
        self.buttons["xxxInvalid"].text =\
            connect_server.buttons["set"].addr + " is not a valid address."
        self.buttons["xxxInvalid"].draw_button_surface()

    error_addrInvalid.update_func = loadBufAddr

    error_addrInvalid.add_button(
        display.menu.UItools.Button("xxxInvalid",\
            rect = pygame.Rect((400,300), (1200,100)) ,\
            text_color       = (15,0,0)              ,\
            background_color = (127,0,0)             ,\
            frame_color      = (0,0,0)               ,\
            frame_thickness  = 10
        )
    )

    error_addrInvalid.add_button(
        display.menu.UItools.Button("back",\
            text             = "Back"                            ,\
            rect             = pygame.Rect((850,500), (300,100)) ,\
            flag             = connect_server                    ,\
            text_color       = (15,0,0)                          ,\
            background_color = (127,0,0)                         ,\
            frame_color      = (0,0,0)                           ,\
            frame_thickness  = 10
        )
    )
    #_ERROR__ADDRINVALID


    #_SET__SUCCESS
    def loadBufAddr(self):#update_func
        self.buttons["xxxSuccess"].text =\
            "Server address set to: " + connect_server.buttons["set"].addr
        self.buttons["xxxSuccess"].draw_button_surface()

    set_success.update_func = loadBufAddr

    set_success.add_button(
        display.menu.UItools.Button("xxxSuccess",\
            rect = pygame.Rect((400,300), (1200,100)) ,\
            text_color       = (15,0,0)              ,\
            background_color = (127,0,0)             ,\
            frame_color      = (0,0,0)               ,\
            frame_thickness  = 10
        )
    )

    set_success.add_button(
        display.menu.UItools.Button("back",\
            text             = "Back"                            ,\
            rect             = pygame.Rect((850,500), (300,100)) ,\
            flag             = connect_server                    ,\
            text_color       = (15,0,0)                          ,\
            background_color = (127,0,0)                         ,\
            frame_color      = (0,0,0)                           ,\
            frame_thickness  = 10
        )
    )
    #_SET__SUCCESS


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
