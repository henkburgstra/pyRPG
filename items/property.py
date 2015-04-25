
class Property(object):
    def __init__(self, name, raw, quantity):
        self.NAME = name
        self.RAW = raw
        self.QUANTITY = quantity


class Skill(Property):
    def __init__(self, quantity=None):
        super().__init__("Skill", "skill", quantity)


class MinIntelligence(Property):
    def __init__(self, quantity=None):
        super().__init__("Min.Intelligence", "min_int", quantity)


class MinStrength(Property):
    def __init__(self, quantity=None):
        super().__init__("Min.Strength", "min_str", quantity)


class MinStamina(Property):
    def __init__(self, quantity=None):
        super().__init__("Min.Stamina", "min_sta", quantity)


class Protection(Property):
    def __init__(self, quantity=None):
        super().__init__("Protection", "prt", quantity)


class Defense(Property):
    def __init__(self, quantity=None):
        super().__init__("Defense", "def", quantity)


class BaseHit(Property):
    def __init__(self, quantity=None):
        super().__init__("Base Hit", "hit", quantity)


class Damage(Property):
    def __init__(self, quantity=None):
        super().__init__("Damage", "dam", quantity)


class Dexterity(Property):
    def __init__(self, quantity=None):
        super().__init__("Dexterity", "dex", quantity)


class Stealth(Property):
    def __init__(self, quantity=None):
        super().__init__("Stealth", "stl", quantity)
