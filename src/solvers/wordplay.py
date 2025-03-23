from solvers.base_solver import BaseSolver
from constants import InvalidInputException


# Positions are the following
# 0 1
# 2 3
# 4 5

WORD_POSITIONS = {
    "OUI": 2,
    "PREMIER": 1,
    "VERRE": 5,
    "OK": 1,
    "MOTS": 5,
    "RIEN": 2,
    "EMPTY_STRING": 4,
    "VIDE": 3,
    "NON": 5,
    "MOT": 2,
    "MAUX": 5,
    "BOUGE": 3,
    "ROUGE": 3,
    "AU": 4,
    "EAU": 4,
    "ATTENDS": 5,
    "TES": 3,
    "T'ES": 5,
    "TON": 3,
    "TONS": 3,
    "THON": 0,
    "TU ES": 5,
    "HAUT": 4,
    "VERS": 3,
    "VERT": 2,
    "C'EST": 5,
    "C": 1,
    "VER": 5,
}


def load_candidates():
    with open("src/wordlists.txt") as f:
        lines = f.readlines()

    candidates = {}
    for line in lines:
        key, value = line.strip().split(":")
        value = value.replace(" ", "")  # replace spaces
        value = value.split(",")
        candidates[key] = value

    return candidates


class Wordplay(BaseSolver):

    def __init__(self, config):
        super().__init__(config)
        self.validate_input()

    def validate_input(self):
        # super().validate_input()
        assert self.input
        assert len(self.input.get("to_watch")) == 6

    def solve(self):
        candidates = load_candidates()
        target_word = self.input.get("target")
        words_to_watch = self.input.get("to_watch")  # 6 tuple
        index_to_watch = WORD_POSITIONS.get(target_word)

        chosen_candidate_list = candidates.get(words_to_watch[index_to_watch])
        for word in chosen_candidate_list:
            if word in words_to_watch:
                return word

        raise Exception("Word not found in list...")
