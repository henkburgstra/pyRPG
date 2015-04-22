

from util import DotDict


class Character(object):
    def __init__(self, name, level, stats, skills, equipment):
        self.NAME = name
        self.RAW = name.strip().lower().replace(" ", "")
        self._level = level
        self._stats = DotDict(stats)
        self._skills = DotDict(skills)
        self._equipment = DotDict(equipment)

        # self._dead = False

    @property
    def stats(self):
        return self._stats

    @property
    def level(self):
        return self._level.quantity

    def stats_update(self):
        self.set_dex()

    def current_hp(self):
        return self._level.current + self._stats.sta.current + self._stats.edu.current

    def max_hp(self):
        return self._level.quantity + self._stats.sta.quantity + self._stats.edu.quantity

    def set_dex(self):
        for value in self._equipment.values():
            self._stats.dex.extra += value.DEXTERITY
        self._stats.dex.total = self._stats.dex.quantity + self._stats.dex.extra

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
