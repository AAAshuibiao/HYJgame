if __name__ == "__main__": raise SystemError("Incorrect starting file")

import socket
import threading
import time

import connection

command_list = []

def receiver_func():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind( ("0.0.0.0", 8000) )

    while True:
        data, address = s.recvfrom(1024)
        addr = address[0]

        data_string = str(data, "ascii")
        print(data_string)#temp
        command_parts = data_string.split(':')

        if address[1] == 10123 and command_parts[4] == "judgelight":
            address[0] = command_parts[3]
            address[1] = 9999

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

        except (SystemError, AssertionError):
            print("WARNING:Unexpected connection")
            continue

        command = content = ID = ''

        try:
            command = command_parts[0]
            content = command_parts[1]
            ID = command_parts[2]
        except (IndexError ,ValueError):
            print("WARNING:Command syntax invalid: " + data_string)
            continue

        try:
            connection.users[ID].command_list.append( (command, content) )
            connection.users[ID].last_receive_time = time.time()
        except KeyError:
            print("WARNING:Command ID invalid: " + data_string)


receiver=threading.Thread(target=receiver_func,name='receiver')
receiver.start()
