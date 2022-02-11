import board
from analogio import AnalogOut, AnalogIn

led = AnalogOut(board.A0)
light =  AnalogIn(board.A1)

while True:
        led.value = 60000
        print(light.value)
