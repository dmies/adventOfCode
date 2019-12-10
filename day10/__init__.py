from util.filehelper import get_map_from_file
import math


def find_unique_angles_to_candidate(map, candidate):
    target_x, target_y = candidate
    res = set()
    y = 0
    while y < len(map):
        x = 0
        while x < len(map[y]):
            if target_x == x and target_y == y:
                # do nothing
                res = res
            elif map[y][x] == "#":
                angle = math.degrees(math.atan2(target_y - y, target_x - x))
                res.add(angle)
            x += 1
        y += 1
    return len(res)


def group_asteroids_by_angle(map, start_point):
    target_x, target_y = start_point
    res = {}
    y = 0
    while y < len(map):
        x = 0
        while x < len(map[y]):
            if target_x == x and target_y == y:
                # do nothing
                res = res
            elif map[y][x] == "#":
                angle = math.degrees(math.atan2(target_y - y, target_x - x))
                if angle < 0:
                    angle += 360
                if angle not in res:
                    res[angle] = [(x, y)]
                else:
                    res[angle].append((x, y))
            x += 1
        y += 1
    return res


def get_location_for_station(map):

    res = 0
    coordinates = (0, 0)
    y = 0
    while y < len(map):
        x = 0
        while x < len(map[y]):
            if map[y][x] == "#":
                candidate = (x, y)
                number_of_unique_angles = find_unique_angles_to_candidate(
                    map, candidate
                )
                # print(f"{candidate}: {number_of_unique_angles}")
                if number_of_unique_angles > res:
                    res = number_of_unique_angles
                    coordinates = candidate
            x += 1
        y += 1
    return (coordinates, res)


def manhattan_distance(a, b):
    x_value, y_value = a
    x_goal, y_goal = b
    return abs(x_value - x_goal) + abs(y_value - y_goal)


def get_200th_vaporized_asteroid(map, station):
    #  group the asteroids by their angle to the station
    asteroid_map = group_asteroids_by_angle(map, station)
    vaporized_asteroids = 0
    first_run = True
    while vaporized_asteroids < 200:
        for key in sorted(asteroid_map):
            if key == 90.0:
                # wait for gun to be at 90 degrees
                first_run = False
            if not first_run:
                list_of_asteroids = asteroid_map[key]
                closest = 0
                i = 1
                while i < len(list_of_asteroids):
                    asteroid = list_of_asteroids[i]
                    distance = manhattan_distance(station, asteroid)
                    if distance < manhattan_distance(
                        station, list_of_asteroids[closest]
                    ):
                        closest = i
                    i += 1
                if vaporized_asteroids == 199:  # we start at 0
                    return list_of_asteroids[closest]
                del list_of_asteroids[closest]
                asteroid_map[key] = list_of_asteroids
                vaporized_asteroids += 1

    return (0, 0)


def day10_01():
    map = get_map_from_file("./puzzles/10/puzzle.txt")
    for line in map:
        map_row = ""
        for item in line:
            map_row += item
    print(f"best location: {get_location_for_station(map)}")


def day10_02():
    map = get_map_from_file("./puzzles/10/puzzle.txt")
    start_point, _ = get_location_for_station(map)
    print(
        f"the 200th vaporized asteroid is on coordinates: {get_200th_vaporized_asteroid(map, start_point)}"
    )

