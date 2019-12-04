def not_all_digits_unique(num):
    num = str(num)
    return len(num) != len(set(num))


def digits_increase(password):
    password_as_number = list(str(password))
    return password_as_number == sorted(password_as_number)


def at_least_one_pair_of_digits(password):
    password_text = str(password)
    for digit in password_text:
        if password_text.count(digit) == 2:
            return True
    return False


def get_number_of_potential_passwords(start, end):
    passwords = [
        password
        for password in range(start, end)
        if not_all_digits_unique(password) and digits_increase(password)
    ]
    return len(passwords)


def get_number_of_potential_passwords_improved(start, end):
    passwords = [
        password
        for password in range(start, end)
        if digits_increase(password) and at_least_one_pair_of_digits(password)
    ]
    return len(passwords)


def day04_01():
    start = 254032
    end = 789860
    res = get_number_of_potential_passwords(start, end)
    print(f"Number of possible passwords: {res}")


def day04_02():
    start = 254032
    end = 789860
    res = get_number_of_potential_passwords_improved(start, end)
    print(f"Number of possible passwords (improved): {res}")
