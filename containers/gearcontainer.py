
from containers.container import Container


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
        self._output.backpack_inventory(self)

    def add(self, gear, quantity=1, verbose=True):
        """Deze is voor purchase, equip en unequip"""
        if quantity < 1:
            self._output.quantity_less_than_one()
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
            self._output.add_item(quantity, gear.NAME, self.NAME)

    def remove(self, gear, quantity=1, verbose=True):
        """Deze is voor sell en equip"""
        if gear not in self:
            self._output.no_item()
            raise AttributeError
        if quantity < 1:
            self._output.quantity_less_than_one()
            raise ValueError

        if gear.quantity > quantity:
            gear.quantity -= quantity
        elif gear.quantity == quantity:
            del self[gear]
        else:
            self._output.error_quantity_not_enough()
            raise ValueError

        if verbose:
            self._output.remove_item(quantity, gear.NAME, self.NAME)
