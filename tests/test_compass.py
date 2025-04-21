from solvers.compass_solver import Compass
from solvers.base_solver import DEFAULT_BOMB_CONFIG
import pytest


@pytest.mark.skip("Compass solver not implemented yet")
def test_compass():
    puzzle_input = (True, True, True, True, True, True, 
                    True, True, True, True, True, True)
    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE1"
    bomb_data["batteries"] = 7

    config = {"input": puzzle_input, "bomb_config": bomb_data}

    solution = Compass(config).solve()
    assert solution == "NORTH"
