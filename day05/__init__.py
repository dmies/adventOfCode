from util.filehelper import get_number_list_from_file
from ship.computer import run_intcode


def day05():
    program = get_number_list_from_file("./puzzles/05/puzzle.txt")

    print(f"input 1: conditioner unit (part 1)")
    print(f"input 5: thermal radiator controller (part 2)")
    print(f"result after processing: {run_intcode(program)}")
