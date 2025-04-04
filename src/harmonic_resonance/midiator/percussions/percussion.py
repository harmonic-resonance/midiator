import harmonic_resonance.midiator as pm
from ..instruments import Instrument


class Percussion(Instrument):
    """Class for creating MIDI percussion tracks using midiator.

    The Percussion class inherits from Instrument and allows setting up
    percussion hits and patterns on the default MIDI drum channel (10 in MIDI
    convention, but 9 in 0-indexed Python).
    """

    def __init__(self, midi_file, instrument_id, channel=9):
        """Initializes a Percussion instance.

        Args:
            midi_file (MidiFile): The MIDI file to which this percussion track
                will be added.
            instrument_id (int): The ID representing the percussion instrument
                as per General MIDI level 1 standard.
            channel (int): The MIDI channel assigned for percussion (usually
                channel 10, which is 9 in 0-indexed).
        """
        self.name = pm.P.PERCUSSIONS[
            instrument_id
        ]  # Get the name of the instrument using its ID
        self.instrument = instrument_id  # Instrument note number on the drum channel
        self.channel = channel  # MIDI channel for drums

        # Create and name a new track for the percussion instrument in the
        # provided MIDI file
        self.track = midi_file.add_track(name=self.name)
        # Set the MIDI program change message to select the correct instrument
        self.track.append(
            pm.Message(
                "program_change", channel=self.channel, program=self.instrument, time=0
            )
        )

        # Add tracks for volume and pan control, similar to Instrument
        self.track_volume = midi_file.add_track(name=f'{self.name}-volume')
        self.track_pan = midi_file.add_track(name=f'{self.name}-pan')
        #  self.track_reverb = pm.set_new_track(mf, name=f'{self.name}-reverb') # Consider adding if needed later
        #  self.track_chorus = pm.set_new_track(mf, name=f'{self.name}-chorus') # Consider adding if needed later


    def set_hit(self, duration, velocity=64):
        """Sets a single percussion hit.

        Args:
            duration (int): The duration of the note in MIDI ticks.
            velocity (int): The velocity (volume) of the note-on message.
        """
        duration = int(duration)
        # Note on for the specified instrument and velocity
        self.track.append(
            pm.Message(
                "note_on",
                note=self.instrument,
                channel=self.channel,
                velocity=velocity,
                time=0,
            )
        )
        # Note off after the specified duration
        self.track.append(
            pm.Message(
                "note_off",
                note=self.instrument,
                channel=self.channel,
                velocity=127,
                time=duration,
            )
        )

    def set_hits(self, duration, divisions, velocity=64):
        """Sets multiple percussion hits equally spaced within the given duration.

        Args:
            duration (int): The total duration in which the hits are to be placed.
            divisions (int): The number of hits to be placed within the total duration.
            velocity (int): The velocity (volume) of each note-on message.
        """
        hit_duration = int(duration / divisions)
        for _ in range(divisions):
            self.set_hit(hit_duration, velocity)

    def add_pattern(self, pattern: str, beat_duration: int, velocity_mod: int = 0):
        """
        Adds a rhythm pattern to the percussion track.

        Args:
            pattern (str): String with characters representing hits (numbers)
                or rests ('_').  A dash ('-') after a hit extends the hit's
                duration by one beat_duration.
            beat_duration (int): The duration of one beat in MIDI ticks.
            velocity_mod (int): Modifier to adjust the overall velocity for the pattern.
        """
        index = 0
        while index < len(pattern):
            p = pattern[index]
            if p == "_":
                # Advance the position for rest
                self.set_rest(beat_duration)
                index += 1
            elif p.isdigit():
                # Calculate the number of subsequent dashes to extend the
                # note's duration
                extension_count = 0
                look_ahead_index = index + 1
                while (
                    look_ahead_index < len(pattern) and pattern[look_ahead_index] == "-"
                ):
                    extension_count += 1
                    look_ahead_index += 1

                total_duration = beat_duration * (1 + extension_count)
                velocity = int(p) * 12 + velocity_mod
                self.set_hit(total_duration, velocity=velocity)

                # Skip over the dashes that have been accounted for in the
                # extended duration
                index = look_ahead_index
            else:
                # For unrecognized characters, simply move to the next character
                index += 1
