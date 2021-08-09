from marsrover import Rover
from marsrover import DataHandler


def main():
    data = DataHandler().data
    if data:
        rover = Rover(data)
        rover.process()
    else:
        print("No data to work with")


if __name__ == "__main__":
    main()
