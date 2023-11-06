from enum import Enum
import phimidi as pm
from rich import print as log
import subprocess

class Notes(Enum):
    C4 = 60
    D4 = 62

part = pm.Part('test', '001')

piano = part.add_piano()
piano.set_note(60, 480)
piano.set_chord(60, 480)
#  piano.set_marker('END', 960)
log(part)
#  log(part.free_channels)

filepath = part.save()

#  subprocess.run(["timidity", '-in', "-c", "~/.photon/timidity.cfg", filepath])
#  subprocess.run(["timidity", "-c", "~/.photon/timidity.cfg", filepath])
part.play()
