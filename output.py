
class Output(object):

    @staticmethod
    def partymembers(party_size, party_maximum, party):
        """Deze is voor party"""
        print()
        print(str(party_size) + "/" + str(party_maximum))
        print()
        for character in sorted(party, key=lambda name: name.SORT):
            print(character.NAME)
        print()

    @staticmethod
    def is_equipping(character_name, item_name):
        """Deze is voor sell, equip en unequip"""
        print("{} is equipping {}.".format(character_name, item_name))

    @staticmethod
    def item_removed(item_quantity, item_name, inventory_name):
        """Deze is voor sell en equip"""
        print("Removed {} {} from {}.".format(item_quantity, item_name, inventory_name))

    @staticmethod
    def character_inventory(character_name, item_quantity, character_equipment):
        """Deze is voor inv"""
        print()
        for value in sorted(character_equipment, key=lambda equipment: equipment.SORT):
            if "empty" not in value.RAW:
                print("{:30} {:15} x{} {}".format(value.NAME, value.__class__.__name__, item_quantity, character_name))
        print()

    @staticmethod
    def backpack_inventory(inventory):
        """Deze is voor inv"""
        print()
        for value in sorted(inventory, key=lambda item: (item.SORT, item.NAME)):
            print("{:30} {:15} x{}".format(value.NAME, value.__class__.__name__, value.quantity))
        print()

    @staticmethod
    def stat(stat_name, stat_quantity, stat_extra):
        """Deze is voor hero stats"""
        if stat_extra == 0:
            print("      {:13}: {}".format(stat_name, stat_quantity))
        elif stat_extra > 0:
            print("      {:13}: {} (+{})".format(stat_name, stat_quantity, stat_extra))
        else:
            print("      {:13}: {} ({})".format(stat_name, stat_quantity, stat_extra))

    @staticmethod
    def equipment(item_raw, item_type, item_name):
        """Deze is voor hero stats"""
        if "empty" not in item_raw:
            print("      {:13}: {}".format(item_type, item_name))
        else:
            print("      {:13}: ".format(item_type))

    @staticmethod
    def character(character_name, character_level, character_current_hp, character_max_hp, character_totalxp,
                  character_stats, character_skills, character_equipment):
        """Deze is voor hero stats"""
        print()
        print("Name: {},\tLevel: {},\tHitPoints: {}/{},\tTotal XP: {}".format(
            character_name, character_level, character_current_hp, character_max_hp, character_totalxp))

        print("Stats:")
        for value in sorted(character_stats, key=lambda stat: stat.SORT):
            value.show_stat()

        print("Skills:")
        for value in sorted(character_skills, key=lambda skill: (skill.SORT, skill.NAME)):
            if value.positive_quantity():
                value.show_stat()

        print("Equipment:")
        for value in sorted(character_equipment, key=lambda equipment: equipment.SORT):
            value.show_gear()

    @staticmethod
    def gear(item_type, item_name, *args):
        """Deze is voor gear stats"""
        print()
        print("{:18}: {}".format(item_type, item_name))
        for prop in args:
            if prop.QUANTITY is not None:
                print("{:18}: {}". format(prop.NAME, prop.QUANTITY))
        print()
