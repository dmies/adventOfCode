import math

from util import coordinates, filehelper


def different_coordinates(a, b):
    x, y = a
    i, j = b
    return not (x == i and y == j)


def group_asteroids_by_angle(asteroid_map, candidate):
    """
  for both tasks we need to find the angles between a candidate / our station
  to all other asteroids.
  In task 1 we need the number of unique angles: the station with most unique
  angles has the best position
  In task 2 we need all asteroids / angle so we can vaporize them in order
  So for task 1 a set would be enough while the dict is needed for task 2.
  I use the same code to avoid duplicates here.
  """
    target_x, target_y = candidate
    res = {}
    for (y, row) in enumerate(asteroid_map):
        for (x, item) in enumerate(row):
            if item == "#" and different_coordinates(candidate, (x, y)):
                angle = math.degrees(math.atan2(target_y - y, target_x - x))
                if angle < 0:
                    angle += 360
                if angle not in res:
                    res[angle] = [(x, y)]
                else:
                    res[angle].append((x, y))
    return res


def get_location_for_station(asteroid_map):
    res = 0
    coords = None
    for y, row in enumerate(asteroid_map):
        for x, item in enumerate(row):
            if item == "#":
                candidate = (x, y)
                # number of keys == number of uniqe angles
                unique_angles = len(group_asteroids_by_angle(asteroid_map, candidate))
                if unique_angles > res:
                    res = unique_angles
                    coords = candidate
    return coords, res


def get_index_of_closest_asteroid(list_of_asteroids, station):
    """
    find closest asteroid (index) by manhattan distance
    """
    res = 0
    for i, asteroid in enumerate(list_of_asteroids):
        distance = coordinates.manhattan_distance(station, asteroid)
        other_asteroid = list_of_asteroids[res]
        if distance < coordinates.manhattan_distance(station, other_asteroid):
            res = i
    return res


def get_200th_vaporized_asteroid(asteroid_map, station):
    """
  we group the asteroids by their angle to our station. then we rotate to 90
  degrees and start vaporizing
  for every angle we get the closest asteroid and vaporize it
  (delete it from our list)
  """
    # group the asteroids by their angle to the station
    asteroid_map = group_asteroids_by_angle(asteroid_map, station)
    vaporized_asteroids = 0
    first_run = True
    sorted_keys = sorted(asteroid_map)
    while vaporized_asteroids < 200:
        # "rotate the gun"
        for key in sorted_keys:
            # wait for gun to be at 90 degrees
            if key == 90.0:
                first_run = False
            if not first_run:
                list_of_asteroids = asteroid_map[key]
                closest = get_index_of_closest_asteroid(list_of_asteroids, station)
                # we start at 0 so our asteroid no 199 is the searched one
                if vaporized_asteroids == 199:
                    return list_of_asteroids[closest]
                """
                if we are still shooting, we delete the vaporized asteroid 
                from our list
                """
                del list_of_asteroids[closest]
                asteroid_map[key] = list_of_asteroids
                vaporized_asteroids += 1
    return -1, -1


def day10_01():
    asteroid_map = filehelper.get_map_from_file("./puzzles/10/puzzle.txt")
    print(f"best location: {get_location_for_station(asteroid_map)}")


def day10_02():
    asteroid_map = filehelper.get_map_from_file("./puzzles/10/puzzle.txt")
    start_point, _ = get_location_for_station(asteroid_map)
    res = get_200th_vaporized_asteroid(asteroid_map, start_point)
    print(f"200th vaporized asteroid is on coordinates: {res}")


if __name__ == "__main__":
    day10_01()
    day10_02()
