import harmonic_resonance.midiator as pm

class Instrument():

    """Docstring for Instrument. """

    def __init__(self, mf, inst_id, channel):
        """TODO: to be defined. """
        self.name = pm.I.INSTRUMENTS[inst_id]
        self.instrument = inst_id
        self.channel = channel

        self.track = mf.add_track(name=self.name)
        self.track.append(pm.Message('program_change', channel=channel, program=inst_id, time=0))

        self.track_volume = mf.add_track(name=f'{self.name}-volume')
        self.track_pan = mf.add_track(name=f'{self.name}-pan')
        #  self.track_reverb = pm.set_new_track(mf, name=f'{self.name}-reverb')
        #  self.track_chorus = pm.set_new_track(mf, name=f'{self.name}-chorus')


    def set_text(self, text, duration=0):
        '''appends  a ``text`` message for the ``duration`` to the Instrument track
        '''
        duration = int(duration)
        self.track.append(pm.MetaMessage('text', text=text, time=duration))

    def set_rest(self, duration):
        '''appends  a ``note_off`` message for the ``duration`` to the Instrument track
        '''
        duration = int(duration)
        self.track.append(pm.Message('note_off', note=0, channel=self.channel, velocity=127, time=duration))

    def set_note(self, note, duration, velocity=64):
        duration = int(duration)
        self.track.append(pm.Message('note_on', note=note, channel=self.channel, velocity=velocity, time=0))
        self.track.append(pm.Message('note_off', note=note, channel=self.channel, velocity=127, time=duration))

    def set_notes(self, notes, duration, offset=0, velocity=64):
        duration = int(duration)
        offset = int(offset)
        # notes on
        for i, note in enumerate(notes):
            if i == 0:
                time = 0
            else:
                time = offset
            self.track.append(pm.Message('note_on', note=note, channel=self.channel, velocity=velocity, time=time))
        # notes off
        for i, note in enumerate(notes):
            if i == 0:
                #  time = duration
                time = duration -  (offset * (len(notes) - 1))
            else:
                time = 0
            self.track.append(pm.Message('note_off', note=note, channel=self.channel, velocity=127, time=time))

    def set_chord(self, root, duration, chord_type=pm.C.major, velocity=64):
        duration = int(duration)
        notes = pm.get_chord_notes(root, chord_type)
        self.set_notes(notes, duration, offset=0, velocity=velocity)
        #  for offset in chord:
            #  self.track.append(pm.Message('note_on', note=root+offset, channel=self.channel, velocity=velocity, time=0))
        #  for offset in chord:
            #  if offset == 0:
                #  time = duration
            #  else:
                #  time = 0
            #  self.track.append(pm.Message('note_off', note=root+offset, channel=self.channel, velocity=127, time=time))

    def ramp_volume_up(self, duration, lo=32, hi=96):
        duration = int(duration)
        steps = range(lo, hi)
        num_steps = len(steps)
        if num_steps == 0: return

        base_step_duration = duration // num_steps
        remainder_ticks = duration % num_steps

        for i, val in enumerate(steps):
            step_duration = base_step_duration
            if i < remainder_ticks: # Distribute remainder to first few steps
                step_duration += 1
            self.set_volume(val, step_duration)

    def ramp_volume_down(self, duration, lo=32, hi=96):
        duration = int(duration)
        steps = range(lo, hi)
        num_steps = len(steps)
        if num_steps == 0: return

        base_step_duration = duration // num_steps
        remainder_ticks = duration % num_steps

        # Iterate through reversed steps but distribute remainder based on loop index
        reversed_steps = list(reversed(steps))
        for i, val in enumerate(reversed_steps):
            step_duration = base_step_duration
            if i < remainder_ticks: # Distribute remainder to first steps of the ramp execution
                 step_duration += 1
            self.set_volume(val, step_duration)

    def set_volume(self, level, duration):
        duration = int(duration)
        self.track_volume.append(pm.Message('control_change', channel=self.channel, control=7, value=level, time=0))
        self.track_volume.append(pm.Message('control_change', channel=self.channel, control=7, value=level, time=duration))


    def set_pan(self, level, duration):
        duration = int(duration)
        self.track_pan.append(pm.Message('control_change', channel=self.channel, control=10, value=level, time=duration))
        # try balance - control=8
        #  self.track_pan.append(pm.Message('control_change', channel=self.channel, control=8, value=level, time=duration))

    #  def set_balance(self, level, duration):
        #  duration = int(duration)
        #  self.track_volume.append(pm.Message('control_change', channel=self.channel, control=8, value=level, time=duration))

    #  def set_reverb(self, level, duration):
        #  duration = int(duration)
        #  self.track_reverb.append(pm.Message('control_change', channel=self.channel, control=91, value=level, time=duration))

    #  def set_chorus(self, level, duration):
        #  duration = int(duration)
        #  self.track_chorus.append(pm.Message('control_change', channel=self.channel, control=93, value=level, time=duration))
