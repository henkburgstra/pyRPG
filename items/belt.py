
from items.gear import Gear


class Belt(Gear):
    def __init__(self, name, raw, sort, value, shop, weight, prt):
        super().__init__(name, raw, sort, value, shop)
        self.WEIGHT = weight
        self.PROTECTION = prt

    @staticmethod
    def factory(belt_dict):
        return Belt(belt_dict.name,
                    belt_dict.raw,
                    belt_dict.sort,
                    belt_dict.value,
                    belt_dict.shop,
                    belt_dict.weight,
                    belt_dict.protection)
