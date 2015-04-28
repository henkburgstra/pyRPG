
class Property(object):
    def __init__(self, name, raw, quantity, sort):
        self.NAME = name
        self.RAW = raw
        self.QUANTITY = quantity
        self.SORT = sort


class WeaponSkill(Property):
    def __init__(self, skill_type=None):    # quantity heet anders en is string, maar verder hetzelfde. (=weaponskill)
        super().__init__("Skill", "skill", skill_type, 1)


class MinIntelligence(Property):
    def __init__(self, quantity=None):
        super().__init__("Min.Intelligence", "min_int", quantity, 2)


class MinStrength(Property):
    def __init__(self, quantity=None):
        super().__init__("Min.Strength", "min_str", quantity, 3)


class MinStamina(Property):
    def __init__(self, quantity=None):
        super().__init__("Min.Stamina", "min_sta", quantity, 4)


class Protection(Property):
    def __init__(self, quantity=None):
        super().__init__("Protection", "prt", quantity, 5)


class Defense(Property):
    def __init__(self, quantity=None):
        super().__init__("Defense", "def", quantity, 6)


class BaseHit(Property):
    def __init__(self, quantity=None):
        super().__init__("Base Hit", "hit", quantity, 7)


class Damage(Property):
    def __init__(self, quantity=None):
        super().__init__("Damage", "dam", quantity, 8)


class Dexterity(Property):
    def __init__(self, quantity=None):
        super().__init__("Dexterity", "dex", quantity, 9)


class Stealth(Property):
    def __init__(self, quantity=None):
        super().__init__("Stealth", "stl", quantity, 10)
