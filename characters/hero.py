

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
    def weight(self):
        total = 0
        for equipment_item in self.equipment.values():
            if equipment_item.WEIGHT is not None:
                total += equipment_item.WEIGHT
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
        for equipment_item in self.equipment.values():
            if equipment_item.PROTECTION is not None:
                total += equipment_item.PROTECTION
        return total

    def gain_experience(self, xp):
        """Deze is voor xp"""
        if xp < 1:
            Output.quantity_less_than_one()
            raise ValueError

        if self.level.quantity < self.level.MAXIMUM:
            self.xpremaining += xp
            self.totalxp += xp
            Output.character_gain_xp(self.NAME, xp)

        while self.level.next(self.totalxp) <= 0:
            self.level.quantity += 1
            self.level.current += 1
            Output.character_gain_level(self.NAME, self.level.quantity)

    def count_equipment(self, gear_raw):
        """Deze is voor shop count"""
        for equipment_item in self.equipment.values():
            if equipment_item.RAW == gear_raw:
                return 1
        return 0

    def get_same_type_from_equipment(self, item):
        """Deze is voor equip"""
        for equipment_type, equipment_item in self.equipment.items():
            if isinstance(equipment_item, type(item)):
                return self.equipment[equipment_type]  # equipment_type, bijv: 'clk'

    def get_equipment(self, gear_raw):
        """Deze is voor stats, sell en unequip"""
        for equipment_item in self.equipment.values():
            if equipment_item.RAW == gear_raw or \
                    (equipment_item.TYPE == gear_raw.title() and "empty" not in equipment_item.RAW):
                return equipment_item

    def set_equipment(self, item, verbose=True):
        """Deze is voor sell, equip en unequip"""
        for equipment_type, equipment_item in self.equipment.items():
            if isinstance(equipment_item, type(item)):
                if self._is_unable_to_equip(item):
                    return False
                self.equipment[equipment_type] = item
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
        """Deze is voor startup en sell, equip en unequip"""
        self._set_dex()
        self._set_agi()
        self._set_skills()
        self._set_total()

    def _set_dex(self):
        self.stats.dex.extra = 0
        for equipment_item in self.equipment.values():
            if equipment_item.DEXTERITY is not None:
                self.stats.dex.extra += equipment_item.DEXTERITY
        self.stats.dex.total = self.stats.dex.quantity + self.stats.dex.extra

    def _set_agi(self):
        self.stats.agi.extra = -round(self.weight / 3)
        self.stats.agi.total = self.stats.agi.quantity + self.stats.agi.extra

    def _set_skills(self):
        for skill in self.skills.values():
            skill.extra = 0
            for equipment_item in self.equipment.values():
                if skill.NAME.upper() in equipment_item:
                    if equipment_item[skill.NAME.upper()] is not None:
                        skill.extra += equipment_item[skill.NAME.upper()]
            skill.total = skill.quantity + skill.extra

        # dit hierboven vervangt hieronder * alle skills
        # if equipment_item.STEALTH is not None:
        #     self.skills.stl.extra += equipment_item.STEALTH
        # if equipment_item.THIEF is not None:
        #     self.skills.thf.extra += equipment_item.THIEF

    def _set_total(self):
        for hero_stat in self.stats.values():
            if hero_stat.total < 1:  # het origineel uit vb.net is < 0, klopt dat?
                hero_stat.total = 1
        for hero_skill in self.skills.values():
            if hero_skill.total < 0 or hero_skill.quantity <= 0:
                hero_skill.total = 0
            # visueel aanpassen als het negatieve van de item groter is dan de skill van de hero
            if hero_skill.extra < 0 and hero_skill.extra < -hero_skill.quantity and hero_skill.quantity > 0:
                hero_skill.extra = -hero_skill.quantity

    # def level_up(self):
    #     self.level += 1

    # def die(self, message="Game over!"):
    #     print(message)
    #     self._health = 0
    #     self._dead = True
    #     input()
