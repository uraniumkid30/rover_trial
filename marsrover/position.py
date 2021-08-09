
class Coordinate(object):
    def __init__(self, value=0):
        self.value = value
    def __get__(self, instance, owner):
        
        return int(self.value)
    def __set__(self, instance, value):
        
        self.value = value

class Position(object):
    x = Coordinate()
    y = Coordinate()

    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def __get__(self, instance, owner):
        return self
    def __set__(self, instance, value):
        if not isinstance(value,tuple):
            raise AttributeError("You can't set a non tuple value on this attribute")
        else:
            
            self.x = value[0]
            self.y = value[1]
    def move_up(self,value=1):
        self.y += value
    
    def move_down(self,value=1):
        self.y -= value
    
    def move_left(self,value=1):
        self.x -= value
    
    def move_right(self,value=1):
        self.x += value

