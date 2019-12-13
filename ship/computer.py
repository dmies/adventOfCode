import enum
import typing


class Mode(enum.Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class IntComputer:
    # before init: static variables

    def __init__(
        self,
        memory: typing.List[int],
        pointer: int = 0,
        inputs: typing.List[int] = [],
        wait_after_output: bool = False,
        wait_for_input: bool = False,
    ):
        self.memory = {i: memory[i] for i in range(len(memory))}
        self.pointer = pointer
        self.inputs = inputs
        self.output = -1
        self.finished = False
        self.waiting = False
        self.relative_base = 0
        self.wait_after_output = wait_after_output
        self.wait_for_input = wait_for_input

        self.opcode_to_function = {
            1: self.add,
            2: self.multiply,
            3: self.save,
            4: self.output_handler,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            9: self.adjust_relative_base,
        }

    # after init instance variables

    def get_position_for_mode(self, idx: int, modes: typing.List[Mode]) -> int:
        mode = modes[idx - 1]
        res = -1
        if mode == Mode.IMMEDIATE:
            res = self.pointer + idx
        elif mode == Mode.RELATIVE:
            res = self.memory[self.pointer + idx] + self.relative_base
        else:
            res = self.memory[self.pointer + idx]
        if res not in self.memory:
            self.memory[res] = 0
        return res

    def get_param(self, idx: int, modes: typing.List[Mode]) -> int:
        index = self.get_position_for_mode(idx, modes)
        return self.memory[index]

    def add(self, modes: typing.List[Mode]) -> None:
        value_1 = self.get_param(1, modes)
        value_2 = self.get_param(2, modes)
        target_position = self.get_position_for_mode(3, modes)
        self.memory[target_position] = value_1 + value_2
        self.pointer += 4

    def multiply(self, modes: typing.List[Mode]) -> None:
        value_1 = self.get_param(1, modes)
        value_2 = self.get_param(2, modes)
        target_position = self.get_position_for_mode(3, modes)
        self.memory[target_position] = value_1 * value_2
        self.pointer += 4

    def save(self, modes: typing.List[Mode]) -> None:
        target_position = self.get_position_for_mode(1, modes)
        if len(self.inputs) > 0:
            user_input = self.inputs.pop(0)
            self.memory[target_position] = user_input
        else:
            self.memory[target_position] = int(input("Input: "))
        self.pointer += 2

    def output_handler(self, modes: typing.List[Mode]) -> None:
        self.output = self.get_param(1, modes)
        self.pointer += 2

    def jump_if_true(self, modes: typing.List[Mode]) -> None:
        parameter_1 = self.get_param(1, modes)
        parameter_2 = self.get_param(2, modes)
        if parameter_1 != 0:
            self.pointer = parameter_2
        else:
            self.pointer += 3

    def jump_if_false(self, modes: typing.List[Mode]) -> None:
        parameter_1 = self.get_param(1, modes)
        parameter_2 = self.get_param(2, modes)
        if parameter_1 == 0:
            self.pointer = parameter_2
        else:
            self.pointer += 3

    def less_than(self, modes: typing.List[Mode]) -> None:
        parameter_1 = self.get_param(1, modes)
        parameter_2 = self.get_param(2, modes)
        target_position = self.get_position_for_mode(3, modes)
        if parameter_1 < parameter_2:
            self.memory[target_position] = 1
        else:
            self.memory[target_position] = 0
        self.pointer += 4

    def equals(self, modes: typing.List[Mode]) -> None:
        parameter_1 = self.get_param(1, modes)
        parameter_2 = self.get_param(2, modes)
        target_position = self.get_position_for_mode(3, modes)
        if parameter_1 == parameter_2:
            self.memory[target_position] = 1
        else:
            self.memory[target_position] = 0
        self.pointer += 4

    def adjust_relative_base(self, modes: typing.List[Mode]) -> None:
        parameter_1 = self.get_param(1, modes)
        self.relative_base += parameter_1
        self.pointer += 2

    def parse_parameter(self) -> typing.Tuple[int, typing.List[Mode]]:
        opcode = self.memory[self.pointer]
        modes = []
        if opcode > 100:
            mode_opcode = opcode / 100
            opcode = opcode % 100
            while mode_opcode > 0:
                modes.append(Mode(int(mode_opcode % 10)))
                mode_opcode = int(mode_opcode / 10)
        while len(modes) < 4:
            modes.append(Mode.POSITION)
        return (opcode, modes)

    def run(self, noun: int = None, verb: int = None) -> typing.Optional[int]:
        self.waiting = False
        while not self.finished:
            """ run intcode program on memory."""
            if 1 in self.memory:
                self.memory[1] = noun or self.memory[1]
            if 2 in self.memory:
                self.memory[2] = verb or self.memory[2]
            opcode, modes = self.parse_parameter()
            """ opcodes 99 and 4 must be handled before default opcode processing """
            if opcode == 99:
                """ program is finished """
                self.waiting = True
                self.finished = True
                return self.output
            elif opcode == 3 and len(self.inputs) == 0 and self.wait_for_input:
                """ program waits for input """
                self.waiting = True
                return None
            else:
                try:
                    func = self.opcode_to_function[opcode]
                except KeyError:  # as e:
                    raise Exception(f"Unknown opcode {opcode}")
                func(modes)
                # output must be returned after processing
                if opcode == 4 and self.wait_after_output:
                    return self.output

