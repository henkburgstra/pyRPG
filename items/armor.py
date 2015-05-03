

from items.gear import Gear


class Armor(Gear):
    def __init__(self, name, value, shop, min_stamina, protection, dexterity, stealth):
        super().__init__(name, value, shop)
        self.MIN_STA = min_stamina
        self.PROTECTION = protection
        self.DEXTERITY = dexterity
        self.STEALTH = stealth

    @staticmethod
    def factory(armor_dict):
        return Armor(armor_dict.name,
                     armor_dict.value,
                     armor_dict.shop,
                     armor_dict.min_sta,
                     armor_dict.protection,
                     armor_dict.dexterity,
                     armor_dict.stealth)

