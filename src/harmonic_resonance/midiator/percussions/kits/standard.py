
from .kit import Kit
from ..percussion import Percussion
import harmonic_resonance.midiator.percussions.percussion_types as P

class Standard(Kit):
    def __init__(self, part):
        """Initialize a standard drum kit with the given MIDI part."""
        super().__init__(part)
        self.kick = Percussion(part, P.acoustic_bass_drum)
        self.snare = Percussion(part, P.acoustic_snare)
        self.closed_hh = Percussion(part, P.closed_hi_hat)
        self.open_hh = Percussion(part, P.open_hi_hat)
        self.ride = Percussion(part, P.ride_cymbal_1)

        self.load_patterns('standard.yaml')

        self.kit = {
            "kick": self.kick,
            "snare": self.snare,
            "closed_hh": self.closed_hh,
            "open_hh": self.open_hh,
            "ride": self.ride,
        }



