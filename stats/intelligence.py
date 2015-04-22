
from stats import Stat


class Intelligence(Stat):
    def __init__(self, quantity):
        self.SORT = 1
        super().__init__("Intelligence", "int", 30, 12, quantity)
