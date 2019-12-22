try:
    #imports
    import sys
    import time

    import pygame

    import connection
    import command
    import display

    while True:
        pass
        #display.menu.start_interface.run()

        #connection.connect.wait_server_connected()

        #display.menu.game_interface.run()

#normal quit
except SystemExit:
    pygame.quit()
    connection.receive.end = True

#close display and connection before catching error
except Exception as error:
    pygame.quit()
    connection.receive.end = True
    raise error
