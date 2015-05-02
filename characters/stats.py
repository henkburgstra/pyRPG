
from output import Output


class Stat(object):
    def __init__(self, name, raw, maximum, upgrade, quantity):
        self.NAME = name
        self.RAW = raw
        self.MAXIMUM = maximum     # maximum mogelijk, bijv 30
        self.UPGRADE = upgrade     # upgrade forumule constante
        self.quantity = quantity   # standaard hoeveelheid op te waarderen stat (tot bijv 30)
        self.extra = 0             # wat geeft gear voor pos/neg extra
        self.total = quantity      # quantity + extra
        self.current = quantity    # gaat af wanneer er bijv schade is (sta, edu, lev)

    def show_stat(self):
        """ Deze is voor hero stats"""
        Output.stat(self.NAME, self.quantity, self.extra)


class Level(Stat):
    def __init__(self, quantity):
        super().__init__("Level", "lev", 40, None, quantity)


class Intelligence(Stat):
    def __init__(self, quantity):
        self.SORT = 1
        super().__init__("Intelligence", "int", 30, 12, quantity)


class Willpower(Stat):
    def __init__(self, quantity):
        self.SORT = 2
        super().__init__("Willpower", "wil", 30, 12, quantity)


class Dexterity(Stat):
    def __init__(self, quantity):
        self.SORT = 3
        super().__init__("Dexterity", "dex", 30, 24, quantity)


class Endurance(Stat):
    def __init__(self, quantity):
        self.SORT = 4
        super().__init__("Endurance", "edu", 40, 12, quantity)


class Strength(Stat):
    def __init__(self, quantity):
        self.SORT = 5
        super().__init__("Strength", "str", 30, 12, quantity)


class Stamina(Stat):
    def __init__(self, quantity):
        self.SORT = 6
        super().__init__("Stamina", "sta", 90, 4, quantity)
