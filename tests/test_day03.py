from day03 import manhattan, parse_command, apply_direction


class TestDay03:
    def test_manhattan_distance(self):
        expected = 2
        input = (0, 2)
        result = manhattan(input)
        assert expected == result

    def test_manhattan_distance_with_negative_number(self):
        expected = 5
        input = (-3, 2)
        result = manhattan(input)
        assert expected == result

    def test_parse_command(self):
        expected = ("R", 123)
        input = "R123"
        result = parse_command(input)
        assert expected == result

    def test_apply_direction_right(self):
        expected = (1, 0)
        input_point = (0, 0)
        input_direction = "R"
        result = apply_direction(input_direction, input_point)
        assert expected == result

    def test_apply_direction_down(self):
        expected = (0, 1)
        input_point = (0, 0)
        input_direction = "D"
        result = apply_direction(input_direction, input_point)
        assert expected == result

    def test_apply_direction_left(self):
        expected = (-1, 0)
        input_point = (0, 0)
        input_direction = "L"
        result = apply_direction(input_direction, input_point)
        assert expected == result

    def test_apply_direction_up(self):
        expected = (0, -1)
        input_point = (0, 0)
        input_direction = "U"
        result = apply_direction(input_direction, input_point)
        assert expected == result

