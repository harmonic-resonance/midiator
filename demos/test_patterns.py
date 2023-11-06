"""
test percusion patterns
"""
import phimidi as pm
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

rhythms = [
        conga.tumbao,
        conga.guaguanco,
        conga.bolero,
        conga.samba,
        ]

for rhythm in rhythms:
    part.set_marker(str(rhythm.__name__), 8*M)

    for i in range(4):
        if i % 2:
            rhythm(2 * M, velocity_mod=-10)
        else:
            rhythm(2 * M)

        pm.patterns.latin.son_clave2(2 * M, clave)
        for _ in range(4):
            shaker.set_hit(M/4, velocity=90)
            shaker.set_hit(M/4, velocity=60)

part.save()
part.play()
