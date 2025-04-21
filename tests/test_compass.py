from solvers.compass_solver import Compass
from solvers.base_solver import DEFAULT_BOMB_CONFIG
import pytest
from constants import InvalidInputException

def test_compass():
    puzzle_input =  ("O", "O", "X", "O", "X", "X",
                         "X", "X", "X", "X", "O", "X")

    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE1"
    bomb_data["batteries"] = 7

    config = {"input": puzzle_input, "bomb_config": bomb_data}

    solution = Compass(config).solve()
    assert solution == "NORTH"

def test_compass_fail():
    puzzle_input =  ("X", "O", "X", "O", "X", "X",
                         "X", "X", "X", "X", "O", "X")

    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE1"
    bomb_data["batteries"] = 7

    config = {"input": puzzle_input, "bomb_config": bomb_data}

    with pytest.raises(InvalidInputException):
        Compass(config).solve()
