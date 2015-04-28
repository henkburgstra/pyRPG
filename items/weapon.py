

from items.gear import Gear

from items import WeaponSkill
from items import MinIntelligence
from items import MinStrength
from items import BaseHit
from items import Damage


class Weapon(Gear):
    def __init__(self, name, value, shop, wpn_skill, min_intelligence, min_strength, base_hit, damage):
        self.SORT = 1
        super().__init__(name, value, shop)
        self.WPN_SKILL = WeaponSkill(wpn_skill)
        self.MIN_INTELLIGENCE = MinIntelligence(min_intelligence)
        self.MIN_STRENGTH = MinStrength(min_strength)
        self.BASE_HIT = BaseHit(base_hit)
        self.DAMAGE = Damage(damage)
        # self.minDMG = damage[0]
        # self.maxDMG = damage[1]

    # def damage(self):
    #     return randint(self.minDMG, self.maxDMG)

    @staticmethod
    def factory(weapon_dict):
        return Weapon(weapon_dict.name,
                      weapon_dict.value,
                      weapon_dict.shop,
                      weapon_dict.skill,
                      weapon_dict.min_int,
                      weapon_dict.min_str,
                      weapon_dict.base_hit,
                      weapon_dict.damage)


# class WeaponEnchanted(Weapon):
#     def __init__(self, name, value, skill, base_hit, damage, effects, equipped_by=None):
#         self.effects = effects
#         super().__init__(name, value, skill, base_hit, damage, equipped_by)
