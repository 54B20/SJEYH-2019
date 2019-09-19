import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut, AnalogIn
import time

redled = DigitalInOut(board.D13)
irled = DigitalInOut(board.D2)

redled.direction = Direction.OUTPUT
irled.direction = Direction.OUTPUT

while True:
    redled.value = True
    irled.value = True
    time.sleep(1)
    redled.value = False
    irled.value = False
    time.sleep(1)
