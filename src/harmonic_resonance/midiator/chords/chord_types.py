'''utils for building chords`
TODO: alternate voicings
'''
major = 'M'
major_6 = '6'
major_7 = 'M7'
dominant_7 = '7'
dominant_9 = '9'
dominant_11 = '11'
dominant_13 = '13'
minor = 'm'
minor_7 = 'm7'
minor_9 = 'm9'
minor_11 = 'm11'
minor_13 = 'm13'
diminished = 'o'
sus2 = 'sus2'
sus4 = 'sus4'

CHORDS = {
  'M': [0, 4, 7],
  '6': [0, 4, 7, 9],
  'M7': [0, 4, 7, 11],
  '7': [0, 4, 7, 10],
  '9': [0, 4, 7, 10, 14],
  '11': [0, 4, 7, 10, 14, 17],
  '13': [0, 4, 7, 10, 14, 17, 21],
  'm': [0, 3, 7],
  'm7': [0, 3, 7, 10],
  'm9': [0, 3, 7, 10, 14],
  'm11': [0, 3, 7, 10, 14, 17],
  'm13': [0, 3, 7, 10, 14, 17, 21],
  'o': [0, 3, 6],
  'sus2': [0, 2, 7],
  'sus4': [0, 5, 7],
}
