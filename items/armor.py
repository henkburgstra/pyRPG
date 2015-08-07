

from items.gear import Gear


class Armor(Gear):
    def __init__(self, name, raw, value, shop, weight, protection, stealth):
        super().__init__(name, raw, value, shop)
        self.WEIGHT = weight
        self.PROTECTION = protection
        self.STEALTH = stealth

    @staticmethod
    def factory(armor_dict):
        return Armor(armor_dict.name,
                     armor_dict.raw,
                     armor_dict.value,
                     armor_dict.shop,
                     armor_dict.weight,
                     armor_dict.protection,
                     armor_dict.stealth)
