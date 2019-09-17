if __name__ == "__main__": raise SystemError("Incorrect starting file")

import time

import connection

def wait_server_connected():
    addr = connection.server_addr

    for t in range(connection.ASKCONNECT_timeout_msec+1):
        time.sleep(0.001)

        if t % connection.ASKCONNECT_send_interval == 0:
            connection.send.ask_connect_request(connection.playerName)
        
        if t==connection.ASKCONNECT_timeout_msec:
            raise TimeoutError("Server connect timeout")

        if connection.receive.command_list != "Server not connected": break
