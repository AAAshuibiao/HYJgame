import time

import command
import connection

connection.connect.wait_server_connected()

loop_count = 1

while True:
    loop_start_time = time.time()

    command.execute.all()

    if loop_count%100 == 0:
        connection.send.command("CALL", "Mr.Smith")
        connection.send.command("ECHO", "Mars")

    connection.connect.dog_check()

    loop_count += 1
    
    while time.time()-loop_start_time < (1/300): pass
