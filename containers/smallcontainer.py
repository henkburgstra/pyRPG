
from containers import Container


class SmallContainer(Container):

    def __getitem__(self, key):
        return self._inside[key.RAW]

    def show_content(self):
        """Deze is voor pouch"""
        if len(self) > 0:
            for item in self:
                print("{} x{}".format(item.NAME, item.quantity))
        else:
            print("Empty")

    def add(self, item, quantity, verbose=True):
        """Deze is voor find en sell"""
        if quantity < 1:
            print("That is not possible.")
            raise ValueError
        if item in self:
            self[item].quantity += quantity
        else:
            self[item] = item                    # self[item] bestaat uit zichzelf al uit quantity = 1
            self[item].quantity += quantity - 1  # dus daarom, wanneer hij voor het eerst wordt toegevoegd: - 1
        if verbose:
            print("Put {} {} in {}.".format(quantity, item.NAME, self.NAME))

    def remove(self, item, price):
        """Deze is voor purchase"""
        if price < 1:
            print("That is not possible.")
            return False
        if item not in self or self[item].quantity < price:
            print("Not enough {}.".format(item.NAME))
            print("You need {} more {}.".format(price - item.quantity, item.NAME))
            return False
        else:
            self[item].quantity -= price
            return True