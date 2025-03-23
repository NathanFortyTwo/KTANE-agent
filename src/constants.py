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
    RELEASE = "RELEASE"


MIN_SIMPLE_WIRES = 3
MAX_SIMPLE_WIRES = 6

S = Symbols
VALID_SEQUENCES = [
    [S.MIRROR, S.AT, S.LAMBDA, S.VOLDEMORT, S.TRIANGLE, S.H_CURSIVE, S.REVERSED_C_DOT],
    [S.E_2DOT, S.MIRROR, S.REVERSE_P, S.CL, S.EMPTY_STAR, S.H_CURSIVE, S.QUESTION],
    [S.CIRCLED_C, S.BALLS, S.CL, S.DOUBLE_K, S.HALF_3, S.LAMBDA, S.EMPTY_STAR],
    [S.SIX, S.REVERSE_P, S.B, S.TRIANGLE, S.DOUBLE_K, S.QUESTION, S.SMILEY],
    [S.MAJ_PSI, S.SMILEY, S.B, S.C_DOT, S.REVERSE_P, S.HORNED_3, S.FULL_STAR],
    [S.SIX, S.E_2DOT, S.HASHTAG, S.AE, S.MAJ_PSI, S.H_BAR, S.OMEGA],
]
