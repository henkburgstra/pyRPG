

from items import Item


class Gear(Item):
    def __init__(self, name, value, shop):
        super().__init__(name)
        self.VALUE = value
        self.SHOP = shop

        self.SKILL = None

        self.MIN_INTELLIGENCE = None
        self.MIN_STRENGTH = None
        self.MIN_STAMINA = None

        self.PROTECTION = None
        self.DEFENSE = None
        self.BASE_HIT = None
        self.DAMAGE = None

        self.DEXTERITY = 0
        self.STEALTH = None

    def show_gear(self):
        """Deze is voor hero stats"""
        if "empty" not in self.RAW:
            print("      {:13}: {}".format(self.__class__.__name__, self.NAME))
        else:
            print("      {:13}: ".format(self.__class__.__name__))

    def show_gear_stats(self):
        """Deze is voor gear stats"""
        print()
        print("{:18}: {}".format(self.__class__.__name__, self.NAME))
        if self.SKILL is not None:
            print("Skill             : {}".format(self.SKILL))
        if self.MIN_INTELLIGENCE is not None:
            print("Min.Intelligence  : {}".format(self.MIN_INTELLIGENCE))
        if self.MIN_STRENGTH is not None:
            print("Min.Strength      : {}".format(self.MIN_STRENGTH))
        if self.MIN_STAMINA is not None:
            print("Min.Stamina       : {}".format(self.MIN_STAMINA))
        if self.PROTECTION is not None:
            print("Protection        : {}".format(self.PROTECTION))
        if self.DEFENSE is not None:
            print("Defense           : {}".format(self.DEFENSE))
        if self.BASE_HIT is not None:
            print("Base Hit          : {}".format(self.BASE_HIT))
        if self.DAMAGE is not None:
            print("Damage            : {}".format(self.DAMAGE))
        if self.DEXTERITY != 0:
            print("Dexterity         : {}".format(self.DEXTERITY))
        if self.STEALTH is not None:
            print("Stealth           : {}".format(self.STEALTH))
        print()
