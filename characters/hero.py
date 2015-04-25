

from characters.character import Character
import output


class Hero(Character):
    def __init__(self, name, sort, level, totalxp, stats, skills, equipment):
        super().__init__(name,       level,         stats, skills, equipment)
        self.SORT = sort
        self._totalxp = totalxp
        self._output = output.Output()

    def count_equipment(self, gear_raw):
        """Deze is voor shop count"""
        for key, value in self._equipment.items():
            if value.RAW == gear_raw:
                return 1
        return 0

    def show_equipment(self):
        """Deze is voor inv"""
        self._output.character_inventory(self.NAME, "1", self._equipment.values())

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
                if (item.MIN_INTELLIGENCE.QUANTITY is not None and item.MIN_INTELLIGENCE.QUANTITY > self._stats.int.quantity) or \
                   (item.MIN_STRENGTH.QUANTITY is not None and item.MIN_STRENGTH.QUANTITY > self._stats.str.quantity) or \
                   (item.MIN_STAMINA.QUANTITY is not None and item.MIN_STAMINA.QUANTITY > self._stats.sta.quantity) or \
                   (self._get_skill(item.__class__.__name__, item.SKILL.QUANTITY) < 1):
                        self._output.not_equipping(self.NAME, item.NAME)
                        return False
                self._equipment[key] = item
                if verbose:
                    self._output.is_equipping(self.NAME, item.NAME)
                return True

    def _get_skill(self, skill, skill_type):
        if skill == "Weapon":
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
        elif skill == "Shield":
            return self._skills.shd.quantity
        else:
            return 1

    def show_hero_stats(self):
        """ Deze is voor hero stats"""
        self.stats_update()
        self._output.character(self.NAME, self.level, self.current_hp(), self.max_hp(), self._totalxp,
                               self._stats.values(), self._skills.values(), self._equipment.values())

    # def level_up(self):
    #     self._level += 1

    # def die(self, message="Game over!"):
    #     print(message)
    #     self._health = 0
    #     self._dead = True
    #     input()
