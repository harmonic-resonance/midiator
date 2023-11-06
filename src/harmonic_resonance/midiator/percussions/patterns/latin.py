from ..percussion import Percussion


def son_clave2(duration, perc: Percussion, velocity_mod=0):
    """3:2 pattern
    2 measures of eigth notes"""
    b = int(duration / 16)
    pattern = "5__3__5_"
    pattern += "__5_3___"
    perc.add_pattern(pattern, b, velocity_mod=velocity_mod)


#  def son_clave(duration, kick, tick, ride, velocity_mod=0):
#  """
#  duration is 2 measure
#  """
#  duration = int(duration)
#  b = int(duration/16)
#  for _ in range(4):
#  kick.set_hit(3 * b, velocity=90+velocity_mod)
#  kick.set_hit(1 * b, velocity=60+velocity_mod)

#  run = [3, 3, 4, 2, 4]
#  for r in run:
#  tick.set_hit(r * b, velocity=90+velocity_mod)

#  ride.set_hits(duration, 16, velocity=60+velocity_mod)


def rhumba(duration, kick, tick, ride, velocity_mod=0):
    """
    duration is 2 measure
    """
    duration = int(duration)
    b = int(duration / 16)
    #  for _ in range(4):
    #  kick.set_hit(3 * b, velocity=90+velocity_mod)
    #  kick.set_hit(1 * b, velocity=60+velocity_mod)
    pattern = "6__46__4"
    pattern += "6__46__4"
    kick.add_pattern(pattern, b, velocity_mod=velocity_mod)

    #  run = [3, 4, 3, 2, 4]
    #  for r in run:
        #  tick.set_hit(r * b, velocity=90 + velocity_mod)
    pattern =  "5__3___5"
    pattern += "__5_3___"
    tick.add_pattern(pattern, b, velocity_mod=velocity_mod)

    ride.set_hits(duration, 16, velocity=60 + velocity_mod)


def bossa_nova(duration, kick, tick, ride, velocity_mod=0):
    """
    duration is 2 measure
    """
    duration = int(duration)
    b = int(duration / 16)
    for _ in range(4):
        kick.set_hit(3 * b, velocity=90 + velocity_mod)
        kick.set_hit(1 * b, velocity=60 + velocity_mod)

    run = [3, 3, 4, 3, 3]
    for r in run:
        tick.set_hit(r * b, velocity=30 + velocity_mod)

    ride.set_hits(duration, 16, velocity=60 + velocity_mod)
