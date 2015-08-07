
from characters.stats import Stat


class Skill(Stat):

    TRAININGSCOSTS = (200, 80, 120, 160, 200, 240, 280, 320, 360, 400, "Max")
    MAXIMUM = 10

    def __init__(self, name, raw, upgrade, quantity):
        super().__init__(name, raw, self.MAXIMUM, upgrade, quantity)

    def positive_quantity(self):
        """ Deze is voor hero stats"""
        if self.quantity >= 1:
            return True
        return False


class Chemist(Skill):
    def __init__(self, quantity):
        super().__init__("Chemist", "chm", 1200, quantity)


class Diplomat(Skill):
    def __init__(self, quantity):
        super().__init__("Diplomat", "dip", 400, quantity)


class Loremaster(Skill):
    def __init__(self, quantity):
        super().__init__("Loremaster", "lor", 600, quantity)


class Mechanic(Skill):
    def __init__(self, quantity):
        super().__init__("Mechanic", "mec", 400, quantity)


class Medic(Skill):
    def __init__(self, quantity):
        super().__init__("Medic", "med", 800, quantity)


class Merchant(Skill):
    def __init__(self, quantity):
        super().__init__("Merchant", "mer", 600, quantity)


class Ranger(Skill):
    def __init__(self, quantity):
        super().__init__("Ranger", "ran", 800, quantity)


class Scientist(Skill):
    def __init__(self, quantity):
        super().__init__("Scientist", "sci", 1200, quantity)


class Stealth(Skill):
    def __init__(self, quantity):
        super().__init__("Stealth", "stl", 400, quantity)


class Thief(Skill):
    def __init__(self, quantity):
        super().__init__("Thief", "thf", 800, quantity)


class Troubadour(Skill):
    def __init__(self, quantity):
        super().__init__("Troubadour", "trb", 800, quantity)


class Warrior(Skill):
    def __init__(self, quantity):
        super().__init__("Warrior", "war", 800, quantity)

    def bonus(self, wpn_base_hit):
        return round((47 - ((wpn_base_hit / 10) * 5)) * (self.total / 10))


class Hafted(Skill):
    def __init__(self, quantity):
        super().__init__("Hafted", "haf", 320, quantity)


class Missile(Skill):
    def __init__(self, quantity):
        super().__init__("Missile", "mis", 480, quantity)


class Pole(Skill):
    def __init__(self, quantity):
        super().__init__("Pole", "pol", 320, quantity)


class Shield(Skill):
    def __init__(self, quantity):
        super().__init__("Shield", "shd", 400, quantity)


class Sword(Skill):
    def __init__(self, quantity):
        super().__init__("Sword", "swd", 480, quantity)


class Thrown(Skill):
    def __init__(self, quantity):
        super().__init__("Thrown", "thr", 320, quantity)
