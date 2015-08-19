
import data


class Output(object):

    HERO_SORT = ['alagos', 'luana', 'grindan', 'rydalin', 'codrif', 'galen', 'raiko',
                 'kiara', 'luthais', 'elias', 'onarr', 'duilio', 'iellwen', 'faeron']

    STAT_SORT = ['int', 'wil', 'dex', 'agi', 'edu', 'str', 'sta']

    SKILL_SORT = ['chm', 'dip', 'lor', 'mec', 'med', 'mer', 'ran', 'sci', 'stl', 'thf', 'trb', 'war',
                  'haf', 'mis', 'pol', 'shd', 'swd', 'thr']

    GEAR_SORT = ['wpn', 'shd', 'hlm', 'nlc', 'arm', 'clk', 'glv', 'blt', 'bts', 'acy']
    INV_SORT = ['weapon', 'shield', 'helmet', 'necklace', 'armor', 'cloak', 'gloves', 'belt', 'boots', 'accessory']
    DECO_SORT = ['weapons', 'shields', 'helmets', 'necklaces', 'armors', 'cloaks', 'gloves', 'belts', 'boots',
                                                                                                      'accessories']

    WPN_SORT = ['sword', 'hafted', 'pole', 'missile', 'thrown']

    BASE_SORT = ['min_int', 'min_str', 'weight', 'movepoints',
                 'protection', 'defense', 'base_hit', 'damage',
                 'intelligence', 'willpower', 'dexterity',
                 'diplomat', 'loremaster', 'ranger', 'scientist', 'stealth', 'thief', 'warrior']

    PROP_SORT = ['wpn_skill'] + BASE_SORT

    SHOP_SORT = ['name', 'value'] + BASE_SORT

    @staticmethod
    def cmd_help():
        """Deze is voor help"""
        print()
        print("Possible commands:")
        print()
        print('help         []')
        print('exit         []')
        print('cls          []')
        print('reset        []')
        print('save         [name_savegame]')
        print('load         [name_savegame]')
        print('party        []')
        print('stats        [hero_name_in_party/gear_name_without_spaces]')
        print('inventory    []')
        print('pouch        []')
        print("find         [quantity] [gold/herbs/spices]")
        print("xp           [hero_name_in_party] [quantity]")
        print("purchaselist [{}]".format("/".join(Output.DECO_SORT)))
        print("purchase     ([quantity]) [gear_name_without_spaces]")
        print("sell         ([quantity]) [gear_name_without_spaces]")
        print("equip        [hero_name_in_party] [gear_name_without_spaces]")
        print("unequip      [hero_name_in_party] [{}]".format("/".join(Output.INV_SORT)))
        print('heroes       []')
        print("join         [hero_name_outside_party]")
        print("leave        [hero_name_in_party]")
        print()

    @staticmethod
    def cmd_save():
        """Deze is voor save"""
        print("Saving gamedata...")

    @staticmethod
    def cmd_load():
        """Deze is voor load"""
        print("Loading gamedata...")

    @staticmethod
    def cmd_party():
        """Deze is voor party
        Mag weg, vervangen door de gui."""
        print()
        print(str(len(data.party))+"/"+str(data.party.MAXIMUM))
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
            hero = data.heroes[hero_raw]
            if hero in data.party:
                # equipment volgorde
                for gear_group in Output.GEAR_SORT:
                    equipment_item = hero.equipment[gear_group]
                    if "empty" not in equipment_item.RAW:
                        print("{:30} {:15} x1 {}".format(equipment_item.NAME, equipment_item.TYPE, hero.NAME))
        # rest van unequipped volgorde
        for gear_group in Output.INV_SORT:
            for inventory_item in sorted(data.inventory, key=lambda x: x.NAME):
                if gear_group == inventory_item.TYPE.lower():
                    if "empty" not in inventory_item.RAW:
                        print("{:30} {:15} x{}".format(
                            inventory_item.NAME, inventory_item.TYPE, inventory_item.quantity))
        print()

    @staticmethod
    def cmd_heroes():
        """Deze is voor heroes
        Mag weg, vervangen door de gui."""
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
        print("      XP Remaining : {}".format(character.experience.remaining))
        if character.level.quantity >= character.level.MAXIMUM:
            totalxp = "Max"
            nextlevel = "Max"
        else:
            totalxp = character.experience.total
            nextlevel = character.level.next(character.experience.total)
        print("      Total XP     : {}".format(totalxp))
        print("      Next Level   : {}".format(nextlevel))
        print()
        print("      Weight       : {}".format(character.weight))
        print("      Movepoints   : {}\t\t({})".format(character.own_movepoints, character.total_movepoints))
        if character.skills.shd.positive_quantity():
            print("      Protection   : {}\t\t({})".format(character.protection, character.equipment.shd.PROTECTION))
        else:
            print("      Protection   : {}".format(character.protection))
        print("      Defense      : {}".format(character.equipment.shd.DEFENSE))
        curr_wpn = character.equipment.wpn
        if character.skills.war.positive_quantity() and "empty" not in curr_wpn.RAW:
            print("      Base Hit     : {}%\t(+{}%)".format(curr_wpn.BASE_HIT,
                                                            character.skills.war.bonus(curr_wpn.BASE_HIT)))
        else:
            print("      Base Hit     : {}%".format(curr_wpn.BASE_HIT))
        print("      Damage       : {}".format(curr_wpn.DAMAGE))
        print()
        print("Stats:")
        for stat_type_raw in Output.STAT_SORT:
            stat = character.stats[stat_type_raw]
            if stat.extra == 0:
                print("      {:13}: {}".format(stat.NAME, stat.quantity))
            elif stat.extra > 0:
                print("      {:13}: {}\t\t(+{})".format(stat.NAME, stat.quantity, stat.extra))
            else:
                print("      {:13}: {}\t\t({})".format(stat.NAME, stat.quantity, stat.extra))
        print("Skills:")
        for skill_type_raw in Output.SKILL_SORT:
            skill = character.skills[skill_type_raw]
            if skill.positive_quantity():
                if skill.extra == 0:
                    print("      {:13}: {}".format(skill.NAME, skill.quantity))
                elif skill.extra > 0:
                    print("      {:13}: {}\t\t(+{})".format(skill.NAME, skill.quantity, skill.extra))
                else:
                    print("      {:13}: {}\t\t({})".format(skill.NAME, skill.quantity, skill.extra))
        print("Equipment:")
        for gear_group in Output.GEAR_SORT:
            equipment_item = character.equipment[gear_group]
            if "empty" not in equipment_item.RAW:
                print("      {:13}: {}".format(equipment_item.TYPE, equipment_item.NAME))
            else:
                print("      {:13}: ".format(equipment_item.TYPE))
        print()

    @staticmethod
    def gear(item):
        """Deze is voor gear stats"""
        print()
        print("{:13}: {}".format(item.TYPE, item.NAME))
        for gear_property_name in Output.PROP_SORT:
            gear_property_value = getattr(item, gear_property_name.upper())
            if gear_property_value is not None:
                print("{:13}: {}". format(gear_property_name.title().replace("_", "."), gear_property_value))
        print()

    @staticmethod
    def _shop_count(key):
        count = data.inventory.count_item(key) + data.party.count_equipment(key)
        if count != 0:
            return count
        else:
            return ""

    @staticmethod
    def shop_list(all_gear, weaponskill=0):
        """Deze is voor purchaselist"""
        columns = []
        for gear_item in Output.SHOP_SORT:
            if gear_item in next(iter(all_gear.values())):
                columns.append(gear_item)
        headers = [item.title().replace("_", ".") for item in columns]
        headers.append('Backpack')

        sortlist = []
        for gear_item in sorted(all_gear.values(), key=lambda x: x.sort):
            templist = []
            if gear_item.shop:
                if weaponskill == "EoCMD" or weaponskill == gear_item.skill.lower():
                    for column_name in columns:
                        if column_name in gear_item:
                            if gear_item[column_name] is None:  # or value1[item] == 0:
                                templist.append("")   # uitgezet, want het is op dit moment niet per se nodig.
                            else:
                                templist.append(str(gear_item[column_name]))
                    templist.append(Output._shop_count(gear_item.raw))
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
    def character_gain_xp(character_name, xp):
        """Deze is voor xp"""
        print("{} earned {} XP.".format(character_name, xp))

    @staticmethod
    def character_gain_level(character_name, character_level):
        """Deze is voor xp"""
        print("{} went up to level {}!".format(character_name, character_level))

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
