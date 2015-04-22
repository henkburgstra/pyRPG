
from stats import Stat


class Stamina(Stat):
    def __init__(self, quantity):
        self.SORT = 6
        super().__init__("Stamina", "sta", 90, 4, quantity)
