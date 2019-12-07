import mock
from ship.computer import IntComputer


class TestShipComputer:
    """
    From day 02
    """

    def test_run_intcode_1(self):
        expected = 2
        input = [1, 0, 0, 0, 99]
        computer = IntComputer(input)
        computer.run()
        result = computer.memory[0]
        assert expected == result

    def test_run_intcode_2(self):
        expected = 2
        input = [2, 3, 0, 3, 99]
        computer = IntComputer(input)
        computer.run()
        result = computer.memory[0]
        assert expected == result

    def test_run_intcode_3(self):
        expected = 2
        input = [2, 4, 4, 5, 99, 0]
        computer = IntComputer(input)
        computer.run()
        result = computer.memory[0]
        assert expected == result

    def test_run_intcode_4(self):
        expected = 30
        input = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        computer = IntComputer(input)
        computer.run()
        result = computer.memory[0]
        assert expected == result

    """
    From day 05
    """

    def test_parse_parameter_supports_standalone_opcode(self):
        """
        a single opcode should result in the matching number as opcode and all modes should be 0
        """
        input = [3]
        expected = (3, [0, 0, 0, 0])
        computer = IntComputer(input)
        result = computer.parse_parameter()
        assert result == expected

    def test_parse_parameter_with_example_from_description(self):
        """
        a single opcode should result in the matching number as opcode and all modes should be 0
        """
        input = [1001]
        expected = (1, [0, 1, 0, 0])
        computer = IntComputer(input)
        result = computer.parse_parameter()
        assert result == expected

    def test_parse_parameter_with_just_one_mode(self):
        input = [102]
        expected = (2, [1, 0, 0, 0])
        computer = IntComputer(input)
        result = computer.parse_parameter()
        assert result == expected

    def test_parse_parameter_with_two_modes(self):
        input = [1103]
        expected = (3, [1, 1, 0, 0])
        computer = IntComputer(input)
        result = computer.parse_parameter()
        assert result == expected

    def test_parse_parameter_with_three_modes(self):
        input = [11104]
        expected = (4, [1, 1, 1, 0])
        computer = IntComputer(input)
        result = computer.parse_parameter()
        assert result == expected

    def test_parse_parameter_with_four_modes(self):
        input = [111104]
        expected = (4, [1, 1, 1, 1])
        computer = IntComputer(input)
        result = computer.parse_parameter()
        assert result == expected

    def test_parse_parameter_with_14(self):
        input = [14]
        expected = (14, [0, 0, 0, 0])
        computer = IntComputer(input)
        result = computer.parse_parameter()
        assert result == expected

    def test_get_position_for_mode_supports_position_mode(self):
        memory = [1, 2, 3, 4]
        idx = 1
        modes = [0, 0, 0, 0]
        expected = 2
        computer = IntComputer(memory)
        result = computer.get_position_for_mode(idx, modes)
        assert result == expected

    def test_get_position_for_mode_supports_immediate_mode(self):
        memory = [1, 2, 3, 4]
        idx = 1
        modes = [1, 0, 0, 0]
        expected = 1
        computer = IntComputer(memory)
        result = computer.get_position_for_mode(idx, modes)
        assert result == expected

    def test_get_param_returns_value_from_position_provided_by_get_position_for_mode(
        self,
    ):
        memory = [1, 2, 3, 4]
        idx = 1
        modes = [1, 0, 0, 0]
        expected = 2
        computer = IntComputer(memory)
        result = computer.get_param(idx, modes)
        assert result == expected

    def test_add(self):
        memory = [1, 1, 1, 1]
        modes = [1, 1, 1, 1]
        expected = 2
        computer = IntComputer(memory)
        computer.add(modes)
        result = computer.memory[-1]
        assert result == expected

    def test_multiply(self):
        memory = [1, 2, 3, 4]
        modes = [1, 1, 1, 1]
        expected = 6
        computer = IntComputer(memory)
        computer.multiply(modes)
        result = computer.memory[-1]
        assert result == expected

    def test_outputHandler(self):
        memory = [1, 2, 3, 4]
        modes = [1, 1, 1, 1]
        expected = 2
        computer = IntComputer(memory)
        computer.outputHandler(modes)
        result = computer.output
        assert result == expected

    def test_jump_if_true(self):
        memory = [1, 2, 3, 4]
        modes = [1, 1, 1, 1]
        expected = 3
        computer = IntComputer(memory)
        computer.jump_if_true(modes)
        result = computer.pointer
        assert result == expected

