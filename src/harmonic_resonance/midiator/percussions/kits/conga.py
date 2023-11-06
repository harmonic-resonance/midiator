from .kit import Kit
from ..percussion import Percussion
import harmonic_resonance.midiator.percussions.percussion_types as P

class Conga(Kit):
    '''conga kit - 2 drums + mute'''
    kit = []

    def __init__(self, part):
        """TODO: Docstring for __init__.
        """
        super().__init__(part)
        self.tumba = Percussion(part, P.low_conga)
        self.conga = Percussion(part, P.open_hi_conga)
        self.mute = Percussion(part, P.mute_hi_conga)

        self.load_patterns('conga.yaml')

        self.kit = {
            "tumba": self.tumba,
            "conga": self.conga,
            "mute": self.mute,
        }

    #  def tumbao(self, duration: int, velocity_mod: int=0):
        #  """2 measure tumbao rhythm

        #  :duration: time for phrase in milliseconds
        #  """
        #  b = int(duration/16)
        #  # 5 heel 4 toe
        #  mute =  '54_454__' + '54___4__'
        #  conga = '__7___55' + '__7___55'
        #  tumba = '________' + '___55___'
        #  # 7 slap - 5 open

        #  self.mute_conga.add_pattern(mute, b, velocity_mod=velocity_mod)
        #  self.conga.add_pattern(conga, b, velocity_mod=velocity_mod)
        #  self.tumba.add_pattern(tumba, b, velocity_mod=velocity_mod)

    #  def guaguanco(self, duration: int, velocity_mod: int=0):
        #  """2 measure guaguanco rhythm

        #  :duration: TODO
        #  """
        #  b = int(duration/16)
        #  # 5 heel 4 toe 3 touch
        #  mute =  '___5_3__' + '_____3__'
        #  conga = '_77____5' + '5-75___5'
        #  tumba = '______7_' + '______8_'
        #  # 7 slap - 5 open

        #  self.mute_conga.add_pattern(mute, b, velocity_mod=velocity_mod)
        #  self.conga.add_pattern(conga, b, velocity_mod=velocity_mod)
        #  self.tumba.add_pattern(tumba, b, velocity_mod=velocity_mod)

    #  def bolero(self, duration: int, velocity_mod: int=0):
        #  """2 measure bolero rhythm

        #  :duration: TODO
        #  """
        #  b = int(duration/16)
        #  # 5 heel 4 toe 3 touch
        #  mute =  '54_454__' + '54_45___'
        #  conga = '__7___55' + '__7___5_'
        #  tumba = '________' + '_____5_5'
        #  # 7 slap - 5 open

        #  self.mute_conga.add_pattern(mute, b, velocity_mod=velocity_mod)
        #  self.conga.add_pattern(conga, b, velocity_mod=velocity_mod)
        #  self.tumba.add_pattern(tumba, b, velocity_mod=velocity_mod)

    #  def samba(self, duration: int, velocity_mod: int=0):
        #  """2 measure  rhythm

        #  :duration: time for phrase in milliseconds
        #  """
        #  b = int(duration/16)
        #  # 5 heel 4 toe
        #  mute =  '_3____3_' + '__3__33_'
        #  conga = '5_77_5_5' + '57_7___5'
        #  tumba = '____5___' + '____5___'
        #  # 7 slap - 5 open

        #  self.mute_conga.add_pattern(mute, b, velocity_mod=velocity_mod)
        #  self.conga.add_pattern(conga, b, velocity_mod=velocity_mod)
        #  self.tumba.add_pattern(tumba, b, velocity_mod=velocity_mod)

