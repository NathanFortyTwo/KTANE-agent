from solvers.base_solver import BaseSolver
from constants import VALID_SEQUENCES


def is_in(candidate, symbol):
    return symbol in candidate


class Keyboard(BaseSolver):
    """returns the INDEX of the wire to cut, starting at 0"""

    def __init__(self, config):
        super().__init__(config)
        self.validate_input()

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
