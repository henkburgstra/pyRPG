
class Output(object):

    @staticmethod
    def cmd_help():
        print()
        print("Possible commands:")
        print()
        print('help         []')
        print('exit         []')
        print('cls          []')
        print('party        []')
        print('stats        [hero_name_in_party/gear_name_without_spaces]')
        print('inventory    []')
        print('pouch        []')
        print("find         [quantity] [gold/herbs/spices]")
        print("purchaselist [weapons/shields/armors] ([weaponskill: sword/hafted/pole/missile/thrown])")
        print("purchase     ([quantity]) [gear_name_without_spaces]")
        print("sell         ([quantity]) [gear_name_without_spaces]")
        print("equip        [hero_name_in_party] [gear_name_without_spaces]")
        print("unequip      [hero_name_in_party] [weapon/shield/armor]")
        print('heroes       []')
        print("join         [hero_name_outside_party]")
        print("leave        [hero_name_in_party]")
        print()

    @staticmethod
    def party(party_size, party_maximum, party):
        """Deze is voor party"""
        print()
        print(str(party_size) + "/" + str(party_maximum))
        print()
        for character in sorted(party, key=lambda name: name.SORT):
            print(character.NAME)
        print()

    @staticmethod
    def pouch(volume, inventory):
        """Deze is voor pouch"""
        print()
        if volume > 0:
            for item in inventory:
                print("{} x{}".format(item.NAME, item.quantity))
        else:
            print("Empty")
        print()

    @staticmethod
    def is_equipping(character_name, item_name):
        """Deze is voor sell, equip en unequip"""
        print("{} is equipping {}.".format(character_name, item_name))

    @staticmethod
    def not_equipping_skl(character_name, item_name):
        """Deze is voor equip"""
        print("{} doesn't have the skill to equip that {}.".format(character_name, item_name))

    @staticmethod
    def not_equipping_int(character_name, item_name, needed_intelligence):
        """Deze is voor equip"""
        print("{} needs {} intelligence to equip that {}.".format(character_name, needed_intelligence, item_name))

    @staticmethod
    def not_equipping_str(character_name, item_name, needed_strength):
        """Deze is voor equip"""
        print("{} needs {} strength to equip that {}.".format(character_name, needed_strength, item_name))

    @staticmethod
    def not_equipping_sta(character_name, item_name, needed_stamina):
        """Deze is voor equip"""
        print("{} needs {} stamina to equip that {}.".format(character_name, needed_stamina, item_name))

    @staticmethod
    def add_item(item_quantity, item_name, inventory_name):
        """Deze is voor find, purchase, sell, equip en unequip"""
        print("Put {} {} in {}.".format(item_quantity, item_name, inventory_name))

    @staticmethod
    def remove_item(item_quantity, item_name, inventory_name):
        """Deze is voor sell en equip"""
        print("Removed {} {} from {}.".format(item_quantity, item_name, inventory_name))

    @staticmethod
    def quantity_not_enough(item_name, item_price, item_quantity):
        """Deze is voor purchase"""
        print("Not enough {}.".format(item_name))
        print("You need {} more {}.".format(item_price - item_quantity, item_name))

    @staticmethod
    def error_quantity_not_enough():
        """Deze is voor sell en equip"""
        print("Item quantity not in container.")

    @staticmethod
    def no_item():
        """Deze is voor sell en equip"""
        print("Item not in container.")

    @staticmethod
    def quantity_less_than_one():
        """Deze is voor find, purchase, sell, equip en unequip"""
        print("That is not possible.")

    @staticmethod
    def character_join_party(character_name, party_name):
        """Deze is voor join"""
        print("{} joined {}.".format(character_name, party_name))

    @staticmethod
    def character_double_join(character_name, party_name):
        """Deze is voor join"""
        print("{} is already in {}.".format(character_name, party_name))

    @staticmethod
    def character_full_party(party_name):
        """Deze is voor join"""
        print("{} is full.".format(party_name))

    @staticmethod
    def character_leave_party(character_name, party_name):
        """Deze is voor leave"""
        print("{} left {}.".format(character_name, party_name))

    @staticmethod
    def leader_not_leave_party():
        """Deze is voor leave"""
        print("The party leader cannot leave his own party!")

    @staticmethod
    def character_inventory(character_name, item_quantity, character_equipment):
        """Deze is voor inv"""
        print()
        for value in sorted(character_equipment, key=lambda equipment: equipment.SORT):
            if "empty" not in value.RAW:
                print("{:30} {:15} x{} {}".format(value.NAME, value.TYPE, item_quantity, character_name))

    @staticmethod
    def backpack_inventory(inventory):
        """Deze is voor inv"""
        print()
        for value in sorted(inventory, key=lambda item: (item.SORT, item.NAME)):
            print("{:30} {:15} x{}".format(value.NAME, value.TYPE, value.quantity))
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
