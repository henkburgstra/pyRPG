
from items.gear import Gear


class Necklace(Gear):
    def __init__(self, name, raw, sort, value, shop, weight, prt):
        super().__init__(name, raw, sort, value, shop)
        self.WEIGHT = weight
        self.PROTECTION = prt

    @staticmethod
    def factory(necklace_dict):
        return Necklace(necklace_dict.name,
                        necklace_dict.raw,
                        necklace_dict.sort,
                        necklace_dict.value,
                        necklace_dict.shop,
                        necklace_dict.weight,
                        necklace_dict.protection)
