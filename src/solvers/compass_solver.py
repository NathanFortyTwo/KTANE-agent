from solvers.base_solver import BaseSolver
from constants import InvalidInputException
class Compass(BaseSolver):
    """
    
    input is a list of 12 booleans, row by row
    We ignore the way the compass is pointing, the player should rotate on its own
    
    """

    def __init__(self, config):
        super().__init__(config)
        self.validate_input()

        self.patterns = {
                        [True, True, True, True, True, True,
                        True, True, True, True, True, True]:"NORTH",

                        [True, True, True, True, True, True,
                        True, True, True, True, True, True]:"NORTH",                        

                        [True, True, True, True, True, True,
                        True, True, True, True, True, True]:"NORTH",
                        
                        [True, True, True, True, True, True,
                        True, True, True, True, True, True]:"NORTH",
                        
                        [True, True, True, True, True, True,
                        True, True, True, True, True, True]:"NORTH",
                        
                        [True, True, True, True, True, True,
                        True, True, True, True, True, True]:"NORTH",
                        } 
        

    def validate_input(self):
        super().validate_input()
        if self.input not in self.patterns:
            raise InvalidInputException("Invalid light pattern")

    def solve(self):
        return self.patterns.get(self.input)
