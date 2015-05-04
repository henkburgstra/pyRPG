
import data
import decorators


class Output(object):

    HERO_SORT = ['alagos', 'luana', 'grindan', 'rydalin', 'codrif', 'galen', 'raiko',
                 'kiara', 'luthais', 'elias', 'onarr', 'duillio', 'iellwen', 'faeron']

    GEAR_SORT = ['weapon', 'shield', 'helmet', 'armor']

    STAT_SORT = ['int', 'wil', 'dex', 'edu', 'str', 'sta']

    SKILL_SORT = ['chm', 'dip', 'lor', 'mec', 'med', 'mer', 'ran', 'sci', 'stl', 'thf', 'trb', 'war',
                  'haf', 'mis', 'pol', 'shd', 'swd', 'thr']

    PROP_SORT = ['wpn_skill', 'min_int', 'min_str', 'min_sta',
                 'protection', 'defense', 'base_hit', 'damage',
                 'dexterity',
                 'stealth']

    SHOP_SORT = ['name', 'value', 'min_int', 'min_str', 'min_sta',
                 'protection', 'defense', 'base_hit', 'damage',
                 'dexterity',
                 'stealth']

    @staticmethod
    def cmd_help():
        """Deze is voor help"""
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
    def cmd_party():
        """Deze is voor party"""
        print()
        print(str(len(data.party)) + "/" + str(data.party.MAXIMUM))
        print()
        for hero_from_const_list in Output.HERO_SORT:
            for character in data.party:
                if hero_from_const_list == character.RAW:
                    print(character.NAME)
                    break
        print()

    @staticmethod
    def cmd_inventory():
        """Deze is voor inv"""
        print()
        # hero volgorde
        for hero_from_const_list in Output.HERO_SORT:
            for character in data.party:
                if hero_from_const_list == character.RAW:
                    # equipment volgorde
                    for gear_from_const_list in Output.GEAR_SORT:
                        for value in sorted(character.equipment.values(), key=lambda equipment: equipment.NAME):
                            if gear_from_const_list == value.TYPE.lower():
                                if "empty" not in value.RAW:
                                    print("{:30} {:15} x1 {}".format(value.NAME, value.TYPE, character.NAME))
        # rest van unequipped volgorde
        for gear_from_const_list in Output.GEAR_SORT:
            for value in sorted(data.inventory, key=lambda item: item.NAME):
                if gear_from_const_list == value.TYPE.lower():
                    print("{:30} {:15} x{}".format(value.NAME, value.TYPE, value.quantity))
        print()

    @staticmethod
    def cmd_heroes():
        """Deze is voor heroes"""
        print()
        for herolist_item in Output.HERO_SORT:
            for value1 in data.heroes.values():
                if herolist_item == value1.RAW:
                    available = "Available"
                    for value2 in data.party:
                        if value1.RAW == value2.RAW:
                            available = "Party member"
                            if value1.RAW == "alagos":
                                available = "Party leader"
                    print("{:10}\t{:1}\t{}".format(value1.NAME, value1.level.quantity, available))
                    break
        print()

    @staticmethod
    def cmd_pouch():
        """Deze is voor pouch"""
        print()
        if len(data.pouch) > 0:
            for item in data.pouch:
                print("{} x{}".format(item.NAME, item.quantity))
        else:
            print("Empty")
        print()

    @staticmethod
    def character(character):
        """Deze is voor hero stats"""
        print()
        print("Name: {},\tLevel: {},\tHitPoints: {}/{},\tTotal XP: {}".format(
            character.NAME, character.level.quantity, character.current_hp(), character.max_hp(), character.totalxp))
        print("Stats:")
        for stat_from_const_list in Output.STAT_SORT:
            for value in character.stats.values():
                if stat_from_const_list == value.RAW:
                    if value.extra == 0:
                        print("      {:13}: {}".format(value.NAME, value.quantity))
                    elif value.extra > 0:
                        print("      {:13}: {} (+{})".format(value.NAME, value.quantity, value.extra))
                    else:
                        print("      {:13}: {} ({})".format(value.NAME, value.quantity, value.extra))
        print("Skills:")
        for skill_from_const_list in Output.SKILL_SORT:
            for value in character.skills.values():
                if skill_from_const_list == value.RAW:
                    if value.positive_quantity():
                        if value.extra == 0:
                            print("      {:13}: {}".format(value.NAME, value.quantity))
                        elif value.extra > 0:
                            print("      {:13}: {} (+{})".format(value.NAME, value.quantity, value.extra))
                        else:
                            print("      {:13}: {} ({})".format(value.NAME, value.quantity, value.extra))
        print("Equipment:")
        for gear_from_const_list in Output.GEAR_SORT:
            for value in character.equipment.values():
                if gear_from_const_list == value.TYPE.lower():
                    if "empty" not in value.RAW:
                        print("      {:13}: {}".format(value.TYPE, value.NAME))
                    else:
                        print("      {:13}: ".format(value.TYPE))

    @staticmethod
    def gear(item):
        """Deze is voor gear stats"""
        print()
        print("{:13}: {}".format(item.TYPE, item.NAME))
        for prop_from_const_list in Output.PROP_SORT:
            for key, value in item:
                if prop_from_const_list == key.lower():
                    if value is not None:
                        print("{:13}: {}". format(key.lower().title().replace("_", "."), value))
        print()

    @staticmethod
    def _shop_count(key):
        count = data.inventory.count_item(key) + data.party.count_equipment(key)
        if count != 0:
            return count
        else:
            return ""

    @staticmethod
    def shop_list(gear, weaponskill=0):
        """Deze is voor purchaselist"""

        if gear == decorators.weapons and weaponskill == "EoCMD":
            raise ValueError

        from texttable import Texttable

        templist = []
        for key1, value1 in gear.items():
            for key2, value2 in value1.items():
                if key2 in Output.SHOP_SORT:
                    templist.append(key2)
            break
        columns = [x for x in Output.SHOP_SORT if x in templist]
        headers = [item.title().replace("_", ".") for item in columns]
        headers.append('Backpack')

        tab = Texttable()
        sortlist = []
        for key1, value1 in sorted(gear.items(), key=lambda x: x[1].sort):
            templist = []
            if value1.shop:
                if weaponskill == "EoCMD" or weaponskill == value1.skill.lower():
                    for item in columns:
                        for key2, value2 in value1.items():
                            if item == key2:
                                if value2 is None:
                                    templist.append("")
                                else:
                                    templist.append(str(value2))
                    templist.append(Output._shop_count(key1))
                    sortlist.append(templist)
        tab.add_rows(sortlist, header=False)

        tab.header(headers)

        align = []
        width = []
        align.append('l')   # vanwege owned erachter, extra kolom
        width.append(20)
        for _ in columns:
            align.append('r')
            width.append(10)
        tab.set_cols_align(align)
        tab.set_cols_width(width)

        print()
        print(tab.draw())
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
