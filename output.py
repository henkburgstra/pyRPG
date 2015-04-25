
class Output(object):

    @staticmethod
    def is_equipping(character_name, item_name):
        """Deze is voor sell, equip en unequip"""
        print("{} is equipping {}.".format(character_name, item_name))

    @staticmethod
    def inventory(item_name, item_type, item_quantity, character_name):
        """Deze is voor inv"""
        print("{:30} {:15} x{} {}".format(item_name, item_type, item_quantity, character_name))

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
