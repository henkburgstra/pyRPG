

from items.gear import Gear

from items import MinStamina
from items import Protection
from items import Dexterity
from items import Stealth


class Armor(Gear):
    def __init__(self, name, value, shop, min_stamina, protection, dexterity, stealth):
        self.SORT = 4
        super().__init__(name, value, shop)
        self.MIN_STAMINA = MinStamina(min_stamina)
        self.PROTECTION = Protection(protection)
        self.DEXTERITY = Dexterity(dexterity)
        self.STEALTH = Stealth(stealth)

    @staticmethod
    def factory(armor_dict):
        return Armor(armor_dict.name,
                     armor_dict.value,
                     armor_dict.shop,
                     armor_dict.min_sta,
                     armor_dict.protection,
                     armor_dict.dexterity,
                     armor_dict.stealth)

