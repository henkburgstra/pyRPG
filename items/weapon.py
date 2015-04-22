

from items import Gear


class Weapon(Gear):
    def __init__(self, name, value, shop, skill, min_intelligence, min_strength, base_hit, damage):
        self.SORT = 1
        super().__init__(name, value, shop)
        self.SKILL = skill
        self.MIN_INTELLIGENCE = min_intelligence
        self.MIN_STRENGTH = min_strength
        self.BASE_HIT = base_hit
        self.DAMAGE = damage
        # self.minDMG = damage[0]
        # self.maxDMG = damage[1]

    # def damage(self):
    #     return randint(self.minDMG, self.maxDMG)

    @staticmethod
    def factory(properties):
        return Weapon(properties['name'], properties['value'], properties['shop'], properties['skill'],
                      properties['min_int'], properties['min_str'], properties['base_hit'], properties['damage'])


# class WeaponEnchanted(Weapon):
#     def __init__(self, name, value, skill, base_hit, damage, effects, equipped_by=None):
#         self.effects = effects
#         super().__init__(name, value, skill, base_hit, damage, equipped_by)
