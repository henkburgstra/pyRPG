

from items import Gear


class Armor(Gear):
    def __init__(self, name, value, shop, min_stamina, protection, dexterity, stealth):
        self.SORT = 3
        super().__init__(name, value, shop)
        self.MIN_STAMINA = min_stamina
        self.PROTECTION = protection
        self.DEXTERITY = dexterity
        self.STEALTH = stealth

    @staticmethod
    def factory(properties):
        return Armor(properties['name'], properties['value'], properties['shop'], properties['min_sta'],
                     properties['protection'], properties['dexterity'], properties['stealth'], )

