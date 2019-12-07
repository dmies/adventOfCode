from ship.computer import IntComputer
from util.filehelper import get_number_list_from_file


def get_all_phases(start, end):
    res = []
    for a in range(start, end):
        for b in filter(lambda x: x not in [a], range(start, end)):
            for c in filter(lambda x: x not in [a, b], range(start, end)):
                for d in filter(lambda x: x not in [a, b, c], range(start, end)):
                    for e in filter(lambda x: x not in [a, b, c, d], range(start, end)):
                        phases = [a, b, c, d, e]
                        res.append(phases)
    return res


def calculate_max_thruster(original_memory):
    res = 0
    all_phases = get_all_phases(0, 5)
    for phases in all_phases:
        second_input = 0
        for phase in phases:
            first_input = phase
            memory = original_memory.copy()
            computer = IntComputer(
                memory[:], inputs=[first_input, second_input], wait_after_output=True
            )
            computer.run()
            second_input = computer.output
        if second_input > res:
            res = second_input
    return res


def calculate_optimized_thruster(original_memory):

    res = 0
    phases = []
    all_phases = get_all_phases(5, 10)
    for phases in all_phases:
        calculating = True
        current_amplifier = 0
        states = []

        for phase in phases:
            first_input = phase
            memory = original_memory.copy()
            amplifier = IntComputer(
                memory, inputs=[first_input], wait_after_output=True
            )
            states.append(amplifier)
        states[0].inputs.append(0)
        while calculating:
            amplifier = states[current_amplifier]

            if not amplifier.finished:
                amplifier.run()
                next_input = amplifier.output
                next_amplifier = states[(current_amplifier + 1) % 5]
                next_amplifier.inputs.append(next_input)
                states[(current_amplifier + 1) % 5] = next_amplifier

            if amplifier.finished:
                calculating = True
                for amp in states:
                    calculating = not (amp.finished and calculating)

            current_amplifier = (current_amplifier + 1) % 5

        last_amplifier = states[-1]

        if res < last_amplifier.output:
            res = last_amplifier.output

    return res


def day07_01():
    program = get_number_list_from_file("./puzzles/07/puzzle.txt")
    res = calculate_max_thruster(program)
    print(f"The highest signal that can be sent to the thrusters is: {res}")


def day07_02():
    program = get_number_list_from_file("./puzzles/07/puzzle.txt")
    res = calculate_optimized_thruster(program)
    print(
        f"The highest signal (combined amplifiers) that can be sent to the thrusters is: {res}"
    )
