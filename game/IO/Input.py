# game packages
# IO packages
from . import Window

# collection packages
from Collection.RangeGroup import RangeGroup

# built-in packages
import random


def get_int(text: str = "text", pre_input=None):
    while True:
        try:
            if pre_input is None:
                num = int(input(text + "\n"))
            else:
                num = pre_input
            Window.clear()
            return num
        except ValueError:
            Window.clear()


def get_string(text: str = "text", pre_input=None):
    Window.clear()
    if pre_input is None:
        string = input(text + "\n")
    else:
        string = pre_input
    Window.clear()
    return string


def get_range(text: str = "text", pre_input=None):
    Window.clear()
    while True:
        try:
            if pre_input is None:
                range_input = input(text + "\n").split("-")
            else:
                range_input = pre_input.split("-")

            if len(range_input) % 2 == 0:
                ranges = []
                index = 0
                range_input = [eval(i) for i in range_input]

                while index < len(range_input):
                    pos1 = range_input[index]
                    pos2 = range_input[index + 1]
                    range = RangeGroup(pos1 - 1, pos2 - 1)
                    ranges.append(range)
                    index += 2

                return ranges
            else:
                print(f"Provide input like so:\n{random.randint(1, 25)}-{random.randint(26, 50)}")
                enter_to_continue()
                break
        except TypeError:
            print(f"Provide input like so:\n{random.randint(1, 25)}-{random.randint(26, 50)}")
            enter_to_continue()
            break


def get_range_or_int(text: str = "text"):
    inp = input(text + ": ")
    try:
        inp = int(inp)
        return get_int(pre_input=inp)
    except ValueError:
        if "-" in inp:
            return get_range(pre_input=inp)
        else:
            if inp == "done":
                return "done"

def enter_to_continue():
    input("press enter to continue...\n")
    Window.clear()
