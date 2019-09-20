"""
FILE: main.py
DESC: Working example of Trinket M0 PING sensor
"""

import board
import busio
from time import sleep
from adafruit_hcsr04 import HCSR04

threshold = 10.0
delay = 0.59    # 59ms (a prime number to discurage race conditions)
uart = busio.UART(board.TX, board.RX, baudrate=115200)

with HCSR04(board.D2, board.D1) as sonar:
    while True:
        try:
            print(sonar.distance)
            if(sonar.distance < threshold):
                uart.write("S")
            # what's my reset/all-clear condition????
            sleep(delay)
        except Exception:
            pass


