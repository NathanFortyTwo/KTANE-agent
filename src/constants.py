from enum import Enum


class Symbols(Enum):
    MIRROR = "MIRROR"
    AT = "AT"
    LAMBDA = "LAMBDA"
    VOLDEMORT = "VOLDEMORT"
    TRIANGLE = "TRIANGLE"
    H_CURSIVE = "H_CURSIVE"
    REVERSED_C_DOT = "REVERSED_C_DOT"
    E_2DOT = "E_2DOT"
    CL = "CL"
    EMPTY_STAR = "EMPTY_STAR"
    QUESTION = "QUESTION"
    CIRCLED_C = "CIRCLED_C"
    BALLS = "BALLS"
    DOUBLE_K = "DOUBLE_K"
    HALF_3 = "HALF_3"
    SIX = "SIX"
    REVERSE_P = "REVERSE_P"
    B = "B"
    SMILEY = "SMILEY"
    MAJ_PSI = "MAJ_PSI"
    C_DOT = "C_DOT"
    HORNED_3 = "HORNED_3"
    FULL_STAR = "FULL_STAR"
    HASHTAG = "HASHTAG"
    AE = "AE"
    H_BAR = "H_BAR"
    OMEGA = "OMEGA"


class Color(Enum):
    RED = "RED"
    YELLOW = "YELLOW"
    WHITE = "WHITE"
    BLACK = "BLACK"
    BLUE = "BLUE"


class InvalidInputException(Exception):
    """Raise for Invalid input"""


class FRButtonText(Enum):
    CANCEL = "Annuler"
    EXPLODE = "Exploser"
    MAINTAIN = "Maintenir"


class ButtonActions(Enum):
    QUICKTAP = "QUICKTAP"
    MAINTAIN = "MAINTAIN"


MIN_SIMPLE_WIRES = 3
MAX_SIMPLE_WIRES = 6
