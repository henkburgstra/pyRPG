

from items.item import Item

from items import Skill
from items import MinIntelligence
from items import MinStrength
from items import MinStamina
from items import Protection
from items import Defense
from items import BaseHit
from items import Damage
from items import Dexterity
from items import Stealth

import output


class Gear(Item):
    def __init__(self, name, value, shop):
        super().__init__(name)
        self.VALUE = value
        self.SHOP = shop

        self.SKILL = Skill()

        self.MIN_INTELLIGENCE = MinIntelligence()
        self.MIN_STRENGTH = MinStrength()
        self.MIN_STAMINA = MinStamina()

        self.PROTECTION = Protection()
        self.DEFENSE = Defense()
        self.BASE_HIT = BaseHit()
        self.DAMAGE = Damage()

        self.DEXTERITY = Dexterity()
        self.STEALTH = Stealth()

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
