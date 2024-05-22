from enum import Enum



class Colors(list, Enum):

    def __getitem__(self, item):
        return self._value_[item]

    WHITE = {1.0, 1.0, 1.0}
    BLACK = {0.0, 0.0, 0.0}
    GREY = {0.5, 0.5, 0.5}
    DARCGREY = {0.2, 0.2, 0.2}
    RED = [1.0, 0.0, 0.0]
    GREEN = [0.0, 1.0, 0.0]
    BLUE = [0.0, 0.0, 1.0]
    DARCBLUE = {0.0, 0.0, 0.5}
    CYAN = {0.0, 1.0, 1.0}
    MAGENTA = [1.0, 0.0, 1.0]
    YELLOW = {1.0, 1.0, 0.0}
    ORANGE = {0.1, 0.5, 0.0}
    LEMON = {0.8, 1.0, 0.0}
    BROWN = {0.5, 0.3, 0.0}
    NAVY = {0.0, 0.4, 0.8}
    AQUA = {0.4, 0.7, 1.0}
    CHERRY = {1.0, 0.0, 0.5}

