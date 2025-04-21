from solvers.base_solver import BaseSolver
from constants import (
    Color,
    InvalidInputException,
)


class Password(BaseSolver):
    """returns the INDEX of the wire to cut, starting at 0"""

    def __init__(self, config):
        super().__init__(config)
        self.validate_input()
        self.wordlist = self.getwordlist()
        self.possibilites = [
            [],
        ] * 5

    def validate_input(self):
        super().validate_input()

    def getwordlist(self):
        with open("FRpassword.txt") as f:
            words = [line.strip() for line in f.readlines()]
        self.wordlist = words

    def solve(self):
        return
