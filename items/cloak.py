
from items.gear import Gear


class Cloak(Gear):
    def __init__(self, name, raw, sort, value, shop, weight, protection, stealth, thief):
        super().__init__(name, raw, sort, value, shop)
        self.WEIGHT = weight
        self.PROTECTION = protection
        self.STEALTH = stealth
        self.THIEF = thief

    @staticmethod
    def factory(cloak_dict):
        return Cloak(cloak_dict.name,
                     cloak_dict.raw,
                     cloak_dict.sort,
                     cloak_dict.value,
                     cloak_dict.shop,
                     cloak_dict.weight,
                     cloak_dict.protection,
                     cloak_dict.stealth,
                     cloak_dict.thief)
