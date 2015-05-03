
from items.gear import Gear

from items import MinStamina
from items import Protection


class Helmet(Gear):
    def __init__(self, name, value, shop, min_stamina, protection):
        super().__init__(name, value, shop)
        self.MIN_STAMINA = MinStamina(min_stamina)
        self.PROTECTION = Protection(protection)

    @staticmethod
    def factory(helmet_dict):
        return Helmet(helmet_dict.name,
                      helmet_dict.value,
                      helmet_dict.shop,
                      helmet_dict.min_sta,
                      helmet_dict.protection)

