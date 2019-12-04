from day04 import not_all_digits_unique, digits_increase, at_least_one_pair_of_digits


class TestDay04:
    def test_not_all_digits_unique(self):
        input = 11234
        expected = True
        result = not_all_digits_unique(input)
        assert result == expected

    def test_not_all_digits_unique_no_sibblings(self):
        input = 12342
        expected = True
        result = not_all_digits_unique(input)
        assert result == expected

    def test_not_all_digits_unique_false(self):
        input = 12345
        expected = False
        result = not_all_digits_unique(input)
        assert result == expected

    def test_digits_increase_positive(self):
        input = 12345
        expected = True
        result = digits_increase(input)
        assert result == expected

    def test_digits_increase_positive_when_all_digits_are_the_same(self):
        input = 111111
        expected = True
        result = digits_increase(input)
        assert result == expected

    def test_digits_increase_negative(self):
        input = 123451
        expected = False
        result = digits_increase(input)
        assert result == expected

    def test_at_least_one_pair_of_digits_example_1(self):
        input = 112233
        expected = True
        result = at_least_one_pair_of_digits(input)
        assert result == expected

    def test_at_least_one_pair_of_digit_example_2(self):
        input = 123444
        expected = False
        result = at_least_one_pair_of_digits(input)
        assert result == expected

    def test_at_least_one_pair_of_digit_example_3(self):
        input = 111122
        expected = True
        result = at_least_one_pair_of_digits(input)
        assert result == expected

    def test_at_least_one_pair_of_digit_example_4(self):
        input = 112345
        expected = True
        result = at_least_one_pair_of_digits(input)
        assert result == expected

    def test_at_least_one_pair_of_digit_example_5(self):
        input = 122345
        expected = True
        result = at_least_one_pair_of_digits(input)
        assert result == expected

    def test_at_least_one_pair_of_digit_example_6(self):
        input = 123345
        expected = True
        result = at_least_one_pair_of_digits(input)
        assert result == expected

    def test_at_least_one_pair_of_digit_example_7(self):
        input = 788999
        expected = True
        result = at_least_one_pair_of_digits(input)
        assert result == expected

    def test_at_least_one_pair_of_digit_example_8(self):
        input = 777777
        expected = False
        result = at_least_one_pair_of_digits(input)
        assert result == expected

