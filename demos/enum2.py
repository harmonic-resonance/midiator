from enum import Enum
import phimidi as pm
from rich import print as log

#  class Notes(Enum):
class Notes(Enum):
    C4 = 60
    Cs4 = 61
    Db4 = 61
    D4 = 62
    Ds4 = 63
    Eb4 = 63

    #  @classmethod
    def name_flat(self):
        return flats[self.value]

flats = {
        61: 'D♭4',
        63: 'Eb4',
        }

N = Notes
root = N.Db4

log(root.name_flat())
