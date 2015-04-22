

class Item(object):
    def __init__(self, name):
        self.NAME = name
        self.RAW = name.strip().lower().replace(" ", "")
        self._quantity = 1

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        self._quantity = quantity

    quantity = property(get_quantity, set_quantity)
