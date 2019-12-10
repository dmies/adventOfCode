from util import coordinates


def test_manhattan_distance():
    expected = 2
    input = (0, 2)
    result = coordinates.manhattan_distance(input)
    assert expected == result


def test_manhattan_distance_with_negative_number():
    expected = 5
    input = (-3, 2)
    result = coordinates.manhattan_distance(input)
    assert expected == result
