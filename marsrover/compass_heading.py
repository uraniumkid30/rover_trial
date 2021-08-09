import sys
from .constants import DIRECTIONS

class Directions(object):
    def __get__(self, instance, owner):
        return DIRECTIONS
    def __set__(self, instance, value):
        
        raise AttributeError("You can't set a value on this attribute")

class CardinalPoint(object):
    if sys.version_info[0] < 3:
        cardinal = Directions()
    def __init__(self, cardinal):
        if sys.version_info[0] >= 3:
            self.cardinal = cardinal
    def __get__(self, instance, owner):
        _ordinal = instance.heading
        _cardinal = {self.cardinal[x]:x for x in self.cardinal}.get(_ordinal)
        return _cardinal
    def __set__(self, instance, value):
        
        self.ordinal = value

class CompassHeading(object):
    
    if sys.version_info[0] >= 3:
        from types import MappingProxyType
        _DIRECTIONS = MappingProxyType(DIRECTIONS)
    else:
        _DIRECTIONS = Directions()
    cardinal = CardinalPoint(_DIRECTIONS)
    def __init__(self,direction):
        self.heading = self._DIRECTIONS.get(direction)
    

    def turn_left(self,):
        #
        self.heading = self._DIRECTIONS['W'] if (self.heading - 1) < self._DIRECTIONS['N'] else self.heading - 1

    def turn_right(self,):
        self.heading = self._DIRECTIONS['N'] if (self.heading + 1) > self._DIRECTIONS['W'] else self.heading + 1

    def __str__(self):
        return self.cardinal
