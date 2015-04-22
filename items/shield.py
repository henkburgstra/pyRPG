

from items import Gear


class Shield(Gear):
    def __init__(self, name, value, shop, min_strength, protection, defense, dexterity, stealth):
        self.SORT = 2
        super().__init__(name, value, shop)
        self.MIN_STRENGTH = min_strength
        self.PROTECTION = protection
        self.DEFENSE = defense
        self.DEXTERITY = dexterity
        self.STEALTH = stealth

    @staticmethod
    def factory(properties):
        return Shield(properties['name'], properties['value'], properties['shop'], properties['min_str'],
                      properties['protection'], properties['defense'], properties['dexterity'], properties['stealth'])

