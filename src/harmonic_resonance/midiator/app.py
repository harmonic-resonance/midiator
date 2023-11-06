"""
run the main app
"""
from .midiator import Midiator


def run() -> None:
    reply = Midiator().run()
    print(reply)
