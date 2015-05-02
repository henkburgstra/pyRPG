

class Item(object):
    def __init__(self, name):
        self.NAME = name
        self.RAW = name.strip().lower().replace(" ", "")
        self.TYPE = self.__class__.__name__
        self.quantity = 1
