from enum import Enum
from solvers.baseSolver import BaseSolver
from constants import Symbols as S

# Moche mais améliore la lisiblité du code

VALID_SEQUENCES = [
    [S.MIRROR, S.AT, S.LAMBDA, S.VOLDEMORT, S.TRIANGLE, S.H_CURSIVE, S.REVERSED_C_DOT],
    [S.E_2DOT, S.MIRROR, S.REVERSE_P, S.CL, S.EMPTY_STAR, S.H_CURSIVE, S.QUESTION],
    [S.CIRCLED_C, S.BALLS, S.CL, S.DOUBLE_K, S.HALF_3, S.LAMBDA, S.EMPTY_STAR],
    [S.SIX, S.REVERSE_P, S.B, S.TRIANGLE, S.DOUBLE_K, S.QUESTION, S.SMILEY],
    [S.MAJ_PSI, S.SMILEY, S.B, S.C_DOT, S.REVERSE_P, S.HORNED_3, S.FULL_STAR],
    [S.SIX, S.E_2DOT, S.HASHTAG, S.AE, S.MAJ_PSI, S.H_BAR, S.OMEGA],
]


def is_in(candidate, symbol):
    return symbol in candidate


class SimpleWire(BaseSolver):
    """returns the INDEX of the wire to cut, starting at 0"""

    def __init__(self, config):
        super().__init__(config)
        ##self.validate_input()

    def validate_input(self):
        super().validate_input()

    def key(self, element):
        return self.candidate.index(element)

    def solve(self):
        candidates = VALID_SEQUENCES
        for symbol in self.input:
            candidates = list(
                filter(lambda candidate: is_in(candidate, symbol), candidates)
            )
        if len(candidates) != 1:
            raise Exception(
                "Illegal wire count [ERROR: should have been caught earlier]"
            )
        self.candidate = candidates[0]

        self.input.sort(key=self.key)
        return self.input


inputs = [S.MAJ_PSI, S.H_BAR, S.HASHTAG, S.SIX]
config = {"input": inputs, "bomb_config": 0}
SimpleWire(config).solve()
