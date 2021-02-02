import usb_midi
import adafruit_midi

from adafruit_midi.timing_clock import TimingClock
from adafruit_midi.channel_pressure import ChannelPressure
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.pitch_bend import PitchBend
from adafruit_midi.polyphonic_key_pressure import PolyphonicKeyPressure
from adafruit_midi.program_change import ProgramChange
from adafruit_midi.start import Start
from adafruit_midi.stop import Stop
from adafruit_midi.system_exclusive import SystemExclusive

from adafruit_midi.midi_message import MIDIUnknownEvent

portIn = usb_midi.ports[0]
midi = adafruit_midi.MIDI(midi_in=portIn, in_channel=0)


def read_midi():
    return midi.receive()
