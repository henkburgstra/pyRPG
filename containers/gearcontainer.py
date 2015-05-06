
from containers.container import Container
from output import Output


class GearContainer(Container):

    def count_item(self, gear_raw):
        """Deze is voor shop count"""
        for item in self:
            if item.RAW == gear_raw:
                return item.quantity
        return 0

    def get_empty_of_this_type(self, gear_type):
        """"Deze is voor sell en unequip"""
        for item in self:
            if item.TYPE == gear_type and "empty" in item.RAW:
                return item

    def remove(self, gear, quantity=1, verbose=True):
        """Deze is voor sell en equip"""
        if gear not in self:
            Output.no_item()
            raise AttributeError
        if quantity < 1:
            Output.quantity_less_than_one()
            raise ValueError

        if gear.quantity > quantity:
            gear.quantity -= quantity
        elif gear.quantity == quantity:
            del self[gear]
        else:
            Output.error_quantity_not_enough()
            raise ValueError

        if verbose:
            Output.remove_item(quantity, gear.NAME, self.NAME)
