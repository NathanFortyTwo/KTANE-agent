from solvers.base_solver import BaseSolver
from constants import Color, InvalidInputException, MIN_SIMPLE_WIRES, MAX_SIMPLE_WIRES


class SimpleWire(BaseSolver):
    """returns the INDEX of the wire to cut, starting at 0"""

    def __init__(self, config):
        super().__init__(config)
        self.validate_input()

    def validate_input(self):
        super().validate_input()

        if len(self.input) < MIN_SIMPLE_WIRES:
            raise InvalidInputException("Not enough wires")
        if len(self.input) > MAX_SIMPLE_WIRES:
            raise InvalidInputException("Not enough wires")
        for color in self.input:
            if type(color) != Color:
                raise InvalidInputException(
                    f"Wrong input type : should be List<Color>, but at least one element has type {type(color)}"
                )

    def solve(self):
        wires_count = len(self.input)
        match wires_count:
            case 3:
                return self.solve_3_wires()
            case 4:
                return self.solve_4_wires()
            case 5:
                return self.solve_5_wires()
            case 6:
                return self.solve_6_wires()

        raise Exception("Illegal wire count [ERROR: should have been caught earlier]")

    def solve_3_wires(self):
        if Color.RED not in self.input:
            return 1
        if self.input[-1] == Color.WHITE:
            return 2  # last wire is index 2
        if self.input.count(Color.BLUE) > 1:
            for index, element in enumerate(self.input):
                if element == Color.BLUE:
                    last_blue_index = index
            return last_blue_index
        return 2

    def solve_4_wires(self):
        last_series_digit = int(self.config["series_number"])

        # more than one red && last digit odd
        if self.input.count(Color.RED) > 1 and (last_series_digit % 2 == 1):
            for index, element in enumerate(self.input):
                if element == Color.RED:
                    last_red_index = index
            return last_red_index

        # last is yellow and no red
        if self.input[-1] == Color.YELLOW and (self.input.count(Color.RED) == 0):
            return 0

        # exactly one blue
        if self.input.count(Color.BLUE) == 1:
            return 0

        # more than 1 yellow
        if self.input.count(Color.YELLOW) > 1:
            return 3

        return 1

    def solve_5_wires(self):
        last_series_digit = int(self.config["series_number"])

        if self.input[-1] == Color.BLACK and (last_series_digit % 2 == 1):
            return 3

        if self.input.count(Color.RED) == 1 and self.input.count(Color.YELLOW) > 1:
            return 0

        if self.input.count(Color.BLACK) == 0:
            return 1

        return 0

    def solve_6_wires(self):
        last_series_digit = int(self.config["series_number"])

        if self.input.count(Color.YELLOW) == 0 and (last_series_digit % 2 == 1):
            return 2

        if self.input.count(Color.YELLOW) == 1 and self.input.count(Color.WHITE) > 1:
            return 3

        if self.input.count(Color.RED) == 0:
            return 5

        return 3
