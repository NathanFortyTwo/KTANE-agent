from solvers.base_solver import BaseSolver
from constants import InvalidInputException
class Compass(BaseSolver):
    """
    
    input is a list of 12 booleans, row by row
    We ignore the way the compass is pointing, the player should rotate on its own
    
    """

    def __init__(self, config):
        super().__init__(config)

        self.patterns = {
                        ("O", "O", "X", "O", "X", "X",
                         "X", "X", "X", "X", "O", "X"):"NORTH",

                        ("X", "O", "X", "O", "X", "O",
                         "O", "X", "X", "O", "X", "X"):"NORTH",

                        ("O", "X", "X", "O", "O", "X",
                         "X", "X", "X", "X", "O", "X"):"SOUTH",

                        ("X", "O", "X", "O", "X", "O",
                         "O", "X", "O", "O", "O", "X"):"SOUTH",

                        ("O", "O", "O", "O", "X", "O",
                         "X", "O", "O", "X", "X", "X"):"WEST",  
                          
                        ("O", "O", "O", "O", "X", "O",
                         "O", "O", "O", "X", "X", "O"):"WEST",

                        ("X", "O", "X", "X", "X", "X",
                         "X", "X", "X", "O", "X", "O"):"EAST",

                        ("X", "O", "X", "X", "O", "O",
                         "X", "X", "X", "O", "X", "O"):"EAST",
                        } 

        self.validate_input()

        

    def validate_input(self):
        super().validate_input()
        if self.input not in self.patterns:
            raise InvalidInputException("Invalid light pattern")

    def solve(self):
        return self.patterns.get(self.input)
