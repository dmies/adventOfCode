from util.filehelper import get_number_list_from_file
from ship.computer import IntComputer


def find_gravity_assist_inputs(memory, desired_output):
    """Find noun and verb that gives desired_output when intcode is run."""
    for noun in range(0, 100):
        for verb in range(0, 100):
            computer = IntComputer(memory=memory[:], pointer=0)
            computer.run(noun=noun, verb=verb)
            output = computer.memory[0]
            if output == desired_output:
                return 100 * noun + verb
    return False


def day02_01():
    program = get_number_list_from_file("./puzzles/02/puzzle.txt")
    computer = IntComputer(memory=program[:], pointer=0)
    computer.run(noun=12, verb=2)
    print("Output prior to fire: {}".format(computer.memory[0]))


def day02_02():
    program = get_number_list_from_file("./puzzles/02/puzzle.txt")
    print(
        "Inputs required for gravity assist calculation: {}".format(
            find_gravity_assist_inputs(program, 19690720)
        )
    )

