import display
#import dotstar
import midi
import time



n = 0
i = 0
while True:
    msg = midi.read_midi()
    if msg != None:
        print(msg.note)
        display.update_data(str(msg.note))
    else:
        n += 1
        if (n % 4 == 0):
            n = 0
            i += 1
            display.update_data('No data ' + str(i))
    time.sleep(0.25)
