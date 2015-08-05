
from items.gear import Gear


class Boots(Gear):
    def __init__(self, name, value, shop, weight, prt):
        super().__init__(name, value, shop)
        self.WEIGHT = weight
        self.PROTECTION = prt

    @staticmethod
    def factory(boots_dict):
        return Boots(boots_dict.name,
                     boots_dict.value,
                     boots_dict.shop,
                     boots_dict.weight,
                     boots_dict.protection)
