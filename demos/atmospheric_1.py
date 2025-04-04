"""
Atmospheric Composition 1: Slow pads and evolving textures.
"""
import harmonic_resonance.midiator as pm
import random
from rich import print as log

# 1. Project Setup
PROJECT = "demos"
title = "atmospheric_1"
bpm = 60  # Slow tempo for atmosphere
bpM = 4
root = pm.N.C3  # C minor for a darker feel
key = "Cm"

part = pm.Part(PROJECT, title, bpm=bpm, bpM=bpM, root=root, key=key)
M = part.measure_ticks()  # Ticks per measure
b = part.ticks_per_beat # Ticks per beat

# 2. Musical Foundation - Simple Minor Chord Progression (i - VI)
# i = Cm = C Eb G
# VI = Ab = Ab C Eb (relative to C)
chords_notes = [
    ("Cm", pm.get_chord_notes(root, pm.C.minor)),
    ("Ab", pm.get_chord_notes(root + 8, pm.C.major)), # Ab Major
]

# 3. Instrumentation - Atmospheric Choices
pad_warm = part.add_instrument(pm.I.pad_2_warm)
pad_halo = part.add_instrument(pm.I.pad_7_halo)
fx_atmosphere = part.add_instrument(pm.I.fx_4_atmosphere)
# Optional: Add a subtle percussion element like a tinkle bell or reverse cymbal
# tinkle = part.add_instrument(pm.I.tinkle_bell)
reverse_cymbal = part.add_instrument(pm.I.reverse_cymbal)


# Initial volumes
pad_warm.set_volume(0, 0)
pad_halo.set_volume(0, 0)
fx_atmosphere.set_volume(60, 0) # Start atmosphere sound at moderate volume
# tinkle.set_volume(40, 0)
reverse_cymbal.set_volume(50, 0)


# 4. Structure and Arrangement - Long notes, swells, sparse events
total_duration_measures = 16
measures_per_chord = 4 # Hold chords for a long time
chord_duration = measures_per_chord * M

part.set_marker("Start", 0)

# --- FX Layer ---
# Play the atmosphere sound throughout, maybe with slight variation
fx_atmosphere.set_note(root + 24, total_duration_measures * M, velocity=60) # High C drone

# --- Pad Layers ---
current_time = 0
for i in range(total_duration_measures // measures_per_chord):
    chord_idx = i % len(chords_notes) # Cycle through chords
    chord_name, chord = chords_notes[chord_idx]
    part.set_marker(f"{chord_name}", current_time)

    # Pad Warm - Low register, slow swell in and out
    pad_warm_chord = [n - 12 for n in chord] # Octave down
    pad_warm.set_volume(0, 0) # Ensure start volume is 0 before swell
    pad_warm.ramp_volume_up(chord_duration / 2, lo=0, hi=70)
    pad_warm.set_notes(pad_warm_chord, chord_duration, velocity=80) # Velocity affects timbre too
    pad_warm.ramp_volume_down(chord_duration / 2, lo=0, hi=70) # Fade out in second half

    # Pad Halo - Higher register, enters slightly later, different swell
    pad_halo_chord = [n + 12 for n in chord] # Octave up
    pad_halo.set_rest(M) # Enter after one measure
    pad_halo.set_volume(0, 0)
    pad_halo.ramp_volume_up(chord_duration - M, lo=0, hi=55) # Slower fade in
    pad_halo.set_notes(pad_halo_chord, chord_duration - M, velocity=70)
    # Let halo pad ring until the next chord starts its swell

    # --- Sparse Percussion ---
    # Add a reverse cymbal hit at the start of each chord change
    # Note: Reverse Cymbal is an Instrument Type (pm.I), not Percussion (pm.P)
    # We use set_note on the instrument instance 'reverse_cymbal' we created earlier.
    # The first argument to set_note should be the MIDI note number for the sound.
    # For GM sounds like Reverse Cymbal (119), the note number often doesn't matter
    # as much as the program change, but we still need to provide one. Let's use C5 (72).
    reverse_cymbal.set_note(pm.N.C5, M, velocity=60) # Use a standard note like C5
    reverse_cymbal.set_rest(chord_duration - M) # Rest until next chord

    # Optional: Add a random tinkle bell note occasionally
    # if random.random() < 0.3: # 30% chance per chord change
    #     tinkle_note = random.choice(chord) + 24 # High note from the current chord
    #     tinkle_rest_before = random.uniform(0.5, 2.5) * M # Random time within the chord
    #     tinkle.set_rest(tinkle_rest_before)
    #     tinkle.set_note(tinkle_note, M / 2, velocity=50)
    #     tinkle.set_rest(chord_duration - tinkle_rest_before - (M / 2))
    # else:
    #     tinkle.set_rest(chord_duration)


    current_time += chord_duration


# Fade out everything at the end
part.set_marker("Fade Out", current_time)
fade_duration = 2 * M
pad_warm.ramp_volume_down(fade_duration, lo=0) # Fade from current volume
pad_halo.ramp_volume_down(fade_duration, lo=0)
fx_atmosphere.ramp_volume_down(fade_duration, lo=0)
reverse_cymbal.set_rest(fade_duration)
# tinkle.set_rest(fade_duration)

# Final silence is achieved by instruments ending or fading out.
# No explicit part.set_rest() is needed.


# 5. Final Output
part.save()
part.play()
# part.convert() # Uncomment to generate audio file
