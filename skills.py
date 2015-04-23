
class Skill(object):

    trainingcost = (200, 80, 120, 160, 200, 240, 280, 320, 360, 400, "Max")
    maximum = 10

    def __init__(self, name, raw, upgrade, quantity, sort=0):
        self.NAME = name
        self.RAW = raw
        self.UPGRADE = upgrade
        self._quantity = quantity
        self._extra = 0
        self._total = quantity
        self.SORT = sort

    def show_skill(self):
        """ Deze is voor hero stats"""
        if self._extra == 0:
            print("      {:13}: {}".format(self.NAME, self._quantity))
        elif self._extra > 0:
            print("      {:13}: {} (+{})".format(self.NAME, self._quantity, self._extra))
        else:
            print("      {:13}: {} ({})".format(self.NAME, self._quantity, self._extra))

    def positive_quantity(self):
        """ Deze is voor hero stats"""
        if self._quantity >= 1:
            return True
        return False

    def get_extra(self):
        return self._extra

    def set_extra(self, extra):
        self._extra = extra

    extra = property(get_extra, set_extra)

    def get_total(self):
        return self._total

    def set_total(self, total):
        self._total = total

    total = property(get_total, set_total)

    @property
    def quantity(self):
        return self._quantity


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
