from day01 import calculate_fuel_needed, calculate_fuel_for_fuel


class TestDay01:
    def test_calculate_fuel_needed_caculates_correct_fuel_for_mass_12(self):
        expected = 2
        mass = 12
        result = calculate_fuel_needed(mass)
        assert expected == result

    def test_calculate_fuel_needed_caculates_correct_fuel_for_mass_14(self):
        expected = 2
        mass = 14
        result = calculate_fuel_needed(mass)
        assert expected == result

    def test_calculate_fuel_needed_caculates_correct_fuel_for_mass_1969(self):
        expected = 654
        mass = 1969
        result = calculate_fuel_needed(mass)
        assert expected == result

    def test_calculate_fuel_needed_caculates_correct_fuel_for_mass_100756(self):
        expected = 33583
        mass = 100756
        result = calculate_fuel_needed(mass)
        assert expected == result

    def test_calculate_fuel_for_fuel_caculates_correct_fuel_for_mass_14(self):
        expected = 2
        mass = 14
        result = calculate_fuel_for_fuel(mass)
        assert expected == result

    def test_calculate_fuel_for_fuel_caculates_correct_fuel_for_mass_1969(self):
        expected = 966
        mass = 1969
        result = calculate_fuel_for_fuel(mass)
        assert expected == result

    def test_calculate_fuel_for_fuel_caculates_correct_fuel_for_mass_100756(self):
        expected = 50346
        mass = 100756
        result = calculate_fuel_for_fuel(mass)
        assert expected == result

