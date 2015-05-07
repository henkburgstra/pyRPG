
from items.gear import Gear


class Helmet(Gear):
    def __init__(self, name, value, shop, weight, prt, intell, wil, dip, lor, sci, war):
        super().__init__(name, value, shop)
        self.WEIGHT = weight
        self.PROTECTION = prt
        self.INTELLIGENCE = intell
        self.WILLPOWER = wil
        self.DIPLOMAT = dip
        self.LOREMASTER = lor
        self.SCIENTIST = sci
        self.WARRIOR = war

    @staticmethod
    def factory(helmet_dict):
        return Helmet(helmet_dict.name,
                      helmet_dict.value,
                      helmet_dict.shop,
                      helmet_dict.weight,
                      helmet_dict.protection,
                      helmet_dict.intelligence,
                      helmet_dict.willpower,
                      helmet_dict.diplomat,
                      helmet_dict.loremaster,
                      helmet_dict.scientist,
                      helmet_dict.warrior)
