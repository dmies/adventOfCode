from day02 import run_intcode, add, multiply


class TestDay02:
    def test_run_intcode_1(self):
        expected = 2
        input = [1, 0, 0, 0, 99]
        result = run_intcode(input)
        assert expected == result

    def test_run_intcode_2(self):
        expected = 2
        input = [2, 3, 0, 3, 99]
        result = run_intcode(input)
        assert expected == result

    def test_run_intcode_3(self):
        expected = 2
        input = [2, 4, 4, 5, 99, 0]
        result = run_intcode(input)
        assert expected == result

    def test_run_intcode_4(self):
        expected = 30
        input = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        result = run_intcode(input)
        assert expected == result

    def test_add_adds_the_values_at_position_2_and_3(self):
        input = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        expected = [1, 1, 1, 4, 2, 5, 6, 0, 99]
        result = add(input, 0)
        assert expected == result

    def test_multiply_multiplies_the_values_at_position_2_and_3(self):
        input = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        expected = [1, 1, 1, 4, 1, 5, 6, 0, 99]
        result = multiply(input, 0)
        assert expected == result

