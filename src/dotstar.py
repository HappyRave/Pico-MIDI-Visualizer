"""

GP15 - SDA
GP14 - SCL

"""

import board
import time
import random
import adafruit_dotstar as star

print(star.__name__ + " version: " + star.__version__)

spi2_mosi = board.GP11
spi2_clk = board.GP10

dots = star.DotStar(spi2_clk, spi2_mosi, 144, brightness=0.9, auto_write=True, baudrate=4000000)

# a random color 0 -> 224
def random_color():
    return random.randrange(0, 8) * 32

n_dots = len(dots)
black = (0,0,0)
while True:
    color = (random_color(), random_color(), random_color())
    for i in range(0,n_dots):

        if (i > 0):
            dots[i-1] = black
        else:
            dots[n_dots-1] = black

        dots[i] = color
