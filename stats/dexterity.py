
from stats import Stat


class Dexterity(Stat):
    def __init__(self, quantity):
        self.SORT = 3
        super().__init__("Dexterity", "dex", 30, 24, quantity)
