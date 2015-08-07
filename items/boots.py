
from items.gear import Gear


class Boots(Gear):
    def __init__(self, name, raw, value, shop, weight, prt, mvp, ran, stl):
        super().__init__(name, raw, value, shop)
        self.WEIGHT = weight
        self.MOVEPOINTS = mvp
        self.PROTECTION = prt
        self.RANGER = ran
        self.STEALTH = stl

    @staticmethod
    def factory(boots_dict):
        return Boots(boots_dict.name,
                     boots_dict.raw,
                     boots_dict.value,
                     boots_dict.shop,
                     boots_dict.weight,
                     boots_dict.protection,
                     boots_dict.movepoints,
                     boots_dict.ranger,
                     boots_dict.stealth)
