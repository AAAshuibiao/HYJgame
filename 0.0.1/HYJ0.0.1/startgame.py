import time

import command
import connection

connection.connect.wait_server_connected()

count = 0

time.sleep(1)
while True:
    loop_start_time = time.time()

    command.execute.all()

    if count%100 == 0:
        connection.send.command("CALL", "Mr.Smith")

    count+=1
    
    TBR = time.time()

    while time.time()-loop_start_time < (1/300): pass
    
    print( (time.time()-TBR)*1000 )
