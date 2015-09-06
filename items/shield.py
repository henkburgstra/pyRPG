

from items.gear import Gear


class Shield(Gear):
    def __init__(self, name, raw, sort, col, row, value, shop, min_strength, protection, defense, dexterity, stealth):
        super().__init__(name, raw, sort, value, shop)
        self.BMP = 'resources/icons/gear/shield2.png'
        self.COL = col
        self.ROW = row
        self.MIN_STR = min_strength
        self.PROTECTION = protection
        self.DEFENSE = defense
        self.DEXTERITY = dexterity
        self.STEALTH = stealth

    @staticmethod
    def factory(shield_dict):
        return Shield(shield_dict.name,
                      shield_dict.raw,
                      shield_dict.sort,
                      shield_dict.col,
                      shield_dict.row,
                      shield_dict.value,
                      shield_dict.shop,
                      shield_dict.min_str,
                      shield_dict.protection,
                      shield_dict.defense,
                      shield_dict.dexterity,
                      shield_dict.stealth)
