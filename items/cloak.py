
from items.gear import Gear


class Cloak(Gear):
    def __init__(self, name, value, shop, weight, protection, stealth, thief):
        super().__init__(name, value, shop)
        self.WEIGHT = weight
        self.PROTECTION = protection
        self.STEALTH = stealth
        self.THIEF = thief

    @staticmethod
    def factory(cloak_dict):
        return Cloak(cloak_dict.name,
                     cloak_dict.value,
                     cloak_dict.shop,
                     cloak_dict.weight,
                     cloak_dict.protection,
                     cloak_dict.stealth,
                     cloak_dict.thief)
