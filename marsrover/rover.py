import re
from .position import Position
from .plateau import Plateau
from .compass_heading import CompassHeading
from .constants import AVAILABLE_COMMANDS


class CommandCenter(object):
    def __init__(self, compass_obj, position_obj):
        self.compass_obj = compass_obj
        self.position_obj = position_obj
        self.wrapped = None

    def __getattr__(self, attrname):
        print("Trace: " + attrname)
        if self.wrapped:
            return getattr(self.wrapped, attrname)

    def __call__(self, command="", can_move=True):
        if command in ("L", "R"):
            self.wrapped = self.compass_obj
        elif command in ("MN", "MS", "ME", "MW") and can_move:
            self.wrapped = self.position_obj
        if self.wrapped:
            return getattr(self.wrapped, AVAILABLE_COMMANDS.get(command))
        self.wrapped = None


class Rover(object):
    position = Position()

    def __init__(
        self,
        data,
    ):
        self.data = data
        plateau_data = self.check_numeric_data(self.data.pop(0))
        self.plateau = None
        if plateau_data:
            self.plateau = Plateau(*plateau_data)

    def __str__(self):
        return self.current_position

    def set_position(self, x, y, heading):
        if not isinstance(self.position, Position):
            self.position = Position(x, y)
        else:
            self.position = (x, y)

        self.compass.heading = heading

    @property
    def current_position(self):
        return "{} {} {}".format(
            self.position.x, self.position.y, self.compass.cardinal
        )

    def process(
        self,
    ):
        for x, row in enumerate(self.data, start=1):
            if x % 2 == 0:
                commands = row
                for command in commands:
                    self.run_command(command)
                print(self)
            else:
                position_data = self.check_numeric_data(row[:2])
                if x == 1:
                    self.compass = CompassHeading(row[2])
                    if position_data:
                        self.position = tuple([x for x in position_data])
                    else:
                        break
                else:
                    self.compass = CompassHeading(row[2])
                    if position_data:
                        self.position = tuple([x for x in position_data])
                    else:
                        break

    def run_command(self, command):
        can_move = self.plateau.can_move(self.position)
        command_center = CommandCenter(self.compass, self.position)
        if command == "M":
            command += self.compass.cardinal
        exec_command = command_center(command, can_move)
        exec_command()

    def check_numeric_data(self, data):
        if len(data) >= 2:
            if all([re.match("\d", x) for x in data]):
                return data[:2]
            else:
                print("i need only numeric values")
        else:
            print("incomplete information")
