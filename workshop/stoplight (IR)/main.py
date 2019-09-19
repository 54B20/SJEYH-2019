import board
from analogio import AnalogOut, AnalogIn
import time

ir = AnalogIn(board.D1)

while True:
    # Read IR detector value
    print("IR: " + str(ir.value))
    time.sleep(1) # make bigger to slow down
