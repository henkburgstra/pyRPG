
from characters.stats import Stat


class Skill(Stat):

    trainingcost = (200, 80, 120, 160, 200, 240, 280, 320, 360, 400, "Max")
    maximum = 10

    def __init__(self, name, raw, upgrade, quantity, sort=0):
        super().__init__(name, raw, self.maximum, upgrade, quantity)
        self.SORT = sort

    def positive_quantity(self):
        """ Deze is voor hero stats"""
        if self._quantity >= 1:
            return True
        return False


class Chemist(Skill):
    def __init__(self, quantity=0):
        super().__init__("Chemist", "chm", 1200, quantity)


class Diplomat(Skill):
    def __init__(self, quantity=0):
        super().__init__("Diplomat", "dip", 400, quantity)


class Loremaster(Skill):
    def __init__(self, quantity=0):
        super().__init__("Loremaster", "lor", 600, quantity)


class Mechanic(Skill):
    def __init__(self, quantity=0):
        super().__init__("Mechanic", "mec", 400, quantity)


class Medic(Skill):
    def __init__(self, quantity=0):
        super().__init__("Medic", "med", 800, quantity)


class Merchant(Skill):
    def __init__(self, quantity=0):
        super().__init__("Merchant", "mer", 600, quantity)


class Ranger(Skill):
    def __init__(self, quantity=0):
        super().__init__("Ranger", "ran", 800, quantity)


class Scientist(Skill):
    def __init__(self, quantity=0):
        super().__init__("Scientist", "sci", 1200, quantity)


class Stealth(Skill):
    def __init__(self, quantity=0):
        super().__init__("Stealth", "stl", 400, quantity)


class Thief(Skill):
    def __init__(self, quantity=0):
        super().__init__("Thief", "thf", 800, quantity)


class Troubadour(Skill):
    def __init__(self, quantity=0):
        super().__init__("Troubadour", "trb", 800, quantity)


class Warrior(Skill):
    def __init__(self, quantity=0):
        super().__init__("Warrior", "war", 800, quantity)


class Hafted(Skill):
    def __init__(self, quantity=0):
        super().__init__("Hafted", "haf", 320, quantity, sort=1)


class Missile(Skill):
    def __init__(self, quantity=0):
        super().__init__("Missile", "mis", 480, quantity, sort=1)


class Pole(Skill):
    def __init__(self, quantity=0):
        super().__init__("Pole", "pol", 320, quantity, sort=1)


class Shield(Skill):
    def __init__(self, quantity=0):
        super().__init__("Shield", "shd", 400, quantity, sort=1)


class Sword(Skill):
    def __init__(self, quantity=0):
        super().__init__("Sword", "swd", 480, quantity, sort=1)


class Thrown(Skill):
    def __init__(self, quantity=0):
        super().__init__("Thrown", "thr", 320, quantity, sort=1)
