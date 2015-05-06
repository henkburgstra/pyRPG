

from characters.character import Character
from output import Output


class Hero(Character):
    def __init__(self, name, level, totalxp, stats, skills, equipment):
        super().__init__(name, level,         stats, skills, equipment)
        self.xpremaining = 0
        self.totalxp = totalxp

    @property
    def current_hp(self):
        """Deze is voor hero stats"""
        return self.level.current + self.stats.sta.current + self.stats.edu.current

    @property
    def max_hp(self):
        """Deze is voor hero stats"""
        return self.level.quantity + self.stats.sta.quantity + self.stats.edu.quantity

    @property
    def nextlevel(self):
        return int((250 / 3) * (2 * self.level.quantity ** 3 +
                                9 * self.level.quantity ** 2 +
                                13 * self.level.quantity + 6) - self.totalxp)

    @property
    def weight(self):
        total = 0
        for value in self.equipment.values():
            if value.WEIGHT is not None:
                total += value.WEIGHT
        return total

    @property
    def own_movepoints(self):
        return 5 + round(self.stats.sta.current / 10)

    @property
    def total_movepoints(self):
        total = round(self.own_movepoints - (self.weight / 2))
        if total < 1:
            return 1
        return total

    @property
    def protection(self):
        total = 0
        for value in self.equipment.values():
            if value.PROTECTION is not None:
                total += value.PROTECTION
        return total

    @property
    def warrior_hit(self):
        return round((47 - ((self.equipment.wpn.BASE_HIT / 10) * 5)) * (self.skills.war.total / 10))

    def count_equipment(self, gear_raw):
        """Deze is voor shop count"""
        for key, value in self.equipment.items():
            if value.RAW == gear_raw:
                return 1
        return 0

    def get_same_type_from_equipment(self, item):
        """Deze is voor equip"""
        for key, value in self.equipment.items():
            if isinstance(value, type(item)):
                return self.equipment[key]

    def get_equipment(self, gear_raw):
        """Deze is voor stats, sell en unequip"""
        for value in self.equipment.values():
            if value.RAW == gear_raw or (value.TYPE == gear_raw.title() and "empty" not in value.RAW):
                return value

    def set_equipment(self, item, verbose=True):
        """Deze is voor sell, equip en unequip"""
        for key, value in self.equipment.items():
            if isinstance(value, type(item)):
                if self._is_unable_to_equip(item):
                    return False
                self.equipment[key] = item
                self.stats_update()
                if verbose:
                    Output.is_equipping(self.NAME, item.NAME)
                return True

    def _is_unable_to_equip(self, item):
        if self._get_skill(item.TYPE, item.WPN_SKILL) < 1:
            Output.not_equipping_skl(self.NAME, item.NAME)
            return True
        if item.MIN_INT is not None and item.MIN_INT > self.stats.int.quantity:
            Output.not_equipping_int(self.NAME, item.NAME, item.MIN_INT)
            return True
        if item.MIN_STR is not None and item.MIN_STR > self.stats.str.quantity:
            Output.not_equipping_str(self.NAME, item.NAME, item.MIN_STR)
            return True
        # if item.MIN_STA is not None and item.MIN_STA > self.stats.sta.quantity:
        #     Output.not_equipping_sta(self.NAME, item.NAME, item.MIN_STA)
        #     return True
        return False

    def _get_skill(self, item_type, skill_type):
        if item_type == "Weapon":
            if skill_type == "Sword":
                return self.skills.swd.quantity
            elif skill_type == "Hafted":
                return self.skills.haf.quantity
            elif skill_type == "Pole":
                return self.skills.pol.quantity
            elif skill_type == "Missile":
                return self.skills.mis.quantity
            elif skill_type == "Thrown":
                return self.skills.thr.quantity
            else:
                return 1    # vanwege "Empty" skill
        elif item_type == "Shield":
            return self.skills.shd.quantity
        else:
            return 1

    def stats_update(self):
        """Deze is voor sell, equip en unequip"""
        self._set_dex()
        self._set_agi()
        self._set_stealth()
        self._set_total()

    def _set_dex(self):
        self.stats.dex.extra = 0
        for value in self.equipment.values():
            if value.DEXTERITY is not None:
                self.stats.dex.extra += value.DEXTERITY
        self.stats.dex.total = self.stats.dex.quantity + self.stats.dex.extra

    def _set_agi(self):
        self.stats.agi.extra = -round(self.weight / 3)
        self.stats.agi.total = self.stats.agi.quantity + self.stats.agi.extra

    def _set_stealth(self):
        self.skills.stl.extra = 0
        for value in self.equipment.values():
            if value.STEALTH is not None:
                self.skills.stl.extra += value.STEALTH
        self.skills.stl.total = self.skills.stl.quantity + self.skills.stl.extra

    def _set_total(self):
        for value in self.stats.values():
            if value.total < 1:  # het origineel uit vb.net is < 0, klopt dat?
                value.total = 1
        for value in self.skills.values():
            if value.total < 0 or value.quantity <= 0:
                value.total = 0
            if 0 > value.extra < value.quantity:
                value.extra = -value.quantity

    # def level_up(self):
    #     self.level += 1

    # def die(self, message="Game over!"):
    #     print(message)
    #     self._health = 0
    #     self._dead = True
    #     input()
