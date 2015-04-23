

from stats import Stat


class Level(Stat):
    def __init__(self, quantity):
        super().__init__("Level", "lev", 40, None, quantity)
