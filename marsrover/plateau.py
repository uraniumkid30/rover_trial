class Plateau(object):
    MIN_WIDTH = 0
    MIN_HEIGHT = 0

    def __init__(
        self,
        width,
        height,
    ):
        if int(width) != int(height):
            print("Width and height are not equall, using max to create square")
            self.width = self.height = max([int(width), int(height)])
        else:
            self.width = int(width)
            self.height = int(height)

    def can_move(self, position):

        width_condition = self.MIN_WIDTH <= position.x <= self.width
        height_condition = self.MIN_HEIGHT <= position.y <= self.height
        return width_condition and height_condition
