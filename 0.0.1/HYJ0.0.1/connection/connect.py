if __name__ == "__main__": raise SystemError("Incorrect starting file")

import os
import time

import connection


def set_server_addr(addr):
    if connection.Check_Address_Validity(addr):
        connection.server_addr = addr
    else:
        raise ValueError

def start_local_server(self = None):
    os.system( "start " + connection.local_server_path )

def dog_check():
    if time.time() - connection.receive.last_receive_time >= 1:
        connection.send.command("ECHO", "dog")
    if time.time() - connection.receive.last_receive_time >= 3:
        raise SystemError("Server connection lost")

def wait_server_connected():
    connection.receive.receiver.start()
    
    addr = connection.server_addr

    for t in range(connection.ASKCONNECT_timeout_msec+1):

        time.sleep(0.001)

        if t % connection.ASKCONNECT_send_interval == 0:
            connection.send.ask_connect_request(connection.playerName)
        
        if t==connection.ASKCONNECT_timeout_msec:
            raise TimeoutError("Server connect timeout")

        if connection.receive.command_list != "Server not connected":
            break
