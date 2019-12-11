from util import filehelper
from ship.computer import IntComputer


def paint(hull, coordinates, color):
    x, y = coordinates
    if x < hull["min_width"]:
        hull["min_width"] = x
    if y < hull["min_height"]:
        hull["min_height"] = y
    if x > hull["width"]:
        hull["width"] = x
    if y > hull["height"]:
        hull["height"] = y
    hull[coordinates] = color
    return hull


def get_color(hull, coordinates):
    if not coordinates in hull:
        hull[coordinates] = 0

    return hull[coordinates]


def paint_hull(robot, computer, hull):

    coordinates, direction = robot
    while not computer.finished:
        current_color = get_color(hull, coordinates)
        computer.inputs = [current_color]
        _, color = computer.run()
        hull = paint(hull, coordinates, color)

        if not computer.finished:
            _, turn = computer.run()

            # 0 = UP 1 = RIGHT 2=DOWN 3 = LEFT
            if turn == 0:  # left
                if direction == 0:
                    direction = 3
                else:
                    direction -= 1
            if turn == 1:  # right
                if direction == 3:
                    direction = 0
                else:
                    direction += 1
            x, y = coordinates
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
            coordinates = (x, y)
    return hull


def day11_01():
    program = filehelper.get_number_list_from_file("./puzzles/11/puzzle.txt")
    robot = ((0, 0), 0)
    computer = IntComputer(program, inputs=[0], wait_after_output=True)
    hull = {"min_width": 0, "min_height": 0, "width": 0, "height": 0}
    hull = paint_hull(robot, computer, hull)
    # len -2 because we store width and height here, too
    print(f"number of painted tiles: {len(hull)-2}")


def day11_02():
    program = filehelper.get_number_list_from_file("./puzzles/11/puzzle.txt")
    robot = ((0, 0), 0)
    computer = IntComputer(program, wait_after_output=True)
    hull = {"min_width": 0, "min_height": 0, "width": 0, "height": 0}
    hull = paint(hull, (0, 0), 1)
    hull = paint_hull(robot, computer, hull)
    # len -4 because we store width and height here, too
    min_width = hull["min_width"]
    width = hull["width"]
    min_height = hull["min_height"]
    height = hull["height"]

    for y in range(height, min_height - 1, -1):
        line = ""
        for x in range(min_width, width):
            item = " "
            coordinates = (x, y)
            if get_color(hull, coordinates) == 1:
                item = "#"
            else:
                item = " "
            line += item
        print(line)


if __name__ == "__main__":
    day11_01()
    day11_02()

