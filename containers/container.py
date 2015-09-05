
from output import Output


class Container(object):
    def __init__(self, name):
        self.NAME = name
        self.inside = {}

    def __len__(self):
        return len(self.inside)

    def __iter__(self):
        return iter(self.inside.values())

    def __contains__(self, key):
        return key.RAW in self.inside

    def __getitem__(self, key):
        return self.inside[key]

    def __setitem__(self, key, value):
        self.inside[key.RAW] = value

    def __delitem__(self, key):
        del self.inside[key.RAW]

    def add(self, item, quantity=1, verbose=True):
        """Deze is voor find, purchase, sell, equip en unequip"""
        if quantity < 1:
            Output.quantity_less_than_one()
            raise ValueError

        if "empty" in item.RAW and item in self:        # de eerste keer moet hij wel alle empty's toevoegen
            return                                      # maar als ze er eenmaal inzitten hoeft dat ingame niet meer

        if item in self:
            self[item.RAW].quantity += quantity
        else:
            self[item] = item                           # self[item] bestaat uit zichzelf al uit quantity = 1
            self[item.RAW].quantity += quantity - 1     # dus daarom, wanneer hij voor het eerst wordt toegevoegd: - 1
        if verbose:
            Output.add_item(quantity, item.NAME, self.NAME)
