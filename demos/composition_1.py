"""
Composition 1: A simple piece using I-vi-ii-V in C minor.
"""
import harmonic_resonance.midiator as pm
from rich import print as log

# 1. Project Setup
PROJECT = "demos"
title = "composition_1"
bpm = 100
bpM = 4
root = pm.N.C3  # C minor
key = "Cm"

part = pm.Part(PROJECT, title, bpm=bpm, bpM=bpM, root=root, key=key)
M = part.measure_ticks()  # Ticks per measure

# 2. Musical Foundation
# Using i-VI-ii-V in C minor (relative major is Eb)
# Note: progressions often use relative major scale for naming, but root defines key
# Let's define it manually for clarity in C minor scale context
# C minor scale notes (relative to C): 0, 2, 3, 5, 7, 8, 10
# i = Cm7 = C, Eb, G, Bb = root, root+3, root+7, root+10
# VI = AbM7 = Ab, C, Eb, G = root+8, root+12, root+15, root+19 (relative to C3)
# ii = Dm7b5 = D, F, Ab, C = root+2, root+5, root+8, root+12 (relative to C3)
# V = G7 = G, B, D, F = root+7, root+11, root+14, root+17 (relative to C3)

chords_notes = [
    ("Cm7", pm.get_chord_notes(pm.N.C3, pm.C.minor_7)),
    ("AbM7", pm.get_chord_notes(pm.N.Gs3, pm.C.major_7)), # Ab3 is enharmonically Gs3
    ("Dm7b5", pm.get_chord_notes(pm.N.D3, pm.C.minor_7)[:-1] + [pm.N.Gs3]), # Manual m7b5, using Gs3 for Ab3
    ("G7", pm.get_chord_notes(pm.N.G3, pm.C.dominant_7)),
]


# 3. Instrumentation
standard_kit = pm.Standard(part)
bass = part.add_instrument(pm.I.electric_bass_finger)
piano = part.add_instrument(pm.I.electric_piano_1) # Using Electric Piano 1
strings = part.add_instrument(pm.I.string_ensemble_1)

# Initial rests/volumes
piano.set_rest(0) # Start immediately but might be overwritten
strings.set_rest(0)
strings.set_volume(0, 0) # Start strings silent

# 4. Structure and Arrangement
num_loops = 4
measures_per_chord = 2 # Each chord lasts 2 measures

part.set_marker("Start", 0)

for loop in range(num_loops):
    part.set_marker(f"Loop {loop + 1}", 0)
    for chord_idx, (chord_name, chord) in enumerate(chords_notes):
        part.set_marker(f"{chord_name}", 0)
        chord_duration = measures_per_chord * M

        # --- Percussion ---
        if loop == 0 and chord_idx == 0: # Start drums slightly later
             standard_kit.rest_all(M // 2)
             standard_kit.set_patterns(standard_kit.patterns["four"], M // 2, velocity_mod=-15)
             standard_kit.set_patterns(standard_kit.patterns["four"], M, velocity_mod=-15)
        elif chord_idx == len(chords_notes) - 1: # Last chord of progression
            # Play regular pattern for first measure
            standard_kit.set_patterns(standard_kit.patterns["four"], M, velocity_mod=-15)
             # Simple fill in the second measure (snare on 2 and 4, kick on 1)
            standard_kit.kick.set_hit(M / 4)
            standard_kit.kick.set_rest(M / 4)
            standard_kit.snare.set_hit(M / 4)
            standard_kit.snare.set_rest(M / 4)
            # Silence others for the fill measure
            standard_kit.closed_hh.set_rest(M)
            standard_kit.open_hh.set_rest(M)
            standard_kit.ride.set_rest(M)
        else:
            # Regular beat
            standard_kit.set_patterns(standard_kit.patterns["four"], chord_duration, velocity_mod=-15)

        # --- Bass ---
        # Simple root notes on the downbeat of each measure
        bass_note = chord[0] - 12 # Play bass note one octave lower
        bass.set_note(bass_note, M, velocity=80)
        bass.set_note(bass_note, M, velocity=80)

        # --- Piano ---
        if loop >= 1: # Introduce piano in the second loop
            piano_chord = [n + 12 for n in chord] # Play piano chord one octave higher
            # Play chord on the first beat of each measure
            piano.set_notes(piano_chord, M, velocity=65)
            piano.set_notes(piano_chord, M, velocity=65)
        else:
            piano.set_rest(chord_duration)

        # --- Strings ---
        if loop >= 2: # Introduce strings in the third loop
            string_chord = [n + 12 for n in chord] # Use same octave as piano
            if chord_idx == 0 and loop == 2: # Fade in strings at the start of loop 3
                 strings.set_volume(0, 0)
                 strings.ramp_volume_up(chord_duration, lo=0, hi=50)
                 strings.set_notes(string_chord, chord_duration, velocity=70)
            else:
                 strings.set_volume(50, 0) # Maintain volume
                 strings.set_notes(string_chord, chord_duration, velocity=70)
        else:
            strings.set_rest(chord_duration)
            strings.set_volume(0, chord_duration) # Ensure strings stay silent


# Fade out at the end
standard_kit.rest_all(M) # One extra measure rest for drums
bass.set_rest(M)
piano.set_rest(M)
strings.ramp_volume_down(M, lo=0, hi=50) # Fade out strings over one measure
strings.set_rest(M) # Ensure final note off


# 5. Final Output
part.save()
part.play()
# part.convert() # Uncomment to generate audio file
