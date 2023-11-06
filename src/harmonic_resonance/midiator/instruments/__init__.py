"""
wrapper for managing instruments
"""
#  import phimidi as pm
from . import instrument_types as I
from .instrument import Instrument


def make_piano(mf, channel):
    return Instrument(mf, I.acoustic_grand_piano, channel)

def make_vibes(mf, channel):
    return Instrument(mf, I.vibraphone, channel)

def make_bass(mf, channel):
    return Instrument(mf, I.acoustic_bass, channel)

def make_horns(mf, channel):
    return Instrument(mf, I.brass_section, channel)

def make_strings(mf, channel):
    return Instrument(mf, I.string_ensemble_1, channel)

