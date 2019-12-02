import unittest
import os
from unittest.mock import patch, mock_open


from day01 import calculate_fuel_needed, calculate_fuel_for_fuel


class TestDay01(unittest.TestCase):
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
