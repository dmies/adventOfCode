from mock import patch
from ship.computer import IntComputer, Mode


class TestShipComputer:
    """
    From day 02
    """

    def test_run_intcode_1(self):
        expected = 2
        memory = [1, 0, 0, 0, 99]
        computer = IntComputer(memory)
        computer.run()
        result = computer.memory[0]
        assert expected == result

    def test_run_intcode_2(self):
        expected = 2
        memory = [2, 3, 0, 3, 99]
        computer = IntComputer(memory)
        computer.run()
        result = computer.memory[0]
        assert expected == result

    def test_run_intcode_3(self):
        expected = 2
        memory = [2, 4, 4, 5, 99, 0]
        computer = IntComputer(memory)
        computer.run()
        result = computer.memory[0]
        assert expected == result

    def test_run_intcode_4(self):
        expected = 30
        memory = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        computer = IntComputer(memory)
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
        memory = [3]
        expected_opcode = 3
        expected_modes = [Mode.POSITION, Mode.POSITION, Mode.POSITION, Mode.POSITION]
        computer = IntComputer(memory)
        result_opcode, result_modes = computer.parse_parameter()
        assert result_opcode == expected_opcode
        assert result_modes == expected_modes

    def test_parse_parameter_with_example_from_description(self):
        """
        a single opcode should result in the matching number as opcode and all modes should be 0
        """
        memory = [1001]
        expected_opcode = 1
        expected_modes = [Mode.POSITION, Mode.IMMEDIATE, Mode.POSITION, Mode.POSITION]
        computer = IntComputer(memory)
        result_opcode, result_modes = computer.parse_parameter()
        assert result_opcode == expected_opcode
        assert result_modes == expected_modes

    def test_parse_parameter_with_just_one_mode(self):
        memory = [102]
        expected_opcode = 2
        expected_modes = [Mode.IMMEDIATE, Mode.POSITION, Mode.POSITION, Mode.POSITION]
        computer = IntComputer(memory)
        result_opcode, result_modes = computer.parse_parameter()
        assert result_opcode == expected_opcode
        assert result_modes == expected_modes

    def test_parse_parameter_with_two_modes(self):
        memory = [1103]
        expected_opcode = 3
        expected_modes = [Mode.IMMEDIATE, Mode.IMMEDIATE, Mode.POSITION, Mode.POSITION]
        computer = IntComputer(memory)
        result_opcode, result_modes = computer.parse_parameter()
        assert result_opcode == expected_opcode
        assert result_modes == expected_modes

    def test_parse_parameter_with_three_modes(self):
        memory = [11104]
        expected_opcode = 4
        expected_modes = [Mode.IMMEDIATE, Mode.IMMEDIATE, Mode.IMMEDIATE, Mode.POSITION]
        computer = IntComputer(memory)
        result_opcode, result_modes = computer.parse_parameter()
        assert result_opcode == expected_opcode
        assert result_modes == expected_modes

    def test_parse_parameter_with_four_modes(self):
        memory = [111104]
        expected_opcode = 4
        expected_modes = [
            Mode.IMMEDIATE,
            Mode.IMMEDIATE,
            Mode.IMMEDIATE,
            Mode.IMMEDIATE,
        ]
        computer = IntComputer(memory)
        result_opcode, result_modes = computer.parse_parameter()
        assert result_opcode == expected_opcode
        assert result_modes == expected_modes

    def test_parse_parameter_with_14(self):
        memory = [14]
        expected_opcode = 14
        expected_modes = [Mode.POSITION, Mode.POSITION, Mode.POSITION, Mode.POSITION]
        computer = IntComputer(memory)
        result_opcode, result_modes = computer.parse_parameter()
        assert result_opcode == expected_opcode
        assert result_modes == expected_modes

    def test_parse_parameter_supports_relative_mode(self):
        memory = [211104]
        expected_opcode = 4
        expected_modes = [
            Mode.IMMEDIATE,
            Mode.IMMEDIATE,
            Mode.IMMEDIATE,
            Mode.RELATIVE,
        ]
        computer = IntComputer(memory)
        result_opcode, result_modes = computer.parse_parameter()
        assert result_opcode == expected_opcode
        assert result_modes == expected_modes

    def test_get_position_for_mode_supports_position_mode(self):
        memory = [1, 2, 3, 4]
        idx = 1
        modes = [Mode.POSITION, Mode.POSITION, Mode.POSITION, Mode.POSITION]
        expected = 2
        computer = IntComputer(memory)
        result = computer.get_position_for_mode(idx, modes)
        assert result == expected

    def test_get_position_for_mode_supports_immediate_mode(self):
        memory = [1, 2, 3, 4]
        idx = 1
        modes = [Mode.IMMEDIATE, Mode.POSITION, Mode.POSITION, Mode.POSITION]
        expected = 1
        computer = IntComputer(memory)
        result = computer.get_position_for_mode(idx, modes)
        assert result == expected

    @patch.object(IntComputer, "get_position_for_mode")
    def test_get_param_returns_value_from_position_provided_by_get_position_for_mode(
        self, mock_get_position_for_mode
    ):
        mock_get_position_for_mode.return_value = 3
        memory = [1, 2, 3, 4]
        idx = 1
        modes = []  # no modes needed because of mock
        expected = 4
        computer = IntComputer(memory)
        result = computer.get_param(idx, modes)
        assert result == expected
        assert mock_get_position_for_mode.called_with(1, [])

    @patch.object(IntComputer, "get_position_for_mode")
    @patch.object(IntComputer, "get_param")
    def test_add(self, mock_get_param, mock_get_position):
        mock_get_param.side_effect = [1, 2]
        mock_get_position.return_value = 0
        memory = [1, 1, 1, 1]
        modes = []  # no modes needed because of mock
        expected = 3
        computer = IntComputer(memory)
        computer.add(modes)
        result = computer.memory[0]  # position form mock
        assert result == expected
        assert 4 == computer.pointer

    @patch.object(IntComputer, "get_position_for_mode")
    @patch.object(IntComputer, "get_param")
    def test_multiply(self, mock_get_param, mock_get_position):
        mock_get_param.side_effect = [3, 2]
        mock_get_position.return_value = 0
        memory = [1, 1, 1, 1]
        modes = []
        expected = 6
        computer = IntComputer(memory)
        computer.multiply(modes)
        result = computer.memory[0]
        assert result == expected
        assert 4 == computer.pointer

    @patch.object(IntComputer, "get_position_for_mode")
    def test_save(self, mock_get_position_for_mode):
        mock_get_position_for_mode.return_value = 0
        expected = 5
        memory = [0]
        computer = IntComputer(memory=memory, inputs=[expected])
        computer.save([])
        assert computer.memory[0] == expected
        assert 2 == computer.pointer

    @patch("builtins.input")
    @patch.object(IntComputer, "get_position_for_mode")
    def test_save_with_no_inputs(self, mock_get_position_for_mode, fake_input):
        expected = 5
        fake_input.return_value = expected
        mock_get_position_for_mode.return_value = 0
        memory = [0]
        computer = IntComputer(memory=memory)
        computer.save([])
        assert computer.memory[0] == expected
        assert 2 == computer.pointer

    @patch.object(IntComputer, "get_param")
    def test_outputHandler_stores_value_from_get_param_in_all_outouts(
        self, mock_get_param
    ):
        expected = 12345
        mock_get_param.return_value = expected
        memory = []
        modes = []
        computer = IntComputer(memory)
        computer.outputHandler(modes)
        result = computer.output
        assert result == expected
        assert computer.all_outputs == [expected]
        assert 2 == computer.pointer

    @patch.object(IntComputer, "get_param")
    def test_jump_if_true(self, mock_get_param):
        expected = 99
        mock_get_param.side_effect = [1, expected]
        memory = []
        modes = []
        computer = IntComputer(memory)
        computer.jump_if_true(modes)
        assert computer.pointer == expected

    @patch.object(IntComputer, "get_param")
    def test_jump_if_true_with_false(self, mock_get_param):
        expected = 3
        mock_get_param.side_effect = [0, 99]
        memory = []
        modes = []
        computer = IntComputer(memory)
        computer.jump_if_true(modes)
        assert computer.pointer == expected

    @patch.object(IntComputer, "get_param")
    def test_jump_if_false(self, mock_get_param):
        expected = 99
        mock_get_param.side_effect = [0, expected]
        memory = []
        modes = []
        computer = IntComputer(memory)
        computer.jump_if_false(modes)
        assert computer.pointer == expected

    @patch.object(IntComputer, "get_param")
    def test_jump_if_false_with_true(self, mock_get_param):
        expected = 3
        mock_get_param.side_effect = [1, 99]
        memory = []
        modes = []
        computer = IntComputer(memory)
        computer.jump_if_false(modes)
        assert computer.pointer == expected

    @patch.object(IntComputer, "get_position_for_mode")
    @patch.object(IntComputer, "get_param")
    def test_less_than_positive(self, mock_get_param, mock_get_position_for_mode):
        expected = 1
        mock_get_param.side_effect = [1, 2]
        mock_get_position_for_mode.return_value = 0
        memory = [-1]
        modes = []
        computer = IntComputer(memory)
        computer.less_than(modes)
        assert computer.memory[0] == expected
        assert computer.pointer == 4

    @patch.object(IntComputer, "get_position_for_mode")
    @patch.object(IntComputer, "get_param")
    def test_less_than_negative(self, mock_get_param, mock_get_position_for_mode):
        expected = 0
        mock_get_param.side_effect = [5, 2]
        mock_get_position_for_mode.return_value = 0
        memory = [-1]
        modes = []
        computer = IntComputer(memory)
        computer.less_than(modes)
        assert computer.memory[0] == expected
        assert computer.pointer == 4

    @patch.object(IntComputer, "get_position_for_mode")
    @patch.object(IntComputer, "get_param")
    def test_equals_positive(self, mock_get_param, mock_get_position_for_mode):
        expected = 1
        mock_get_param.side_effect = [1, 1]
        mock_get_position_for_mode.return_value = 0
        memory = [-1]
        modes = []
        computer = IntComputer(memory)
        computer.equals(modes)
        assert computer.memory[0] == expected
        assert computer.pointer == 4

    @patch.object(IntComputer, "get_position_for_mode")
    @patch.object(IntComputer, "get_param")
    def test_equals_negative(self, mock_get_param, mock_get_position_for_mode):
        expected = 0
        mock_get_param.side_effect = [5, 2]
        mock_get_position_for_mode.return_value = 0
        memory = [-1]
        modes = []
        computer = IntComputer(memory)
        computer.equals(modes)
        assert computer.memory[0] == expected
        assert computer.pointer == 4

    @patch.object(IntComputer, "get_param")
    def test_adjust_relative_base(self, mock_get_param):
        expected_relative_base = 99
        expected_pointer = 2
        mock_get_param.return_value = expected_relative_base
        memory = []
        modes = []
        computer = IntComputer(memory)
        computer.adjust_relative_base(modes)
        assert computer.pointer == expected_pointer
        assert computer.relative_base == expected_relative_base

    @patch.object(IntComputer, "add")
    @patch.object(IntComputer, "parse_parameter")
    def test_run_does_nothing_when_finished(self, mock_parse_parameter, mock_add):
        mock_parse_parameter.return_value = (1, [])
        computer = IntComputer([])
        computer.finished = True
        computer.run()
        assert mock_add.called == False

    @patch.object(IntComputer, "parse_parameter")
    def test_run_finishes_on_opcode_99(self, mock_parse_parameter):
        mock_parse_parameter.return_value = (99, [])
        computer = IntComputer([])
        assert computer.finished == False
        computer.run()
        computer.finished = True

    @patch.object(IntComputer, "add")
    @patch.object(IntComputer, "parse_parameter")
    def test_run_executes_add_on_opcode_1(self, mock_parse_parameter, mock_add):
        mock_parse_parameter.side_effect = [(1, []), (99, [])]
        computer = IntComputer([])
        computer.run()
        assert mock_add.called == True

    @patch.object(IntComputer, "multiply")
    @patch.object(IntComputer, "parse_parameter")
    def test_run_executes_multiply_on_opcode_2(
        self, mock_parse_parameter, mock_multiply
    ):
        mock_parse_parameter.side_effect = [(2, []), (99, [])]
        computer = IntComputer([])
        computer.run()
        assert mock_multiply.called == True

    @patch.object(IntComputer, "save")
    @patch.object(IntComputer, "parse_parameter")
    def test_run_executes_save_on_opcode_3(self, mock_parse_parameter, mock_save):
        mock_parse_parameter.side_effect = [(3, []), (99, [])]
        computer = IntComputer([])
        computer.run()
        assert mock_save.called == True

    @patch.object(IntComputer, "outputHandler")
    @patch.object(IntComputer, "parse_parameter")
    def test_run_executes_outputHandler_on_opcode_4(
        self, mock_parse_parameter, mock_outputHandler
    ):
        mock_parse_parameter.side_effect = [(4, []), (99, [])]
        computer = IntComputer([])
        computer.run()
        assert mock_outputHandler.called == True

    @patch.object(IntComputer, "jump_if_true")
    @patch.object(IntComputer, "parse_parameter")
    def test_run_executes_jump_if_true_on_opcode_5(
        self, mock_parse_parameter, mock_jump_if_true
    ):
        mock_parse_parameter.side_effect = [(5, []), (99, [])]
        computer = IntComputer([])
        computer.run()
        assert mock_jump_if_true.called == True

    @patch.object(IntComputer, "jump_if_false")
    @patch.object(IntComputer, "parse_parameter")
    def test_run_executes_jump_if_false_on_opcode_6(
        self, mock_parse_parameter, mock_jump_if_false
    ):
        mock_parse_parameter.side_effect = [(6, []), (99, [])]
        computer = IntComputer([])
        computer.run()
        assert mock_jump_if_false.called == True

    @patch.object(IntComputer, "less_than")
    @patch.object(IntComputer, "parse_parameter")
    def test_run_executes_less_than_on_opcode_7(
        self, mock_parse_parameter, mock_less_than
    ):
        mock_parse_parameter.side_effect = [(7, []), (99, [])]
        computer = IntComputer([])
        computer.run()
        assert mock_less_than.called == True

    @patch.object(IntComputer, "equals")
    @patch.object(IntComputer, "parse_parameter")
    def test_run_executes_equals_on_opcode_8(self, mock_parse_parameter, mock_equals):
        mock_parse_parameter.side_effect = [(8, []), (99, [])]
        computer = IntComputer([])
        computer.run()
        assert mock_equals.called == True

    @patch.object(IntComputer, "adjust_relative_base")
    @patch.object(IntComputer, "parse_parameter")
    def test_run_executes_adjust_relative_base_on_opcode_8(
        self, mock_parse_parameter, mock_adjust_relative_base
    ):
        mock_parse_parameter.side_effect = [(9, []), (99, [])]
        computer = IntComputer([])
        computer.run()
        assert mock_adjust_relative_base.called == True

    # Day 09

    def test_with_large_numbers(self):
        memory = [
            109,
            1,
            204,
            -1,
            1001,
            100,
            1,
            100,
            1008,
            100,
            16,
            101,
            1006,
            101,
            0,
            99,
        ]
        computer = IntComputer(memory)
        computer.run()
        result = computer.all_outputs
        assert result == memory

    def test_with_16_digit_number(self):
        memory = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
        computer = IntComputer(memory)
        computer.run()
        expected = 1219070632396864
        result = computer.output
        assert result == expected

    def test_with_1125899906842624(self):
        memory = [104, 1125899906842624, 99]
        computer = IntComputer(memory)
        computer.run()
        expected = 1125899906842624
        result = computer.output
        assert result == expected
