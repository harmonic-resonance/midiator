import phimidi as pm
import math as math
import subprocess as subprocess


PROJECT = 'phi-midi'
NAME = 'drums'

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

pulse = 120
tempo = pm.bpm2tempo(pulse)
mf = pm.new_midi(title=title, tempo=tempo)
M = 4 * mf.ticks_per_beat

tick = pm.Percussion(mf, pm.P.side_stick)
kick = pm.Percussion(mf, pm.P.acoustic_bass_drum)
snare = pm.Percussion(mf, pm.P.acoustic_snare)
hihat_closed = pm.Percussion(mf, pm.P.closed_hi_hat)
ride = pm.Percussion(mf, pm.P.ride_cymbal_1)

#  kicks = 8

#  for i in range(kicks):
    #  kick.set_hit(480, velocity=100)
    #  if i > 1:
        #  for _ in range(4):
            #  snare.set_hit(120, velocity=40)
        #  for _ in range(12):
            #  tick.set_hit(40, velocity=20)
    #  else:
        #  snare.set_rest(480)
        #  tick.set_rest(480)
        
# count
kick.set_rest(M)
snare.set_rest(M)
hihat_closed.set_rest(M)
ride.set_rest(M)
mf.tracks[0].append(pm.MetaMessage('lyrics', text='count', time=0))
tick.set_hits(M, 4, velocity=40)

#  ride.set_hit(M)
#  kick.set_rest(M)
#  kick.set_hits(4 * M, 16)
#  ride.set_rest(M)
#  ride.set_hits(3 * M, 24)

mf.tracks[0].append(pm.MetaMessage('marker', text='billie jean', time=M))
ride.set_rest(2 * M)
for _ in range(2):
    pm.patterns.funky.billie_jean(M, kick, snare, hihat_closed)

mf.tracks[0].append(pm.MetaMessage('marker', text='swing', time=2 * M))
snare.set_rest(2 * M)
hihat_closed.set_rest(2 * M)
for _ in range(4):
    pm.patterns.swing.swing(M, kick, ride)

mf.tracks[0].append(pm.MetaMessage('marker', text='funky drummer', time=2 * M))
for _ in range(2):
    pm.patterns.funky.funky_drummer(2 * M, kick, snare, hihat_closed, ride)

mf.tracks[0].append(pm.MetaMessage('marker', text='deep_house', time=4 * M))
for _ in range(2):
    pm.patterns.techno.deep_house(2 * M, kick, snare, hihat_closed, ride)
    pm.patterns.techno.deep_house(2 * M, ride, kick, snare, hihat_closed)


mf.tracks[0].append(pm.MetaMessage('marker', text='jungle', time=8 * M))
for _ in range(2):
    pm.patterns.funky.jungle(2 * M, kick, snare, hihat_closed, ride)

mf.tracks[0].append(pm.MetaMessage('marker', text='drum_bass', time=4 * M))
for _ in range(4):
    pm.patterns.techno.drum_bass(2 * M, kick, snare, hihat_closed, ride)

filepath = pm.save_midi(mf, folder, filename)

subprocess.run(["timidity", '-in', '-c', '~/.photon/timidity.cfg', filepath])
