

from util import DotDict


class Character(object):
    def __init__(self, name, level, stats, skills, equipment):
        self.NAME = name
        self.RAW = name.strip().lower().replace(" ", "")
        self.level = level
        self.stats = DotDict(stats)
        self.skills = DotDict(skills)
        self.equipment = DotDict(equipment)

        # self._dead = False

    def stats_update(self):
        self._set_dex()
        self._set_stealth()
        self._set_total()

    def current_hp(self):
        return self.level.current + self.stats.sta.current + self.stats.edu.current

    def max_hp(self):
        return self.level.quantity + self.stats.sta.quantity + self.stats.edu.quantity

    def _set_dex(self):
        self.stats.dex.extra = 0
        for value in self.equipment.values():
            if value.DEXTERITY.QUANTITY is not None:
                self.stats.dex.extra += value.DEXTERITY.QUANTITY
        self.stats.dex.total = self.stats.dex.quantity + self.stats.dex.extra

    def _set_stealth(self):
        self.skills.stl.extra = 0
        for value in self.equipment.values():
            if value.STEALTH.QUANTITY is not None:
                self.skills.stl.extra += value.STEALTH.QUANTITY
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

    # @staticmethod
    # def make_car_sound():
    #     print('Vrooom')

    # def attack(self, other):
    #     pass

    # def is_dead(self):
    #     return self._dead

    # def update(self):
    #     if self._health <= 0:
    #         self._health = 0
    #         self._dead = True

    # def take_damage(self, damage):
    #     self._health -= damage
    #     self.is_dead()
