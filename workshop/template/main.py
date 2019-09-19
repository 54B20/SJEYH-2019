import board
import busio
import time

uart = busio.UART(board.TX, board.RX, baudrate=9600)

while True:
    print("Template-Do Stuff Here!!")

    uart.write("?")
    time.sleep(1)
