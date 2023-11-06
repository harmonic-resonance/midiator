'''
voices are contained in the KBH_Real_and_Swell_Choir.sf2 soundfont

timidity requires voices.cfg file to establish voices on bank 1
'''
import phimidi as pm
import subprocess as subprocess

PROJECT = 'phi-midi'
NAME = 'voices'

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

bpm = 120
tempo = int(pm.bpm2tempo(bpm))

root = pm.N.D3
octaves = 3
scale_type = pm.S.dorian

scale = pm.build_scale(
    root=root, 
    scale_type=scale_type, 
    octaves=octaves)

mf = pm.new_midi(title=title, tempo=tempo)
M = 4 * mf.ticks_per_beat

   
solo_ooh = pm.Voice(mf, voice_name=pm.V.solo_ooh)
solo_aah = pm.Voice(mf, voice_name=pm.V.solo_aah)
choir_aah = pm.Voice(mf, voice_name=pm.V.choir_aah)
choir_ooh = pm.Voice(mf, voice_name=pm.V.choir_ooh)
choir_mixed = pm.Voice(mf, voice_name=pm.V.choir_mixed)
choir_swell = pm.Voice(mf, voice_name=pm.V.choir_swell)
choir_little_swell = pm.Voice(mf, voice_name=pm.V.choir_little_swell)

solo_ooh.set_note(pm.N.C5, M)
solo_ooh.set_rest(M)

solo_aah.set_rest(M)
solo_aah.set_note(pm.N.C5, M)

choir_ooh.set_rest(2 * M)
choir_aah.set_rest(2 * M)
choir_ooh.set_note(pm.N.C5, M)
choir_ooh.set_rest(M)
choir_aah.set_rest(M)
choir_aah.set_note(pm.N.C5, M)
choir_ooh.set_note(pm.N.C5, M, velocity=100)
choir_ooh.set_rest(M)
choir_aah.set_rest(M)
choir_aah.set_note(pm.N.C5, M, velocity=100)

choir_little_swell.set_rest(6 * M)
choir_swell.set_rest(6 * M)
choir_little_swell.set_note(pm.N.C5, M)
choir_swell.set_rest(M)
choir_little_swell.set_rest(M)
choir_swell.set_note(pm.N.C5, M)

choir_mixed.set_rest(8 * M)
choir_mixed.set_chord(pm.N.C4, M*2, chord_type=pm.C.major)
choir_mixed.set_chord(pm.N.G4, M*2, chord_type=pm.C.major_7)
choir_mixed.set_chord(pm.N.F4, M*2, chord_type=pm.C.major_7)
choir_mixed.set_chord(pm.N.C4, M*2, chord_type=pm.C.sus2)

filepath = pm.save_midi(mf, folder, filename)

mf.print_tracks()

#  !timidity -c voices.cfg $filename
subprocess.run(["timidity", filepath, "-c", "voices.cfg", '-OF'])
subprocess.run(["timidity", "-c", "voices.cfg", filepath])
