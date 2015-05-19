

class Item(object):
    def __init__(self, name):
        self.NAME = name
        self.RAW = name.strip().lower().replace(" ", "")
        self.TYPE = self.__class__.__name__
        self.quantity = 1


class PouchItem(Item):
    pass


class Gear(Item):
    def __init__(self, name, value, shop):
        super().__init__(name)
        self.VALUE = value
        self.SHOP = shop

        self.WPN_SKILL = None

        self.MIN_INT = None
        self.MIN_STR = None
        self.WEIGHT = None

        self.PROTECTION = None
        self.DEFENSE = None
        self.BASE_HIT = None
        self.DAMAGE = None

        self.INTELLIGENCE = None
        self.WILLPOWER = None
        self.DEXTERITY = None
        self.DIPLOMAT = None
        self.LOREMASTER = None
        self.SCIENTIST = None
        self.STEALTH = None
        self.THIEF = None
        self.WARRIOR = None

    # def __iter__(self):   # niet meer nodig volgens mij
    #     """Hiermee kun je door bovenstaande variabelen loopen"""
    #     for key, value in self.__dict__.items():
    #         yield key, value
