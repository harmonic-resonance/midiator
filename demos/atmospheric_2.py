"""
Atmospheric Composition 2: Gentle pads with a simple melody.
"""
import harmonic_resonance.midiator as pm
from harmonic_resonance.midiator.scales import Scale # Import Scale
import random
from rich import print as log

# 1. Project Setup
PROJECT = "demos"
title = "atmospheric_2"
bpm = 65  # Slightly faster than the previous, but still slow
bpM = 4
root = pm.N.C4  # C Major for a gentler feel
key = "C"
key_scale_type = pm.S.major # Use the major scale type

part = pm.Part(PROJECT, title, bpm=bpm, bpM=bpM, root=root, key=key)
M = part.measure_ticks()  # Ticks per measure
b = part.ticks_per_beat # Ticks per beat

# Define key notes for melody generation (e.g., C3 to C6)
key_notes_scale = Scale(root - 12, key_scale_type, octaves=3) # C3 to C5 range
key_notes = list(key_notes_scale.notes.values())

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

# 4. Structure and Arrangement - Long notes, swells, dynamic melody
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

        # --- Dynamic Vibraphone Melody ---
        # Combine chord notes (original, +12) and key notes for selection pool
        chord_notes_melody_range = [n for n in chord] + [n + 12 for n in chord]
        available_notes = sorted(list(set(chord_notes_melody_range + key_notes)))
        # Filter notes to a reasonable range (e.g., C3 to C7)
        available_notes = [n for n in available_notes if pm.N.C3 <= n <= pm.N.C7]

        possible_durations = [b / 2, b, b * 1.5, b * 2] # Eighth, quarter, dotted q, half
        last_note = root + 12 # Start melody near C5

        for measure in range(measures_per_chord):
            measure_time_elapsed = 0
            while measure_time_elapsed < M:
                # Ensure duration doesn't exceed measure boundary
                remaining_time = M - measure_time_elapsed
                valid_durations = [d for d in possible_durations if d <= remaining_time]
                if not valid_durations: # Should not happen if M is multiple of b/2
                     duration = remaining_time
                else:
                    duration = random.choice(valid_durations)

                # Decide note or rest
                if random.random() < 0.85: # 85% chance of playing a note
                    # Select note: 70% chord tone (any octave), 30% key tone
                    if random.random() < 0.70 and chord_notes_melody_range:
                        note_pool = [n for n in chord_notes_melody_range if pm.N.C3 <= n <= pm.N.C7]
                        if not note_pool: # Fallback if chord notes out of range
                             note_pool = available_notes
                    else:
                        note_pool = available_notes

                    # Avoid large leaps sometimes by biasing towards notes near the last one
                    if last_note and random.random() < 0.6: # 60% chance to bias
                        notes_with_distance = sorted([(abs(n - last_note), n) for n in note_pool])
                        # Prefer notes within an octave jump
                        close_notes = [n for dist, n in notes_with_distance if dist <= 12]
                        if close_notes:
                            note_to_play = random.choice(close_notes)
                        else: # If no notes within an octave, pick the absolute closest
                            note_to_play = notes_with_distance[0][1]
                    else: # Pick randomly from the selected pool
                         note_to_play = random.choice(note_pool)


                    velocity = random.randint(55, 80)
                    vibes.set_note(note_to_play, duration, velocity=velocity)
                    last_note = note_to_play
                else:
                    # Play a rest
                    vibes.set_rest(duration)
                    # Don't reset last_note during rests

                measure_time_elapsed += duration

        current_time += chord_duration


# Fade out everything at the end
part.set_marker("Fade Out", current_time)
fade_duration = 2 * M
pad_warm.ramp_volume_down(fade_duration, lo=0)
pad_halo.ramp_volume_down(fade_duration, lo=0)
fx_atmosphere.ramp_volume_down(fade_duration, lo=0)
#  vibes.ramp_volume_down(fade_duration, lo=0) # Fade out vibes too

# 5. Final Output
part.save()
part.play()
# part.convert() # Uncomment to generate audio file
