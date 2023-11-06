
major = 'major'
minor = 'minor'
melodic_minor = 'melodicminor'
harmonic_minor = 'harmonicminor'
pentatonic_major = 'pentatonicmajor'
blues_major = 'bluesmajor'
pentatonic_minor = 'pentatonicminor'
blues_minor = 'bluesminor'
augmented = 'augmented'
diminished = 'diminished'
chromatic = 'chromatic'
whole_half = 'wholehalf'
half_whole = 'halfwhole'
whole_tone = 'wholetone'
augmented_fifth = 'augmentedfifth'
japanese = 'japanese'
oriental = 'oriental'
ionian = 'ionian'
dorian = 'dorian'
phrygian = 'phrygian'
lydian = 'lydian'
mixolydian = 'mixolydian'
aeolian = 'aeolian'
locrian = 'locrian'

SCALES = {
    'major': (2, 2, 1, 2, 2, 2, 1),
    'minor': (2, 1, 2, 2, 1, 2, 2),
    'melodicminor': (2, 1, 2, 2, 2, 2, 1),
    'harmonicminor': (2, 1, 2, 2, 1, 3, 1),
    'pentatonicmajor': (2, 2, 3, 2, 3),
    'bluesmajor': (3, 2, 1, 1, 2, 3),
    'pentatonicminor': (3, 2, 2, 3, 2),
    'bluesminor': (3, 2, 1, 1, 3, 2),
    'augmented': (3, 1, 3, 1, 3, 1),
    'diminished': (2, 1, 2, 1, 2, 1, 2, 1),
    'chromatic': (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    'wholehalf': (2, 1, 2, 1, 2, 1, 2, 1),
    'halfwhole': (1, 2, 1, 2, 1, 2, 1, 2),
    'wholetone': (2, 2, 2, 2, 2, 2),
    'augmentedfifth': (2, 2, 1, 2, 1, 1, 2, 1),
    'japanese': (1, 4, 2, 1, 4),
    'oriental': (1, 3, 1, 1, 3, 1, 2),
    'ionian': (2, 2, 1, 2, 2, 2, 1),
    'dorian': (2, 1, 2, 2, 2, 1, 2),
    'phrygian': (1, 2, 2, 2, 1, 2, 2),
    'lydian': (2, 2, 2, 1, 2, 2, 1),
    'mixolydian': (2, 2, 1, 2, 2, 1, 2),
    'aeolian': (2, 1, 2, 2, 1, 2, 2),
    'locrian': (1, 2, 2, 1, 2, 2, 2),
}
