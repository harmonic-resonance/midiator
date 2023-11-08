import harmonic_resonance.midiator as hrm
from harmonic_resonance.midiator.percussions.kits import Kit
from harmonic_resonance.midiator.percussions.percussion import Percussion
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


if __name__ == "__main__":
    PROJECT = "percussion"
    title = "standard demo"
    bpm = 120  # beats per minute
    bpM = 4  # beats per Measure

    part = hrm.Part(PROJECT, title, bpm=bpm)
    M = part.measure_ticks()

    standard = hrm.Standard(part)
    for pattern_name, pattern in standard.patterns.items():
        #  patterns = standard.patterns["funky_drummer"]
        part.set_marker(pattern_name, 2 * M)
        standard.set_patterns(pattern, M)
        standard.set_patterns(pattern, M)

    part.save()
    part.play()


