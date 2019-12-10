from util.filehelper import get_number_list_from_file
from ship.computer import IntComputer


def day09_01():
    program = get_number_list_from_file("./puzzles/09/puzzle.txt")
    computer = IntComputer(memory=program, inputs=[1])
    computer.run()
    print(f"BOOST keycode {computer.all_outputs}")


def day09_02():
    program = get_number_list_from_file("./puzzles/09/puzzle.txt")
    computer = IntComputer(memory=program, inputs=[2])
    computer.run()
    print(f"Coordinates {computer.all_outputs}")


if __name__ == "__main__":
    day09_01()
    day09_02()
