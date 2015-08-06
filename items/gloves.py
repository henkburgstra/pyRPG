
from items.gear import Gear


class Gloves(Gear):
    def __init__(self, name, value, shop, weight, prt):
        super().__init__(name, value, shop)
        self.WEIGHT = weight
        self.PROTECTION = prt

    @staticmethod
    def factory(gloves_dict):
        return Gloves(gloves_dict.name,
                      gloves_dict.value,
                      gloves_dict.shop,
                      gloves_dict.weight,
                      gloves_dict.protection)
