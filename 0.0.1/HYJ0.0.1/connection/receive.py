if __name__ == "__main__": raise SystemError("Incorrect starting file")

import socket
import threading
import time

import connection

command_list = "Server not connected"

def receiver_func():
    global command_list

    while True:
        if connection.server_addr != "Undefined": break
        time.sleep(0.1)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind( ("127.0.0.1", 9912) )
    command_list = []

    while True:
        data, addr = s.recvfrom(1024)
        if addr == (connection.server_addr,8001):
            data_string = str(data, 'ascii')
            command_list.append(data_string)

receiver=threading.Thread(target=receiver_func,name='receiver')
receiver.start()
