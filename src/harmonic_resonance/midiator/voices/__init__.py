from .voice import Voice
from .voice import Voice
from . import voice_types as V

def make_solo_ooh(mf, channel):
    return Voice(mf, voice_name=V.solo_ooh, channel=channel)

def make_solo_aah(mf, channel):
    return Voice(mf, voice_name=V.solo_aah, channel=channel)

def make_choir_aah(mf, channel):
    return Voice(mf, voice_name=V.choir_aah, channel=channel)

def make_choir_ooh(mf, channel):
    return Voice(mf, voice_name=V.choir_ooh, channel=channel)

def make_choir_mixed(mf, channel):
    return Voice(mf, voice_name=V.choir_mixed, channel=channel)

def make_choir_swell(mf, channel):
    return Voice(mf, voice_name=V.choir_swell, channel=channel)

def make_choir_little_swell(mf, channel):
    return Voice(mf, voice_name=V.choir_little_swell, channel=channel)
