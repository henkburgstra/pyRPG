
from stats import Stat


class Strength(Stat):
    def __init__(self, quantity):
        self.SORT = 5
        super().__init__("Strength", "str", 30, 12, quantity)
