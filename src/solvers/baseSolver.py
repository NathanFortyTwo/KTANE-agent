from enum import Enum


class InvalidInputException(Exception):
    """Raise for Invalid input"""


class Color(Enum):
    RED = "RED"
    YELLOW = "YELLOW"
    WHITE = "WHITE"
    BLACK = "BLACK"
    BLUE = "BLUE"


DEFAULT_BOMB_CONFIG = {
    "series_number": "ABCDE0",
    "battery_number": 0,
    "CAR": False,
    "FRK": False,
}


class BaseSolver:
    def __init__(self, config):
        self.config = config.get("bomb_config")
        self.input = config.get("input")

    def validate_input(self):
        if self.config is None:
            raise InvalidInputException("No bomb configuration found")

        series_number = self.config["series_number"]
        if len(series_number) != 6:
            raise InvalidInputException(
                f"Invalid series number : should have 6 digits but has {len(series_number)}"
            )
        last_digit = series_number[-1]
        try:
            last_digit = int(last_digit)
        except ValueError:
            raise InvalidInputException(
                f"Invalid series number : last char should be a digit but is {last_digit}"
            )

    def solve():
        raise NotImplementedError
