"""
Composition: A simple jazz piece using ii-V-I in F major.
"""
import harmonic_resonance.midiator as pm
import random
from rich import print as log

# 1. Project Setup
PROJECT = "demos"
title = "jazz_1"
bpm = 130  # Moderate swing tempo
bpM = 4
root = pm.N.F3  # F Major
key = "F"

part = pm.Part(PROJECT, title, bpm=bpm, bpM=bpM, root=root, key=key)
M = part.measure_ticks()  # Ticks per measure
b = part.ticks_per_beat # Ticks per beat (quarter note)

# 2. Musical Foundation
# ii-V-I-I in F Major
# ii = Gm7 (G Bb D F)
# V = C7 (C E G Bb)
# I = FM7 (F A C E) or F6 (F A C D)
chords = pm.progressions.ii_V_I_I(root)

# 3. Instrumentation
standard_kit = pm.Standard(part)
bass = part.add_instrument(pm.I.acoustic_bass)
piano = part.add_instrument(pm.I.acoustic_grand_piano)

# Initial setup
standard_kit.ride.set_volume(70, 0) # Make ride prominent but not overpowering
standard_kit.kick.set_volume(80, 0)
standard_kit.closed_hh.set_volume(0, 0) # Silence HH initially, focus on ride
standard_kit.snare.set_volume(0, 0) # Silence snare initially
standard_kit.open_hh.set_volume(0, 0) # Silence open HH

# 4. Structure and Arrangement
num_loops = 4
measures_per_chord = 1 # Each chord lasts 1 measure in this progression

part.set_marker("Start", 0)

for loop in range(num_loops):
    part.set_marker(f"Loop {loop + 1}", 0)
    for chord_idx, (chord_name, chord) in enumerate(chords):
        part.set_marker(f"{chord_name}", 0)
        chord_duration = measures_per_chord * M

        # --- Percussion (Swing Ride Pattern) ---
        # Use the predefined swing pattern
        standard_kit.set_patterns(standard_kit.patterns["swing"], chord_duration, velocity_mod=-10)
        # Ensure other parts are silent if not in the pattern definition
        if "snare" not in standard_kit.patterns["swing"]: standard_kit.snare.set_rest(chord_duration)
        if "closed_hh" not in standard_kit.patterns["swing"]: standard_kit.closed_hh.set_rest(chord_duration)
        if "open_hh" not in standard_kit.patterns["swing"]: standard_kit.open_hh.set_rest(chord_duration)


        # --- Bass (Simple Walking: Root on 1, Fifth on 3) ---
        bass_note_root = chord[0] - 12 # Octave down
        # Find the fifth (usually 7 semitones above root)
        # Handle cases where chord might not have a perfect fifth easily defined
        bass_note_fifth = bass_note_root + 7

        bass.set_note(bass_note_root, b, velocity=85) # Beat 1
        bass.set_rest(b) # Beat 2 (rest for simplicity)
        bass.set_note(bass_note_fifth, b, velocity=75) # Beat 3
        bass.set_rest(b) # Beat 4 (rest for simplicity)


        # --- Piano (Comping with 7th chords, syncopated) ---
        piano_chord = chord # Use the 7th chords from the progression
        piano_chord_voiced = [n + 12 for n in piano_chord] # Voicing up one octave

        # Simple syncopated rhythm: hit on 'and' of 1, hold through 3
        piano.set_rest(b / 2) # Rest for first half of beat 1
        piano.set_notes(piano_chord_voiced, M - (b / 2), velocity=60) # Hit on 'and' of 1, hold


# Final Chord
part.set_marker("End Chord", 0)
final_chord_notes = pm.get_chord_notes(root, pm.C.major_7)
final_chord_voiced = [n + 12 for n in final_chord_notes]
piano.set_notes(final_chord_voiced, M, velocity=70)
bass.set_note(root - 12, M, velocity=80)
# Final ride hit
standard_kit.ride.set_hit(M, velocity=75)
standard_kit.kick.set_rest(M)
standard_kit.snare.set_rest(M)
standard_kit.closed_hh.set_rest(M)
standard_kit.open_hh.set_rest(M)


# 5. Final Output
part.save()
part.play()
# part.convert()
