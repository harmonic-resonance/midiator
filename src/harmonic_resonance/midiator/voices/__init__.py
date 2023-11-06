from .voice import Voice
from . import voice_types as V

def make_solo_ooh(mf):
    return Voice(mf, voice_name=V.solo_ooh)

def make_solo_aah(mf):
    return Voice(mf, voice_name=V.solo_aah)

def make_choir_aah(mf):
    return Voice(mf, voice_name=V.choir_aah)

def make_choir_ooh(mf):
    return Voice(mf, voice_name=V.choir_ooh)

def make_choir_mixed(mf):
    return Voice(mf, voice_name=V.choir_mixed)

def make_choir_swell(mf):
    return Voice(mf, voice_name=V.choir_swell)

def make_choir_little_swell(mf):
    return Voice(mf, voice_name=V.choir_little_swell)
