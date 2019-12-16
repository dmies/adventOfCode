from day16 import fft, decode_signal


def test_fft_1_phase():
    signal = [int(letter) for letter in "12345678"]
    expected = "48226158"
    result = fft(signal, phases=1)
    assert result == expected


def test_fft_2_phases():
    signal = [int(letter) for letter in "12345678"]
    expected = "34040438"
    result = fft(signal, phases=2)
    assert result == expected


def test_fft_3_phases():
    signal = [int(letter) for letter in "12345678"]
    expected = "03415518"
    result = fft(signal, phases=3)
    assert result == expected


def test_fft():
    signal = [int(letter) for letter in "80871224585914546619083218645595"]
    expected = "24176176"
    result = fft(signal)
    assert result == expected


def test_fft_2():
    signal = [int(letter) for letter in "19617804207202209144916044189917"]
    expected = "73745418"
    result = fft(signal)
    assert result == expected


def test_fft_3():
    signal = [int(letter) for letter in "69317163492948606335995924319873"]
    expected = "52432133"
    result = fft(signal)
    assert result == expected


def test_decode_signal():
    signal = [int(letter) for letter in "03036732577212944063491565474664"]
    expected = "84462026"
    result = decode_signal(signal)
    assert result == expected


def test_decode_signal_2():
    signal = [int(letter) for letter in "02935109699940807407585447034323"]
    expected = "78725270"
    result = decode_signal(signal)
    assert result == expected


def test_decode_signal_3():
    signal = [int(letter) for letter in "03081770884921959731165446850517"]
    expected = "53553731"
    result = decode_signal(signal)
    assert result == expected
