'''
arpeggio functions
'''

def add_arp_up(instrument, notes, length):
    '''sequence notes in succession divided evenly across length'''
    beat = length / len(notes)
    for note in notes:
        instrument.set_note(note, beat)

def add_arp_down(instrument, notes, length):
    '''sequence notes in reverse succession divided evenly across length'''
    beat = length / len(notes)
    for note in reversed(notes):
        instrument.set_note(note, beat)


