if __name__ == "__main__": raise SystemError("Incorrect starting file")

import time

import connection

def wait_server_connected():
    addr = connection.server_addr

    try:
        assert len(addr.split('.')) == 4
        for ap in addr.split('.'):
            assert ap.isnumeric() and 0<=int(ap)<256
    except AssertionError:
        raise ValueError("Invalid server address")

    for t in range(connection.ASKCONNECT_timeout_msec+1):
        time.sleep(0.001)

        if t % connection.ASKCONNECT_send_interval == 0:
            connection.send.ask_connect_request(connection.playerName)
        
        if t==connection.ASKCONNECT_timeout_msec:
            raise TimeoutError("Server connect timeout")

        if connection.receive.command_list != "Server not connected":
            for command in connection.receive.command_list:
                if command.split(':')[0] == "ACCEPTCONNECT": break
                if command.split(':')[0] == "REJECTCONNECT":
                    raise SystemError("Server connect rejected\nReason:"+command.split(':')[1])
            else: continue
        break
