from util.filehelper import get_number_list_from_file
from ship.computer import IntComputer


def day09_01():
    program = get_number_list_from_file("./puzzles/09/puzzle.txt")
    computer = IntComputer(memory=program, inputs=[1], wait_after_output=True)
    boost_keycode = computer.run()
    print(f"BOOST keycode {boost_keycode}")


def day09_02():
    program = get_number_list_from_file("./puzzles/09/puzzle.txt")
    computer = IntComputer(memory=program, inputs=[2], wait_after_output=True)
    coordinates = computer.run()
    print(f"Coordinates {coordinates}")


if __name__ == "__main__":
    day09_01()
    day09_02()
