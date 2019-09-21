"""
FILE: main.py
DESC: Sample solution for Trinket M0 Speedometer (interruptor) sensor
"""

import board
import busio
import pulseio
from time import sleep

target_rate = 10  # goal in ticks/sec
delay = 0.67
pulses = pulseio.PulseIn(board.D2)
uart = busio.UART(board.TX, board.RX, baudrate=9600)


while True:
    count = len(pulses)
    rate = count/delay
    print("RATE: " + str(rate) + " ticks/sec")

    if rate < target_rate:
        uart.write("+")
    elif rate > target_rate:
        uart.write("-")
    else:
        uart.write("=")

    pulses.clear()
    sleep(delay)
