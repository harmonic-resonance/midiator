


def swing(length, kick, ride):
    length = int(length)
    b = int(length/12)
    kick.set_hit(5 * b)
    kick.set_hit(1 * b)
    ride.set_hit(3 * b)
    ride.set_hit(2 * b, velocity=80)
    ride.set_hit(1 * b)

