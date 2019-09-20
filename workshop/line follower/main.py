"""
FILE: main.py
DESC: CircuitPython solution for Trinket M0 3-sensor line-follower
"""

import board
import busio
from analogio import AnalogOut, AnalogIn
import time

threshold = 20000
left = AnalogIn(board.D0)
middle = AnalogIn(board.D1)
right = AnalogIn(board.D2)
uart = busio.UART(board.TX, board.RX, baudrate=115200)

while True:
    print("RIGHT: %0.2f" % right.value)
    print("MIDDLE: %0.2f" % middle.value)
    print("LEFT: %0.2f\n\n\n" % left.value)

    if middle.value>threshold and left.value<=threshold and right.value<=threshold:
        pass
    elif middle.value>threshold and left.value>threshold:
        uart.write("r")
    elif middle.value <= threshold and left.value > threshold:
        uart.write("R")
    elif middle.value > threshold and right.value > threshold:
        uart.write("l")
    elif middle.value <= threshold and right.value > threshold:
        uart.write("L")
    else:
        uart.write("S")

    time.sleep(1)
