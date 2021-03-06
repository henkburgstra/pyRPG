

from items.gear import Gear


class Weapon(Gear):
    def __init__(self, name, raw, sort, col, row, value, shop, wpn_skill, min_intelligence, min_strength, base_hit, damage):
        super().__init__(name, raw, sort, value, shop)
        self.BMP = 'resources/icons/gear/weapon1.png'
        self.COL = col
        self.ROW = row
        self.WPN_SKILL = wpn_skill
        self.MIN_INT = min_intelligence
        self.MIN_STR = min_strength
        self.BASE_HIT = base_hit
        self.DAMAGE = damage
        # self.minDMG = damage[0]
        # self.maxDMG = damage[1]

    # def damage(self):
    #     return randint(self.minDMG, self.maxDMG)

    @staticmethod
    def factory(weapon_dict):
        return Weapon(weapon_dict.name,
                      weapon_dict.raw,
                      weapon_dict.sort,
                      weapon_dict.col,
                      weapon_dict.row,
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
