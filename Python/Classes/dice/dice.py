"""
    This module will hold the model of a die, which will have
    as many of sides as the user needs and will also have a method
    for roling that die.
"""
from random import randint

class Die():
    """Model of a die."""

    def __init__(self):
        self.sides = 6

    def roll_dice(self, times):
        while times > 0:
            x = randint(1, self.sides)
            print('\n\tYou roll your {} sided die and get {}'.format(
            self.sides, x))
            times -= 1

