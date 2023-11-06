
factors = [1, 1, 2, 3, 4, 5, 6, 10, 12, 15, 30, 60, 120, 180, 240, 300]
#  factors = factors[:-1]
print(factors)

fibs = [1, 1]
for _ in range(len(factors) - 2):
    fibs.append(fibs[-1] + fibs[-2])
print(fibs)

frames = []
for i, f in enumerate(fibs):
    for n in range(f):
        bpm = factors[i] * 60
        #  dur = pm.bpm2tempo(bpm) / 1_000_000
        frames.append(bpm)

print('frames: ', len(frames))
#  print(frames)

