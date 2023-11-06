import harmonic_resonance.midiator as pm
from . import voice_types as V
from ..instruments import Instrument

class Voice(Instrument):
    """Voice is a special instrument that connects to a separate
    soundfont specified in the timidity config"""

    def __init__(self, mf, voice_name: str, channel: int):
        """TODO: to be defined. """
        voice_dict = V.VOICES[voice_name]
        self.name = voice_name
        self.instrument = voice_dict['program']
        self.channel = channel

        self.track = mf.add_track(name=self.name)

        self.track.append(pm.Message(
            'control_change',
            control =  0,
            value = voice_dict['bank'],
            channel = self.channel,
            time = 0
        ))
        self.track.append(pm.Message(
            'control_change',
            control = 32,
            value = voice_dict['subbank'],
            channel = self.channel,
            time = 0
        ))
        self.track.append(pm.Message(
            'program_change',
            program = voice_dict['program'],
            channel = self.channel,
            time = 1))

        self.track_volume = mf.add_track(name=f'{self.name}-volume')
        self.track_pan = mf.add_track(name=f'{self.name}-pan')


