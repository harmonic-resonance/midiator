## src/harmonic_resonance/midiator/__init__.py

```py
"""
midiator
========

HARMONIC resonance
------------------



"""
__author__ = "harmonic-resonance"
__maintainer__ = "harmonic-resonance"
__email__ = "github@phiarchitect.com"
__version__ = "0.0.1"
__licence__ = "MIT"

from mido import MidiFile, Message, MetaMessage, bpm2tempo, second2tick, tick2second

#  import .notes as N
from . import notes as N
from .scales import *
from .chords import *
from .instruments import *
from .voices import *
from .percussions import *
from .arps import *
from .part import *

import subprocess


def new_midi(title="", tempo=500000) -> MidiFile:
    """sets up a mido midi file with initial meta track"""
    mf = MidiFile()

    track = mf.add_track(name="meta")
    if title:
        track.append(MetaMessage("text", text=title, time=0))
    track.append(MetaMessage("set_tempo", tempo=tempo, time=0))
    return mf


def set_new_track(mf, name="", instrument=""):
    track = mf.add_track(name=name)
    # if instrument:
    # track.append(MetaMessage('text', text='TITLE', time=0))
    return track


def save_midi(mf, folder, filename):
    import os

    sessions = os.path.expanduser("~") + "/Sessions"
    out = f"{sessions}/{folder}/"
    os.makedirs(out, exist_ok=True)
    filepath = out + filename
    mf.save(filepath)
    print(f"    * {filepath}")
    return filepath


def play(filepath: str):
    """TODO: Docstring for play.

    :filepath: TODO
    :returns: TODO

    """
    subprocess.run(["timidity", "-in", "-c", "~/.photon/timidity.cfg", filepath])

```

## src/harmonic_resonance/midiator/__main__.py

```py
"""The package entry point into the application."""

from .app import run

if __name__ == "__main__":
    run()
```

## src/harmonic_resonance/midiator/app.py

```py
"""
run the main app
"""
from .midiator import Midiator


def run() -> None:
    reply = Midiator().run()
    print(reply)

```

## src/harmonic_resonance/midiator/midiator.py

```py
"""
midiator
"""
```

## src/harmonic_resonance/midiator/notes.py

```py
NOTES = {
    12: "C0",
    13: "C#0",
    14: "D0",
    15: "D#0",
    16: "E0",
    17: "F0",
    18: "F#0",
    19: "G0",
    20: "G#0",
    21: "A0",
    22: "A#0",
    23: "B0",
    24: "C1",
    25: "C#1",
    26: "D1",
    27: "D#1",
    28: "E1",
    29: "F1",
    30: "F#1",
    31: "G1",
    32: "G#1",
    33: "A1",
    34: "A#1",
    35: "B1",
    36: "C2",
    37: "C#2",
    38: "D2",
    39: "D#2",
    40: "E2",
    41: "F2",
    42: "F#2",
    43: "G2",
    44: "G#2",
    45: "A2",
    46: "A#2",
    47: "B2",
    48: "C3",
    49: "C#3",
    50: "D3",
    51: "D#3",
    52: "E3",
    53: "F3",
    54: "F#3",
    55: "G3",
    56: "G#3",
    57: "A3",
    58: "A#3",
    59: "B3",
    60: "C4",
    61: "C#4",
    62: "D4",
    63: "D#4",
    64: "E4",
    65: "F4",
    66: "F#4",
    67: "G4",
    68: "G#4",
    69: "A4",
    70: "A#4",
    71: "B4",
    72: "C5",
    73: "C#5",
    74: "D5",
    75: "D#5",
    76: "E5",
    77: "F5",
    78: "F#5",
    79: "G5",
    80: "G#5",
    81: "A5",
    82: "A#5",
    83: "B5",
    84: "C6",
    85: "C#6",
    86: "D6",
    87: "D#6",
    88: "E6",
    89: "F6",
    90: "F#6",
    91: "G6",
    92: "G#6",
    93: "A6",
    94: "A#6",
    95: "B6",
    96: "C7",
    97: "C#7",
    98: "D7",
    99: "D#7",
    100: "E7",
    101: "F7",
    102: "F#7",
    103: "G7",
    104: "G#7",
    105: "A7",
    106: "A#7",
    107: "B7",
    108: "C8",
    109: "C#8",
    110: "D8",
    111: "D#8",
    112: "E8",
    113: "F8",
    114: "F#8",
    115: "G8",
    116: "G#8",
    117: "A8",
    118: "A#8",
    119: "B8",
}

NOTES_BY_NAME = {value: key for key, value in NOTES.items()}


C0 = 12
Cs0 = 13
D0 = 14
Ds0 = 15
E0 = 16
F0 = 17
Fs0 = 18
G0 = 19
Gs0 = 20
A0 = 21
As0 = 22
B0 = 23
C1 = 24
Cs1 = 25
D1 = 26
Ds1 = 27
E1 = 28
F1 = 29
Fs1 = 30
G1 = 31
Gs1 = 32
A1 = 33
As1 = 34
B1 = 35
C2 = 36
Cs2 = 37
D2 = 38
Ds2 = 39
E2 = 40
F2 = 41
Fs2 = 42
G2 = 43
Gs2 = 44
A2 = 45
As2 = 46
B2 = 47
C3 = 48
Cs3 = 49
D3 = 50
Ds3 = 51
E3 = 52
F3 = 53
Fs3 = 54
G3 = 55
Gs3 = 56
A3 = 57
As3 = 58
B3 = 59
C4 = 60
Cs4 = 61
D4 = 62
Ds4 = 63
E4 = 64
F4 = 65
Fs4 = 66
G4 = 67
Gs4 = 68
A4 = 69
As4 = 70
B4 = 71
C5 = 72
Cs5 = 73
D5 = 74
Ds5 = 75
E5 = 76
F5 = 77
Fs5 = 78
G5 = 79
Gs5 = 80
A5 = 81
As5 = 82
B5 = 83
C6 = 84
Cs6 = 85
D6 = 86
Ds6 = 87
E6 = 88
F6 = 89
Fs6 = 90
G6 = 91
Gs6 = 92
A6 = 93
As6 = 94
B6 = 95
C7 = 96
Cs7 = 97
D7 = 98
Ds7 = 99
E7 = 100
F7 = 101
Fs7 = 102
G7 = 103
Gs7 = 104
A7 = 105
As7 = 106
B7 = 107
C8 = 108
Cs8 = 109
D8 = 110
Ds8 = 111
E8 = 112
F8 = 113
Fs8 = 114
G8 = 115
Gs8 = 116
A8 = 117
As8 = 118
B8 = 119

```

## src/harmonic_resonance/midiator/part.py

```py
"""
Part extend the mido ``MidiFile`` object
- keeps track of instruments, channels
"""
from pathlib import Path
import subprocess
from mido import MidiFile, Message, MetaMessage, bpm2tempo
from .instruments import Instrument, I
from .voices import Voice, V
from .percussions import Percussion, P

class Part(MidiFile):
    """Part object extends the mido MidoFile"""

    free_channels = list(range(16))
    perc_channel = free_channels.remove(9)

    instruments = []

    def __init__(self, project: str, title: str, 
            bpm: int=120, bpM: int=4, beat_val: int=4,
            root: int=60, key: str='C'):
        """TODO: to be defined.

        :project: for the session, used to folder
        :title: for the musical part
        :tempo: milliseconds per beat
        :bpm: int value beats per minute for settings tempo
        :bpM: int - beats per Measure
        :beat_val: for time signature

        """
        super().__init__()

        self.project = project
        self.title = title
        self.root = root
        self.key = key

        track = self.add_track(name='meta')
        if title:
            track.append(MetaMessage('text', text=f'{project} - {title}', time=0))

        self.bpm = int(bpm)
        self.bpM = int(bpM)
        self.beat_val = int(beat_val)
        self.tempo = int(bpm2tempo(self.bpm))
        track.append(MetaMessage('set_tempo', tempo=self.tempo, time=0))
        track.append(MetaMessage('key_signature', key=self.key, time=0))

    def measure_ticks(self):
        """return measure duration in ticks
        used for setting the ``M`` variable in a composition

        :returns:  int

        """
        return self.bpM * self.ticks_per_beat

    def set_marker(self, text, duration=0):
        '''appends  a ``marker`` message at ``duration`` to the meta track
        :duration: offset for placement of marker
        '''
        duration = int(duration)
        self.tracks[0].append(MetaMessage('marker', text=text, time=0))
        self.tracks[0].append(MetaMessage('marker', text='', time=duration))

    def get_mid_path(self) -> Path:
        #  folder = Path(f'~/Sessions/{self.project}').expanduser()
        #  folder.mkdir(parents=True, exist_ok=True)
        #  midi_file = folder / f'{self.title}.mid'
        midi_file = Path(f'./{self.project}-{self.title}-{self.key}-{self.bpm}.mid')
        return midi_file

    def save(self):
        midi_file = self.get_mid_path()
        filepath = str(midi_file)
        super().save(filepath)
        #  print(f'    * {filepath}')
        return filepath

    def play(self):
        """
        this overrides the mido play function
        """
        midi_file = self.get_mid_path()
        filepath = str(midi_file)
        subprocess.run(["timidity", '-in', "-c", "~/.photon/timidity.cfg", filepath])

    def convert(self):
        """
        this overrides the mido play function
        """
        midi_file = self.get_mid_path()
        filepath = str(midi_file)
        subprocess.run(["timidity", '-in', "-c", "~/.photon/timidity.cfg", "-Ov", filepath])

    def add_instrument(self, instrument_type: I) -> Instrument:
        """add instrument to session
        set to next available channel

        :instrument_type: TODO
        :returns: TODO

        """
        channel = self.free_channels.pop(0)
        instrument = Instrument(self, instrument_type, channel)
        self.instruments.append(instrument)
        return instrument

    def add_voice(self, voice_type: V) -> Voice:
        """add instrument to session
        set to next available channel

        :instrument_type: TODO
        :returns: TODO

        """
        channel = self.free_channels.pop(0)
        instrument = Voice(self, voice_type, channel)
        self.instruments.append(instrument)
        return instrument

    def add_kick(self):
        return Percussion(self, P.acoustic_bass_drum)

    def add_piano(self):
        return self.add_instrument(I.acoustic_grand_piano)

    def add_vibes(self):
        return self.add_instrument(I.vibraphone)

    def add_bass(self):
        return self.add_instrument(I.acoustic_bass)

    def add_horns(self):
        return self.add_instrument(I.brass_section)

    def add_strings(self):
        return self.add_instrument(I.string_ensemble_1)

    def add_solo_ooh(self):
        return self.add_voice(V.solo_ooh)

    def add_solo_aah(self):
        return self.add_voice(V.solo_aah)

    def add_choir_aah(self):
        return self.add_voice(V.choir_aah)

    def add_choir_ooh(self):
        return self.add_voice(V.choir_ooh)

    def add_choir_mixed(self):
        return self.add_voice(V.choir_mixed)

    def add_choir_swell(self):
        return self.add_voice(V.choir_swell)

    def add_choir_little_swell(self):
        return self.add_voice(V.choir_little_swell)

```

## src/harmonic_resonance/midiator/arps/__init__.py

```py
'''
arpeggio functions
'''

def add_arp_up(instrument, notes, length):
    '''sequence notes in succession divided evenly across length'''
    beat = length / len(notes)
    for note in notes:
        instrument.set_note(note, beat)

def add_arp_down(instrument, notes, length):
    '''sequence notes in reverse succession divided evenly across length'''
    beat = length / len(notes)
    for note in reversed(notes):
        instrument.set_note(note, beat)



```

## src/harmonic_resonance/midiator/chords/__init__.py

```py
#  import phimidi.chords.chord_types as C
from . import chord_types as C
from . import progressions

def get_chord_notes(root, chord_type):
    notes = []
    chord_intervals = C.CHORDS[chord_type]
    for interval in chord_intervals:
        notes.append(root + interval)
    return notes
    

```

## src/harmonic_resonance/midiator/chords/chord_types.py

```py
'''utils for building chords`
TODO: alternate voicings
'''
major = 'M'
major_6 = '6'
major_7 = 'M7'
dominant_7 = '7'
dominant_9 = '9'
dominant_11 = '11'
dominant_13 = '13'
minor = 'm'
minor_7 = 'm7'
minor_9 = 'm9'
minor_11 = 'm11'
minor_13 = 'm13'
diminished = 'o'
sus2 = 'sus2'
sus4 = 'sus4'

CHORDS = {
  'M': [0, 4, 7],
  '6': [0, 4, 7, 9],
  'M7': [0, 4, 7, 11],
  '7': [0, 4, 7, 10],
  '9': [0, 4, 7, 10, 14],
  '11': [0, 4, 7, 10, 14, 17],
  '13': [0, 4, 7, 10, 14, 17, 21],
  'm': [0, 3, 7],
  'm7': [0, 3, 7, 10],
  'm9': [0, 3, 7, 10, 14],
  'm11': [0, 3, 7, 10, 14, 17],
  'm13': [0, 3, 7, 10, 14, 17, 21],
  'o': [0, 3, 6],
  'sus2': [0, 2, 7],
  'sus4': [0, 5, 7],
}

```

## src/harmonic_resonance/midiator/chords/progressions.py

```py
'''
chord progressions
includes patterns from:
https://www.learnjazzstandards.com/blog/learning-jazz/jazz-theory/3-important-jazz-chord-progressions-need-master/
'''
import harmonic_resonance.midiator as pm
from . import chord_types as C

EAGsABE = [
        (pm.N.E4, 2, C.major),
        (pm.N.A4, 2, C.major),
        (pm.N.Gs4, 4, C.minor_7),
        (pm.N.A3, 2, C.major),
        (pm.N.B3, 2, C.dominant_7),
        (pm.N.E3, 4, C.major),
        ]
p5 = [
        (pm.N.C3, 4, C.major),
        (pm.N.F3, 4, C.dominant_9),
        (pm.N.A3, 4, C.minor_7),
        (pm.N.G3, 4, C.dominant_11),
        (pm.N.A3, 4, C.minor_11),
        (pm.N.F3, 4, C.dominant_9),
        (pm.N.C3, 8, C.dominant_13),
        ]

EBCsA = [
        (pm.N.E4, 4, C.major),
        (pm.N.B3, 4, C.major),
        (pm.N.Cs4, 4, C.minor),
        (pm.N.A3, 4, C.major),
        ]

def build_progression(key: pm.Scale, chords: list) -> list:
    """assemble all notes for chords in the progression

    :key: dict of midi note id for each position in key
    :chords: list of tuples with ``(pos_name, pos_id, chord_type)``
    :returns: list

    """
    progression = []
    for pos_name, note, chord_type in chords:
        notes = pm.get_chord_notes(key[note], chord_type)
        progression.append((pos_name, notes))

    return progression

def I_V_vis_IV(root):
    I = pm.get_chord_notes(0 + root, C.major)
    V = pm.get_chord_notes(7 + root, C.dominant_7)
    vis = pm.get_chord_notes(10 + root, C.minor)
    IV = pm.get_chord_notes(5 + root, C.dominant_7)

    return [I, V, vis, IV]


def ii_V_I_I(root):
    key = pm.Scale(root, scale_type=pm.S.major)
    chords = [
            ('ii7', 2, C.minor_7),
            ('V7', 5, C.dominant_7),
            ('IM7', 1, C.major_7),
            ('I6', 1, C.major_6),
            ]
    return build_progression(key, chords)


def ii_V_i_i(root):
    key = pm.Scale(root, scale_type=pm.S.major)
    chords = [
            ('ii7', 2, C.minor_7),
            ('V7', 5, C.dominant_7),
            ('i7', 1, C.minor_7),
            ('i9', 1, C.minor_9),
            ]
    return build_progression(key, chords)



def I_vi_ii_V(root: int):
    key = pm.Scale(root, scale_type=pm.S.major)
    chords = [ ('IM7', 1, C.major_7),
            ('vi7', 6, C.minor_7),
            ('ii7', 2, C.minor_7),
            ('V7', 5, C.dominant_7)
            ]
    return build_progression(key, chords)


def i_vi_ii_V(root: int):
    key = pm.Scale(root, scale_type=pm.S.major)
    chords = [ ('i7', 1, C.minor_7),
            ('vi7', 6, C.minor_7),
            ('ii7', 2, C.minor_7),
            ('V7', 5, C.dominant_7)
            ]
    return build_progression(key, chords)


def thelio(root):
    key = pm.Scale(root, scale_type=pm.S.major)
    chords = [ ('IM7', 1, C.major_7),
            ('IV9', 4, C.dominant_9),
            ('vi7', 6, C.minor_7),
            ('V11', 5, C.dominant_11),
            ('vi9', 6, C.minor_9),
            #  ('ii7', 2, C.minor_7),
            ('V13', 5, C.dominant_13),
            ]
    return build_progression(key, chords)



```

## src/harmonic_resonance/midiator/instruments/__init__.py

```py
"""
wrapper for managing instruments
"""
#  import phimidi as pm
from . import instrument_types as I
from .instrument import Instrument


def make_piano(mf, channel):
    return Instrument(mf, I.acoustic_grand_piano, channel)

def make_vibes(mf, channel):
    return Instrument(mf, I.vibraphone, channel)

def make_bass(mf, channel):
    return Instrument(mf, I.acoustic_bass, channel)

def make_horns(mf, channel):
    return Instrument(mf, I.brass_section, channel)

def make_strings(mf, channel):
    return Instrument(mf, I.string_ensemble_1, channel)


```

## src/harmonic_resonance/midiator/instruments/instrument.py

```py
import harmonic_resonance.midiator as pm

class Instrument():

    """Docstring for Instrument. """

    def __init__(self, mf, inst_id, channel):
        """TODO: to be defined. """
        self.name = pm.I.INSTRUMENTS[inst_id]
        self.instrument = inst_id
        self.channel = channel

        self.track = mf.add_track(name=self.name)
        self.track.append(pm.Message('program_change', channel=channel, program=inst_id, time=0))

        self.track_volume = mf.add_track(name=f'{self.name}-volume')
        self.track_pan = mf.add_track(name=f'{self.name}-pan')
        #  self.track_reverb = pm.set_new_track(mf, name=f'{self.name}-reverb')
        #  self.track_chorus = pm.set_new_track(mf, name=f'{self.name}-chorus')


    def set_text(self, text, duration=0):
        '''appends  a ``text`` message for the ``duration`` to the Instrument track
        '''
        duration = int(duration)
        self.track.append(pm.MetaMessage('text', text=text, time=duration))

    def set_rest(self, duration):
        '''appends  a ``note_off`` message for the ``duration`` to the Instrument track
        '''
        duration = int(duration)
        self.track.append(pm.Message('note_off', note=0, channel=self.channel, velocity=127, time=duration))

    def set_note(self, note, duration, velocity=64):
        duration = int(duration)
        self.track.append(pm.Message('note_on', note=note, channel=self.channel, velocity=velocity, time=0))
        self.track.append(pm.Message('note_off', note=note, channel=self.channel, velocity=127, time=duration))

    def set_notes(self, notes, duration, offset=0, velocity=64):
        duration = int(duration)
        offset = int(offset)
        # notes on
        for i, note in enumerate(notes):
            if i == 0:
                time = 0
            else:
                time = offset
            self.track.append(pm.Message('note_on', note=note, channel=self.channel, velocity=velocity, time=time))
        # notes off
        for i, note in enumerate(notes):
            if i == 0:
                #  time = duration
                time = duration -  (offset * (len(notes) - 1))
            else:
                time = 0
            self.track.append(pm.Message('note_off', note=note, channel=self.channel, velocity=127, time=time))

    def set_chord(self, root, duration, chord_type=pm.C.major, velocity=64):
        duration = int(duration)
        notes = pm.get_chord_notes(root, chord_type)
        self.set_notes(notes, duration, offset=0, velocity=velocity)
        #  for offset in chord:
            #  self.track.append(pm.Message('note_on', note=root+offset, channel=self.channel, velocity=velocity, time=0))
        #  for offset in chord:
            #  if offset == 0:
                #  time = duration
            #  else:
                #  time = 0
            #  self.track.append(pm.Message('note_off', note=root+offset, channel=self.channel, velocity=127, time=time))

    def ramp_volume_up(self, duration, lo=32, hi=96):
        duration = int(duration)
        steps = range(lo, hi)
        for val in steps:
            self.set_volume(val, duration/len(steps))

    def ramp_volume_down(self, duration, lo=32, hi=96):
        duration = int(duration)
        steps = range(lo, hi)
        for val in reversed(steps):
            self.set_volume(val, duration/len(steps))

    def set_volume(self, level, duration):
        duration = int(duration)
        self.track_volume.append(pm.Message('control_change', channel=self.channel, control=7, value=level, time=0))
        self.track_volume.append(pm.Message('control_change', channel=self.channel, control=7, value=level, time=duration))


    def set_pan(self, level, duration):
        duration = int(duration)
        self.track_pan.append(pm.Message('control_change', channel=self.channel, control=10, value=level, time=duration))
        # try balance - control=8
        #  self.track_pan.append(pm.Message('control_change', channel=self.channel, control=8, value=level, time=duration))

    #  def set_balance(self, level, duration):
        #  duration = int(duration)
        #  self.track_volume.append(pm.Message('control_change', channel=self.channel, control=8, value=level, time=duration))

    #  def set_reverb(self, level, duration):
        #  duration = int(duration)
        #  self.track_reverb.append(pm.Message('control_change', channel=self.channel, control=91, value=level, time=duration))

    #  def set_chorus(self, level, duration):
        #  duration = int(duration)
        #  self.track_chorus.append(pm.Message('control_change', channel=self.channel, control=93, value=level, time=duration))

```

## src/harmonic_resonance/midiator/instruments/instrument_types.py

```py
acoustic_grand_piano = 0
bright_acoustic_piano = 1
electric_grand_piano = 2
honky_tonk_piano = 3
electric_piano_1 = 4
electric_piano_2 = 5
harpsichord = 6
clavi = 7
celesta = 8
glockenspiel = 9
music_box = 10
vibraphone = 11
marimba = 12
xylophone = 13
tubular_bells = 14
dulcimer = 15
drawbar_organ = 16
percussive_organ = 17
rock_organ = 18
church_organ = 19
reed_organ = 20
accordion = 21
harmonica = 22
tango_accordion = 23
acoustic_guitar_nylon = 24
acoustic_guitar_steel = 25
electric_guitar_jazz = 26
electric_guitar_clean = 27
electric_guitar_muted = 28
overdriven_guitar = 29
distortion_guitar = 30
guitar_harmonics = 31
acoustic_bass = 32
electric_bass_finger = 33
electric_bass_pick = 34
fretless_bass = 35
slap_bass_1 = 36
slap_bass_2 = 37
synth_bass_1 = 38
synth_bass_2 = 39
violin = 40
viola = 41
cello = 42
contrabass = 43
tremolo_strings = 44
pizzicato_strings = 45
orchestral_harp = 46
timpani = 47
string_ensemble_1 = 48
string_ensemble_2 = 49
synthstrings_1 = 50
synthstrings_2 = 51
choir_aahs = 52
voice_oohs = 53
synth_voice = 54
orchestra_hit = 55
trumpet = 56
trombone = 57
tuba = 58
muted_trumpet = 59
french_horn = 60
brass_section = 61
synthbrass_1 = 62
synthbrass_2 = 63
soprano_sax = 64
alto_sax = 65
tenor_sax = 66
baritone_sax = 67
oboe = 68
english_horn = 69
bassoon = 70
clarinet = 71
piccolo = 72
flute = 73
recorder = 74
pan_flute = 75
blown_bottle = 76
shakuhachi = 77
whistle = 78
ocarina = 79
lead_1_square = 80
lead_2_sawtooth = 81
lead_3_calliope = 82
lead_4_chiff = 83
lead_5_charang = 84
lead_6_voice = 85
lead_7_fifths = 86
lead_8_bass_and_lead = 87
pad_1_new_age = 88
pad_2_warm = 89
pad_3_polysynth = 90
pad_4_choir = 91
pad_5_bowed = 92
pad_6_metallic = 93
pad_7_halo = 94
pad_8_sweep = 95
fx_1_rain = 96
fx_2_soundtrack = 97
fx_3_crystal = 98
fx_4_atmosphere = 99
fx_5_brightness = 100
fx_6_goblins = 101
fx_7_echoes = 102
fx_8_sci_fi = 103
sitar = 104
banjo = 105
shamisen = 106
koto = 107
kalimba = 108
bag_pipe = 109
fiddle = 110
shanai = 111
tinkle_bell = 112
agogo = 113
steel_drums = 114
woodblock = 115
taiko_drum = 116
melodic_tom = 117
synth_drum = 118
reverse_cymbal = 119
guitar_fret_noise = 120
breath_noise = 121
seashore = 122
bird_tweet = 123
telephone_ring = 124
helicopter = 125
applause = 126
gunshot = 127

INSTRUMENTS = [
    'Acoustic Grand Piano',
    'Bright Acoustic Piano',
    'Electric Grand Piano',
    'Honky-tonk Piano',
    'Electric Piano 1',
    'Electric Piano 2',
    'Harpsichord',
    'Clavi',
    'Celesta',
    'Glockenspiel',
    'Music Box',
    'Vibraphone',
    'Marimba',
    'Xylophone',
    'Tubular Bells',
    'Dulcimer',
    'Drawbar Organ',
    'Percussive Organ',
    'Rock Organ',
    'Church Organ',
    'Reed Organ',
    'Accordion',
    'Harmonica',
    'Tango Accordion',
    'Acoustic Guitar (nylon)',
    'Acoustic Guitar (steel)',
    'Electric Guitar (jazz)',
    'Electric Guitar (clean)',
    'Electric Guitar (muted)',
    'Overdriven Guitar',
    'Distortion Guitar',
    'Guitar harmonics',
    'Acoustic Bass',
    'Electric Bass (finger)',
    'Electric Bass (pick)',
    'Fretless Bass',
    'Slap Bass 1',
    'Slap Bass 2',
    'Synth Bass 1',
    'Synth Bass 2',
    'Violin',
    'Viola',
    'Cello',
    'Contrabass',
    'Tremolo Strings',
    'Pizzicato Strings',
    'Orchestral Harp',
    'Timpani',
    'String Ensemble 1',
    'String Ensemble 2',
    'SynthStrings 1',
    'SynthStrings 2',
    'Choir Aahs',
    'Voice Oohs',
    'Synth Voice',
    'Orchestra Hit',
    'Trumpet',
    'Trombone',
    'Tuba',
    'Muted Trumpet',
    'French Horn',
    'Brass Section',
    'SynthBrass 1',
    'SynthBrass 2',
    'Soprano Sax',
    'Alto Sax',
    'Tenor Sax',
    'Baritone Sax',
    'Oboe',
    'English Horn',
    'Bassoon',
    'Clarinet',
    'Piccolo',
    'Flute',
    'Recorder',
    'Pan Flute',
    'Blown Bottle',
    'Shakuhachi',
    'Whistle',
    'Ocarina',
    'Lead 1 (square)',
    'Lead 2 (sawtooth)',
    'Lead 3 (calliope)',
    'Lead 4 (chiff)',
    'Lead 5 (charang)',
    'Lead 6 (voice)',
    'Lead 7 (fifths)',
    'Lead 8 (bass + lead)',
    'Pad 1 (new age)',
    'Pad 2 (warm)',
    'Pad 3 (polysynth)',
    'Pad 4 (choir)',
    'Pad 5 (bowed)',
    'Pad 6 (metallic)',
    'Pad 7 (halo)',
    'Pad 8 (sweep)',
    'FX 1 (rain)',
    'FX 2 (soundtrack)',
    'FX 3 (crystal)',
    'FX 4 (atmosphere)',
    'FX 5 (brightness)',
    'FX 6 (goblins)',
    'FX 7 (echoes)',
    'FX 8 (sci-fi)',
    'Sitar',
    'Banjo',
    'Shamisen',
    'Koto',
    'Kalimba',
    'Bag pipe',
    'Fiddle',
    'Shanai',
    'Tinkle Bell',
    'Agogo',
    'Steel Drums',
    'Woodblock',
    'Taiko Drum',
    'Melodic Tom',
    'Synth Drum',
    'Reverse Cymbal',
    'Guitar Fret Noise',
    'Breath Noise',
    'Seashore',
    'Bird Tweet',
    'Telephone Ring',
    'Helicopter',
    'Applause',
    'Gunshot'
]

```

## src/harmonic_resonance/midiator/percussions/__init__.py

```py
'''
https://docs.google.com/spreadsheets/d/19_3BxUMy3uy1Gb0V8Wc-TcG7q16Amfn6e8QVw4-HuD0/edit#gid=0
'''
from . import percussion_types as P
from . import patterns
from .percussion import Percussion
from .kits import *

def make_tick(mf):
    return Percussion(mf, P.side_stick)

def make_kick(mf):
    return Percussion(mf, P.acoustic_bass_drum)

def make_low_tom(mf):
    return Percussion(mf, P.low_tom)

def make_high_tom(mf):
    return Percussion(mf, P.high_tom)

def make_floor_tom(mf):
    return Percussion(mf, P.low_floor_tom)

def make_snare(mf):
    return Percussion(mf, P.acoustic_snare)

def make_hihat_closed(mf):
    return Percussion(mf, P.closed_hi_hat)

def make_hihat_open(mf):
    return Percussion(mf, P.open_hi_hat)

def make_crash(mf):
    return Percussion(mf, P.crash_cymbal_1)

def make_ride(mf):
    return Percussion(mf, P.ride_cymbal_1)

def make_kit_1(mf):
    tick = make_tick(mf)
    kick = make_kick(mf)
    snare = make_snare(mf)
    hihat_c = make_hihat_closed(mf)
    hihat_o = make_hihat_open(mf)
    ride = make_ride(mf)

    return tick, kick, snare, hihat_c, hihat_o, ride
    
def make_kit_toms(mf):
    kit_1 = make_kit_1(mf)
    low_tom = make_low_tom(mf)
    high_tom = make_high_tom(mf)
    floor_tom = make_floor_tom(mf)

    return *kit_1, low_tom, high_tom, floor_tom

```

## src/harmonic_resonance/midiator/percussions/percussion.py

```py
import harmonic_resonance.midiator as pm
from ..instruments import Instrument


class Percussion(Instrument):
    """Class for creating MIDI percussion tracks using midiator.

    The Percussion class inherits from Instrument and allows setting up
    percussion hits and patterns on the default MIDI drum channel (10 in MIDI
    convention, but 9 in 0-indexed Python).
    """

    def __init__(self, midi_file, instrument_id, channel=9):
        """Initializes a Percussion instance.

        Args:
            midi_file (MidiFile): The MIDI file to which this percussion track
                will be added.
            instrument_id (int): The ID representing the percussion instrument
                as per General MIDI level 1 standard.
            channel (int): The MIDI channel assigned for percussion (usually
                channel 10, which is 9 in 0-indexed).
        """
        self.name = pm.P.PERCUSSIONS[
            instrument_id
        ]  # Get the name of the instrument using its ID
        self.instrument = instrument_id  # Instrument note number on the drum channel
        self.channel = channel  # MIDI channel for drums

        # Create and name a new track for the percussion instrument in the
        # provided MIDI file
        self.track = midi_file.add_track(name=self.name)
        # Set the MIDI program change message to select the correct instrument
        self.track.append(
            pm.Message(
                "program_change", channel=self.channel, program=self.instrument, time=0
            )
        )

    def set_hit(self, duration, velocity=64):
        """Sets a single percussion hit.

        Args:
            duration (int): The duration of the note in MIDI ticks.
            velocity (int): The velocity (volume) of the note-on message.
        """
        duration = int(duration)
        # Note on for the specified instrument and velocity
        self.track.append(
            pm.Message(
                "note_on",
                note=self.instrument,
                channel=self.channel,
                velocity=velocity,
                time=0,
            )
        )
        # Note off after the specified duration
        self.track.append(
            pm.Message(
                "note_off",
                note=self.instrument,
                channel=self.channel,
                velocity=127,
                time=duration,
            )
        )

    def set_hits(self, duration, divisions, velocity=64):
        """Sets multiple percussion hits equally spaced within the given duration.

        Args:
            duration (int): The total duration in which the hits are to be placed.
            divisions (int): The number of hits to be placed within the total duration.
            velocity (int): The velocity (volume) of each note-on message.
        """
        hit_duration = int(duration / divisions)
        for _ in range(divisions):
            self.set_hit(hit_duration, velocity)

    def add_pattern(self, pattern: str, beat_duration: int, velocity_mod: int = 0):
        """
        Adds a rhythm pattern to the percussion track.

        Args:
            pattern (str): String with characters representing hits (numbers)
                or rests ('_').  A dash ('-') after a hit extends the hit's
                duration by one beat_duration.
            beat_duration (int): The duration of one beat in MIDI ticks.
            velocity_mod (int): Modifier to adjust the overall velocity for the pattern.
        """
        index = 0
        while index < len(pattern):
            p = pattern[index]
            if p == "_":
                # Advance the position for rest
                self.set_rest(beat_duration)
                index += 1
            elif p.isdigit():
                # Calculate the number of subsequent dashes to extend the
                # note's duration
                extension_count = 0
                look_ahead_index = index + 1
                while (
                    look_ahead_index < len(pattern) and pattern[look_ahead_index] == "-"
                ):
                    extension_count += 1
                    look_ahead_index += 1

                total_duration = beat_duration * (1 + extension_count)
                velocity = int(p) * 12 + velocity_mod
                self.set_hit(total_duration, velocity=velocity)

                # Skip over the dashes that have been accounted for in the
                # extended duration
                index = look_ahead_index
            else:
                # For unrecognized characters, simply move to the next character
                index += 1

```

## src/harmonic_resonance/midiator/percussions/percussion_types.py

```py
acoustic_bass_drum = 35
bass_drum_1 = 36
side_stick = 37
acoustic_snare = 38
hand_clap = 39
electric_snare = 40
low_floor_tom = 41
closed_hi_hat = 42
high_floor_tom = 43
pedal_hi_hat = 44
low_tom = 45
open_hi_hat = 46
low_and_mid_tom = 47
hi_and_mid_tom = 48
crash_cymbal_1 = 49
high_tom = 50
ride_cymbal_1 = 51
chinese_cymbal = 52
ride_bell = 53
tambourine = 54
splash_cymbal = 55
cowbell = 56
crash_symbol_2 = 57
vibraslap = 58
ride_cymbal_2 = 59
hi_bongo = 60
low_bongo = 61
mute_hi_conga = 62
open_hi_conga = 63
low_conga = 64
high_timbale = 65
low_timbale = 66
high_agogo = 67
low_agogo = 68
cabasa = 69
maracas = 70
short_whistle = 71
long_whistle = 72
short_guiro = 73
long_guiro = 74
claves = 75
hi_wood_block = 76
low_wood_block = 77
mute_cuica = 78
open_cuica = 79
mute_triangle = 80
open_triangle = 81
shaker = 82

PERCUSSIONS = {
        35: 'Acoustic Bass Drum',
        36: 'Bass Drum 1',
        37: 'Side Stick',
        38: 'Acoustic Snare',
        39: 'Hand Clap',
        40: 'Electric Snare',
        41: 'Low Floor Tom',
        42: 'Closed Hi-Hat',
        43: 'High Floor Tom',
        44: 'Pedal Hi-Hat',
        45: 'Low Tom',
        46: 'Open Hi-Hat',
        47: 'Low-Mid Tom',
        48: 'Hi-Mid Tom',
        49: 'Crash Cymbal 1',
        50: 'High Tom',
        51: 'Ride Cymbal 1',
        52: 'Chinese Cymbal',
        53: 'Ride Bell',
        54: 'Tambourine',
        55: 'Splash Cymbal',
        56: 'Cowbell',
        57: 'Crash Symbol 2',
        58: 'Vibraslap',
        59: 'Ride Cymbal 2',
        60: 'Hi Bongo',
        61: 'Low Bongo',
        62: 'Mute Hi Conga',
        63: 'Open Hi Conga',
        64: 'Low Conga',
        65: 'High Timbale',
        66: 'Low Timbale',
        67: 'High Agogo',
        68: 'Low Agogo',
        69: 'Cabasa',
        70: 'Maracas',
        71: 'Short Whistle',
        72: 'Long Whistle',
        73: 'Short Guiro',
        74: 'Long Guiro',
        75: 'Claves',
        76: 'Hi Wood Block',
        77: 'Low Wood Block',
        78: 'Mute Cuica',
        79: 'Open Cuica',
        80: 'Mute Triangle',
        81: 'Open Triangle',
        82: 'Shaker'
}

```

## src/harmonic_resonance/midiator/percussions/kits/__init__.py

```py
from .kit import *
from .conga import *
from .standard import *


```

## src/harmonic_resonance/midiator/percussions/kits/conga.py

```py
from .kit import Kit
from ..percussion import Percussion
import harmonic_resonance.midiator.percussions.percussion_types as P

class Conga(Kit):
    '''conga kit - 2 drums + mute'''
    kit = []

    def __init__(self, part):
        """TODO: Docstring for __init__.
        """
        super().__init__(part)
        self.tumba = Percussion(part, P.low_conga)
        self.conga = Percussion(part, P.open_hi_conga)
        self.mute = Percussion(part, P.mute_hi_conga)

        self.load_patterns('conga.yaml')

        self.kit = {
            "tumba": self.tumba,
            "conga": self.conga,
            "mute": self.mute,
        }

    #  def tumbao(self, duration: int, velocity_mod: int=0):
        #  """2 measure tumbao rhythm

        #  :duration: time for phrase in milliseconds
        #  """
        #  b = int(duration/16)
        #  # 5 heel 4 toe
        #  mute =  '54_454__' + '54___4__'
        #  conga = '__7___55' + '__7___55'
        #  tumba = '________' + '___55___'
        #  # 7 slap - 5 open

        #  self.mute_conga.add_pattern(mute, b, velocity_mod=velocity_mod)
        #  self.conga.add_pattern(conga, b, velocity_mod=velocity_mod)
        #  self.tumba.add_pattern(tumba, b, velocity_mod=velocity_mod)

    #  def guaguanco(self, duration: int, velocity_mod: int=0):
        #  """2 measure guaguanco rhythm

        #  :duration: TODO
        #  """
        #  b = int(duration/16)
        #  # 5 heel 4 toe 3 touch
        #  mute =  '___5_3__' + '_____3__'
        #  conga = '_77____5' + '5-75___5'
        #  tumba = '______7_' + '______8_'
        #  # 7 slap - 5 open

        #  self.mute_conga.add_pattern(mute, b, velocity_mod=velocity_mod)
        #  self.conga.add_pattern(conga, b, velocity_mod=velocity_mod)
        #  self.tumba.add_pattern(tumba, b, velocity_mod=velocity_mod)

    #  def bolero(self, duration: int, velocity_mod: int=0):
        #  """2 measure bolero rhythm

        #  :duration: TODO
        #  """
        #  b = int(duration/16)
        #  # 5 heel 4 toe 3 touch
        #  mute =  '54_454__' + '54_45___'
        #  conga = '__7___55' + '__7___5_'
        #  tumba = '________' + '_____5_5'
        #  # 7 slap - 5 open

        #  self.mute_conga.add_pattern(mute, b, velocity_mod=velocity_mod)
        #  self.conga.add_pattern(conga, b, velocity_mod=velocity_mod)
        #  self.tumba.add_pattern(tumba, b, velocity_mod=velocity_mod)

    #  def samba(self, duration: int, velocity_mod: int=0):
        #  """2 measure  rhythm

        #  :duration: time for phrase in milliseconds
        #  """
        #  b = int(duration/16)
        #  # 5 heel 4 toe
        #  mute =  '_3____3_' + '__3__33_'
        #  conga = '5_77_5_5' + '57_7___5'
        #  tumba = '____5___' + '____5___'
        #  # 7 slap - 5 open

        #  self.mute_conga.add_pattern(mute, b, velocity_mod=velocity_mod)
        #  self.conga.add_pattern(conga, b, velocity_mod=velocity_mod)
        #  self.tumba.add_pattern(tumba, b, velocity_mod=velocity_mod)


```

## src/harmonic_resonance/midiator/percussions/kits/kit.py

```py
import yaml
from pathlib import Path


class Kit:
    """
    A base class for a drum kit, defining common functionalities for percussion
    instruments that can be subclassed for specific drum kit configurations.
    """

    def __init__(self, part):
        """
        Initialize the drum kit with a specified MIDI part.

        :param part: The MIDI part to be used for this kit, typically defining the
                     MIDI channel or instrument preset used for the percussion sounds.
        """
        self.part = part
        self.kit = {}

    def rest_all(self, duration: int):
        """
        Set a rest for all percussion instruments in the kit for a specified duration.

        This function silences every instrument in the kit, effectively
        creating a pause or break in the rhythm.

        :param duration: The duration of the rest in MIDI ticks. This is not in
            milliseconds but in the MIDI's delta time based on ticks per beat.
        """
        duration = int(duration)  # Ensuring duration is an integer value.
        for perc in self.kit.values():
            perc.set_rest(duration)

    def set_patterns(self, pattern_set, duration, velocity_mod=0):
        """
        Apply a set of rhythm patterns to the instruments in the drum kit.

        This method reads a pattern set and configures each percussion instrument
        with its specified pattern, length, and dynamic modifications.

        :param pattern_set: A dictionary mapping instrument names to their
            rhythm patterns.  Each key is the name of an instrument as stored in
            the kit, and its value is the pattern string to be set for the
            instrument.
        :param duration: The total duration over which the pattern set should
            be applied, given in MIDI ticks.
        :param velocity_mod: A modifier to the default velocity (intensity) of
            each note in the pattern, allowing for dynamic variations.
        """
        #  for perc, pattern in pattern_set.items():
            #  b = int(duration / len(pattern))
            #  self.kit[perc].add_pattern(pattern, b, velocity_mod=velocity_mod)
        for perc_name, perc in self.kit.items():
            if perc_name in pattern_set:
                pattern = pattern_set[perc_name]
                b = int(duration / len(pattern))
                perc.add_pattern(pattern, b, velocity_mod=velocity_mod)
            else:
                perc.set_rest(duration)
                

    def load_patterns(self, yaml_file_name: str):
        """
        load patterns from associated yaml file
        """
        # TODO: if no file name - get yaml file with same name as script
        script_dir = Path(__file__).parent.absolute()
        yaml_file_path = script_dir / yaml_file_name

        with open(yaml_file_path, "r") as f:
            self.patterns = yaml.safe_load(f)

```

## src/harmonic_resonance/midiator/percussions/kits/standard.py

```py
import harmonic_resonance.midiator as hrm
from harmonic_resonance.midiator.percussions.kits import Kit
from harmonic_resonance.midiator.percussions.percussion import Percussion
import harmonic_resonance.midiator.percussions.percussion_types as P

class Standard(Kit):
    def __init__(self, part):
        """Initialize a standard drum kit with the given MIDI part."""
        super().__init__(part)
        self.kick = Percussion(part, P.acoustic_bass_drum)
        self.snare = Percussion(part, P.acoustic_snare)
        self.closed_hh = Percussion(part, P.closed_hi_hat)
        self.open_hh = Percussion(part, P.open_hi_hat)
        self.ride = Percussion(part, P.ride_cymbal_1)

        self.load_patterns('standard.yaml')

        self.kit = {
            "kick": self.kick,
            "snare": self.snare,
            "closed_hh": self.closed_hh,
            "open_hh": self.open_hh,
            "ride": self.ride,
        }


if __name__ == "__main__":
    PROJECT = "percussion"
    title = "standard demo"
    bpm = 120  # beats per minute
    bpM = 4  # beats per Measure

    part = hrm.Part(PROJECT, title, bpm=bpm)
    M = part.measure_ticks()

    standard = hrm.Standard(part)
    for pattern_name, pattern in standard.patterns.items():
        #  patterns = standard.patterns["funky_drummer"]
        part.set_marker(pattern_name, 2 * M)
        standard.set_patterns(pattern, M)
        standard.set_patterns(pattern, M)

    part.save()
    part.play()



```

## src/harmonic_resonance/midiator/percussions/patterns/__init__.py

```py
from . import swing
from . import funky
from . import techno
from . import latin

```

## src/harmonic_resonance/midiator/percussions/patterns/funky.py

```py

def billie_jean(length, kick, snare, hihat_closed):
    length = int(length)
    b = int(length/16)
    kick.set_hit(8 * b, velocity=100)
    kick.set_hit(8 * b, velocity=90)
    for _ in range(2):
        snare.set_rest(4 * b)
        snare.set_hit(4 * b)
    hihat_closed.set_hits(length, 8)


def funky_drummer(length, kick, snare, hihat_closed, hihat_open):
    length = int(length)
    b = int(length/16)
    kick.set_hit(2 * b, velocity=100)
    kick.set_hit(4 * b, velocity=90)
    kick.set_hit(4 * b, velocity=90)
    kick.set_hit(3 * b, velocity=90)
    kick.set_hit(3 * b, velocity=90)
    snare.set_rest(4 * b)
    snare.set_hit(3 * b)
    snare.set_hit(2 * b)
    snare.set_hit(2 * b)
    snare.set_hit(1 * b)
    snare.set_hit(3 * b)
    snare.set_hit(1 * b)
    hihat_closed.set_hits(7 * b, 7)
    hihat_closed.set_rest(1 * b)
    hihat_closed.set_hits(5 * b, 5)
    hihat_closed.set_rest(1 * b)
    hihat_closed.set_hits(2 * b, 2)
    hihat_open.set_rest(7 * b)
    hihat_open.set_hit(6 * b)
    hihat_open.set_hit(3 * b)
    

def jungle(length, kick, snare, hihat_closed, hihat_open):
    length = int(length)
    b = int(length/32)
    hihat_open.set_hit(length, velocity=90)
    kick.set_hit(2 * b, velocity=90)
    kick.set_hit(8 * b, velocity=70)
    kick.set_hit(7 * b, velocity=90)
    kick.set_hit(1 * b, velocity=70)
    kick.set_hit(8 * b, velocity=70)
    kick.set_hit(6 * b, velocity=70)
    hihat_closed.set_hits(length, 16)
    snare.set_rest(4 * b)
    snare.set_hit(3 * b, velocity=90)
    snare.set_hit(2 * b, velocity=60)
    snare.set_hit(5 * b, velocity=60)
    snare.set_hit(3 * b, velocity=90)
    snare.set_hit(3 * b, velocity=60)
    snare.set_hit(3 * b, velocity=60)
    snare.set_hit(2 * b, velocity=60)
    snare.set_hit(5 * b, velocity=60)
    snare.set_hit(2 * b, velocity=60)


```

## src/harmonic_resonance/midiator/percussions/patterns/latin.py

```py
from ..percussion import Percussion


def son_clave2(duration, perc: Percussion, velocity_mod=0):
    """3:2 pattern
    2 measures of eigth notes"""
    b = int(duration / 16)
    pattern = "5__3__5_"
    pattern += "__5_3___"
    perc.add_pattern(pattern, b, velocity_mod=velocity_mod)


#  def son_clave(duration, kick, tick, ride, velocity_mod=0):
#  """
#  duration is 2 measure
#  """
#  duration = int(duration)
#  b = int(duration/16)
#  for _ in range(4):
#  kick.set_hit(3 * b, velocity=90+velocity_mod)
#  kick.set_hit(1 * b, velocity=60+velocity_mod)

#  run = [3, 3, 4, 2, 4]
#  for r in run:
#  tick.set_hit(r * b, velocity=90+velocity_mod)

#  ride.set_hits(duration, 16, velocity=60+velocity_mod)


def rhumba(duration, kick, tick, ride, velocity_mod=0):
    """
    duration is 2 measure
    """
    duration = int(duration)
    b = int(duration / 16)
    #  for _ in range(4):
    #  kick.set_hit(3 * b, velocity=90+velocity_mod)
    #  kick.set_hit(1 * b, velocity=60+velocity_mod)
    pattern = "6__46__4"
    pattern += "6__46__4"
    kick.add_pattern(pattern, b, velocity_mod=velocity_mod)

    #  run = [3, 4, 3, 2, 4]
    #  for r in run:
        #  tick.set_hit(r * b, velocity=90 + velocity_mod)
    pattern =  "5__3___5"
    pattern += "__5_3___"
    tick.add_pattern(pattern, b, velocity_mod=velocity_mod)

    ride.set_hits(duration, 16, velocity=60 + velocity_mod)


def bossa_nova(duration, kick, tick, ride, velocity_mod=0):
    """
    duration is 2 measure
    """
    duration = int(duration)
    b = int(duration / 16)
    for _ in range(4):
        kick.set_hit(3 * b, velocity=90 + velocity_mod)
        kick.set_hit(1 * b, velocity=60 + velocity_mod)

    run = [3, 3, 4, 3, 3]
    for r in run:
        tick.set_hit(r * b, velocity=30 + velocity_mod)

    ride.set_hits(duration, 16, velocity=60 + velocity_mod)

```

## src/harmonic_resonance/midiator/percussions/patterns/swing.py

```py



def swing(length, kick, ride):
    length = int(length)
    b = int(length/12)
    # 3____43__4_3
    kick.set_hit(5 * b)
    kick.set_hit(1 * b)
    ride.set_hit(3 * b)
    ride.set_hit(2 * b, velocity=80)
    ride.set_hit(1 * b)


```

## src/harmonic_resonance/midiator/percussions/patterns/techno.py

```py

def deep_house(length, kick, clap, hihat_closed, hihat_open):
    length = int(length)
    b = int(length/32)
    kick.set_hits(length, 8, velocity=90)

    hihat_open.set_rest(2 * b)
    hihat_open.set_hit(4 * b, velocity=90)
    hihat_open.set_hit(4 * b, velocity=60)
    hihat_open.set_hit(4 * b, velocity=90)
    hihat_open.set_hit(4 * b, velocity=60)
    hihat_open.set_hit(4 * b, velocity=90)
    hihat_open.set_hit(4 * b, velocity=60)
    hihat_open.set_hit(4 * b, velocity=90)
    hihat_open.set_hit(2 * b, velocity=60)

    hihat_closed.set_rest(1 * b)
    hihat_closed.set_hit(6 * b, velocity=90)
    hihat_closed.set_hit(2 * b, velocity=60)
    hihat_closed.set_hit(8 * b, velocity=60)
    hihat_closed.set_hit(6 * b, velocity=90)
    hihat_closed.set_hit(2 * b, velocity=60)
    hihat_closed.set_hit(7 * b, velocity=60)

    clap.set_rest(4 * b)
    clap.set_hit(8 * b, velocity=90)
    clap.set_hit(8 * b, velocity=90)
    clap.set_hit(8 * b, velocity=90)
    clap.set_hit(4 * b, velocity=90)

def drum_bass(length, kick, snare, hihat_closed, hihat_open):
    length = int(length)
    b = int(length/32)
    hihat_open.set_hit(length, velocity=90)
    kick.set_hit(6 * b, velocity=90)
    kick.set_hit(10 * b, velocity=70)
    kick.set_hit(10 * b, velocity=90)
    kick.set_hit(6 * b, velocity=70)
    hihat_closed.set_hits(length, 16)
    snare.set_rest(4 * b)
    snare.set_hit(6 * b, velocity=90)
    snare.set_hit(2 * b, velocity=60)
    snare.set_hit(8 * b, velocity=60)
    snare.set_hit(8 * b, velocity=90)
    snare.set_hit(4 * b, velocity=60)


```

## src/harmonic_resonance/midiator/scales/__init__.py

```py
'''utils for building scales'''
from . import scale_types as S

def build_scale(root=48, scale_type=S.major, octaves=3):
    notes = [root]
    scale = S.SCALES[scale_type]
    for octave in range(octaves):
        jump = 0
        for interval in scale:
            jump += interval
            note = (octave * 12) + root + jump
            notes.append(note)
    return notes

class Scale(dict):
    #  notes = {}
    def __init__(self, root, scale_type, octaves=1):
        """TODO: Docstring for __init__.

        :root: TODO
        :scale_type: TODO
        :octaves: TODO

        """
        pos = 1
        #  self.notes[pos] = root
        self[pos] = root
        self.root = root
        self.intervals = S.SCALES[scale_type]
        for octave in range(octaves):
            jump = 0
            for interval in self.intervals:
                jump += interval
                pos += 1
                note = (octave * 12) + root + jump
                self[pos] = note


class Key():
    """
    generate classic key offsets for a root note
    """
    _pos = dict()

    def __init__(self, root: int):
        root = int(root)
        self.root = root
        self.I = root
        self.II = root + 2
        self.III = root + 4
        self.IV = root + 5
        self.V = root + 7
        self.VI = root + 9
        self.VII = root + 11

        self._pos[1] = self.I
        self._pos[2] = self.II
        self._pos[3] = self.III
        self._pos[4] = self.IV
        self._pos[5] = self.V
        self._pos[6] = self.VI
        self._pos[7] = self.VII

    def position(self, num: int):
        """
        numeric position
        """
        return self._pos[num]

```

## src/harmonic_resonance/midiator/scales/scale_types.py

```py

major = 'major'
minor = 'minor'
melodic_minor = 'melodicminor'
harmonic_minor = 'harmonicminor'
pentatonic_major = 'pentatonicmajor'
blues_major = 'bluesmajor'
pentatonic_minor = 'pentatonicminor'
blues_minor = 'bluesminor'
augmented = 'augmented'
diminished = 'diminished'
chromatic = 'chromatic'
whole_half = 'wholehalf'
half_whole = 'halfwhole'
whole_tone = 'wholetone'
augmented_fifth = 'augmentedfifth'
japanese = 'japanese'
oriental = 'oriental'
ionian = 'ionian'
dorian = 'dorian'
phrygian = 'phrygian'
lydian = 'lydian'
mixolydian = 'mixolydian'
aeolian = 'aeolian'
locrian = 'locrian'

SCALES = {
    'major': (2, 2, 1, 2, 2, 2, 1),
    'minor': (2, 1, 2, 2, 1, 2, 2),
    'melodicminor': (2, 1, 2, 2, 2, 2, 1),
    'harmonicminor': (2, 1, 2, 2, 1, 3, 1),
    'pentatonicmajor': (2, 2, 3, 2, 3),
    'bluesmajor': (3, 2, 1, 1, 2, 3),
    'pentatonicminor': (3, 2, 2, 3, 2),
    'bluesminor': (3, 2, 1, 1, 3, 2),
    'augmented': (3, 1, 3, 1, 3, 1),
    'diminished': (2, 1, 2, 1, 2, 1, 2, 1),
    'chromatic': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    'wholehalf': (2, 1, 2, 1, 2, 1, 2, 1),
    'halfwhole': (1, 2, 1, 2, 1, 2, 1, 2),
    'wholetone': (2, 2, 2, 2, 2, 2),
    'augmentedfifth': (2, 2, 1, 2, 1, 1, 2, 1),
    'japanese': (1, 4, 2, 1, 4),
    'oriental': (1, 3, 1, 1, 3, 1, 2),
    'ionian': (2, 2, 1, 2, 2, 2, 1),
    'dorian': (2, 1, 2, 2, 2, 1, 2),
    'phrygian': (1, 2, 2, 2, 1, 2, 2),
    'lydian': (2, 2, 2, 1, 2, 2, 1),
    'mixolydian': (2, 2, 1, 2, 2, 1, 2),
    'aeolian': (2, 1, 2, 2, 1, 2, 2),
    'locrian': (1, 2, 2, 1, 2, 2, 2),
}

```

## src/harmonic_resonance/midiator/voices/__init__.py

```py
from .voice import Voice
from . import voice_types as V

def make_solo_ooh(mf):
    return Voice(mf, voice_name=V.solo_ooh)

def make_solo_aah(mf):
    return Voice(mf, voice_name=V.solo_aah)

def make_choir_aah(mf):
    return Voice(mf, voice_name=V.choir_aah)

def make_choir_ooh(mf):
    return Voice(mf, voice_name=V.choir_ooh)

def make_choir_mixed(mf):
    return Voice(mf, voice_name=V.choir_mixed)

def make_choir_swell(mf):
    return Voice(mf, voice_name=V.choir_swell)

def make_choir_little_swell(mf):
    return Voice(mf, voice_name=V.choir_little_swell)

```

## src/harmonic_resonance/midiator/voices/voice.py

```py
import harmonic_resonance.midiator as pm
from . import voice_types as V
from ..instruments import Instrument

class Voice(Instrument):
    """Voice is a special instrument that connects to a separate
    soundfont specified in the timidity config"""

    def __init__(self, mf, voice_name: str, channel: int):
        """TODO: to be defined. """
        voice_dict = V.VOICES[voice_name]
        self.name = voice_name
        self.instrument = voice_dict['program']
        self.channel = channel

        self.track = mf.add_track(name=self.name)

        self.track.append(pm.Message(
            'control_change',
            control =  0,
            value = voice_dict['bank'],
            channel = self.channel,
            time = 0
        ))
        self.track.append(pm.Message(
            'control_change',
            control = 32,
            value = voice_dict['subbank'],
            channel = self.channel,
            time = 0
        ))
        self.track.append(pm.Message(
            'program_change',
            program = voice_dict['program'],
            channel = self.channel,
            time = 1))

        self.track_volume = mf.add_track(name=f'{self.name}-volume')
        self.track_pan = mf.add_track(name=f'{self.name}-pan')



```

## src/harmonic_resonance/midiator/voices/voice_types.py

```py

VOICES = {
    'Solo Ooh': {'bank': 1, 'subbank': 0, 'channel': 8, 'program': 0},
    'Solo Aah': {'bank': 1, 'subbank': 0, 'channel': 10, 'program': 1},
    'Mixed Choir': {'bank': 1, 'subbank': 0, 'channel': 11, 'program': 2},
    'Little Swell Choir': {'bank': 1, 'subbank': 0, 'channel': 12, 'program': 3},
    'Swell Choir': {'bank': 1, 'subbank': 0, 'channel': 13, 'program': 4},
    'Choir Ooh': {'bank': 1, 'subbank': 0, 'channel': 14, 'program': 5},
    'Choir Aah': {'bank': 1, 'subbank': 0, 'channel': 15, 'program': 6},
}

solo_ooh = 'Solo Ooh'
solo_aah = 'Solo Aah'
choir_mixed = 'Mixed Choir'
choir_little_swell = 'Little Swell Choir'
choir_swell = 'Swell Choir'
choir_ooh = 'Choir Ooh'
choir_aah = 'Choir Aah'

```

