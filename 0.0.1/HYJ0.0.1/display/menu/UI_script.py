if __name__ == "__main__": raise SystemError("Incorrect starting file")

import pygame

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
    def goto_main_menu(self, key):
        print(key)
        self.UI.flag = main_menu

    press_any_key.key_func = goto_main_menu

    press_any_key.add_pic(
        display.menu.UItools.Pic(
            "PAK", display.menu.UItools.print_text(
                "press any key to start..", size = 0.5
            ), poz = (800,1000)
        )
    )
    #PERSS_ANY_KEY


    #MAIN_MENU
    main_menu.add_button(
        display.menu.UItools.Button(
            "start", "Start", pygame.Rect((850,350), (300,100)),\
            flag             = connect_server,\
            text_color       = (15,0,0)        ,\
            background_color = (127,0,0) ,\
            frame_color      = (0,0,0)        ,\
            frame_thickness  = 10
        )
    )

    main_menu.add_button(
        display.menu.UItools.Button(
            "server", "Server", pygame.Rect((850,500), (300,100)),\
            flag             = server_menu,\
            text_color       = (15,0,0)        ,\
            background_color = (127,0,0) ,\
            frame_color      = (0,0,0)        ,\
            frame_thickness  = 10
        )
    )

    main_menu.add_button(
        display.menu.UItools.Button(
            "back", "Back", pygame.Rect((850,850), (300,100)),\
            flag             = press_any_key ,\
            text_color       = (15,0,0)      ,\
            background_color = (127,0,0)     ,\
            frame_color      = (0,0,0)       ,\
            frame_thickness  = 10
        )
    )

    main_menu.add_button(
        display.menu.UItools.Button(
            "settings", "Settings", pygame.Rect((250, 250), (300,100)),\
            flag             = server_menu ,\
            text_color       = (15,0,0)      ,\
            background_color = (127,0,0)     ,\
            frame_color      = (0,0,0)       ,\
            frame_thickness  = 10                 
        )
    )

    #MAIN_MENU


    #CONNECT_SERVER
    connect_server.add_pic(
        display.menu.UItools.Pic(
            "Input_box0", display.picbuf["Input_box"],\
            rect = pygame.Rect((300,350), (300,100)),\
        )
    )

    connect_server.add_pic(
        display.menu.UItools.Pic(
            "Input_box1", display.picbuf["Input_box"],\
            rect = pygame.Rect((650,350), (300,100)),\
        )
    )

    connect_server.add_pic(
        display.menu.UItools.Pic(
            "Input_box2", display.picbuf["Input_box"],\
            rect = pygame.Rect((1000,350), (300,100)),\
        )
    )

    connect_server.add_pic(
        display.menu.UItools.Pic(
            "Input_box3", display.picbuf["Input_box"],\
            rect = pygame.Rect((1350,350), (300,100)),\
        )
    )

    connect_server.Input_boxes = []
    for i in range(4):
        connect_server.Input_boxes.append(
            connect_server.pics["Input_box"+str(i)]
        )

    connect_server.add_button(
        display.menu.UItools.Button(
            "back", "Back", pygame.Rect((850,850), (300,100)),\
            flag             = main_menu ,\
            text_color       = (15,0,0)      ,\
            background_color = (127,0,0)     ,\
            frame_color      = (0,0,0)       ,\
            frame_thickness  = 10
        )
    )
    #CONNECT_SERVER


    #SERVER_MENU
    server_menu.add_button(
        display.menu.UItools.Button(
            "server_start", "Start Local Server", pygame.Rect((600,350), (750,100)),\
            collide_func     = connection.connect.start_local_server,\
            text_color       = (15,0,0)        ,\
            background_color = (127,0,0) ,\
            frame_color      = (0,0,0)        ,\
            frame_thickness  = 10
        )
    )

    server_menu.add_button(
        display.menu.UItools.Button(
            "back", "Back", pygame.Rect((850,650), (300,100)),\
            flag             = main_menu ,\
            text_color       = (15,0,0)      ,\
            background_color = (127,0,0)     ,\
            frame_color      = (0,0,0)       ,\
            frame_thickness  = 10
        )
    )
    #SERVER_MENU

    return UI
