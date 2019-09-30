if __name__ == "__main__": raise SystemError("Incorrect starting file")

import pygame

import display

def load_UI():
    UI = display.menu.UItools.UI_class("start_interface", display.screen)

    press_any_key = display.menu.UItools.Page("press_any_key")

    main_menu = display.menu.UItools.Page("main_menu")

    server_menu = display.menu.UItools.Page("server_menu")

    UI.add_pages( [press_any_key, main_menu, server_menu] )


    #PERSS_ANY_KEY
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
            text_color = (15,0,0)        ,\
            background_color = (127,0,0) ,\
            frame_color = (0,0,0)        ,\
            frame_thickness = 10
        )
    )

    main_menu.add_button(
        display.menu.UItools.Button(
            "server", "Server", pygame.Rect((850,500), (300,100)),\
            flag = server_menu,\
            text_color = (15,0,0)        ,\
            background_color = (127,0,0) ,\
            frame_color = (0,0,0)        ,\
            frame_thickness = 10
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


    #SERVER_MENU
    server_menu.add_button(
        display.menu.UItools.Button(
            "server_start", "Start Local Server", pygame.Rect((600,300), (750,100)),\
            text_color = (15,0,0)        ,\
            background_color = (127,0,0) ,\
            frame_color = (0,0,0)        ,\
            frame_thickness = 10
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
