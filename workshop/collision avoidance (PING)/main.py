import board
from time import sleep
from adafruit_hcsr04 import HCSR04

with HCSR04(board.D2, board.D1) as sonar:
    while True:
        try:
            print(sonar.distance)
            sleep(1)
        except Exception:
            pass


