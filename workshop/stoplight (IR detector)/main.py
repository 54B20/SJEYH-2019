"""
FILE: main.py
DESC: Working example for IR (stoplight) sensor
"""
import board
import busio
from analogio import AnalogOut, AnalogIn
from time import sleep

threshold = 30000
delay = 0.61

ir = AnalogIn(board.D1)
uart = busio.UART(board.TX, board.RX, baudrate=9600)


while True:
    print("IR: " + str(ir.value))
    if ir.value > threshold:
        uart.write("!")
        uart.write("!")
        uart.write("!")
    else:
        uart.write("^")
        uart.write("^")
        uart.write("^")

    sleep(delay)
