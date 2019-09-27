import time

import command
import connection
import display

display.menu.start_interface.run()

#connection.connect.wait_server_connected()

"""
loop_count = 1

while True:
    loop_start_time = time.time()

    command.execute.all()

    connection.connect.dog_check()

    if loop_count%10 == 0:
        display.update.game()

    loop_count += 1
    
    while time.time()-loop_start_time < (1/300): pass
"""
