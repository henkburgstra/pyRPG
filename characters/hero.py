

from characters.character import Character
from output import Output


class Hero(Character):
    def __init__(self, name, level, totalxp, stats, skills, equipment):
        super().__init__(name, level,         stats, skills, equipment)
        self.xpremaining = 0
        self.totalxp = totalxp

    @property
    def nextlevel(self):
        return int((250 / 3) * (2 * self.level.quantity ** 3 +
                                9 * self.level.quantity ** 2 +
                                13 * self.level.quantity + 6) - self.totalxp)

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
        if item.MIN_STA is not None and item.MIN_STA > self.stats.sta.quantity:
            Output.not_equipping_sta(self.NAME, item.NAME, item.MIN_STA)
            return True
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

    # def level_up(self):
    #     self.level += 1

    # def die(self, message="Game over!"):
    #     print(message)
    #     self._health = 0
    #     self._dead = True
    #     input()
