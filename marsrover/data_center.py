import re
import sys
import argparse


class DataHandler(object):
    DATA_SIZE_MIN = 3
    DATA_SIZE_MAX = 5

    def __init__(self, data_source="console"):
        self.data = self.data_factory(data_source)

    def data_factory(self, data_source):
        try:
            if data_source == "console":
                self.console_wrapper()
            else:
                pass
        except:
            e = sys.exc_info()[0]
            print(e)
            return self.default()

    def clean_data(self, data):
        data_size = len(data)
        if data_size and (
            (data_size % DATA_SIZE_MIN == 0) or (data_size % DATA_SIZE_MAX == 0)
        ):
            cleaned_data = [re.sub("\W", "", data[x]) for x in range(len(data))]
            return cleaned_data
        else:
            print("data is corrupted")

    def default(self):
        data_input = input(
            "You can use the ENTER key to EXIT or type in rover information directly: "
        )
        response = self.clean_data(data_input.split(","))
        return response

    def console_wrapper(self):
        help_text = "create a textfile (NN.txt) and run 'main.py @NN.txt' "
        parser = argparse.ArgumentParser(
            fromfile_prefix_chars="@",
            prog="Rover app",
            description="get all information required to run rover app from a text file (optional)",
            epilog="Enjoy the program! :)",
        )
        parser.add_argument(
            "rover_information", help=help_text, type=str, nargs="*", default=""
        )
        args = parser.parse_args()
        response = self.clean_data(args.rover_information)
        return response
