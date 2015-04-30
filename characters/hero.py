

from characters.character import Character
from output import Output


class Hero(Character):
    def __init__(self, name, sort, level, totalxp, stats, skills, equipment):
        super().__init__(name,       level,         stats, skills, equipment)
        self.SORT = sort
        self._totalxp = totalxp

    def count_equipment(self, gear_raw):
        """Deze is voor shop count"""
        for key, value in self._equipment.items():
            if value.RAW == gear_raw:
                return 1
        return 0

    def show_equipment(self):
        """Deze is voor inv"""
        Output.character_inventory(self.NAME, "1", self._equipment.values())

    def get_same_type_equipment_of(self, item):
        """Deze is voor equip en unequip"""
        for key, value in self._equipment.items():
            if isinstance(value, type(item)):
                return self._equipment[key]

    def get_equipment(self, gear_raw):
        """Deze is voor sell en stats"""
        for value in self._equipment.values():
            if value.RAW == gear_raw:
                if "empty" not in value.RAW:
                    return value

    def set_equipment(self, item, verbose=True):
        """Deze is voor sell, equip en unequip"""
        for key, value in self._equipment.items():
            if isinstance(value, type(item)):
                if self._is_unable_to_equip(item):
                    return False
                self._equipment[key] = item
                self.stats_update()
                if verbose:
                    Output.is_equipping(self.NAME, item.NAME)
                return True

    def _is_unable_to_equip(self, item):
        if self._get_skill(item.TYPE, item.WPN_SKILL.QUANTITY) < 1:
            Output.not_equipping_skl(self.NAME, item.NAME)
            return True
        if item.MIN_INTELLIGENCE.QUANTITY is not None and item.MIN_INTELLIGENCE.QUANTITY > self._stats.int.quantity:
            Output.not_equipping_int(self.NAME, item.NAME, item.MIN_INTELLIGENCE.QUANTITY)
            return True
        if item.MIN_STRENGTH.QUANTITY is not None and item.MIN_STRENGTH.QUANTITY > self._stats.str.quantity:
            Output.not_equipping_str(self.NAME, item.NAME, item.MIN_STRENGTH.QUANTITY)
            return True
        if item.MIN_STAMINA.QUANTITY is not None and item.MIN_STAMINA.QUANTITY > self._stats.sta.quantity:
            Output.not_equipping_sta(self.NAME, item.NAME, item.MIN_STAMINA.QUANTITY)
            return True
        return False

    def _get_skill(self, item_type, skill_type):
        if item_type == "Weapon":
            if skill_type == "Sword":
                return self._skills.swd.quantity
            elif skill_type == "Hafted":
                return self._skills.haf.quantity
            elif skill_type == "Pole":
                return self._skills.pol.quantity
            elif skill_type == "Missile":
                return self._skills.mis.quantity
            elif skill_type == "Thrown":
                return self._skills.thr.quantity
            else:
                return 1    # vanwege "Empty" skill
        elif item_type == "Shield":
            return self._skills.shd.quantity
        else:
            return 1

    def show_hero_stats(self):
        """ Deze is voor hero stats"""
        Output.character(self.NAME, self.level, self.current_hp(), self.max_hp(), self._totalxp,
                         self._stats.values(), self._skills.values(), self._equipment.values())

    # def level_up(self):
    #     self._level += 1

    # def die(self, message="Game over!"):
    #     print(message)
    #     self._health = 0
    #     self._dead = True
    #     input()
