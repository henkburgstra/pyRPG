

from items.gear import Gear


class Accessory(Gear):
    def __init__(self, name, value, shop, weight, prt):
        super().__init__(name, value, shop)
        self.WEIGHT = weight
        self.PROTECTION = prt

    @staticmethod
    def factory(accessory_dict):
        return Accessory(accessory_dict.name,
                         accessory_dict.value,
                         accessory_dict.shop,
                         accessory_dict.weight,
                         accessory_dict.protection)
