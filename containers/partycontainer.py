
from containers import Container


class PartyContainer(Container):
    def __init__(self, name, maximum):
        super().__init__(name)
        self.MAXIMUM = maximum

    def count_equipment(self, gear_raw):
        """Deze is voor shop count"""
        total = 0
        for character in self:
            total += character.count_equipment(gear_raw)
        return total

    def show_equipment(self):
        """Deze is voor inv"""
        for character in sorted(self, key=lambda x: x.SORT):
            character.show_equipment()

    def get_member_with_this_equipment(self, gear_raw):
        """Deze is voor sell en stats"""
        for character in self:
            item = character.get_equipment(gear_raw)
            if item is not None and item.RAW == gear_raw:
                return character

    def show_members(self):
        """Deze is voor party"""
        print(str(len(self)) + "/" + str(self.MAXIMUM))
        for character in sorted(self, key=lambda x: x.SORT):
            print(character.NAME)

    def add(self, character, verbose=True):
        """Deze is voor join"""
        if character in self:
            print("{} is already in {}.".format(character.NAME, self.NAME))
        elif len(self) < self.MAXIMUM:
            self[character] = character
            if verbose:
                print("{} joined {}.".format(character.NAME, self.NAME))
        else:
            print("{} is full.".format(self.NAME))

    def remove(self, character):
        """Deze is voor leave"""
        if character.RAW == 'alagos':
            print("The party leader cannot leave his own party!")
        elif character in self:
            print("{} left {}.".format(character.NAME, self.NAME))
            del self[character]
