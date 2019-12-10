from collections import defaultdict
from util.filehelper import get_string_lists_from_file


def manhattan(point):
    """
    calculates the manhattan distance of a point to (0,0)
    """
    x, y = point
    return abs(x) + abs(y)


def parse_command(command):
    direction = command[0]
    distance = int(command[1:])
    return (direction, distance)


def apply_direction(direction, origin):
    x, y = origin
    if direction == "R":
        x += 1
    elif direction == "L":
        x -= 1
    elif direction == "D":
        y += 1
    elif direction == "U":
        y -= 1
    return (x, y)


def map_to_points(wire):
    origin = (0, 0)
    positions = set()
    commands = [parse_command(command) for command in wire]
    for direction, distance in commands:
        for _ in range(distance):
            origin = apply_direction(direction, origin)
            positions.add(origin)

    return positions


def get_distance_for_crossings(wire, crossings):
    crossing = defaultdict(int)
    current_distance = 0
    current_point = (0, 0)
    commands = [parse_command(command) for command in wire]

    for direction, distance in commands:
        for _ in range(distance):
            current_point = apply_direction(direction, current_point)
            current_distance += 1
            if current_point in crossings:
                crossing[current_point] = current_distance

    return crossing


def get_crossings(wire_1, wire_2):
    positions_1 = map_to_points(wire_1)
    positions_2 = map_to_points(wire_2)
    return positions_1.intersection(positions_2)


def get_minimal_distance_to_intersection(wire_1, wire_2):
    crossings = get_crossings(wire_1, wire_2)
    return min([manhattan(pos) for pos in crossings])


def get_closest_intersection(wire_1, wire_2):
    crossings = get_crossings(wire_1, wire_2)
    crossing_distance_1 = get_distance_for_crossings(wire_1, crossings)
    crossing_distance_2 = get_distance_for_crossings(wire_2, crossings)

    return min(
        [
            crossing_distance_1[crossing] + crossing_distance_2[crossing]
            for crossing in crossings
        ]
    )


def day03_01():
    wires = get_string_lists_from_file("./puzzles/03/puzzle.txt")
    wire_1 = wires[0]
    wire_2 = wires[1]

    min_distance = get_minimal_distance_to_intersection(wire_1, wire_2)

    print(f"The minimal distance is: {min_distance}")


def day03_02():
    wires = get_string_lists_from_file("./puzzles/03/puzzle.txt")
    wire_1 = wires[0]
    wire_2 = wires[1]

    fewest_steps = get_closest_intersection(wire_1, wire_2)

    print(f"fewest steps: {fewest_steps}")


if __name__ == "__main__":
    day03_01()
    day03_02()
