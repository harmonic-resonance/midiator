"""
Love's in need of love today
Stevie Wonder
"""
import phimidi as pm
from rich import print as log

PROJECT = 'stevie'
bpm = 100  # beats per minute
bpM = 4  # beats per Measure
root = pm.N.Ds3  # the root note of the key
key = 'Eb'

part = pm.Part(PROJECT, 'loves-in-need', bpm=bpm, root=root, key=key)
M = bpM * part.ticks_per_beat  # ticks per Measure

piano = part.add_piano()
#  bass = part.add_bass()
#  strings = part.add_strings()

kick = pm.make_kick(part)
snare = pm.make_snare(part)
ride = pm.make_ride(part)
tick = pm.make_tick(part)

choir = part.add_choir_ooh()

verse_chords = [
        (pm.N.Ds3, pm.C.major,  M),
        (pm.N.Cs3, pm.C.diminished,  M),

        (pm.N.F3, pm.C.minor_7,  M),
        (pm.N.As3, pm.C.major_6,  M/2),
        (pm.N.As3, pm.C.major,  M/2),

        (pm.N.F3, pm.C.minor_7, M),
        (pm.N.As3, pm.C.major_6, M/2),
        (pm.N.As3, pm.C.major, M/2),

        (pm.N.Gs3, pm.C.major_7,  M/2),
        (pm.N.G3, pm.C.minor_7,  M/2),
        (pm.N.F3, pm.C.minor,  M/2),
        (pm.N.As3, pm.C.sus4,  M/2),
        ]

chorus_chords = [
        (pm.N.Ds3, pm.C.major,  M),
        (pm.N.C3, pm.C.minor,  M),
        (pm.N.G3, pm.C.minor_7,  M),
        (pm.N.G3, pm.C.minor_7,  M),

        (pm.N.F3, pm.C.minor_7,  M),
        (pm.N.F3, pm.C.minor_7,  M),
        (pm.N.C3, pm.C.minor,  M),
        (pm.N.As3, pm.C.sus4,  M/2),
        (pm.N.As3, pm.C.major,  M/2),

        ]

break_chords = [
        (pm.N.Ds3, pm.C.major,  M/2),
        (pm.N.As3, pm.C.minor,  M/2),
        (pm.N.Cs3, pm.C.diminished,  M/2),
        (pm.N.Cs3, pm.C.diminished,  M/2),

        (pm.N.F3, pm.C.minor_7,  M/2),
        (pm.N.F3, pm.C.minor_7,  M/2),
        (pm.N.Gs3, pm.C.minor_7,  M/2),
        (pm.N.Gs3, pm.C.minor,  M/2),
        ]

rhythm = pm.patterns.techno.drum_bass

kick.set_hit(M)
tick.set_hits(M, 4, velocity=20)
piano.set_rest(M)

for _ in range(2):
    kick.set_rest(4 * M)
    tick.set_rest(4 * M)
    for chord_num, (root, chord_type, duration) in enumerate(break_chords):
        piano.set_chord(root, duration, chord_type)

for verse in range(2):
    kick.set_hits(8 * M, 16)
    tick.set_hits(8 * M, 32, velocity=20)
    for chord_num, (root, chord_type, duration) in enumerate(verse_chords):
        piano.set_chord(root, duration, chord_type)

for chorus in range(2):
    kick.set_hits(8 * M, 16)
    tick.set_hits(8 * M, 32, velocity=20)
    for chord_num, (root, chord_type, duration) in enumerate(chorus_chords):
        piano.set_chord(root, duration, chord_type)



part.save()
part.play()
