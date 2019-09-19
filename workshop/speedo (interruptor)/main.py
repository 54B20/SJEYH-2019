import board
import busio
import pulseio
import time

# uart = busio.UART(board.TX, board.RX, baudrate=9600)
pulses = pulseio.PulseIn(board.D2)

while True:
    count = len(pulses)
    print("COUNT: " + str(count))
    pulses.clear()
    time.sleep(1)
