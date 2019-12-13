from util import filehelper
from itertools import combinations
from typing import List, Dict, Optional
import math


class Coordinates:
    x = 0
    y = 0
    z = 0


class Moon:
    def __init__(self, line):
        stripped = line[1:-1]
        coords = stripped.split(", ")

        key_values = [i.split("=") for i in coords]
        self.x = int(key_values[0][1])
        self.y = int(key_values[1][1])
        self.z = int(key_values[2][1])
        self.velocity = (0, 0, 0)
        self.initial_state = (self.x, self.y, self.z, self.velocity)

    def apply_gravity(self, neighbor) -> None:
        x, y, z = self.velocity
        if self.x > neighbor.x:
            x -= 1
        elif self.x < neighbor.x:
            x += 1
        if self.y > neighbor.y:
            y -= 1
        elif self.y < neighbor.y:
            y += 1
        if self.z > neighbor.z:
            z -= 1
        elif self.z < neighbor.z:
            z += 1
        self.velocity = (x, y, z)

    def apply_velocity(self) -> None:
        x, y, z = self.velocity
        self.x += x
        self.y += y
        self.z += z

    def get_potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def get_kinetic_energy(self):
        x, y, z = self.velocity
        return abs(x) + abs(y) + abs(z)

    def get_total_energy(self):
        return self.get_potential_energy() * self.get_kinetic_energy()

    def at_initial_position(self) -> bool:
        current_state = (self.x, self.y, self.z, self.velocity)
        return current_state == self.initial_state

    def hash_x(self):
        x, _, _ = self.velocity
        return "{},{}".format(self.x, x)

    def hash_y(self):
        _, y, _ = self.velocity
        return "{},{}".format(self.y, y)

    def hash_z(self):
        _, _, z = self.velocity
        return "{},{}".format(self.z, z)

    def __eq__(self, other):
        if isinstance(other, Moon):
            return (
                self.x == other.x
                and self.y == other.y
                and self.z == other.z
                and self.velocity == other.velocity
            )
        return NotImplemented

    def __repr__(self):
        return f"Moon(x={self.x}, y={self.y}, z={self.z}, velocity={self.velocity})"


def simulate_moons(moons: [Moon], steps=1):
    for _ in range(steps):
        for moon, other in combinations(moons, 2):
            moon.apply_gravity(other)
            other.apply_gravity(moon)
        for moon in moons:
            moon.apply_velocity()

    return moons


def get_total_energy(moons, steps):
    total_energy = 0

    simulate_moons(moons, steps)
    for moon in moons:
        total_energy += moon.get_total_energy()
    return total_energy


def least_common_multiple(x: int, y: int, z: int) -> int:
    least_common_multiple_xy = x // math.gcd(x, y) * y
    return least_common_multiple_xy // math.gcd(least_common_multiple_xy, z) * z


def get_repetitions(moons: [Moon]) -> Dict[str, Optional[int]]:
    history = {"x": set(), "y": set(), "z": set()}
    repetitions: Dict[str, Optional[int]] = {"x": None, "y": None, "z": None}
    loop = 0
    while True:
        if all(x is not None for x in repetitions.values()):
            break
        simulate_moons(moons)

        if repetitions["x"] is None:
            x_key = ";".join(x.hash_x() for x in moons)
            if x_key in history["x"]:
                repetitions["x"] = loop
            history["x"].add(x_key)
        if repetitions["y"] is None:
            y_key = ";".join(x.hash_y() for x in moons)
            if y_key in history["y"]:
                repetitions["y"] = loop
            history["y"].add(y_key)
        if repetitions["z"] is None:
            z_key = ";".join(x.hash_z() for x in moons)
            if z_key in history["z"]:
                repetitions["z"] = loop
            history["z"].add(z_key)
        loop += 1
    return repetitions


def get_steps_to_find_same_state(moons: [Moon]):
    repetitions = get_repetitions(moons)
    rx, ry, rz = repetitions["x"], repetitions["y"], repetitions["z"]
    return least_common_multiple(rx, ry, rz)


def day12_01():
    text = filehelper.get_string_list_from_file("./puzzles/12/puzzle.txt")
    moons = [Moon(line) for line in text]
    total_energy = get_total_energy(moons, steps=1000)

    print(f"The total energy in the system after 100 steps is {total_energy}")


def day12_02():
    text = filehelper.get_string_list_from_file("./puzzles/12/puzzle.txt")
    moons = [Moon(line) for line in text]
    steps = get_steps_to_find_same_state(moons)
    print(
        f"Number of steps needed to reach the first state that exactly matches a previous state: {steps}"
    )


if __name__ == "__main__":
    day12_01()
    day12_02()
