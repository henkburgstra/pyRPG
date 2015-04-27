

import data


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


def cmd_exit():
    quit("Thanks for playing!")
    # player.die("Thanks for playing!")


def cmd_cls():
    import os

    if os.name == "posix":
        os.system("clear")
    elif os.name in ("nit", "dos", "ce", "nt"):
        os.system("CLS")
    else:
        print('\n' * 100)


def cmd_party():
    data.party.show_members()


def cmd_stats(*params):
    try:
        data.party[params[0]].show_hero_stats()
    except KeyError:
        try:
            item = data.inventory[params[0]]
            item.show_gear_stats()
        except KeyError:
            try:
                hero = data.party.get_member_with_this_equipment(params[0])
                item = hero.get_equipment(params[0])
                item.show_gear_stats()
            except AttributeError:
                print('stats [hero_name_in_party/gear_name_without_spaces]')


def cmd_inventory():
    data.party.show_equipment()
    data.inventory.show_content()


def cmd_pouch():
    data.pouch.show_content()


def cmd_find(*params):
    try:
        data.pouch.add(data.pouchitems[params[1]], int(params[0]))
    except (KeyError, ValueError):
        print("find [quantity] [gold/herbs/spices]")


def cmd_purchaselist(*params):

    from decorators import weapons, shields, helmets, armors

    if params[0] == "weapons" and params[1] in ("sword", "hafted", "pole", "missile", "thrown"):
        print()
        print("{:30}{:13}{:15}{:14}{:17}{:13}{}".format("Name", "Value", "Min.Int", "Min.Str", "Base Hit", "Damage",
                                                                                                           "Quantity"))
        print()
        for key, value in sorted(weapons.items(), key=lambda weapon: weapon[1].sort):
            if value.shop and value.skill.lower() == params[1]:
                print("{:20}{:15}{:15}{:15}{:15}{:15}{:15}".format(value.name,
                                                                   value.value,
                                                                   value.min_int if value.min_int is not None
                                                                   else "",
                                                                   value.min_str if value.min_str is not None
                                                                   else "",
                                                                   value.base_hit,
                                                                   value.damage,
                                                                   shop_count(key)))
        print()

    elif params[0] == "shields":
        print()
        print("{:30}{:13}{:12}{:18}{:13}{:17}{:14}{}".format("Name", "Value", "Min.Str", "Protection", "Defense",
                                                                              "Dexterity", "Stealth", "Quantity"))
        print()
        for key, value in sorted(shields.items(), key=lambda shield: shield[1].sort):
            if value.shop:
                print("{:20}{:15}{:15}{:15}{:15}{:15}{:15}{:15}".format(value.name,
                                                                        value.value,
                                                                        value.min_str,
                                                                        value.protection,
                                                                        value.defense,
                                                                        value.dexterity,
                                                                        value.stealth,
                                                                        shop_count(key)))
        print()

    elif params[0] == "helmets":
        shop_list(helmets)

    elif params[0] == "armors":
        shop_list(armors)
        # print()
        # print("{:30}{:13}{:12}{:16}{:17}{:14}{}".format("Name", "Value", "Min.Sta", "Protection", "Dexterity",
        #                                                                             "Stealth", "Quantity"))
        # print()
        # for key, value in sorted(armors.items(), key=lambda armor: armor[1].sort):
        #     if value.shop:
        #         print("{:20}{:15}{:15}{:15}{:15}{:15}{:15}".format(value.name,
        #                                                            value.value,
        #                                                            value.min_sta,
        #                                                            value.protection,
        #                                                            value.dexterity,
        #                                                            value.stealth,
        #                                                            shop_count(key)))
        # print()

    else:
        print("purchaselist [weapons/shields/helmets/armors] ([weaponskill: sword/hafted/pole/missile/thrown])")


def shop_list(gear):

    from tabulate import tabulate
    from terminaltables import AsciiTable
    from texttable import Texttable

    sortlist = ['name', 'value', 'min_int', 'min_str', 'min_sta', 'protection', 'defense', 'base_hit', 'damage', 'dexterity', 'stealth']

    templist = []
    print()
    for key1, value1 in gear.items():
        for key2, value2 in value1.items():
            if key2 in sortlist:
                templist.append(key2)
        break
    sortlist = [x for x in sortlist if x in templist]
    caplist = [item.title().replace("_", ".") for item in sortlist]

    tab = Texttable()
    templist = []
    for key1, value1 in sorted(gear.items(), key=lambda x: x[1].sort):
        for item in sortlist:
            for key2, value2 in value1.items():
                if item == key2:
                    templist.append(str(value2))

    # for i in range(1,11):
    #     templist.append([i,i**2,i**3])

    tab.add_rows(templist)
    tab.set_cols_align(['r', 'r', 'r', 'r'])
    tab.header(caplist)
    print(tab.draw())


    # w = next(iter([x for x in gear[next(iter(y for y in gear))]]))

    # y = [x.keys() for x in gear.values()]
    # print(y)

    # for value in gear.values():
    #     for key in value.keys():
    #         if key not in sortlist:
    #             del value[key]
    return

    print(tabulate(sorted(gear.values(), key=lambda x: x.sort), headers=next(iter(gear.values())), tablefmt="rst"))

    return

    sortlist = ['min_int', 'min_str', 'min_sta', 'protection', 'defense', 'base_hit', 'damage', 'dexterity', 'stealth']
    templist = []
    print()
    for key1, value1 in gear.items():
        for key2, value2 in value1.items():
            if key2 in sortlist:
                templist.append(key2)
        break
    sortlist = [x for x in sortlist if x in templist]
    caplist = [item.title().replace("_", ".") for item in sortlist]
    print("{:30}{:15}{:15}{:5}{}".format("Name", "Value", "\t\t\t".join(caplist), "", "Quantity"))
    print()
    for key, value in sorted(gear.items(), key=lambda x: x[1].sort):

        templist = []
        for item in sortlist:
            for key2, value2 in value.items():
                if item == key2:
                    templist.append(str(value2))

        if value.shop:
            print("{:20}{:15}{:15}{:15}{:5}{}".format(value.name, value.value,
                                                      "", "\t\t\t\t ".join(templist),
                                                      "", shop_count(key)))
    print()



def cmd_purchase(*params):

    from decorators import weapons, shields, helmets, armors
    from items import Weapon, Shield, Helmet, Armor

    try:
        if params[1] == "EoCMD":
            gear_raw = params[0]
            quantity = 1
        else:
            gear_raw = params[1]
            quantity = int(params[0])

        item = None
        if gear_raw in weapons:
            item = Weapon.factory(weapons[gear_raw])
        if gear_raw in shields:
            item = Shield.factory(shields[gear_raw])
        if gear_raw in helmets:
            item = Helmet.factory(helmets[gear_raw])
        if gear_raw in armors:
            item = Armor.factory(armors[gear_raw])

        if item.SHOP:
            if data.pouch.remove(data.pouchitems.gold, item.VALUE * quantity):
                print("Purchased {} {} for {} gold.".format(quantity, item.NAME, item.VALUE * quantity))
                data.inventory.add(item, quantity)
    except (AttributeError, ValueError):
        print("purchase ([quantity]) [gear_name_without_spaces]")


def cmd_sell(*params):
    try:
        if params[1] == "EoCMD":
            item = data.inventory[params[0]]
            quantity = 1
        else:
            item = data.inventory[params[1]]
            quantity = int(params[0])

        data.inventory.remove(item, quantity)
        data.pouch.add(data.pouchitems.gold, int((item.VALUE * quantity) / 2))
    except (KeyError, AttributeError, ValueError):
        try:
            hero = data.party.get_member_with_this_equipment(params[0])
            item = hero.get_equipment(params[0])
            empty_item = create_empty_gear(params[0].lower())

            hero.set_equipment(empty_item, False)
            print("Sold {}.".format(item.NAME))
            print("{} was equipped by {}.".format(item.NAME, hero.NAME))
            data.pouch.add(data.pouchitems.gold, int(item.VALUE / 2))
        except (AttributeError, ValueError):
            print("sell ([quantity]) [gear_name_without_spaces]")


def cmd_equip(*params):
    try:
        hero = data.party[params[0]]
        item = data.inventory[params[1]]
        equipped_item = hero.get_same_type_equipment_of(item)

        if hero.set_equipment(item):
            data.inventory.add(equipped_item)
            data.inventory.remove(item, verbose=False)
    except (KeyError, AttributeError):
        print("equip [hero_name_in_party] [gear_name_without_spaces]")


def cmd_unequip(*params):
    try:
        hero = data.party[params[0]]
        empty_item = create_empty_gear(params[1].lower())
        equipped_item = hero.get_same_type_equipment_of(empty_item)

        data.inventory.add(equipped_item)
        hero.set_equipment(empty_item, False)
    except (KeyError, AttributeError):
        print("unequip [hero_name_in_party] [weapon/shield/helmet/armor]")


def cmd_heroes():
    print()
    for ext_hero in sorted(data.heroes.values(), key=lambda x: x.SORT):   # extern
        available = "Available"
        for int_hero in data.party:                                       # intern
            if ext_hero == int_hero:
                available = "Party member"
                if int_hero == data.heroes.alagos:
                    available = "Party leader"
                break
        print("{:10}\t{}\t{}".format(ext_hero.NAME, ext_hero.level, available))
    print()


def cmd_join(*params):
    try:
        data.party.add(data.heroes[params[0]])
    except KeyError:
        print("join [hero_name_outside_party]")


def cmd_leave(*params):
    try:
        data.party.remove(data.heroes[params[0]])
    except KeyError:
        print("leave [hero_name_in_party]")


def run_command(cmd, *params):
    if cmd == 'help':
        cmd_help()
    elif cmd in ('exit', 'quit'):
        cmd_exit()
    elif cmd in ('cls', 'clear'):
        cmd_cls()
    elif cmd == 'party':
        cmd_party()
    elif cmd == 'stats':
        cmd_stats(*params)
    elif cmd in ('backpack', 'inventory', 'inv'):
        cmd_inventory()
    elif cmd == 'pouch':
        cmd_pouch()
    elif cmd == 'find':
        cmd_find(*params)
    elif cmd in ('purchaselist', 'shoplist'):
        cmd_purchaselist(*params)
    elif cmd in ('purchase', 'shop'):
        cmd_purchase(*params)
    elif cmd == 'sell':
        cmd_sell(*params)
    elif cmd == 'equip':
        cmd_equip(*params)
    elif cmd == 'unequip':
        cmd_unequip(*params)
    elif cmd == 'heroes':
        cmd_heroes()
    elif cmd == 'join':
        cmd_join(*params)
    elif cmd == 'leave':
        cmd_leave(*params)


def yes_or_no(prompt="(Y/N)?"):
    while True:
        answer = input(prompt)
        answer = answer.strip()
        answer = answer.lower()

        if answer in ('yes', 'y', 'ye'):
            return True
        elif answer in ('no', 'n', 'nope'):
            return False
        else:
            continue


def create_empty_gear(gear_type):

        from items import Weapon, Shield, Helmet, Armor
        from decorators import weapons, shields, helmets, armors

        # 2 verschillende mogelijk van gear_type, eentje komt van sell en de ander van unequip

        if gear_type == "weapon" or gear_type in weapons:
            return Weapon.factory(weapons.emptyweapon)
        elif gear_type == "shield" or gear_type in shields:
            return Shield.factory(shields.emptyshield)
        elif gear_type == "helmet" or gear_type in helmets:
            return Helmet.factory(helmets.emptyhelmet)
        elif gear_type == "armor" or gear_type in armors:
            return Armor.factory(armors.emptyarmor)


def shop_count(key):
    count = data.inventory.count_item(key) + data.party.count_equipment(key)
    if count != 0:
        return count
    else:
        return ""