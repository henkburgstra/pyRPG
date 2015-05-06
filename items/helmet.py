
from items.gear import Gear


class Helmet(Gear):
    def __init__(self, name, value, shop, weight, protection):
        super().__init__(name, value, shop)
        self.WEIGHT = weight
        self.PROTECTION = protection

    @staticmethod
    def factory(helmet_dict):
        return Helmet(helmet_dict.name,
                      helmet_dict.value,
                      helmet_dict.shop,
                      helmet_dict.weight,
                      helmet_dict.protection)
