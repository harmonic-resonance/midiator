"""
Part extend the mido ``MidiFile`` object
- keeps track of instruments, channels
"""
from pathlib import Path
import subprocess
from mido import MidiFile, Message, MetaMessage, bpm2tempo
from .instruments import Instrument, I
from .voices import Voice, V
from .percussions import Percussion, P

class Part(MidiFile):
    """Part object extends the mido MidoFile"""

    free_channels = list(range(16))
    perc_channel = free_channels.remove(9)

    instruments = []

    def __init__(self, project: str, title: str, 
            bpm: int=120, bpM: int=4, beat_val: int=4,
            root: int=60, key: str='C'):
        """TODO: to be defined.

        :project: for the session, used to folder
        :title: for the musical part
        :tempo: milliseconds per beat
        :bpm: int value beats per minute for settings tempo
        :bpM: int - beats per Measure
        :beat_val: for time signature

        """
        super().__init__()

        self.project = project
        self.title = title
        self.root = root
        self.key = key

        track = self.add_track(name='meta')
        if title:
            track.append(MetaMessage('text', text=f'{project} - {title}', time=0))

        self.bpm = int(bpm)
        self.bpM = int(bpM)
        self.beat_val = int(beat_val)
        self.tempo = int(bpm2tempo(self.bpm))
        track.append(MetaMessage('set_tempo', tempo=self.tempo, time=0))
        track.append(MetaMessage('key_signature', key=self.key, time=0))

    def measure_ticks(self):
        """return measure duration in ticks
        used for setting the ``M`` variable in a composition

        :returns:  int

        """
        return self.bpM * self.ticks_per_beat

    def set_marker(self, text, duration=0):
        '''appends  a ``marker`` message at ``duration`` to the meta track
        :duration: offset for placement of marker
        '''
        duration = int(duration)
        self.tracks[0].append(MetaMessage('marker', text=text, time=0))
        self.tracks[0].append(MetaMessage('marker', text='', time=duration))

    def get_mid_path(self) -> Path:
        #  folder = Path(f'~/Sessions/{self.project}').expanduser()
        #  folder.mkdir(parents=True, exist_ok=True)
        #  midi_file = folder / f'{self.title}.mid'
        midi_file = Path(f'./{self.project}-{self.title}-{self.key}-{self.bpm}.mid')
        return midi_file

    def save(self):
        midi_file = self.get_mid_path()
        filepath = str(midi_file)
        super().save(filepath)
        #  print(f'    * {filepath}')
        return filepath

    def play(self):
        """
        this overrides the mido play function
        """
        midi_file = self.get_mid_path()
        filepath = str(midi_file)
        subprocess.run(["timidity", '-in', "-c", "~/.photon/timidity.cfg", filepath])

    def convert(self):
        """
        this overrides the mido play function
        """
        midi_file = self.get_mid_path()
        filepath = str(midi_file)
        subprocess.run(["timidity", '-in', "-c", "~/.photon/timidity.cfg", "-Ov", filepath])

    def add_instrument(self, instrument_type: I) -> Instrument:
        """add instrument to session
        set to next available channel

        :instrument_type: TODO
        :returns: TODO

        """
        channel = self.free_channels.pop(0)
        instrument = Instrument(self, instrument_type, channel)
        self.instruments.append(instrument)
        return instrument

    def add_voice(self, voice_type: V) -> Voice:
        """add instrument to session
        set to next available channel

        :instrument_type: TODO
        :returns: TODO

        """
        channel = self.free_channels.pop(0)
        instrument = Voice(self, voice_type, channel)
        self.instruments.append(instrument)
        return instrument

    def add_kick(self):
        return Percussion(self, P.acoustic_bass_drum)

    def add_piano(self):
        return self.add_instrument(I.acoustic_grand_piano)

    def add_vibes(self):
        return self.add_instrument(I.vibraphone)

    def add_bass(self):
        return self.add_instrument(I.acoustic_bass)

    def add_horns(self):
        return self.add_instrument(I.brass_section)

    def add_strings(self):
        return self.add_instrument(I.string_ensemble_1)

    def add_solo_ooh(self):
        return self.add_voice(V.solo_ooh)

    def add_solo_aah(self):
        return self.add_voice(V.solo_aah)

    def add_choir_aah(self):
        return self.add_voice(V.choir_aah)

    def add_choir_ooh(self):
        return self.add_voice(V.choir_ooh)

    def add_choir_mixed(self):
        return self.add_voice(V.choir_mixed)

    def add_choir_swell(self):
        return self.add_voice(V.choir_swell)

    def add_choir_little_swell(self):
        return self.add_voice(V.choir_little_swell)
