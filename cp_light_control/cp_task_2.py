import board
from analogio import AnalogOut

light = AnalogOut(board.A0)

while True:
    for i in range(0, 65535, 64):
        light.value = i
    

  
