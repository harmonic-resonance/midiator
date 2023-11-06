import phimidi as pm

#  for i, inst in enumerate(pm.I.INSTRUMENTS):
for key in pm.P.PERCUSSIONS:
    inst = key.lower()
    inst = inst.replace(' ', '_')
    inst = inst.replace('(', '')
    inst = inst.replace(')', '')
    inst = inst.replace('-', '_and_')
    inst = inst.replace('+', '_and_')
    print(f'{inst} = {pm.P.PERCUSSIONS[key]}')
