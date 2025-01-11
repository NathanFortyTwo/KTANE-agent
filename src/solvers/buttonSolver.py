from enum import Enum
from solvers.baseSolver import BaseSolver, InvalidInputException, Color


class FRButtonText(Enum):
    CANCEL = "Annuler"
    EXPLODE = "Exploser"
    MAINTAIN = "Maintenir"


class ButtonActions(Enum):
    QUICKTAP = "QUICKTAP"
    MAINTAIN = "MAINTAIN"


class SimpleWire(BaseSolver):
    """returns the INDEX of the wire to cut, starting at 0"""

    def validate_input(self):
        super().validate_input()
        color = self.input.get("color")
        if type(color) != Color:
            raise InvalidInputException

    def solve(self):
        color, text, bandcolor = self.input
        battery_number = self.config["battery_number"]
        car = self.config["CAR"]
        frk = self.config["FRK"]

        # if button not pressed yet
        if bandcolor != Color.BLACK:
            match bandcolor:
                case Color.BLUE:
                    return {"Action": "RELEASE", "digit": 4}
                case Color.WHITE:
                    return {"Action": "RELEASE", "digit": 1}
                case Color.YELLOW:
                    return {"Action": "RELEASE", "digit": 5}
                case _:
                    return {"Action": "RELEASE", "digit": 1}

        if text == FRButtonText.CANCEL and color == Color.BLUE:
            return {"Action": ButtonActions.MAINTAIN}
        if text == FRButtonText.EXPLODE and battery_number > 1:
            return {"Action": ButtonActions.QUICKTAP}
        if color == Color.WHITE and car:
            return {"Action": ButtonActions.MAINTAIN}
        if frk and battery_number > 2:
            return {"Action": ButtonActions.QUICKTAP}
        if color == Color.YELLOW:
            return {"Action": ButtonActions.MAINTAIN}
        if color == Color.RED and text == FRButtonText.MAINTAIN:
            return {"Action": ButtonActions.QUICKTAP}

        return {"Action": ButtonActions.MAINTAIN}

    def __init__(self, config):
        super().__init__(config)
        self.validate_input()
