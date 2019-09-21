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

def uart_write(c):
    with busio.UART(board.TX, board.RX, baudrate=9600) as uart:
        uart.write(c)

while True:
    irval = ir.value
    print("IR: " + str(irval))
    if irval > threshold:
        uart_write('!')
    else:
        uart_write('^')

    sleep(delay)
