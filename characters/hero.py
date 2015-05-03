

from characters.character import Character
from output import Output


class Hero(Character):
    def __init__(self, name, level, totalxp, stats, skills, equipment):
        super().__init__(name, level,         stats, skills, equipment)
        self.totalxp = totalxp

    def count_equipment(self, gear_raw):
        """Deze is voor shop count"""
        for key, value in self.equipment.items():
            if value.RAW == gear_raw:
                return 1
        return 0

    def get_same_type_equipment_of(self, item):
        """Deze is voor equip en unequip"""
        for key, value in self.equipment.items():
            if isinstance(value, type(item)):
                return self.equipment[key]

    def get_equipment(self, gear_raw):
        """Deze is voor sell en stats"""
        for value in self.equipment.values():
            if value.RAW == gear_raw:
                if "empty" not in value.RAW:
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
        if self._get_skill(item.TYPE, item.WPN_SKILL.QUANTITY) < 1:
            Output.not_equipping_skl(self.NAME, item.NAME)
            return True
        if item.MIN_INTELLIGENCE.QUANTITY is not None and item.MIN_INTELLIGENCE.QUANTITY > self.stats.int.quantity:
            Output.not_equipping_int(self.NAME, item.NAME, item.MIN_INTELLIGENCE.QUANTITY)
            return True
        if item.MIN_STRENGTH.QUANTITY is not None and item.MIN_STRENGTH.QUANTITY > self.stats.str.quantity:
            Output.not_equipping_str(self.NAME, item.NAME, item.MIN_STRENGTH.QUANTITY)
            return True
        if item.MIN_STAMINA.QUANTITY is not None and item.MIN_STAMINA.QUANTITY > self.stats.sta.quantity:
            Output.not_equipping_sta(self.NAME, item.NAME, item.MIN_STAMINA.QUANTITY)
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
    #     self._level += 1

    # def die(self, message="Game over!"):
    #     print(message)
    #     self._health = 0
    #     self._dead = True
    #     input()
