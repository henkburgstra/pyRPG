
from containers.container import Container
from output import Output


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

    def get_member_with_this_equipment(self, gear_raw):
        """Deze is voor sell en stats"""
        for character in self:
            item = character.get_equipment(gear_raw)
            if item is not None and item.RAW == gear_raw:
                return character

    def add(self, character, verbose=True):
        """Deze is voor join"""
        if character in self:
            Output.character_double_join(character.NAME, self.NAME)
        elif len(self) < self.MAXIMUM:
            self[character] = character
            if verbose:
                Output.character_join_party(character.NAME, self.NAME)
        else:
            Output.character_full_party(self.NAME)

    def remove(self, character):
        """Deze is voor leave"""
        if character.RAW == 'alagos':
            Output.leader_not_leave_party()
        elif character in self:
            Output.character_leave_party(character.NAME, self.NAME)
            del self[character]
        else:
            raise KeyError
