from enum import Enum
from typing import List, Tuple


class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class IntComputer:
    def __init__(
        self,
        memory: List[int],
        pointer: int = 0,
        inputs: List[int] = [],
        wait_after_output: bool = False,
    ):
        self.memory = {i: memory[i] for i in range(len(memory))}
        self.pointer = pointer
        self.inputs = inputs
        self.output = -1
        self.all_outputs = []
        self.finished = False
        self.relative_base = 0
        self.wait_after_output = wait_after_output

    def get_position_for_mode(self, idx: int, modes: List[Mode]) -> int:
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

    def get_param(self, idx: int, modes: List[Mode]) -> int:
        index = self.get_position_for_mode(idx, modes)
        return self.memory[index]

    def add(self, modes: List[Mode]) -> None:
        value_1 = self.get_param(1, modes)
        value_2 = self.get_param(2, modes)
        target_position = self.get_position_for_mode(3, modes)
        self.memory[target_position] = value_1 + value_2
        self.pointer += 4

    def multiply(self, modes: List[Mode]) -> None:
        value_1 = self.get_param(1, modes)
        value_2 = self.get_param(2, modes)
        target_position = self.get_position_for_mode(3, modes)
        self.memory[target_position] = value_1 * value_2
        self.pointer += 4

    def save(self, modes: List[Mode]) -> None:
        target_position = self.get_position_for_mode(1, modes)
        if len(self.inputs) > 0:
            user_input = self.inputs.pop(0)
            self.memory[target_position] = user_input
        else:
            self.memory[target_position] = int(input("Input: "))
        self.pointer += 2

    def outputHandler(self, modes: List[Mode]) -> None:
        target_position = self.get_position_for_mode(1, modes)
        self.output = self.memory[target_position]
        self.all_outputs.append(self.output)
        self.pointer += 2

    def jump_if_true(self, modes: List[Mode]) -> None:
        parameter_1 = self.get_param(1, modes)
        parameter_2 = self.get_param(2, modes)
        if parameter_1 != 0:
            self.pointer = parameter_2
        else:
            self.pointer += 3

    def jump_if_false(self, modes: List[Mode]) -> None:
        parameter_1 = self.get_param(1, modes)
        parameter_2 = self.get_param(2, modes)
        if parameter_1 == 0:
            self.pointer = parameter_2
        else:
            self.pointer += 3

    def less_than(self, modes: List[Mode]) -> None:
        parameter_1 = self.get_param(1, modes)
        parameter_2 = self.get_param(2, modes)
        target_position = self.get_position_for_mode(3, modes)
        if parameter_1 < parameter_2:
            self.memory[target_position] = 1
        else:
            self.memory[target_position] = 0
        self.pointer += 4

    def equals(self, modes: List[Mode]) -> None:
        parameter_1 = self.get_param(1, modes)
        parameter_2 = self.get_param(2, modes)
        target_position = self.get_position_for_mode(3, modes)
        if parameter_1 == parameter_2:
            self.memory[target_position] = 1
        else:
            self.memory[target_position] = 0
        self.pointer += 4

    def adjust_relative_base(self, modes: List[Mode]) -> None:
        parameter_1 = self.get_param(1, modes)
        self.relative_base += parameter_1
        self.pointer += 2

    def parse_parameter(self) -> Tuple[int, List[Mode]]:
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

    def run(self, noun: int = None, verb: int = None) -> Tuple[int, int]:
        while not self.finished:
            """ run intcode program on memory."""
            self.memory[1] = noun or self.memory[1]
            self.memory[2] = verb or self.memory[2]
            opcode, modes = self.parse_parameter()
            if opcode == 99:
                self.finished = True
                return (-1, self.output)
            elif opcode == 1:
                self.add(modes)
            elif opcode == 2:
                self.multiply(modes)
            elif opcode == 3:
                self.save(modes)
            elif opcode == 4:
                self.outputHandler(modes)
                if self.wait_after_output:
                    return (1, self.output)
            elif opcode == 5:
                self.jump_if_true(modes)
            elif opcode == 6:
                self.jump_if_false(modes)
            elif opcode == 7:
                self.less_than(modes)
            elif opcode == 8:
                self.equals(modes)
            elif opcode == 9:
                self.adjust_relative_base(modes)
            else:
                print(f"illegal opcode: {opcode}")

