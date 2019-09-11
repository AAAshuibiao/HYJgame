if __name__ == "__main__": raise SystemError("Incorrect starting file")

import time

import connection

def wait_server_connected(timeoutsecs = 10):
    addr = connection.server_addr
    try:
        assert len(addr.split('.')) == 4
        for ap in addr.split('.'):
            assert ap.isnumeric() and 0<=int(ap)<256
    except AssertionError:
        raise ValueError("Invalid server address")
    for t in range(timeoutsecs*10):
        accepted = False
        if t%10 == 0: connection.send.server_connect_request(t//10)
        if t==timeoutsecs*10-1: raise TimeoutError("Server connect timeout")
        if connection.receive.command_list != "Server not connected":
            for command in connection.receive.command_list:
                if command.split(':')[0] == "ACCEPTCONNECT":
                    accepted = True
                if command.split(':')[0] == "REJECTCONNECT": raise SystemError("Server connect rejected\nReason:"+command.split(':')[1])
        if accepted: break
        time.sleep(0.1)
