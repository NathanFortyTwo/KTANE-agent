from solvers.base_solver import BaseSolver
from constants import (
    InvalidInputException,
)


class Memory(BaseSolver):
    """
    Returns the INDEX of the button to press,
    Index 1 means 2nd button from the left
    """

    def __init__(self, config):
        super().__init__(config)
        self.history = self.config.get("MEMORY_HISTORY")
        self.validate_input()

        self.current_number_displayed = self.input.get("number_displayed")
        self.button_numbers = self.input.get("button_numbers")
        self.current_step = self.input.get("step")

    def validate_input(self):
        super().validate_input()
        if not 1 <= self.input.get("step") <= 5:
            raise InvalidInputException(f"step should be between 1 and 5, got{self.input.get("steps")}")

        if not 1 <= self.input.get("number_displayed") <= 4:
            raise InvalidInputException(
                f"Number displayed on top should be between 1 and 4, got {self.input.get('number_displayed')}"
            )

        if not len(self.input.get("button_numbers")) == 4:
            raise InvalidInputException(f"Should only receive 4 button values, got {self.input.get("button_numbers")}")

    def _handle_step_1(self):

        if self.current_number_displayed == 1:
            return 1
        return self.current_number_displayed - 1

    def _handle_step_2(self):
        if self.current_number_displayed == 1:
            return self.button_numbers.index(4)
        if self.current_number_displayed == 3:
            return 1
        return self.history[0].get("index")  # return same position as step 1

    def _handle_step_3(self):
        if self.current_number_displayed == 1:
            digit_at_step_2 = self.history[1].get("value")
            return self.button_numbers.index(digit_at_step_2)
        if self.current_number_displayed == 2:
            digit_at_step_1 = self.history[0].get("value")
            return self.button_numbers.index(digit_at_step_1)
        if self.current_number_displayed == 3:
            return 2
        if self.current_number_displayed == 4:
            return self.button_numbers.index(4)

    def _handle_step_4(self):
        if self.current_number_displayed == 1:
            return self.history[0].get("index")  # same position as step 1
        if self.current_number_displayed == 2:
            return 0
        return self.history[1].get("index")  # same position as step 2

    def _handle_step_5(self):
        if self.current_number_displayed == 1:
            digit_at_step_1 = self.history[0].get("value")
            return self.button_numbers.index(digit_at_step_1)
        if self.current_number_displayed == 2:
            digit_at_step_2 = self.history[1].get("value")
            return self.button_numbers.index(digit_at_step_2)
        if self.current_number_displayed == 3:
            digit_at_step_4 = self.history[3].get("value")
            return self.button_numbers.index(digit_at_step_4)
        if self.current_number_displayed == 4:
            digit_at_step_3 = self.history[1].get("value")
            return self.button_numbers.index(digit_at_step_3)

    def solve(self):
        return getattr(self, f"_handle_step_{self.current_step}")
