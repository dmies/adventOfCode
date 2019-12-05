import mock
from day05 import (
    parse_parameter,
    get_position_for_mode,
    get_param,
    add,
    multiply,
    output,
    jump_if_true,
    jump_if_false,
    less_than,
    equals,
)


class TestDay05:
    def test_parse_parameter_supports_standalone_opcode(self):
        """
        a single opcode should result in the matching number as opcode and all modes should be 0
        """
        input = 3
        expected = (3, [0, 0, 0, 0])
        result = parse_parameter(input)
        assert result == expected

    def test_parse_parameter_with_example_from_description(self):
        """
        a single opcode should result in the matching number as opcode and all modes should be 0
        """
        input = 1001
        expected = (1, [0, 1, 0, 0])
        result = parse_parameter(input)
        assert result == expected

    def test_parse_parameter_with_just_one_mode(self):
        input = 102
        expected = (2, [1, 0, 0, 0])
        result = parse_parameter(input)
        assert result == expected

    def test_parse_parameter_with_two_modes(self):
        input = 1103
        expected = (3, [1, 1, 0, 0])
        result = parse_parameter(input)
        assert result == expected

    def test_parse_parameter_with_three_modes(self):
        input = 11104
        expected = (4, [1, 1, 1, 0])
        result = parse_parameter(input)
        assert result == expected

    def test_parse_parameter_with_four_modes(self):
        input = 111104
        expected = (4, [1, 1, 1, 1])
        result = parse_parameter(input)
        assert result == expected

    def test_parse_parameter_with_14(self):
        input = 14
        expected = (14, [0, 0, 0, 0])
        result = parse_parameter(input)
        assert result == expected

    def test_get_position_for_mode_supports_position_mode(self):
        memory = [1, 2, 3, 4]
        pos = 0
        idx = 1
        modes = [0, 0, 0, 0]
        expected = 2
        result = get_position_for_mode(memory, pos, idx, modes)
        assert result == expected

    def test_get_position_for_mode_supports_immediate_mode(self):
        memory = [1, 2, 3, 4]
        pos = 0
        idx = 1
        modes = [1, 0, 0, 0]
        expected = 1
        result = get_position_for_mode(memory, pos, idx, modes)
        assert result == expected

    @mock.patch("day05.get_position_for_mode")
    def test_get_param_returns_value_from_position_provided_by_get_position_for_mode(
        self, mock_get_position
    ):
        mock_get_position.return_value = 3
        memory = [1, 2, 3, 4]
        pos = 0
        idx = 1
        modes = [1, 0, 0, 0]
        expected = 4
        result = get_param(memory, pos, idx, modes)
        assert result == expected
        assert mock_get_position.called == True

    @mock.patch("day05.get_position_for_mode")
    @mock.patch("day05.get_param")
    def test_add(self, mock_get_param, mock_get_position_for_mode):
        # simulate that these numbers should be added
        mock_get_param.side_effect = [1, 2]
        # write everything to index 0
        mock_get_position_for_mode.return_value = 0
        memory = [-1]
        pos = 0
        modes = []
        expected = ([3], 4)
        result = add(memory, pos, modes)
        assert result == expected

    @mock.patch("day05.get_position_for_mode")
    @mock.patch("day05.get_param")
    def test_multiply(self, mock_get_param, mock_get_position_for_mode):
        # simulate that these numbers should be added
        mock_get_param.side_effect = [3, 4]
        # write everything to index 0
        mock_get_position_for_mode.return_value = 0
        memory = [-1]
        pos = 0
        modes = []
        expected = ([12], 4)
        result = multiply(memory, pos, modes)
        assert result == expected

    @mock.patch("day05.get_position_for_mode")
    def test_output(self, mock_get_position_for_mode):
        # write everything to index 0
        mock_get_position_for_mode.return_value = 0
        memory = [-1]
        pos = 0
        modes = []
        expected = (memory, 2)
        result = output(memory, pos, modes)
        assert result == expected

    @mock.patch("day05.get_param")
    def test_jump_if_true(self, mock_get_param):
        mock_get_param.side_effect = [1, 22]
        memory = [-1]
        pos = 0
        modes = []
        expected = (memory, 22)
        result = jump_if_true(memory, pos, modes)
        assert result == expected

    @mock.patch("day05.get_param")
    def test_jump_if_true_negative(self, mock_get_param):
        mock_get_param.side_effect = [0, 22]
        memory = [-1]
        pos = 0
        modes = []
        expected = (memory, 3)
        result = jump_if_true(memory, pos, modes)
        assert result == expected

    @mock.patch("day05.get_param")
    def test_jump_if_false(self, mock_get_param):
        mock_get_param.side_effect = [0, 22]
        memory = [-1]
        pos = 0
        modes = []
        expected = (memory, 22)
        result = jump_if_false(memory, pos, modes)
        assert result == expected

    @mock.patch("day05.get_param")
    def test_jump_if_false_negative(self, mock_get_param):
        mock_get_param.side_effect = [1, 22]
        memory = [-1]
        pos = 0
        modes = []
        expected = (memory, 3)
        result = jump_if_false(memory, pos, modes)
        assert result == expected

    @mock.patch("day05.get_position_for_mode")
    @mock.patch("day05.get_param")
    def test_less_than(self, mock_get_param, mock_get_position_for_mode):
        mock_get_param.side_effect = [1, 22]
        mock_get_position_for_mode.return_value = 0
        memory = [-1]
        pos = 0
        modes = []
        expected = ([1], 4)
        result = less_than(memory, pos, modes)
        assert result == expected

    @mock.patch("day05.get_position_for_mode")
    @mock.patch("day05.get_param")
    def test_less_than_negative(self, mock_get_param, mock_get_position_for_mode):
        mock_get_param.side_effect = [100, 22]
        mock_get_position_for_mode.return_value = 0
        memory = [-1]
        pos = 0
        modes = []
        expected = ([0], 4)
        result = less_than(memory, pos, modes)
        assert result == expected

    @mock.patch("day05.get_position_for_mode")
    @mock.patch("day05.get_param")
    def test_equals(self, mock_get_param, mock_get_position_for_mode):
        mock_get_param.side_effect = [22, 22]
        mock_get_position_for_mode.return_value = 0
        memory = [-1]
        pos = 0
        modes = []
        expected = ([1], 4)
        result = equals(memory, pos, modes)
        assert result == expected

    @mock.patch("day05.get_position_for_mode")
    @mock.patch("day05.get_param")
    def test_equals_negative(self, mock_get_param, mock_get_position_for_mode):
        mock_get_param.side_effect = [100, 22]
        mock_get_position_for_mode.return_value = 0
        memory = [-1]
        pos = 0
        modes = []
        expected = ([0], 4)
        result = equals(memory, pos, modes)
        assert result == expected
