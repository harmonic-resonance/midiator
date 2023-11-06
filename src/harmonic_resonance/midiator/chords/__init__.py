#  import phimidi.chords.chord_types as C
from . import chord_types as C
from . import progressions

def get_chord_notes(root, chord_type):
    notes = []
    chord_intervals = C.CHORDS[chord_type]
    for interval in chord_intervals:
        notes.append(root + interval)
    return notes
    
