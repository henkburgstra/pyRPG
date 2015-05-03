
from containers.container import Container
from output import Output


class SmallContainer(Container):

    def __getitem__(self, key):
        return self.inside[key.RAW]

    def add(self, item, quantity, verbose=True):
        """Deze is voor find en sell"""
        if quantity < 1:
            Output.quantity_less_than_one()
            raise ValueError
        if item in self:
            self[item].quantity += quantity
        else:
            self[item] = item                    # self[item] bestaat uit zichzelf al uit quantity = 1
            self[item].quantity += quantity - 1  # dus daarom, wanneer hij voor het eerst wordt toegevoegd: - 1
        if verbose:
            Output.add_item(quantity, item.NAME, self.NAME)

    def remove(self, item, price):
        """Deze is voor purchase"""
        if price < 1:
            Output.quantity_less_than_one()
            return False
        if item not in self:
            Output.quantity_not_enough(item.NAME, price, item.quantity - 1)
            return False
        elif self[item].quantity < price:
            Output.quantity_not_enough(item.NAME, price, item.quantity)
            return False
        else:
            self[item].quantity -= price
            return True