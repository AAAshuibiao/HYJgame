if __name__ == "__main__": raise SystemError("Incorrect starting file")

import socket
import threading

import connection

command_list = []

def receiver_func():
    global command_list
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind( ("127.0.0.1", 8000) )

    while True:
        data, address = s.recvfrom(1024)
        addr = address[0]

        command_parts = str(data, "ascii").split(':')

        if command_parts[0] == "ASKCONNECT":
            connection.connect.accept(addr, command_parts[1])
            continue

        try:
            assert address[1] == 9999

            for user_ID in connection.users:
                user_addr = connection.users[user_ID].addr
                if addr == user_addr:
                    break
            else: raise SystemError

        except SystemError or AssertionError:
            print("WARNING:Unexpected connection")
            continue

        command = content = ID = ''

        try:
            command = command_parts[0]
            content = command_parts[1]
            ID = int(command_parts[2])
        except IndexError or ValueError:
            print("WARNING:Command syntax invalid")
            continue

        try:
            connection.users[ID].command_list.append( (command, content) )
        except KeyError:
            print("WARNING:Command ID invalid")


receiver=threading.Thread(target=receiver_func,name='receiver')
receiver.start()
