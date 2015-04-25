
from containers.container import Container


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
        self._output.party(len(self), self.MAXIMUM, self)

    def add(self, character, verbose=True):
        """Deze is voor join"""
        if character in self:
            self._output.character_double_join(character.NAME, self.NAME)
        elif len(self) < self.MAXIMUM:
            self[character] = character
            if verbose:
                self._output.character_join_party(character.NAME, self.NAME)
        else:
            self._output.character_full_party(self.NAME)

    def remove(self, character):
        """Deze is voor leave"""
        if character.RAW == 'alagos':
            self._output.leader_not_leave_party()
        elif character in self:
            self._output.character_leave_party(character.NAME, self.NAME)
            del self[character]
        else:
            raise KeyError
