from solvers.simpleWire import SimpleWire, Color
from solvers.baseSolver import DEFAULT_BOMB_CONFIG
import pytest


def test_pytest_ok():
    with pytest.raises(AssertionError):
        assert 1 == 0


def test_simple_wire():
    simple_wire_input = [Color.BLACK, Color.BLUE, Color.RED]
    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE1"
    bomb_data["batteries"] = 7

    simple_wire_config = {"input": simple_wire_input, "bomb_config": bomb_data}

    solution = SimpleWire(simple_wire_config).solve()
    assert type(solution) == int
    assert solution > 0
    assert solution < len(simple_wire_input)


def test_simple_3wire_many():
    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE2"
    bomb_data["batteries"] = 7
    inputs = [
        ([Color.BLACK, Color.BLUE, Color.BLACK], 1),  # NORED
        ([Color.RED, Color.RED, Color.RED], 2),  # DEFAULT
        ([Color.RED, Color.BLUE, Color.WHITE], 2),  # LAST_WHITE
        ([Color.BLUE, Color.BLUE, Color.RED], 1),  #  MULT_BLUE
        ([Color.BLUE, Color.RED, Color.BLUE], 2),  # MULT_BLUE
    ]
    for k in range(len(inputs)):
        simple_wire_input, solution = inputs[k]
        simple_wire_config = {"input": simple_wire_input, "bomb_config": bomb_data}
        assert SimpleWire(simple_wire_config).solve() == solution
