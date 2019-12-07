class IntComputer:
    def __init__(self, memory, pointer=0, inputs=[], wait_after_output=False):
        self.memory = memory
        self.pointer = pointer
        self.inputs = inputs
        self.output = -1
        self.finished = False
        self.wait_after_output = wait_after_output

    def get_position_for_mode(self, idx, modes):
        if modes[idx - 1] == 1:
            return self.pointer + idx
        else:
            return self.memory[self.pointer + idx]

    def get_param(self, idx, modes):
        index = self.get_position_for_mode(idx, modes)
        return self.memory[index]

    def add(self, modes):
        value_1 = self.get_param(1, modes)
        value_2 = self.get_param(2, modes)
        pos = self.get_position_for_mode(3, modes)
        self.memory[pos] = value_1 + value_2
        self.pointer += 4

    def multiply(self, modes):
        value_1 = self.get_param(1, modes)
        value_2 = self.get_param(2, modes)
        pos = self.get_position_for_mode(3, modes)
        self.memory[pos] = value_1 * value_2
        self.pointer += 4

    def save(self, modes):
        if len(self.inputs) > 0:
            user_input = self.inputs.pop(0)
            self.memory[self.get_position_for_mode(1, modes)] = user_input

        else:
            self.memory[self.get_position_for_mode(1, modes)] = int(input("Input: "))
        self.pointer += 2

    def outputHandler(self, modes):
        target_position = self.get_position_for_mode(1, modes)
        self.output = self.memory[target_position]
        self.pointer += 2

    def jump_if_true(self, modes):
        parameter_1 = self.get_param(1, modes)
        parameter_2 = self.get_param(2, modes)
        if parameter_1 != 0:
            self.pointer = parameter_2
        else:
            self.pointer += 3

    def jump_if_false(self, modes):
        parameter_1 = self.get_param(1, modes)
        parameter_2 = self.get_param(2, modes)
        if parameter_1 == 0:
            self.pointer = parameter_2
        else:
            self.pointer += 3

    def less_than(self, modes):
        parameter_1 = self.get_param(1, modes)
        parameter_2 = self.get_param(2, modes)
        if parameter_1 < parameter_2:
            self.memory[self.get_position_for_mode(3, modes)] = 1
        else:
            self.memory[self.get_position_for_mode(3, modes)] = 0
        self.pointer += 4

    def equals(self, modes):
        parameter_1 = self.get_param(1, modes)
        parameter_2 = self.get_param(2, modes)
        if parameter_1 == parameter_2:
            self.memory[self.get_position_for_mode(3, modes)] = 1
        else:
            self.memory[self.get_position_for_mode(3, modes)] = 0
        self.pointer += 4

    def parse_parameter(self):
        opcode = self.memory[self.pointer]
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

    def run(self, noun=None, verb=None):
        """ run intcode program on memory."""
        self.memory[1] = noun or self.memory[1]
        self.memory[2] = verb or self.memory[2]
        opcode, modes = self.parse_parameter()
        if opcode == 99:
            self.finished = True
            return (-1, -1)
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
        else:
            print(f"illegal opcode: {opcode}")

        return self.run()
