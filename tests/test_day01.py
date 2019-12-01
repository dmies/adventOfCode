import unittest
import os
from unittest.mock import patch, mock_open


from day01 import file_to_array, calculate_fuel_needed, calculate_fuel_for_fuel


class TestSum(unittest.TestCase):
    def test_file_to_array_opens_the_corrrect_file(self):
        path = "./puzzles/01/puzzle.txt"
        with patch("builtins.open", mock_open(read_data="8\n9\n10")) as mock_file:
            file_to_array(path)
            assert open(path).read() == "8\n9\n10"
            mock_file.assert_called_with(path)

    def test_file_to_array_transforms_file_Content_to_array(self):
        path = "./puzzles/01/puzzle2.txt"
        with patch("builtins.open", mock_open(read_data="8\n9\n10")):
            expected = [8, 9, 10]
            result = file_to_array(path)
            assert len(expected) == len(result)
            assert sorted(expected) == sorted(result)

    def test_calculate_fuel_needed_caculates_correct_fuel_for_mass_12(self):
        expected = 2
        input = 12
        result = calculate_fuel_needed(input)
        assert expected == result

    def test_calculate_fuel_needed_caculates_correct_fuel_for_mass_14(self):
        expected = 2
        input = 14
        result = calculate_fuel_needed(input)
        assert expected == result

    def test_calculate_fuel_needed_caculates_correct_fuel_for_mass_1969(self):
        expected = 654
        input = 1969
        result = calculate_fuel_needed(input)
        assert expected == result

    def test_calculate_fuel_needed_caculates_correct_fuel_for_mass_100756(self):
        expected = 33583
        input = 100756
        result = calculate_fuel_needed(input)
        assert expected == result

    def test_calculate_fuel_for_fuel_caculates_correct_fuel_for_mass_14(self):
        expected = 2
        input = 14
        result = calculate_fuel_for_fuel(input)
        assert expected == result

    def test_calculate_fuel_for_fuel_caculates_correct_fuel_for_mass_1969(self):
        expected = 966
        input = 1969
        result = calculate_fuel_for_fuel(input)
        assert expected == result

    def test_calculate_fuel_for_fuel_caculates_correct_fuel_for_mass_100756(self):
        expected = 50346
        input = 100756
        result = calculate_fuel_for_fuel(input)
        assert expected == result


if __name__ == "__main__":
    unittest.main()
