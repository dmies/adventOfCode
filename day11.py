from util import filehelper
from ship.computer import IntComputer
import enum


class Turn(enum.IntEnum):
    LEFT = 0
    RIGHT = 1


class Direction(enum.IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def turn(self, turn: Turn):
        # dir 0: left 1: right
        if turn == Turn.LEFT and self == Direction.UP:
            return Direction.LEFT
        elif turn == Turn.LEFT:
            return Direction(int(self) - 1)
        elif turn == Turn.RIGHT and self == Direction.LEFT:
            return Direction.UP
        else:
            return Direction(int(self) + 1)

    def move_in_direction(self, coordinates: (int, int)) -> (int, int):
        x, y = coordinates
        if self == Direction.UP:
            y += 1
        elif self == Direction.RIGHT:
            x += 1
        elif self == Direction.DOWN:
            y -= 1
        elif self == Direction.LEFT:
            x -= 1
        return (x, y)


class Hull:
    min_width = 0
    width = 0
    min_height = 0
    height = 0
    data = {}

    def paint(self, coordinates: (int, int), color: int) -> None:
        x, y = coordinates
        self.min_width = min(x, self.min_width)
        self.min_height = min(y, self.min_height)
        self.width = max(x, self.width)
        self.height = max(y, self.height)
        self.data[coordinates] = color

    def get_color(self, coordinates: (int, int)) -> int:
        if not coordinates in self.data:
            self.data[coordinates] = 0
        return self.data[coordinates]

    def get_size(self):
        return len(self.data)

    def render(self) -> None:
        for y in range(self.height, self.min_height - 1, -1):
            line = ""
            for x in range(self.min_width, self.width):
                item = " "
                coordinates = (x, y)
                if self.get_color(coordinates) == 1:
                    item = "#"
                else:
                    item = " "
                line += item
            print(line)


def paint_hull(robot, computer, hull: Hull) -> Hull:
    coordinates, direction = robot
    while not computer.finished:
        current_color = hull.get_color(coordinates)
        computer.inputs = [current_color]
        _, color = computer.run()
        hull.paint(coordinates, color)

        if not computer.finished:
            _, turn = computer.run()
            direction = Direction(direction).turn(Turn(turn))
            coordinates = Direction(direction).move_in_direction(coordinates)

    return hull


def day11_01():
    program = filehelper.get_number_list_from_file("./puzzles/11/puzzle.txt")
    robot = ((0, 0), Direction.UP)
    computer = IntComputer(program, inputs=[0], wait_after_output=True)
    hull = Hull()
    hull = paint_hull(robot, computer, hull)
    print(f"number of painted tiles: {hull.get_size()}")


def day11_02():
    program = filehelper.get_number_list_from_file("./puzzles/11/puzzle.txt")
    robot = ((0, 0), Direction.UP)
    computer = IntComputer(program, wait_after_output=True)
    hull = Hull()
    hull.paint((0, 0), 1)
    hull = paint_hull(robot, computer, hull)
    hull.render()


if __name__ == "__main__":
    day11_01()
    day11_02()

