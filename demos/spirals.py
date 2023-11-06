import phimidi as pm
import math as math
import subprocess as subprocess
from fibs import *

phi = (1 + math.sqrt(5)) / 2
angle = (2 * math.pi) - ((2 * math.pi) / phi)
#  angle = (2 * math.pi) - ((2 * math.pi) / 144/89)
angles = []

print('phi:', phi)
print('angle:', angle)
print('degrees:', math.degrees(angle))
print()

# number of nodes
n = 986

# relating to color cycles in plot
cycles = 13

bpm = 60
tempo = int(pm.bpm2tempo(bpm))

root =  pm.N.D3
scale_type = pm.S.harmonic_minor
scale_type = pm.S.melodic_minor
scale_type = pm.S.dorian
#  scale_type = pm.S.pentatonic_minor
#  scale_type = pm.S.pentatonic_major
octaves = 2

scale = pm.build_scale(
    root=root, 
    scale_type=scale_type, 
    octaves=octaves)
#  scale = pm.get_chord_notes(root, pm.C.dominant_7)
#  scale.extend(pm.get_chord_notes(root + 12, pm.C.dominant_7))
#  scale.extend(pm.get_chord_notes(root + 24, pm.C.dominant_7))
print('scale:', scale)

PROJECT = 'spirals'
NAME = 'copper'

for i in range(n):
    theta = angle * i
    angles.append(theta)
    
#  print(angles)
#  print()

sins = list(map(lambda a: math.sin(a), angles))
coss = list(map(lambda a: math.cos(a), angles))

def get_note_linear(x):
    '''range -1 to 1'''
    divs = len(scale)
    i = int((x+1)/2 * divs)
    return scale[i]

def get_note_circle(angle):
    divs = math.pi * 2 / len(scale)
    angle = angle % (2 * math.pi)
    i = int(angle / divs)
    note = scale[i]
    #  print(angle, i, note)
    return note

def get_pan(x):
    '''range -1 to 1'''
    divs = 127
    i = int((x+1)/2 * divs)
    return i

notes = list(map(get_note_circle, angles))
pans = list(map(get_pan, coss))

offsets = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#  offsets.append(89)
#  offsets.append(144)

import os
sessions = os.path.expanduser('~') + '/Sessions'


for cycle in range(1, cycles+1):

    folder = f'{PROJECT}/{NAME}/{cycle:04}'
    title = f'{PROJECT} - {NAME}'

    filename = f'{scale_type}-{n}-{cycle:04}.mid'

    tempo = int(pm.bpm2tempo(bpm))
    mf = pm.new_midi(title=filename, tempo=tempo)
    beat = mf.ticks_per_beat
    #  mf.tracks[0].append(pm.MetaMessage('set_tempo', tempo=tempo, time=beat))

    vibes = pm.make_vibes(mf, 1)
    bass = pm.make_bass(mf, 2)
    horns = pm.make_horns(mf, 3)
    v1 = pm.make_choir_mixed(mf)

    out = f'{sessions}/{folder}/'
    os.makedirs(out, exist_ok=True)

    with open(f'{out}/sequence.txt', 'w') as sequence:
        vibes.set_volume(60, 0)
        v1.set_volume(90, 0)
        horns.set_volume(10, 0)
        for i in range(n):
            #  level = int(30 + ((i/n) * 60)) 
            level = int(10 + ((i/n) * 60)) 
            horns.set_volume(level, beat)
            level = int(70 - ((i/n) * 60)) 
            bass.set_volume(level, beat)
            bass.set_note(root - 12, duration=beat/2, velocity=60)
            bass.set_note(root - 24, duration=beat/2, velocity=20)

                
        for note_id, note in enumerate(notes):
            tempo = int(pm.bpm2tempo(frames[note_id]))
            mf.tracks[0].append(pm.MetaMessage('set_tempo', tempo=tempo, time=beat))

            vibes.set_pan(pans[note_id], 0)
            offset = 0
            #  if i < len(offsets):
              #  offset = offsets[i] * beat
            vibes.set_note(24 + note, duration=beat)
            if note_id % cycle == 0:
                d = (cycle * beat)
                #  v1.set_note(note, duration=d)
                v1.set_note(note, duration=(d - beat))
                v1.set_rest(beat)
                v1.set_volume(20, 0)
                for i in range(8):
                    level = 20 + (i) * 8
                    #  level = i * 4 + 20
                    v1.set_volume(level, d/24)
                for i in reversed(range(16)):
                    level = 20 + (i) * 4
                    #  level = i * 4 + 20
                    v1.set_volume(level, d/24)
            if note_id in fibs:
                d = note_id * beat

                horns.set_note(note - 12, duration=d-beat)
                horns.set_rest(beat)
                #  horns.set_volume(10, 0)
                #  for i in range(8):
                    #  level = (i) * 8 + 10
                    #  #  level = i * 4 + 20
                    #  horns.set_volume(level, d/24)
                #  for i in reversed(range(16)):
                    #  level = (i) * 4 + 10
                    #  #  level = i * 4 + 20
                    #  horns.set_volume(level, d/24)

            sequence.write(f'file {( note_id + 1 ):04}.png\n')
            #  tempo = int(pm.bpm2tempo(new_bpm))
            #  seq_dur = pm.tick2second(beat, beat, tempo)
            seq_dur = tempo / 1000000
            #  seq_dur = seq_dur * 2
            sequence.write(f'duration {seq_dur}\n')
            #  breakpoint()
        
        filepath = pm.save_midi(mf, folder, 'sequence.mid')
        #  subprocess.run(["timidity", filepath, "-c", "voices.cfg", '-Ov'])

    #  mf.print_tracks()

    #  subprocess.run(["timidity", '-in', "-c", "voices.cfg", filepath])
    #  subprocess.run(["timidity", filepath])
