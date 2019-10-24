if __name__ == "__main__": raise SystemError("Incorrect starting file")

import time

import command
import connection
import display

def main_loop():

    screen = display.screen

    while True:
        loop_start_time = time.time()

        command.execute.all()

        connection.connect.dog_check()
    
        while time.time()-loop_start_time < (1/display.frame_rate):
            time.sleep(0.001)

def run():
    main_loop()
