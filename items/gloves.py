
from items.gear import Gear


class Gloves(Gear):
    def __init__(self, name, raw, sort, value, shop, weight, prt):
        super().__init__(name, raw, sort, value, shop)
        self.WEIGHT = weight
        self.PROTECTION = prt

    @staticmethod
    def factory(gloves_dict):
        return Gloves(gloves_dict.name,
                      gloves_dict.raw,
                      gloves_dict.sort,
                      gloves_dict.value,
                      gloves_dict.shop,
                      gloves_dict.weight,
                      gloves_dict.protection)
