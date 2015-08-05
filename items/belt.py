
from items.gear import Gear


class Belt(Gear):
    def __init__(self, name, value, shop, weight, prt):
        super().__init__(name, value, shop)
        self.WEIGHT = weight
        self.PROTECTION = prt

    @staticmethod
    def factory(belt_dict):
        return Belt(belt_dict.name,
                    belt_dict.value,
                    belt_dict.shop,
                    belt_dict.weight,
                    belt_dict.protection)
