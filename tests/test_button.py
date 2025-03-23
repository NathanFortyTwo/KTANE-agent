from solvers.button_solver import Button, Color, FRButtonText, ButtonActions
from solvers.base_solver import DEFAULT_BOMB_CONFIG
import pytest


def test_button_rule1():
    button_input = {
        "button_color": Color.BLUE,
        "button_text": FRButtonText.CANCEL,
        "button_bandcolor": Color.BLACK,
    }

    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE1"
    bomb_data["batteries"] = 7

    button_config = {"input": button_input, "bomb_config": bomb_data}

    solution = Button(button_config).solve()
    assert solution.get("Action") == ButtonActions.MAINTAIN


def test_button_rule2():
    button_input = {
        "button_color": Color.BLUE,
        "button_text": FRButtonText.EXPLODE,
        "button_bandcolor": Color.BLACK,
    }

    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE1"
    bomb_data["batteries"] = 7

    button_config = {"input": button_input, "bomb_config": bomb_data}

    solution = Button(button_config).solve()
    assert solution.get("Action") == ButtonActions.QUICKTAP


def test_button_rule3():
    button_input = {
        "button_color": Color.WHITE,
        "button_text": FRButtonText.CANCEL,
        "button_bandcolor": Color.BLACK,
    }

    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE1"
    bomb_data["batteries"] = 7
    bomb_data["CAR"] = True

    button_config = {"input": button_input, "bomb_config": bomb_data}

    solution = Button(button_config).solve()
    assert solution.get("Action") == ButtonActions.MAINTAIN


def test_button_rule_default():
    button_input = {
        "button_color": Color.RED,
        "button_text": FRButtonText.CANCEL,
        "button_bandcolor": Color.BLACK,
    }

    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE1"
    bomb_data["batteries"] = 7
    bomb_data["CAR"] = True

    button_config = {"input": button_input, "bomb_config": bomb_data}

    solution = Button(button_config).solve()
    assert solution.get("Action") == ButtonActions.MAINTAIN


def test_button_blueband():
    button_input = {
        "button_color": Color.RED,
        "button_text": FRButtonText.CANCEL,
        "button_bandcolor": Color.BLUE,
    }

    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE1"
    bomb_data["batteries"] = 7
    bomb_data["CAR"] = True

    button_config = {"input": button_input, "bomb_config": bomb_data}

    solution = Button(button_config).solve()
    assert solution.get("Action") == ButtonActions.RELEASE
    assert solution.get("digit") == 4


def test_button_redband():
    button_input = {
        "button_color": Color.RED,
        "button_text": FRButtonText.CANCEL,
        "button_bandcolor": Color.RED,
    }

    bomb_data = DEFAULT_BOMB_CONFIG
    bomb_data["series_number"] = "ABCDE1"
    bomb_data["batteries"] = 7
    bomb_data["CAR"] = True

    button_config = {"input": button_input, "bomb_config": bomb_data}

    solution = Button(button_config).solve()
    assert solution.get("Action") == ButtonActions.RELEASE
    assert solution.get("digit") == 1
