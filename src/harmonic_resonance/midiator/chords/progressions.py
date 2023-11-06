'''
chord progressions
includes patterns from:
https://www.learnjazzstandards.com/blog/learning-jazz/jazz-theory/3-important-jazz-chord-progressions-need-master/
'''
import harmonic_resonance.midiator as pm
from . import chord_types as C

EAGsABE = [
        (pm.N.E4, 2, C.major),
        (pm.N.A4, 2, C.major),
        (pm.N.Gs4, 4, C.minor_7),
        (pm.N.A3, 2, C.major),
        (pm.N.B3, 2, C.dominant_7),
        (pm.N.E3, 4, C.major),
        ]
p5 = [
        (pm.N.C3, 4, C.major),
        (pm.N.F3, 4, C.dominant_9),
        (pm.N.A3, 4, C.minor_7),
        (pm.N.G3, 4, C.dominant_11),
        (pm.N.A3, 4, C.minor_11),
        (pm.N.F3, 4, C.dominant_9),
        (pm.N.C3, 8, C.dominant_13),
        ]

EBCsA = [
        (pm.N.E4, 4, C.major),
        (pm.N.B3, 4, C.major),
        (pm.N.Cs4, 4, C.minor),
        (pm.N.A3, 4, C.major),
        ]

def build_progression(key: pm.Scale, chords: list) -> list:
    """assemble all notes for chords in the progression

    :key: dict of midi note id for each position in key
    :chords: list of tuples with ``(pos_name, pos_id, chord_type)``
    :returns: list

    """
    progression = []
    for pos_name, note, chord_type in chords:
        notes = pm.get_chord_notes(key[note], chord_type)
        progression.append((pos_name, notes))

    return progression

def I_V_vis_IV(root):
    I = pm.get_chord_notes(0 + root, C.major)
    V = pm.get_chord_notes(7 + root, C.dominant_7)
    vis = pm.get_chord_notes(10 + root, C.minor)
    IV = pm.get_chord_notes(5 + root, C.dominant_7)

    return [I, V, vis, IV]


def ii_V_I_I(root):
    key = pm.Scale(root, scale_type=pm.S.major)
    chords = [
            ('ii7', 2, C.minor_7),
            ('V7', 5, C.dominant_7),
            ('IM7', 1, C.major_7),
            ('I6', 1, C.major_6),
            ]
    return build_progression(key, chords)


def ii_V_i_i(root):
    key = pm.Scale(root, scale_type=pm.S.major)
    chords = [
            ('ii7', 2, C.minor_7),
            ('V7', 5, C.dominant_7),
            ('i7', 1, C.minor_7),
            ('i9', 1, C.minor_9),
            ]
    return build_progression(key, chords)



def I_vi_ii_V(root: int):
    key = pm.Scale(root, scale_type=pm.S.major)
    chords = [ ('IM7', 1, C.major_7),
            ('vi7', 6, C.minor_7),
            ('ii7', 2, C.minor_7),
            ('V7', 5, C.dominant_7)
            ]
    return build_progression(key, chords)


def i_vi_ii_V(root: int):
    key = pm.Scale(root, scale_type=pm.S.major)
    chords = [ ('i7', 1, C.minor_7),
            ('vi7', 6, C.minor_7),
            ('ii7', 2, C.minor_7),
            ('V7', 5, C.dominant_7)
            ]
    return build_progression(key, chords)


def thelio(root):
    key = pm.Scale(root, scale_type=pm.S.major)
    chords = [ ('IM7', 1, C.major_7),
            ('IV9', 4, C.dominant_9),
            ('vi7', 6, C.minor_7),
            ('V11', 5, C.dominant_11),
            ('vi9', 6, C.minor_9),
            #  ('ii7', 2, C.minor_7),
            ('V13', 5, C.dominant_13),
            ]
    return build_progression(key, chords)


