def get_position_for_mode(memory, pos, idx, modes):
    if modes[idx - 1] == 1:
        return pos + idx
    else:
        return memory[pos + idx]


def get_param(memory, pos, idx, modes):
    index = get_position_for_mode(memory, pos, idx, modes)
    return memory[index]


def add(memory, pointer, modes):
    value_1 = get_param(memory, pointer, 1, modes)
    value_2 = get_param(memory, pointer, 2, modes)
    pos = get_position_for_mode(memory, pointer, 3, modes)
    memory[pos] = value_1 + value_2
    return (memory, pointer + 4)


def multiply(memory, pointer, modes):
    value_1 = get_param(memory, pointer, 1, modes)
    value_2 = get_param(memory, pointer, 2, modes)
    pos = get_position_for_mode(memory, pointer, 3, modes)
    memory[pos] = value_1 * value_2
    return (memory, pointer + 4)


def save(memory, pointer, modes):
    memory[get_position_for_mode(memory, pointer, 1, modes)] = int(input("Input: "))
    return (memory, pointer + 2)


def output(memory, pointer, modes):
    target_position = get_position_for_mode(memory, pointer, 1, modes)
    print(f"output: {memory[target_position]}")
    return (memory, pointer + 2)


def jump_if_true(memory, pointer, modes):
    parameter_1 = get_param(memory, pointer, 1, modes)
    parameter_2 = get_param(memory, pointer, 2, modes)
    if parameter_1 != 0:
        return (memory, parameter_2)
    else:
        return (memory, pointer + 3)


def jump_if_false(memory, pointer, modes):
    parameter_1 = get_param(memory, pointer, 1, modes)
    parameter_2 = get_param(memory, pointer, 2, modes)
    if parameter_1 == 0:
        return (memory, parameter_2)
    else:
        return (memory, pointer + 3)


def less_than(memory, pointer, modes):
    parameter_1 = get_param(memory, pointer, 1, modes)
    parameter_2 = get_param(memory, pointer, 2, modes)
    if parameter_1 < parameter_2:
        memory[get_position_for_mode(memory, pointer, 3, modes)] = 1
    else:
        memory[get_position_for_mode(memory, pointer, 3, modes)] = 0
    return (memory, pointer + 4)


def equals(memory, pointer, modes):
    parameter_1 = get_param(memory, pointer, 1, modes)
    parameter_2 = get_param(memory, pointer, 2, modes)
    if parameter_1 == parameter_2:
        memory[get_position_for_mode(memory, pointer, 3, modes)] = 1
    else:
        memory[get_position_for_mode(memory, pointer, 3, modes)] = 0
    return (memory, pointer + 4)


operations = {
    1: add,
    2: multiply,
    3: save,
    4: output,
    5: jump_if_true,
    6: jump_if_false,
    7: less_than,
    8: equals,
}


def parse_parameter(opcode):
    modes = []
    if opcode > 100:
        mode_opcode = opcode / 100
        opcode = opcode % 100
        while mode_opcode > 0:
            modes.append(int(mode_opcode % 10))
            mode_opcode = int(mode_opcode / 10)
    while len(modes) < 4:
        modes.append(0)
    return (opcode, modes)


def run_intcode(memory, pointer=0, noun=None, verb=None):
    """ run intcode program on memory."""
    memory[1] = noun or memory[1]
    memory[2] = verb or memory[2]

    opcode, modes = parse_parameter(memory[pointer])
    if opcode == 99:
        return memory[0]
    else:
        func = operations.get(opcode, None)
        memory, updated_pointer = func(memory, pointer, modes)
        return run_intcode(memory, updated_pointer)
