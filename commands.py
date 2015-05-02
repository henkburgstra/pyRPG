

import data
from output import Output


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
        shop_list(weapons, params[1])
    elif params[0] == "shields":
        shop_list(shields, 0)
    elif params[0] == "helmets":
        shop_list(helmets, 0)
    elif params[0] == "armors":
        shop_list(armors, 0)
    else:
        print("purchaselist [weapons/shields/helmets/armors] ([weaponskill: sword/hafted/pole/missile/thrown])")


def shop_list(gear, weaponskill):

    from texttable import Texttable

    columns = ['name', 'value', 'min_int', 'min_str', 'min_sta',
               'protection', 'defense', 'base_hit', 'damage',
               'dexterity', 'stealth']

    print()

    templist = []
    for key1, value1 in gear.items():
        for key2, value2 in value1.items():
            if key2 in columns:
                templist.append(key2)
        break
    columns = [x for x in columns if x in templist]
    headers = [item.title().replace("_", ".") for item in columns]
    headers.append('Backpack')

    tab = Texttable()
    sortlist = []
    for key1, value1 in sorted(gear.items(), key=lambda x: x[1].sort):
        templist = []
        if value1.shop:
            if weaponskill == 0 or weaponskill == value1.skill.lower():
                for item in columns:
                    for key2, value2 in value1.items():
                        if item == key2:
                            if value2 is None:
                                templist.append("")
                            else:
                                templist.append(str(value2))
                templist.append(shop_count(key1))
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

    # tab.set_deco(Texttable.HEADER | Texttable.VLINES | Texttable.BORDER)
    print(tab.draw())
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
        Output.cmd_help()
    elif cmd in ('exit', 'quit'):
        cmd_exit()
    elif cmd in ('cls', 'clear'):
        cmd_cls()
    elif cmd == 'party':
        Output.cmd_party()
    elif cmd == 'stats':
        cmd_stats(*params)
    elif cmd in ('backpack', 'inventory', 'inv'):
        Output.cmd_inventory()
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
        Output.cmd_heroes()
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