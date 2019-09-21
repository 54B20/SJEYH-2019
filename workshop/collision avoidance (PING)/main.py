"""
FILE: main.py
DESC: Working example of Trinket M0 PING sensor
"""

import board
import busio
from time import sleep
from adafruit_hcsr04 import HCSR04

threshold = 10.0
delay = 0.59

uart = busio.UART(board.TX, board.RX, baudrate=9600)

with HCSR04(board.D2, board.D1) as sonar:
    while True:
        try:
            print(sonar.distance)
            if(sonar.distance < threshold):
                uart.write("X")
            else:
                uart.write("*")
            sleep(delay)
        except Exception:
            pass


