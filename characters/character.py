

class Character(object):
    def __init__(self, name, cond, stats, skills, equipment):
        self.NAME = name
        self.RAW = name.strip().lower().replace(" ", "")
        self.level = cond.lev
        self.stats = stats
        self.skills = skills
        self.equipment = equipment

        # self._dead = False

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
