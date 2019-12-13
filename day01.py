from util.filehelper import file_to_array


def calculate_fuel_needed(mass: int) -> int:
    """
    Fuel required to launch a given module is based on its mass. 
    Specifically, to find the fuel required for a module, take its mass, divide
    by three, round down, and subtract 2.
    """
    return int(mass / 3) - 2


def calculate_fuel_for_fuel(mass: int) -> int:
    """
    So, for each module mass, calculate its fuel and add it to the total. 
    Then, treat the fuel amount you just calculated as the input mass and
    repeat the process,
    continuing until a fuel requirement is zero or negative. 
    """
    fuel_needed = calculate_fuel_needed(mass)
    if fuel_needed <= 0:
        return 0
    else:
        return fuel_needed + calculate_fuel_for_fuel(fuel_needed)


def day01_01():
    path = "./puzzles/01/puzzle.txt"
    fuel_list = [calculate_fuel_needed(mass) for mass in file_to_array(path)]
    fuel_needed = sum(fuel_list)
    print(f"fuel needed: {fuel_needed}")


def day01_02():
    path = "./puzzles/01/puzzle02.txt"
    fuel_list = [calculate_fuel_for_fuel(mass) for mass in file_to_array(path)]
    fuel_needed = sum(fuel_list)
    print(f"fuel needed for fuel: {fuel_needed}")


if __name__ == "__main__":
    day01_01()
    day01_02()
