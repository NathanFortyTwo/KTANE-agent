from solvers.wordplay import Wordplay
from solvers.base_solver import DEFAULT_BOMB_CONFIG
import pytest


def test_wordplay():
    puzzle_input = {
        "target": "OUI",
        "to_watch": ["PRET", "PREMIER", "NON", " VIDE", "RIEN", "OUI"],
    }
    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE1"
    bomb_data["batteries"] = 7

    config = {"input": puzzle_input, "bomb_config": bomb_data}

    solution = Wordplay(config).solve()
    assert solution == "PREMIER"


def test_wordplay_2():
    puzzle_input = {
        "target": "OUI",
        "to_watch": ["PRET", "PREMIER", "DROITE", " VIDE", "RIEN", "OUI"],
    }
    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE1"
    bomb_data["batteries"] = 7

    config = {"input": puzzle_input, "bomb_config": bomb_data}

    solution = Wordplay(config).solve()
    assert solution == "OUI"


def test_wordplay_3():
    puzzle_input = {
        "target": "VERRE",
        "to_watch": ["PRET", "PREMIER", "DROITE", " VIDE", "RIEN", "OUI"],
    }
    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE1"
    bomb_data["batteries"] = 7

    config = {"input": puzzle_input, "bomb_config": bomb_data}

    solution = Wordplay(config).solve()
    assert solution == "DROITE"
