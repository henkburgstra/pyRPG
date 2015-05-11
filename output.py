
import data


class Output(object):

    HERO_SORT = ['alagos', 'luana', 'grindan', 'rydalin', 'codrif', 'galen', 'raiko',
                 'kiara', 'luthais', 'elias', 'onarr', 'duillio', 'iellwen', 'faeron']

    GEAR_SORT = ['weapon', 'shield', 'helmet', 'armor', 'cloak']

    STAT_SORT = ['int', 'wil', 'dex', 'agi', 'edu', 'str', 'sta']

    SKILL_SORT = ['chm', 'dip', 'lor', 'mec', 'med', 'mer', 'ran', 'sci', 'stl', 'thf', 'trb', 'war',
                  'haf', 'mis', 'pol', 'shd', 'swd', 'thr']

    PROP_SORT = ['wpn_skill', 'min_int', 'min_str', 'weight',
                 'protection', 'defense', 'base_hit', 'damage',
                 'intelligence', 'willpower', 'dexterity',
                 'diplomat', 'loremaster', 'scientist', 'stealth', 'thief', 'warrior']

    SHOP_SORT = ['name', 'value', 'min_int', 'min_str', 'weight',
                 'protection', 'defense', 'base_hit', 'damage',
                 'intelligence', 'willpower', 'dexterity',
                 'diplomat', 'loremaster', 'scientist', 'stealth', 'thief', 'warrior']

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
        print("purchaselist [weapons/shields/helmets/armors/cloaks]")
        print("purchase     ([quantity]) [gear_name_without_spaces]")
        print("sell         ([quantity]) [gear_name_without_spaces]")
        print("equip        [hero_name_in_party] [gear_name_without_spaces]")
        print("unequip      [hero_name_in_party] [weapon/shield/armor/cloak]")
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
        for hero_raw in Output.HERO_SORT:
            hero = data.heroes[hero_raw]
            if hero in data.party:
                print(hero.NAME)
        print()

    @staticmethod
    def cmd_inventory():
        """Deze is voor inv"""
        print()
        # hero volgorde
        for hero_raw in Output.HERO_SORT:
            for character in data.party:
                if hero_raw == character.RAW:
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
                    if "empty" not in value.RAW:
                        print("{:30} {:15} x{}".format(value.NAME, value.TYPE, value.quantity))
        print()

    @staticmethod
    def cmd_heroes():
        """Deze is voor heroes"""
        print()
        for hero_raw in Output.HERO_SORT:
            hero = data.heroes[hero_raw]
            available = "Available"
            if hero in data.party:
                available = "Party member"
            if hero.RAW == "alagos":
                available = "Party leader"
            print("{:10}\t{:1}\t{}".format(hero.NAME, hero.level.quantity, available))
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
        print("Name: {},\tLevel: {},\tHitPoints: {}/{}".format(
            character.NAME, character.level.quantity, character.current_hp, character.max_hp))
        print()
        print("      XP Remaining : {}".format(character.xpremaining))
        print("      Total XP     : {}".format(character.totalxp))
        print("      Next Level   : {}".format(character.nextlevel))
        print()
        print("      Weight       : {}".format(character.weight))
        print("      Movepoints   : {}\t\t({})".format(character.own_movepoints, character.total_movepoints))
        if character.skills.shd.quantity > 0:
            print("      Protection   : {}\t\t({})".format(character.protection, character.equipment.shd.PROTECTION))
        else:
            print("      Protection   : {}".format(character.protection))
        print("      Defense      : {}".format(character.equipment.shd.DEFENSE))
        if character.skills.war.quantity > 0 and "empty" not in character.equipment.wpn.RAW:
            print("      Base Hit     : {}%\t(+{}%)".format(character.equipment.wpn.BASE_HIT, character.warrior_hit))
        else:
            print("      Base Hit     : {}%".format(character.equipment.wpn.BASE_HIT))
        print("      Damage       : {}".format(character.equipment.wpn.DAMAGE))
        print()
        print("Stats:")
        for stat_from_const_list in Output.STAT_SORT:
            for value in character.stats.values():
                if stat_from_const_list == value.RAW:
                    if value.extra == 0:
                        print("      {:13}: {}".format(value.NAME, value.quantity))
                    elif value.extra > 0:
                        print("      {:13}: {}\t\t(+{})".format(value.NAME, value.quantity, value.extra))
                    else:
                        print("      {:13}: {}\t\t({})".format(value.NAME, value.quantity, value.extra))
        print("Skills:")
        for skill_from_const_list in Output.SKILL_SORT:
            for value in character.skills.values():
                if skill_from_const_list == value.RAW:
                    if value.positive_quantity():
                        if value.extra == 0:
                            print("      {:13}: {}".format(value.NAME, value.quantity))
                        elif value.extra > 0:
                            print("      {:13}: {}\t\t(+{})".format(value.NAME, value.quantity, value.extra))
                        else:
                            print("      {:13}: {}\t\t({})".format(value.NAME, value.quantity, value.extra))
        print("Equipment:")
        for gear_from_const_list in Output.GEAR_SORT:
            for value in character.equipment.values():
                if gear_from_const_list == value.TYPE.lower():
                    if "empty" not in value.RAW:
                        print("      {:13}: {}".format(value.TYPE, value.NAME))
                    else:
                        print("      {:13}: ".format(value.TYPE))
        print()

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
        templist = []
        for key1, value1 in gear.items():
            for key2, value2 in value1.items():
                if key2 in Output.SHOP_SORT:
                    templist.append(key2)
            break
        columns = [x for x in Output.SHOP_SORT if x in templist]
        headers = [item.title().replace("_", ".") for item in columns]
        headers.append('Backpack')

        sortlist = []
        for value in sorted(gear.values(), key=lambda x: x.sort):
            templist = []
            if value.shop:
                if weaponskill == "EoCMD" or weaponskill == value.skill.lower():
                    for item in columns:
                        if item in value:
                            if value[item] is None:  # or value1[item] == 0:
                                templist.append("")   # uitgezet, want het is op dit moment niet per se nodig.
                            else:
                                templist.append(str(value[item]))
                    templist.append(Output._shop_count(value.raw))
                    sortlist.append(templist)

        from texttable import Texttable
        tab = Texttable()
        tab.add_rows(sortlist, header=False)
        tab.header(headers)
        align = []
        width = []
        align.append('l')   # vanwege owned erachter, extra kolom
        width.append(20)
        for _ in columns:
            align.append('r')
            width.append(12)
        tab.set_cols_align(align)
        tab.set_cols_width(width)

        print()
        print(tab.draw())
        print()

    @staticmethod
    def buy(item_quantity, item_name, item_value):
        """Deze is voor purchase"""
        print("Purchased {} {} for {} gold.".format(item_quantity, item_name, item_value * item_quantity))

    @staticmethod
    def sold1(item_name):
        """Deze is voor sell"""
        print("Sold {}.".format(item_name))

    @staticmethod
    def sold2(item_name, character_name):
        """Deze is voor sell"""
        print("{} was equipped by {}.".format(item_name, character_name))

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
