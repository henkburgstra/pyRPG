
from containers.container import Container
from output import Output


class SmallContainer(Container):

    def remove(self, item, price):
        """Deze is voor purchase"""
        if price < 1:
            Output.quantity_less_than_one()
            return False
        if item not in self:
            Output.quantity_not_enough(item.NAME, price, item.quantity - 1)
            return False
        elif self[item.RAW].quantity < price:
            Output.quantity_not_enough(item.NAME, price, item.quantity)
            return False
        else:
            self[item.RAW].quantity -= price
            return True
