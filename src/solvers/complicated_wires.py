from solvers.base_solver import BaseSolver
from constants import InvalidInputException, Color
from enum import Enum


class ComplicatedWireInput(BaseSolver):
    def __init__(self, color1, color2, star, light):
        self.color1 = color1
        self.color2 = color2
        self.star = star
        self.light = light


class ComplicatedWires(BaseSolver):
    """
    Returns an array of booleans the same lenght of the input
    True means we should cut the wire
    """

    def __init__(self, config):
        super().__init__(config)
        self.validate_input()

        last_digit = int(self.config["series_number"][-1])
        self.C = True  # cut
        self.N = False  # dont cut
        self.S = last_digit % 2 == 0  # cut if last digit even
        self.P = (
            self.config["parallel_port_count"] >= 1
        )  # cut if at least one parallel port

        self.B = self.config["batteries"] >= 2  # cut if 2 or more batteries

    def validate_input(self):
        super().validate_input()
        assert 1 <= len(self.input) <= 6
        for wire in self.input:
            if type(wire) != ComplicatedWireInput:
                raise InvalidInputException(
                    f"{wire} should have type ComplicatedWireInput"
                )
            assert type(wire.color1) == Color or type(wire.color2) == Color
            assert wire.color1 in [Color.RED, Color.BLUE, Color.WHITE, None]
            assert wire.color2 in [Color.RED, Color.BLUE, Color.WHITE, None]

    def get_value(self, contains_red, contains_blue, light, star):
        C, N, S, P, B = self.C, self.N, self.S, self.P, self.B
        mapping = {
            (False, False, False, False): C,
            (False, False, False, True): C,
            (False, False, True, False): N,
            (False, False, True, True): B,
            (False, True, False, False): S,
            (False, True, False, True): N,
            (False, True, True, False): P,
            (False, True, True, True): P,
            (True, False, False, False): S,
            (True, False, False, True): C,
            (True, False, True, False): B,
            (True, False, True, True): B,
            (True, True, False, False): S,
            (True, True, False, True): P,
            (True, True, True, False): S,
            (True, True, True, True): N,
        }
        return mapping[(contains_red, contains_blue, light, star)]

    def solve_wire(self, wire):
        contains_red = wire.color1 == Color.RED or wire.color2 == Color.RED
        contains_blue = wire.color1 == Color.BLUE or wire.color2 == Color.BLUE
        light = wire.light
        star = wire.star

        return self.get_value(contains_red, contains_blue, light, star)

    def solve(self):
        solution = []
        for wire in self.input:
            solution.append(self.solve_wire(wire))
        return solution
