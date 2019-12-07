from util.filehelper import get_number_list_from_file
from ship.computer import IntComputer


def day05_01():
    program = get_number_list_from_file("./puzzles/05/puzzle.txt")
    computer = IntComputer(memory=program)
    computer.inputs = [1]
    computer.run()
    print(f"conditioner unit (part 1) {computer.output}")


def day05_02():
    program = get_number_list_from_file("./puzzles/05/puzzle.txt")
    computer = IntComputer(memory=program)
    computer.inputs = [5]
    computer.run()
    print(f"thermal radiator controller (part 2) {computer.output}")

