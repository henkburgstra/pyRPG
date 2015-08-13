

class Item(object):
    def __init__(self, name):
        self.NAME = name
        self.RAW = name.strip().lower().replace(" ", "")  # .replace("'", "")
        self.TYPE = self.__class__.__name__
        self.quantity = 1


class PouchItem(Item):
    pass


# class StatSkillBoosts(object):
#     def __init__(self, boostdict):
#         self.boostdict = boostdict
#
#     def get_boost(self, stat_or_skill_name):
#         if stat_or_skill_name in self.boostdict:
#             return self.boostdict[stat_or_skill_name]
#         else:
#             return 0


class Gear(Item):
    def __init__(self, name, raw, value, shop):  # , boostdict):
        super().__init__(name)
        self.RAW = raw
        self.VALUE = value
        self.SHOP = shop
        # self.boostdict = boostdict

        self.WPN_SKILL = None

        self.MIN_INT = None
        self.MIN_STR = None
        self.WEIGHT = None

        self.MOVEPOINTS = None

        self.PROTECTION = None
        self.DEFENSE = None
        self.BASE_HIT = None
        self.DAMAGE = None

        self.INTELLIGENCE = None
        self.WILLPOWER = None
        self.DEXTERITY = None

        self.DIPLOMAT = None
        self.LOREMASTER = None
        self.RANGER = None
        self.SCIENTIST = None
        self.STEALTH = None
        self.THIEF = None
        self.WARRIOR = None

    # def get_boost(self, stat_or_skill_name):
    #     return self.boostdict.get_boost(stat_or_skill_name)

    # def __iter__(self):
    #     """Hiermee kun je door bovenstaande variabelen (atributen) loopen"""
    #     for key, value in self.__dict__.items():
    #         yield key, value

    def __contains__(self, key):
        return key in self.__dict__

    def __getitem__(self, key):
        return self.__dict__[key]
