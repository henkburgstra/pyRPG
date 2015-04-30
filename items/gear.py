

from items.item import Item

from items import WeaponSkill
from items import MinIntelligence
from items import MinStrength
from items import MinStamina
from items import Protection
from items import Defense
from items import BaseHit
from items import Damage
from items import Dexterity
from items import Stealth

from output import Output


class Gear(Item):
    def __init__(self, name, value, shop):
        super().__init__(name)
        self.VALUE = value
        self.SHOP = shop

        self.WPN_SKILL = WeaponSkill()

        self.MIN_INTELLIGENCE = MinIntelligence()
        self.MIN_STRENGTH = MinStrength()
        self.MIN_STAMINA = MinStamina()

        self.PROTECTION = Protection()
        self.DEFENSE = Defense()
        self.BASE_HIT = BaseHit()
        self.DAMAGE = Damage()

        self.DEXTERITY = Dexterity()
        self.STEALTH = Stealth()

    def show_gear(self):
        """Deze is voor hero stats"""
        Output.equipment(self.RAW, self.TYPE, self.NAME)

    def show_gear_stats(self):
        """Deze is voor gear stats"""
        Output.gear(self.TYPE, self.NAME, self.WPN_SKILL,
                    self.MIN_INTELLIGENCE, self.MIN_STRENGTH, self.MIN_STAMINA,
                    self.PROTECTION, self.DEFENSE, self.BASE_HIT, self.DAMAGE,
                    self.DEXTERITY,
                    self.STEALTH)
