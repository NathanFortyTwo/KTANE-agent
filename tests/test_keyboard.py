from solvers.keyboard_solver import Keyboard
from constants import Symbols as S
from solvers.base_solver import DEFAULT_BOMB_CONFIG
import pytest


def test_ok():
    kb_input = [S.H_BAR, S.OMEGA, S.SIX, S.SIX]

    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE1"
    bomb_data["batteries"] = 7

    config = {"input": kb_input, "bomb_config": bomb_data}

    solution = Keyboard(config).solve()
    assert len(solution) == 4

def test_fail():
    kb_input = [S.H_BAR, S.OMEGA, S.EMPTY_STAR, S.SIX]

    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE1"
    bomb_data["batteries"] = 7

    config = {"input": kb_input, "bomb_config": bomb_data}
    with pytest.raises(Exception):
        Keyboard(config).solve()
    