from solvers.base_solver import BaseSolver
from constants import (
    Color,
    InvalidInputException,
    FRButtonText,
    ButtonActions,
)


class Button(BaseSolver):
    """returns the INDEX of the wire to cut, starting at 0"""

    def __init__(self, config):
        super().__init__(config)
        self.validate_input()

    def validate_input(self):
        super().validate_input()
        if type(self.input.get("button_color")) != Color:
            raise InvalidInputException
        if type(self.input.get("button_text")) != FRButtonText:
            raise InvalidInputException
        if type(self.input.get("button_bandcolor")) != Color:
            raise InvalidInputException

    def solve(self):
        color = self.input.get("button_color")
        text = self.input.get("button_text")
        bandcolor = self.input.get("button_bandcolor")

        batteries = self.config["batteries"]
        car = self.config.get("CAR", None)
        frk = self.config.get("FRK", None)

        # if button not pressed yet
        if bandcolor != Color.BLACK:
            match bandcolor:
                case Color.BLUE:
                    return {"Action": ButtonActions.RELEASE, "digit": 4}
                case Color.WHITE:
                    return {"Action": ButtonActions.RELEASE, "digit": 1}
                case Color.YELLOW:
                    return {"Action": ButtonActions.RELEASE, "digit": 5}
                case _:
                    return {"Action": ButtonActions.RELEASE, "digit": 1}
        print(text, color, car)
        if text == FRButtonText.CANCEL and color == Color.BLUE:
            return {"Action": ButtonActions.MAINTAIN}
        if text == FRButtonText.EXPLODE and batteries > 1:
            return {"Action": ButtonActions.QUICKTAP}
        if color == Color.WHITE and car:
            return {"Action": ButtonActions.MAINTAIN}
        if frk and batteries > 2:
            return {"Action": ButtonActions.QUICKTAP}
        if color == Color.YELLOW:
            return {"Action": ButtonActions.MAINTAIN}
        if color == Color.RED and text == FRButtonText.MAINTAIN:
            return {"Action": ButtonActions.QUICKTAP}

        return {"Action": ButtonActions.MAINTAIN}
