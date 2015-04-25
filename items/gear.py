

from items import Item
import output


class Gear(Item):
    def __init__(self, name, value, shop):
        super().__init__(name)
        self.VALUE = value
        self.SHOP = shop

        self.SKILL = None

        self.MIN_INTELLIGENCE = None
        self.MIN_STRENGTH = None
        self.MIN_STAMINA = None

        self.PROTECTION = None
        self.DEFENSE = None
        self.BASE_HIT = None
        self.DAMAGE = None

        self.DEXTERITY = None
        self.STEALTH = None

        self._output = output.Output()

    def show_gear(self):
        """Deze is voor hero stats"""
        self._output.equipment(self.RAW, self.__class__.__name__, self.NAME)

    def show_gear_stats(self):
        """Deze is voor gear stats"""
        self._output.gear(self.__class__.__name__, self.NAME, self.SKILL,
                          self.MIN_INTELLIGENCE, self.MIN_STRENGTH, self.MIN_STAMINA,
                          self.PROTECTION, self.DEFENSE, self.BASE_HIT, self.DAMAGE,
                          self.DEXTERITY,
                          self.STEALTH)
