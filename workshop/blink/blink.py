
import board
from digitalio import DigitalInOut, Direction
from time import sleep

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

while True:
    print("Hi!")
    led.value = True
    sleep(1)
    led.value = False
    sleep(1)
