
from stats import Stat


class Endurance(Stat):
    def __init__(self, quantity):
        self.SORT = 4
        super().__init__("Endurance", "edu", 40, 12, quantity)
