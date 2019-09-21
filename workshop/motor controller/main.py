"""
FILE: main.py
DESC: Motor controller obeys commands from sensors
"""

import board
import busio
from motor import DCMotor
from time import sleep
from pulseio import PWMOut

uart = busio.UART(None, board.RX, baudrate=9600)
left = PWMOut(board.D2)
right = PWMOut(board.D0)

left.duty_cycle = 30000 # int(0xffff * abs(0.5))

def stop():
    print("Stopping!")

    try:
        left.duty_cycle = 0
        right.duty_cycle = 0
    except Exception as e:
        print("Exception in stop(): " + e.args[0])
        pass


while True:
    data = uart.read(1)

    if data is not None:
        data_string = ''.join([chr(b) for b in data])
        print("DATA: " + data_string)

        if data_string == '*':
            pass
        elif data_string == 'X':
            stop()
        else:
            print("NOISE: " + data_string)

    # XXX
    sleep(1)
