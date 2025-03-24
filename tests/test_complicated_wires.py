from solvers.complicated_wires import ComplicatedWires, ComplicatedWireInput, Color
from solvers.base_solver import DEFAULT_BOMB_CONFIG
import pytest


def test_complicated_wires1():
    puzzle_input = [
        ComplicatedWireInput(Color.RED, Color.BLUE, True, False),
        ComplicatedWireInput(Color.RED, Color.BLUE, True, True),
        ComplicatedWireInput(Color.RED, None, True, False),
        ComplicatedWireInput(Color.BLUE, Color.WHITE, True, False),
        ComplicatedWireInput(Color.WHITE, Color.BLUE, True, False),
        ComplicatedWireInput(Color.WHITE, None, False, False),
    ]
    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE1"
    bomb_data["batteries"] = 7
    bomb_data["parallel_port_count"] = 7

    config = {"input": puzzle_input, "bomb_config": bomb_data}

    solution = ComplicatedWires(config).solve()
    assert solution == [
        True,
        False,
        True,
        False,
        False,
        True,
    ]
