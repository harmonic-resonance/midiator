"""
test percusion patterns
"""
import harmonic_resonance.midiator as pm
from rich import print as log


PROJECT = 'test_patterns'
title = 'conga'
bpm = 180  # beats per minute
bpM = 4  # beats per Measure
root = pm.N.D3  # the root note of the key
key = 'D'

part = pm.Part(PROJECT, title, bpm=bpm, bpM=bpM, root=root, key=key)
M = part.measure_ticks()

clave = pm.Percussion(part, pm.P.claves)
shaker = pm.Percussion(part, pm.P.shaker)
conga = pm.Conga(part)

part.set_marker('count', M)

clave.set_hits(M, 4)
conga.rest_all(M)
shaker.set_rest(M)

#  rhythms = [
        #  conga.tumbao,
        #  conga.guaguanco,
        #  conga.bolero,
        #  conga.samba,
        #  ]

#  patterns = conga.patterns["tumbao"]

#  for rhythm in rhythms:
for key, pattern in conga.patterns.items():
    part.set_marker(key, duration=8*M)

    for i in range(4):
        if i % 2:
            conga.set_patterns(pattern, 2 * M, velocity_mod=10)
        else:
            conga.set_patterns(pattern, 2 * M, velocity_mod=10)

        pm.patterns.latin.son_clave2(2 * M, clave)
        for _ in range(4):
            shaker.set_hit(M/4, velocity=90)
            shaker.set_hit(M/4, velocity=60)

part.save()
part.play()
