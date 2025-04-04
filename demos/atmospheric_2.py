"""
Atmospheric Composition 2: Gentle pads with a simple melody.
"""
import harmonic_resonance.midiator as pm
import random
from rich import print as log

# 1. Project Setup
PROJECT = "demos"
title = "atmospheric_2"
bpm = 65  # Slightly faster than the previous, but still slow
bpM = 4
root = pm.N.C4  # C Major for a gentler feel
key = "C"

part = pm.Part(PROJECT, title, bpm=bpm, bpM=bpM, root=root, key=key)
M = part.measure_ticks()  # Ticks per measure
b = part.ticks_per_beat # Ticks per beat

# 2. Musical Foundation - Simple Major Chord Progression (I - IV - V - I)
chords_notes = [
    ("Cmaj7", pm.get_chord_notes(root, pm.C.major_7)),
    ("Fmaj7", pm.get_chord_notes(root + 5, pm.C.major_7)), # Fmaj7
    ("G7", pm.get_chord_notes(root + 7, pm.C.dominant_7)), # G7
    ("Cmaj7", pm.get_chord_notes(root, pm.C.major_7)),
]

# 3. Instrumentation - Atmospheric Choices + Melody
pad_warm = part.add_instrument(pm.I.pad_2_warm)
pad_halo = part.add_instrument(pm.I.pad_7_halo)
fx_atmosphere = part.add_instrument(pm.I.fx_4_atmosphere)
vibes = part.add_instrument(pm.I.vibraphone) # Gentle melody instrument

# Initial volumes
pad_warm.set_volume(0, 0)
pad_halo.set_volume(0, 0)
fx_atmosphere.set_volume(55, 0) # Slightly lower atmosphere
vibes.set_volume(70, 0) # Moderate volume for vibes melody

# 4. Structure and Arrangement - Long notes, swells, sparse melody
total_loops = 3
measures_per_chord = 4 # Hold chords for a long time
chord_duration = measures_per_chord * M
total_duration = len(chords_notes) * chord_duration * total_loops

part.set_marker("Start", 0)

# --- FX Layer ---
# Play the atmosphere sound throughout
fx_atmosphere.set_note(root + 12, total_duration, velocity=50) # High C drone

# --- Pad Layers & Melody ---
current_time = 0
for loop in range(total_loops):
    part.set_marker(f"Loop {loop+1}", current_time)
    for chord_idx, (chord_name, chord) in enumerate(chords_notes):
        part.set_marker(f"{chord_name}", current_time)

        # Pad Warm - Low register, slow swell in and out
        pad_warm_chord = [n - 12 for n in chord] # Octave down
        pad_warm.set_volume(0, 0)
        pad_warm.ramp_volume_up(chord_duration / 2, lo=0, hi=65)
        pad_warm.set_notes(pad_warm_chord, chord_duration, velocity=75)
        pad_warm.ramp_volume_down(chord_duration / 2, lo=0, hi=65)

        # Pad Halo - Higher register, different swell
        pad_halo_chord = chord # Use original octave
        pad_halo.set_rest(M / 2) # Enter slightly later
        pad_halo.set_volume(0, 0)
        pad_halo.ramp_volume_up(chord_duration - M/2, lo=0, hi=50)
        pad_halo.set_notes(pad_halo_chord, chord_duration - M/2, velocity=65)

        # --- Gentle Vibraphone Melody ---
        # Simple pattern: Play 1st and 3rd notes of the chord (higher octave)
        # Hold each for almost 2 measures with a rest in between
        melody_note_1 = chord[0] + 12 # First note, octave up
        melody_note_2 = chord[2] + 12 # Third note, octave up
        note_duration = M * 2 - b # Hold for almost 2 measures
        rest_duration = b # Short rest

        vibes.set_note(melody_note_1, note_duration, velocity=60)
        vibes.set_rest(rest_duration)
        vibes.set_note(melody_note_2, note_duration, velocity=55)
        vibes.set_rest(rest_duration)

        current_time += chord_duration


# Fade out everything at the end
part.set_marker("Fade Out", current_time)
fade_duration = 2 * M
pad_warm.ramp_volume_down(fade_duration, lo=0)
pad_halo.ramp_volume_down(fade_duration, lo=0)
fx_atmosphere.ramp_volume_down(fade_duration, lo=0)
vibes.ramp_volume_down(fade_duration, lo=0) # Fade out vibes too

# 5. Final Output
part.save()
part.play()
# part.convert() # Uncomment to generate audio file
