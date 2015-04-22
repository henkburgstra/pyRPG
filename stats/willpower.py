
from stats import Stat


class Willpower(Stat):
    def __init__(self, quantity):
        self.SORT = 2
        super().__init__("Willpower", "wil", 30, 12, quantity)
