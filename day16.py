from util import filehelper


def fft(signal: [int], phases=100) -> str:
    middle_plus_one = len(signal) // 2 + 1
    length = len(signal)
    for _ in range(phases):
        original_signal = signal[:]
        for i in range(middle_plus_one):
            j = i
            k = i + 1
            actual_sum = 0
            while j < length:
                actual_sum += sum(original_signal[j : j + k])
                j += 2 * k
                actual_sum -= sum(original_signal[j : j + k])
                j += 2 * k
            signal[i] = abs(actual_sum) % 10
        for i in range(len(original_signal) - 2, len(original_signal) // 2, -1):
            signal[i] = (signal[i] + signal[i + 1]) % 10

    return "".join(map(str, signal[:8]))


def decode_signal(signal: [int]):
    skip = int("".join(map(str, signal[:7])))
    nums = (signal * 10000)[skip:]
    length = len(nums)
    for _ in range(100):
        for i in range(length - 2, -1, -1):
            nums[i] = (nums[i] + nums[i + 1]) % 10

    return "".join(map(str, nums[:8]))


def day16_01():
    signal = filehelper.get_numbers_from_string_from_file("./puzzles/16/puzzle.txt")
    print(f"first eight digits in output list: {fft(signal)}")


def day16_02():
    signal = filehelper.get_numbers_from_string_from_file("./puzzles/16/puzzle.txt")
    print(f"message embedded in the final output list: {decode_signal(signal)}")


if __name__ == "__main__":
    day16_01()
    day16_02()
