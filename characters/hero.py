

from characters import Character


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
        for value in sorted(self._equipment.values(), key=lambda equipment: equipment.SORT):
            if "empty" not in value.RAW:
                print("{:30} {:15} x{} {}".format(value.NAME, value.__class__.__name__, "1", self.NAME))

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
                self._equipment[key] = item
        if verbose:
            print("{} is equipping {}.".format(self.NAME, item.NAME))

    def show_hero_stats(self):
        """ Deze is voor hero stats"""
        self.stats_update()
        print()
        print("Name: {},\tLevel: {},\tHitPoints: {}/{},\tTotal XP: {}".format(
            self.NAME, self.level, self.current_hp(), self.max_hp(), self._totalxp))

        print("Stats:")
        for value in sorted(self._stats.values(), key=lambda stat: stat.SORT):
            value.show_stat()

        print("Skills:")
        for value in sorted(self._skills.values(), key=lambda skill: (skill.SORT, skill.NAME)):
            if value.positive_quantity():
                value.show_skill()

        print("Equipment:")
        for value in sorted(self._equipment.values(), key=lambda equipment: equipment.SORT):
            value.show_gear()

    # def level_up(self):
    #     self._level += 1

    # def die(self, message="Game over!"):
    #     print(message)
    #     self._health = 0
    #     self._dead = True
    #     input()
