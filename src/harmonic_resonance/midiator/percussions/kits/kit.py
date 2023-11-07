import yaml
from pathlib import Path


class Kit:
    """
    A base class for a drum kit, defining common functionalities for percussion
    instruments that can be subclassed for specific drum kit configurations.
    """

    def __init__(self, part):
        """
        Initialize the drum kit with a specified MIDI part.

        :param part: The MIDI part to be used for this kit, typically defining the
                     MIDI channel or instrument preset used for the percussion sounds.
        """
        self.part = part
        self.kit = {}

    def rest_all(self, duration: int):
        """
        Set a rest for all percussion instruments in the kit for a specified duration.

        This function silences every instrument in the kit, effectively
        creating a pause or break in the rhythm.

        :param duration: The duration of the rest in MIDI ticks. This is not in
            milliseconds but in the MIDI's delta time based on ticks per beat.
        """
        duration = int(duration)  # Ensuring duration is an integer value.
        for perc in self.kit.values():
            perc.set_rest(duration)

    def set_patterns(self, pattern_set, duration, velocity_mod=0):
        """
        Apply a set of rhythm patterns to the instruments in the drum kit.

        This method reads a pattern set and configures each percussion instrument
        with its specified pattern, length, and dynamic modifications.

        :param pattern_set: A dictionary mapping instrument names to their
            rhythm patterns.  Each key is the name of an instrument as stored in
            the kit, and its value is the pattern string to be set for the
            instrument.
        :param duration: The total duration over which the pattern set should
            be applied, given in MIDI ticks.
        :param velocity_mod: A modifier to the default velocity (intensity) of
            each note in the pattern, allowing for dynamic variations.
        """
        #  for perc, pattern in pattern_set.items():
            #  b = int(duration / len(pattern))
            #  self.kit[perc].add_pattern(pattern, b, velocity_mod=velocity_mod)
        for perc_name, perc in self.kit.items():
            if perc_name in pattern_set:
                pattern = pattern_set[perc_name]
                b = int(duration / len(pattern))
                perc.add_pattern(pattern, b, velocity_mod=velocity_mod)
            else:
                perc.set_rest(duration)
                

    def load_patterns(self, yaml_file_name: str):
        """
        load patterns from associated yaml file
        """
        # TODO: if no file name - get yaml file with same name as script
        script_dir = Path(__file__).parent.absolute()
        yaml_file_path = script_dir / yaml_file_name

        with open(yaml_file_path, "r") as f:
            self.patterns = yaml.safe_load(f)
