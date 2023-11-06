'''
voices are contained in the KBH_Real_and_Swell_Choir.sf2 soundfont

timidity requires voices.cfg file to establish voices on bank 1
'''
import phimidi as pm
import subprocess as subprocess

PROJECT = 'phi-midi'
NAME = 'arps'

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

bpm = 120
tempo = int(pm.bpm2tempo(bpm))

root = pm.N.D3
octaves = 1
scale_type = pm.S.dorian

scale = pm.build_scale(
    root=root, 
    scale_type=scale_type, 
    octaves=octaves)

mf = pm.new_midi(title=title, tempo=tempo)
# one measure in ticks
M = 4 * mf.ticks_per_beat

EBCsA = [
        (pm.N.E4, M, pm.C.major),
        (pm.N.B3, M, pm.C.major),
        (pm.N.Cs4, M, pm.C.minor),
        (pm.N.A3, M, pm.C.major),
        ]
EAGsABE = [
        (pm.N.E4, M/2, pm.C.major),
        (pm.N.A4, M/2, pm.C.major),
        (pm.N.Gs4, M, pm.C.minor_7),
        (pm.N.A4, M/2, pm.C.major),
        (pm.N.B4, M/2, pm.C.dominant_7),
        (pm.N.E3, M, pm.C.major),
        ]
p3 = []
chord = pm.get_chord_notes(pm.N.C4, pm.C.major)
chord.append(pm.N.C3)
p3.append(chord)

chord = pm.get_chord_notes(pm.N.G4, pm.C.major)
chord.append(pm.N.D3)
p3.append(chord)

chord = pm.get_chord_notes(pm.N.C4, pm.C.major)
chord.append(pm.N.E3)
p3.append(chord)

chord = pm.get_chord_notes(pm.N.F4, pm.C.major)
chord.append(pm.N.F3)
p3.append(chord)

chord = pm.get_chord_notes(pm.N.G4, pm.C.major)
chord.append(pm.N.G3)
p3.append(chord)

chord = pm.get_chord_notes(pm.N.F4, pm.C.major)
chord.append(pm.N.A3)
p3.append(chord)

chord = pm.get_chord_notes(pm.N.G4, pm.C.major)
chord.append(pm.N.B3)
p3.append(chord)

chord = pm.get_chord_notes(pm.N.C4, pm.C.major)
p3.append(chord)

##########################
p4 = []
chord = pm.get_chord_notes(pm.N.C4, pm.C.major)
p4.append(chord)

chord = pm.get_chord_notes(pm.N.G4, pm.C.major)
chord.append(pm.N.B3)
p4.append(chord)

chord = pm.get_chord_notes(pm.N.A4, pm.C.minor)
chord.append(pm.N.A3)
p4.append(chord)

chord = pm.get_chord_notes(pm.N.A4, pm.C.minor)
chord.append(pm.N.G3)
p4.append(chord)

chord = pm.get_chord_notes(pm.N.F4, pm.C.major)
chord.append(pm.N.F3)
p4.append(chord)

chord = pm.get_chord_notes(pm.N.C4, pm.C.major)
chord.append(pm.N.E3)
p4.append(chord)

chord = pm.get_chord_notes(pm.N.D4, pm.C.minor_7)
chord.append(pm.N.D3)
p4.append(chord)

chord = pm.get_chord_notes(pm.N.C4, pm.C.major)
chord.append(pm.N.C3)
p4.append(chord)

#####################

p5 = [
        (pm.N.C4, M, pm.C.major),
        (pm.N.A3, M, pm.C.dominant_7),
        (pm.N.D3, M, pm.C.dominant_9),
        (pm.N.G3, M, pm.C.dominant_11),
        (pm.N.C3, M, pm.C.dominant_13),
        ]

choir = pm.make_choir_swell(mf)
vibes = pm.Instrument(mf, pm.I.vibraphone, 0)

for _ in range(2):
    for root, duration, chord_type in p5:
        choir.set_chord(root, duration, chord_type=chord_type)
        notes = pm.get_chord_notes(root, chord_type)
        while len(notes) < 8:
            notes.extend(notes[0:8-len(notes)])
        pm.add_arp_up(vibes, notes, duration)

choir.set_rest(M)
vibes.set_rest(M)

for _ in range(2):
    for root, duration, chord_type in EBCsA:
        choir.set_chord(root, duration, chord_type=chord_type)
        notes = pm.get_chord_notes(root, chord_type)
        notes.append(notes[1])
        pm.add_arp_up(vibes, notes, duration)
    for root, duration, chord_type in EBCsA:
        choir.set_chord(root, duration, chord_type=chord_type)
        notes = pm.get_chord_notes(root, chord_type)
        notes.append(notes[1])
        pm.add_arp_down(vibes, notes, duration)

choir.set_rest(M)
vibes.set_rest(M)


for _ in range(2):
    for root, duration, chord_type in EAGsABE:
        choir.set_chord(root, duration, chord_type=chord_type)
        notes = pm.get_chord_notes(root, chord_type)
        notes.append(notes[1])
        pm.add_arp_up(vibes, notes, duration)

choir.set_rest(M)
vibes.set_rest(M)



#  for _ in range(1):
    #  for chord in p3:
        #  main.set_notes(chord, M)
    #  main.set_rest(M)

#  for _ in range(1):
    #  for chord in p4:
        #  main.set_notes(chord, M)
    #  main.set_rest(M)

filepath = pm.save_midi(mf, folder, filename)

#  mf.print_tracks()

subprocess.run(["timidity", "-c", "voices.cfg", filepath])
#  subprocess.run(["timidity", filepath, "-c", "voices.cfg", '-OF'])
