'''
https://docs.google.com/spreadsheets/d/19_3BxUMy3uy1Gb0V8Wc-TcG7q16Amfn6e8QVw4-HuD0/edit#gid=0
'''
from . import percussion_types as P
from . import patterns
from .percussion import Percussion
from .kits import *

def make_tick(mf):
    return Percussion(mf, P.side_stick)

def make_kick(mf):
    return Percussion(mf, P.acoustic_bass_drum)

def make_low_tom(mf):
    return Percussion(mf, P.low_tom)

def make_high_tom(mf):
    return Percussion(mf, P.high_tom)

def make_floor_tom(mf):
    return Percussion(mf, P.low_floor_tom)

def make_snare(mf):
    return Percussion(mf, P.acoustic_snare)

def make_hihat_closed(mf):
    return Percussion(mf, P.closed_hi_hat)

def make_hihat_open(mf):
    return Percussion(mf, P.open_hi_hat)

def make_crash(mf):
    return Percussion(mf, P.crash_cymbal_1)

def make_ride(mf):
    return Percussion(mf, P.ride_cymbal_1)

def make_kit_1(mf):
    tick = make_tick(mf)
    kick = make_kick(mf)
    snare = make_snare(mf)
    hihat_c = make_hihat_closed(mf)
    hihat_o = make_hihat_open(mf)
    ride = make_ride(mf)

    return tick, kick, snare, hihat_c, hihat_o, ride
    
def make_kit_toms(mf):
    kit_1 = make_kit_1(mf)
    low_tom = make_low_tom(mf)
    high_tom = make_high_tom(mf)
    floor_tom = make_floor_tom(mf)

    return *kit_1, low_tom, high_tom, floor_tom
