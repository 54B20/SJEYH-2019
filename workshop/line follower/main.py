"""
FILE: main.py
DESC: CircuitPython solution for Trinket M0 3-sensor line-follower
"""

import board
import busio
from analogio import AnalogOut, AnalogIn
import time

delay = 0.53    # 59ms (a prime number to discurage race conditions)
threshold = 20000
left = AnalogIn(board.D0)
middle = AnalogIn(board.D1)
right = AnalogIn(board.D2)
uart = busio.UART(board.TX, board.RX, baudrate=9600)

while True:
    print("RIGHT: %0.2f" % right.value)
    print("MIDDLE: %0.2f" % middle.value)
    print("LEFT: %0.2f\n\n\n" % left.value)

    if middle.value <= threshold and right.value > threshold:
        uart.write("L")
        uart.write("L")
        uart.write("L")
    elif middle.value > threshold and right.value > threshold:
        uart.write("l")
        uart.write("l")
        uart.write("l")
    elif middle.value>threshold and left.value<=threshold and right.value<=threshold:
        uart.write("|")
        uart.write("|")
        uart.write("|")
    elif middle.value>threshold and left.value>threshold:
        uart.write("r")
        uart.write("r")
        uart.write("r")
    elif middle.value <= threshold and left.value > threshold:
        uart.write("R")
        uart.write("R")
        uart.write("R")
    else:
        uart.write("?")
        uart.write("?")
        uart.write("?")

    time.sleep(delay)
