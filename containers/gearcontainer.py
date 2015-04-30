
from containers.container import Container
from output import Output


class GearContainer(Container):

    def get_item(self, gear_raw):
        """Deze is dubbel met __getitem__, maar dat is nodig vanwege de key.
        Wordt gebruikt in add. Dat lukte helaas niet met __getitem__"""
        for item in self:
            if item.RAW == gear_raw:
                return item

    def count_item(self, gear_raw):
        """Deze is voor shop count"""
        for item in self:
            if item.RAW == gear_raw:
                return item.quantity
        return 0

    def show_content(self):
        """Deze is voor inv"""
        Output.backpack_inventory(self)

    def add(self, gear, quantity=1, verbose=True):
        """Deze is voor purchase, equip en unequip"""
        if quantity < 1:
            Output.quantity_less_than_one()
            raise ValueError
        if "empty" in gear.RAW:
            return

        if gear in self:
            # self[gear].quantity += quantity
            self.get_item(gear.RAW).quantity += quantity
        else:
            self[gear] = gear                                 # self[gear] bestaat uit zichzelf al uit quantity = 1
            # self[gear].quantity += quantity - 1
            self.get_item(gear.RAW).quantity += quantity - 1  # dus daarom, wanneer nieuw: plus - 1

        if verbose:
            Output.add_item(quantity, gear.NAME, self.NAME)

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
