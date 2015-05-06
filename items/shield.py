

from items.gear import Gear


class Shield(Gear):
    def __init__(self, name, value, shop, min_strength, protection, defense, dexterity, stealth):
        super().__init__(name, value, shop)
        self.MIN_STR = min_strength
        self.PROTECTION = protection
        self.DEFENSE = defense
        self.DEXTERITY = dexterity
        self.STEALTH = stealth

    @staticmethod
    def factory(shield_dict):
        return Shield(shield_dict.name,
                      shield_dict.value,
                      shield_dict.shop,
                      shield_dict.min_str,
                      shield_dict.protection,
                      shield_dict.defense,
                      shield_dict.dexterity,
                      shield_dict.stealth)
