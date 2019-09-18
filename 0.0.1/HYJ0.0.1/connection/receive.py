if __name__ == "__main__": raise SystemError("Incorrect starting file")

import socket
import threading
import time

import connection

command_list = "Server not connected"
last_receive_time = time.time()

def receiver_func():
    global command_list
    global last_receive_time

    while True:
        if connection.server_addr != "Undefined": break
        time.sleep(0.001)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind( ("0.0.0.0", 9912) )

    while True:
        try:
            data, address = s.recvfrom(1024)
            last_receive_time = time.time()
            data_string = str(data, 'ascii')

            command_parts = data_string.split(':')
            command = command_parts[0]
            content = command_parts[1]
            ID = command_parts[2]

            if command == "ACCEPTCONNECT":
                connection.ID = ID
                command_list = []
                continue

            if address == (connection.server_addr, 8001) and\
                    ID == connection.ID and command_list != "Server not connected":
                command_list.append( (command, content) )
        except IndexError:
            print("WARNING:Command syntax invalid", data_string)
        

receiver=threading.Thread(target=receiver_func, name='receiver')
receiver.start()
