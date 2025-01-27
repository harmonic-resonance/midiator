


# midiator



## recent logs






### mission



* [goals](#goals)



Summary



#### goals







### usage




### modules




#### harmonic\_resonance.midiator



##### midiator



###### HARMONIC resonance






harmonic\_resonance.midiator.new\_midi(*title=''*, *tempo=500000*) → MidiFile
sets up a mido midi file with initial meta track





harmonic\_resonance.midiator.set\_new\_track(*mf*, *name=''*, *instrument=''*)



harmonic\_resonance.midiator.save\_midi(*mf*, *folder*, *filename*)



harmonic\_resonance.midiator.play(*filepath: [str](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")*)
TODO: Docstring for play.



Filepath:
TODO



Returns:
TODO







#### harmonic\_resonance.midiator.part


Part extend the mido `MidiFile` object
- keeps track of instruments, channels




*class* harmonic\_resonance.midiator.part.Part(*project: [str](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")*, *title: [str](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")*, *bpm: [int](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)") = 120*, *bpM: [int](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)") = 4*, *beat\_val: [int](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)") = 4*, *root: [int](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)") = 60*, *key: [str](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)") = 'C'*)
Bases: `MidiFile`


Part object extends the mido MidoFile




free\_channels *= [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]*



perc\_channel *= None*



instruments *= []*



measure\_ticks()
return measure duration in ticks
used for setting the `M` variable in a composition



Returns:
int







set\_marker(*text*, *duration=0*)
appends a `marker` message at `duration` to the meta track
:duration: offset for placement of marker





get\_mid\_path() → [Path](https://docs.python.org/3.9/library/pathlib.html#pathlib.Path "(in Python v3.9)")



save()
Save to a file.


If file is passed the data will be saved to that file. This is
typically an in-memory file or and already open file like sys.stdout.


If filename is passed the data will be saved to that file.


Raises ValueError if both file and filename are None,
or if a type 0 file has != one track.





play()
this overrides the mido play function





convert()
this overrides the mido play function





add\_instrument(*instrument\_type: <module 'harmonic\_resonance.midiator.instruments.instrument\_types' from '/home/phiarchitect/PROJECTS/harmonic-resonance/midiator/src/harmonic\_resonance/midiator/instruments/instrument\_types.py'>*) → Instrument
add instrument to session
set to next available channel



Instrument\_type:
TODO



Returns:
TODO







add\_voice(*voice\_type: <module 'harmonic\_resonance.midiator.voices.voice\_types' from '/home/phiarchitect/PROJECTS/harmonic-resonance/midiator/src/harmonic\_resonance/midiator/voices/voice\_types.py'>*) → Voice
add instrument to session
set to next available channel



Instrument\_type:
TODO



Returns:
TODO







add\_kick()



add\_piano()



add\_vibes()



add\_bass()



add\_horns()



add\_strings()



add\_solo\_ooh()



add\_solo\_aah()



add\_choir\_aah()



add\_choir\_ooh()



add\_choir\_mixed()



add\_choir\_swell()



add\_choir\_little\_swell()




#### harmonic\_resonance.midiator.notes




#### harmonic\_resonance.midiator.scales


utils for building scales




harmonic\_resonance.midiator.scales.build\_scale(*root=48*, *scale\_type='major'*, *octaves=3*)



*class* harmonic\_resonance.midiator.scales.Scale(*root*, *scale\_type*, *octaves=1*)
Bases: [`dict`](https://docs.python.org/3.9/library/stdtypes.html#dict "(in Python v3.9)")





*class* harmonic\_resonance.midiator.scales.Key(*root: [int](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")*)
Bases: [`object`](https://docs.python.org/3.9/library/functions.html#object "(in Python v3.9)")


generate classic key offsets for a root note




position(*num: [int](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")*)
numeric position






#### harmonic\_resonance.midiator.chords




harmonic\_resonance.midiator.chords.get\_chord\_notes(*root*, *chord\_type*)



#### harmonic\_resonance.midiator.instruments


wrapper for managing instruments




harmonic\_resonance.midiator.instruments.make\_piano(*mf*, *channel*)



harmonic\_resonance.midiator.instruments.make\_vibes(*mf*, *channel*)



harmonic\_resonance.midiator.instruments.make\_bass(*mf*, *channel*)



harmonic\_resonance.midiator.instruments.make\_horns(*mf*, *channel*)



harmonic\_resonance.midiator.instruments.make\_strings(*mf*, *channel*)



#### harmonic\_resonance.midiator.percussions


<https://docs.google.com/spreadsheets/d/19_3BxUMy3uy1Gb0V8Wc-TcG7q16Amfn6e8QVw4-HuD0/edit#gid=0>




harmonic\_resonance.midiator.percussions.make\_tick(*mf*)



harmonic\_resonance.midiator.percussions.make\_kick(*mf*)



harmonic\_resonance.midiator.percussions.make\_low\_tom(*mf*)



harmonic\_resonance.midiator.percussions.make\_high\_tom(*mf*)



harmonic\_resonance.midiator.percussions.make\_floor\_tom(*mf*)



harmonic\_resonance.midiator.percussions.make\_snare(*mf*)



harmonic\_resonance.midiator.percussions.make\_hihat\_closed(*mf*)



harmonic\_resonance.midiator.percussions.make\_hihat\_open(*mf*)



harmonic\_resonance.midiator.percussions.make\_crash(*mf*)



harmonic\_resonance.midiator.percussions.make\_ride(*mf*)



harmonic\_resonance.midiator.percussions.make\_kit\_1(*mf*)



harmonic\_resonance.midiator.percussions.make\_kit\_toms(*mf*)



#### harmonic\_resonance.midiator.voices




harmonic\_resonance.midiator.voices.make\_solo\_ooh(*mf*)



harmonic\_resonance.midiator.voices.make\_solo\_aah(*mf*)



harmonic\_resonance.midiator.voices.make\_choir\_aah(*mf*)



harmonic\_resonance.midiator.voices.make\_choir\_ooh(*mf*)



harmonic\_resonance.midiator.voices.make\_choir\_mixed(*mf*)



harmonic\_resonance.midiator.voices.make\_choir\_swell(*mf*)



harmonic\_resonance.midiator.voices.make\_choir\_little\_swell(*mf*)



#### harmonic\_resonance.midiator.arps


arpeggio functions




harmonic\_resonance.midiator.arps.add\_arp\_up(*instrument*, *notes*, *length*)
sequence notes in succession divided evenly across length





harmonic\_resonance.midiator.arps.add\_arp\_down(*instrument*, *notes*, *length*)
sequence notes in reverse succession divided evenly across length







### demos




#### demo



```


```






### references






### todos






## indices


* [Index](genindex.html)
* [Module Index](py-modindex.html)
* [Search Page](search.html)







