import unittest
from marsrover import *


class TestPosition(unittest.TestCase):
    def testConstructor(self):
        position = Position()
        self.assertEqual(position.x, 0)
        self.assertEqual(position.y, 0)

        position = Position(33, 56)
        self.assertEqual(position.x, 33)
        self.assertEqual(position.y, 56)


class TestPlateau(unittest.TestCase):
    def testConstructor(self):
        plateau = Plateau(3, 20)

        self.assertEqual(plateau.width, 20)
        self.assertEqual(plateau.height, 20)


class TestRover(unittest.TestCase):
    def testConstructor(self):
        data = [
            "55",
            "12N",
            "LMLMLMLMM",
            "33E",
            "MMRMMRMRRM",
        ]

        rover = Rover(data)
        rover.process()
        self.assertEqual(str(rover), "5 1 E")


if __name__ == "__main__":
    unittest.main()
