from util.filehelper import get_string_list_from_file


def parse_orbit_map(orbit_map):
    planets = orbit_map.split(")")
    return planets[0], planets[1]


def create_moon_to_planet_map(orbit_data):
    orbit_dict = {}
    for line in orbit_data:
        planet, planet_in_orbit = parse_orbit_map(line)
        if planet_in_orbit in orbit_dict:
            print("no!")

        orbit_dict[planet_in_orbit] = planet

    return orbit_dict


def create_planet_to_moon_map(orbit_data):
    orbit_dict = {}
    for line in orbit_data:
        planet, planet_in_orbit = parse_orbit_map(line)
        childs = []
        if planet in orbit_dict:
            childs = orbit_dict[planet]
        childs.append(planet_in_orbit)
        orbit_dict[planet] = childs
    return orbit_dict


def find_orbit(current_planet, planet_to_moon_map):
    planets = []
    for planet, moons in planet_to_moon_map.items():
        if current_planet in moons:
            planets.append(planet)
    return planets


def collect_planets_in_center(planet, planet_to_moon_map):
    planets_in_center = find_orbit(planet, planet_to_moon_map)
    if planet in planet_to_moon_map:
        planets_in_center.extend(planet_to_moon_map[planet])
    return planets_in_center


def find_route(start, to, visited, depth, planet_to_moon_map):
    if start in visited:
        return 0
    visited.append(start)
    planets_in_center = collect_planets_in_center(start, planet_to_moon_map)
    if to in planets_in_center:
        return depth - 1
    for planet in planets_in_center:
        distance = find_route(planet, to, visited, depth + 1, planet_to_moon_map)
        if distance > 0:
            return distance
    return -1


def get_number_of_direct_and_indirect_orbits(orbit_data):
    orbit_dict = create_moon_to_planet_map(orbit_data)

    number_of_orbits = 0
    for _, planet in orbit_dict.items():
        number_of_orbits += 1
        p = planet
        while p in orbit_dict:
            number_of_orbits += 1
            p = orbit_dict[p]
    return number_of_orbits


def day06_01():
    orbit_data = get_string_list_from_file("./puzzles/06/puzzle.txt")
    result = get_number_of_direct_and_indirect_orbits(orbit_data)
    print(f"total number of direct and indirect orbits: {result}")


def day06_02():
    orbit_data = get_string_list_from_file("./puzzles/06/puzzle.txt")
    planet_to_moon_map = create_planet_to_moon_map(orbit_data)
    orbital_transfers = find_route("YOU", "SAN", [], 0, planet_to_moon_map)
    print(f"minimum number of orbital transfers required {orbital_transfers}")


if __name__ == "__main__":
    day06_01()
    day06_02()
