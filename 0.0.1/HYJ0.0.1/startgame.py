import time

import connection

if connection.server_addr == "Undefined":
    print("input the server address:", end = '')
    connection.server_addr = str( input() )

connection.connect.wait_server_connected()

while True:
    print(connection.receive.command_list)
