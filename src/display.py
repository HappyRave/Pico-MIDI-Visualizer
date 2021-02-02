"""
Example of CircuitPython/RaspberryPi Pico
to display on 1.14" 135x240 (RGB) IPS screen
with ST7789 driver via SPI interface.

Connection between Pico and
the IPS screen, with ST7789 SPI interface.
3V3  - BLK (backlight, always on)
GP17 - CS
GP16 - DC
PIN RUN - RES
GP19 - SDA
GP18 - SCL
3V3  - VCC
GND  - GND
"""

import time
import os
# pylint: disable=E0401
# ignore load error on circuitpython modules
import board
import terminalio
import displayio
import busio
# pylint: disable=E0611
# pylint not fiding name label
from adafruit_display_text import label
import adafruit_st7789 as display_st7789
import adafruit_imageload

print("==============================")
# pylint: disable=E1101
# os from circuitpython has uname
print(os.uname())
print("Hello Raspberry Pi Pico/CircuitPython ST7789 SPI IPS Display")
print(display_st7789.__name__ + " version: " + display_st7789.__version__)
print()

# Release any resources currently in use for the displays
displayio.release_displays()

tft_cs = board.GP17
tft_dc = board.GP16
spi_mosi = board.GP19
spi_clk = board.GP18

spi = busio.SPI(spi_clk, MOSI=spi_mosi)

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)

display = display_st7789.ST7789(
    display_bus, width=240, height=135, rowstart=40, colstart=53, rotation=90)

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)

color_bitmap = displayio.Bitmap(240, 135, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00  # green

bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(238, 133, 16)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x0000FF  # blue
inner_sprite = displayio.TileGrid(inner_bitmap,
                                  pixel_shader=inner_palette, x=1, y=1)
splash.append(inner_sprite)

# bitmap test
bitmap, palette = adafruit_imageload.load(
    "/bmp/btn_OK.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
palette.make_transparent(0)

tile_grid = displayio.TileGrid(
    bitmap, pixel_shader=palette, width=1,
    height=1, tile_width=30, tile_height=67)

tile_group = displayio.Group(max_size=2, scale=1, x=120, y=20)
tile_group.append(tile_grid)

# Draw a label
text_group1 = displayio.Group(max_size=10, scale=2, x=20, y=40)
TEXT1 = "Listening midi"
text_area1 = label.Label(terminalio.FONT, text=TEXT1, color=0xFF0000)
text_group1.append(text_area1)  # Subgroup for text scaling
# Draw a label
text_group2 = displayio.Group(max_size=10, scale=1, x=20, y=60)
TEXT2 = "no data"
text_area2 = label.Label(terminalio.FONT, text=TEXT2, color=0xFFFFFF)
text_group2.append(text_area2)  # Subgroup for text scaling

splash.append(text_group1)
splash.append(text_group2)

splash.append(tile_group)


def update_data(text):
    """ update_data """
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
    text_group2[0] = text_area


def cycle_btn(source):
    """ cycle """
    tile_grid[0, 0] = source


tile_source = 0

for i in range(0, 10):
    tile_grid[0, 0] = tile_source
    tile_source = (tile_source + 1) % 2
    time.sleep(2)
