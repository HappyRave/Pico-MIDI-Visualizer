"""

Main module

"""

import time
import display
# import dotstar
import midi

TILE_SOURCE = 0

N, i = 0, 0
while True:
    msg = midi.read_midi()
    if msg is not None:
        print(msg.note)
        display.update_data(str(msg.note))
    else:
        N = (N + 1) % 4
        if N == 0:
            i += 1
            display.update_data('No data ' + str(TILE_SOURCE))
            # display.cycle_btn(TILE_SOURCE)
            TILE_SOURCE = (TILE_SOURCE + 1) % 2
    time.sleep(0.25)
