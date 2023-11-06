"""
midiator
========

HARMONIC resonance
------------------



"""
__author__ = "harmonic-resonance"
__maintainer__ = "harmonic-resonance"
__email__ = "github@phiarchitect.com"
__version__ = "0.0.1"
__licence__ = "MIT"

from mido import MidiFile, Message, MetaMessage, bpm2tempo, second2tick, tick2second

#  import .notes as N
from . import notes as N
from .scales import *
from .chords import *
from .instruments import *
from .voices import *
from .percussions import *
from .arps import *
from .part import *

import subprocess


def new_midi(title="", tempo=500000) -> MidiFile:
    """sets up a mido midi file with initial meta track"""
    mf = MidiFile()

    track = mf.add_track(name="meta")
    if title:
        track.append(MetaMessage("text", text=title, time=0))
    track.append(MetaMessage("set_tempo", tempo=tempo, time=0))
    return mf


def set_new_track(mf, name="", instrument=""):
    track = mf.add_track(name=name)
    # if instrument:
    # track.append(MetaMessage('text', text='TITLE', time=0))
    return track


def save_midi(mf, folder, filename):
    import os

    sessions = os.path.expanduser("~") + "/Sessions"
    out = f"{sessions}/{folder}/"
    os.makedirs(out, exist_ok=True)
    filepath = out + filename
    mf.save(filepath)
    print(f"    * {filepath}")
    return filepath


def play(filepath: str):
    """TODO: Docstring for play.

    :filepath: TODO
    :returns: TODO

    """
    subprocess.run(["timidity", "-in", "-c", "~/.photon/timidity.cfg", filepath])
