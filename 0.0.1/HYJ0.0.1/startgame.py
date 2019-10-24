try:
    import sys
    import time

    import pygame

    import connection
    import command
    import display

    while True:
        display.menu.start_interface.run()

        connection.connect.wait_server_connected()

        display.game.game_interface.run()

except SystemExit:
    pygame.quit()
    connection.receive.end = True

except Exception as error:
    pygame.quit()
    raise error
