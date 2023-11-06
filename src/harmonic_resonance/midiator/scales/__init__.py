'''utils for building scales'''
from . import scale_types as S

def build_scale(root=48, scale_type=S.major, octaves=3):
    notes = [root]
    scale = S.SCALES[scale_type]
    for octave in range(octaves):
        jump = 0
        for interval in scale:
            jump += interval
            note = (octave * 12) + root + jump
            notes.append(note)
    return notes

class Scale(dict):
    #  notes = {}
    def __init__(self, root, scale_type, octaves=1):
        """TODO: Docstring for __init__.

        :root: TODO
        :scale_type: TODO
        :octaves: TODO

        """
        pos = 1
        #  self.notes[pos] = root
        self[pos] = root
        self.root = root
        self.intervals = S.SCALES[scale_type]
        for octave in range(octaves):
            jump = 0
            for interval in self.intervals:
                jump += interval
                pos += 1
                note = (octave * 12) + root + jump
                self[pos] = note


class Key():
    """
    generate classic key offsets for a root note
    """
    _pos = dict()

    def __init__(self, root: int):
        root = int(root)
        self.root = root
        self.I = root
        self.II = root + 2
        self.III = root + 4
        self.IV = root + 5
        self.V = root + 7
        self.VI = root + 9
        self.VII = root + 11

        self._pos[1] = self.I
        self._pos[2] = self.II
        self._pos[3] = self.III
        self._pos[4] = self.IV
        self._pos[5] = self.V
        self._pos[6] = self.VI
        self._pos[7] = self.VII

    def position(self, num: int):
        """
        numeric position
        """
        return self._pos[num]
