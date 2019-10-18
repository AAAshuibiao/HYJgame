try:
    import sys
    import time

    import pygame

    import command
    import connection
    import display

    display.menu.start_interface.run()

    connection.connect.wait_server_connected()


    while True:
        loop_start_time = time.time()

        command.execute.all()

        connection.connect.dog_check()
        
        while time.time()-loop_start_time < (1/300): pass
    

except SystemExit:
    pygame.quit()
    connection.receive.end = True

except Exception as error:
    pygame.quit()
    raise error
