from ship.computer import IntComputer
from util import filehelper

EMPTY = 0
WALL = 1
BLOCK = 2
PADDLE = 3
BALL = 4

NO_MOVE = 0
LEFT = -1
RIGHT = 1

BLOCK_TYPES = {
    EMPTY: " ",
    WALL: "#",
    BLOCK: "@",
    PADDLE: "_",
    BALL: "o",
}


class Game:
    def __init__(self, program, play=True, visual_mode=False):
        if play:
            # set memory at position 0 to 2 to play
            program[0] = 2
        self.computer = IntComputer(
            program, wait_for_input=True, wait_after_output=True
        )
        self.visual_mode = visual_mode
        self.game_map = {}
        self.score = None

    def render(self):
        last_row = 0
        # Reset all terminal settings to default
        print("\033c", end="")
        for y, x in sorted(self.game_map.keys()):
            if last_row != y:
                print("")
            print(BLOCK_TYPES[self.game_map[(y, x)]], end="")
            last_row = y
        print("")

    def play_game(self):
        n = 0
        current_x = None
        current_y = None
        ball_x = None
        paddle_x = None
        while not self.computer.finished:
            n += 1
            output = self.computer.run()
            ready = not self.computer.finished and not self.computer.waiting
            if self.computer.waiting:  # waiting for input
                if paddle_x > ball_x:
                    i = LEFT
                elif paddle_x < ball_x:
                    i = RIGHT
                else:
                    i = NO_MOVE
                self.computer.inputs = [i]
                if self.visual_mode:
                    self.render()
                # reset n because we need to run again with the needed input
                n -= 1
            elif ready and n == 1:
                current_x = output
            elif ready and n == 2:
                current_y = output
            elif ready and n == 3:
                if current_x == -1 and current_y == 0:
                    self.score = output
                else:
                    current_tile = output
                    self.game_map[(current_y, current_x)] = current_tile
                    if current_tile == 4:  # ball
                        ball_x = current_x
                    if current_tile == 3:  # paddle
                        paddle_x = current_x
                n = 0


def day13_01():
    program = filehelper.get_number_list_from_file("./puzzles/13/puzzle.txt")

    game = Game(program, play=False, visual_mode=False)
    game.play_game()

    count = 0

    for item in game.game_map:
        if game.game_map[item] == BLOCK:
            count += 1
    print(f"number of block tiles: {count} ")


def day13_02():
    program = filehelper.get_number_list_from_file("./puzzles/13/puzzle.txt")
    game = Game(program, play=True, visual_mode=False)
    game.play_game()
    print(f"final score: {game.score}")


if __name__ == "__main__":
    day13_01()
    day13_02()
