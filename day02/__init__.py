from util import get_list_from_file


def add(memory, pos):
    param_one = memory[pos + 1]
    param_two = memory[pos + 2]
    param_three = memory[pos + 3]
    memory[param_three] = memory[param_one] + memory[param_two]
    return memory


def multiply(memory, pos):
    param_one = memory[pos + 1]
    param_two = memory[pos + 2]
    param_three = memory[pos + 3]
    memory[param_three] = memory[param_one] * memory[param_two]
    return memory


operations = {1: add, 2: multiply}


def run_intcode(memory, pointer=0, noun=None, verb=None):
    """ run intcode program on memory."""
    memory[1] = noun or memory[1]
    memory[2] = verb or memory[2]

    opcode = memory[pointer]
    if opcode == 99:
        return memory[0]
    else:
        func = operations.get(opcode, None)
        memory = func(memory, pointer)
        return run_intcode(memory, pointer + 4)


def find_gravity_assist_inputs(memory, desired_output):
    """Find noun and verb that gives desired_output when intcode is run."""
    for noun in range(0, 100):
        for verb in range(0, 100):
            output = run_intcode(memory[:], noun, verb)
            if output == desired_output:
                return 100 * noun + verb
    return False


def day02_01():
    program = get_list_from_file("./puzzles/02/puzzle.txt")
    program[1] = 12
    program[2] = 2
    print("Output prior to fire: {}".format(run_intcode(program[:], 12, 2)))


def day02_02():
    program = get_list_from_file("./puzzles/02/puzzle.txt")
    print(
        "Inputs required for gravity assist calculation: {}".format(
            find_gravity_assist_inputs(program, 19690720)
        )
    )

