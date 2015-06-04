

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
        hero = data.party[params[0]]
        Output.character(hero)
    except KeyError:
        try:
            item = data.inventory[params[0]]
            Output.gear(item)
        except KeyError:
            try:
                hero = data.party.get_member_with_this_equipment(params[0])
                item = hero.get_equipment(params[0])
                Output.gear(item)
            except AttributeError:
                print('stats [hero_name_in_party/gear_name_without_spaces]')


def cmd_find(*params):
    try:
        data.pouch.add(data.pouchitems[params[1]], int(params[0]))
    except (KeyError, ValueError):
        print("find [quantity] [gold/herbs/spices]")


def cmd_purchaselist(*params):
    try:
        if params[0] == "weapons" and params[1] not in Output.WPN_SORT:
            raise ValueError
        Output.shop_list(data.list_gear_dict[params[0]][0], params[1])
    except KeyError:
        print("purchaselist [{}]".format("/".join(Output.DECO_SORT)))
    except ValueError:
        print("purchaselist weapons [{}]".format("/".join(Output.WPN_SORT)))


def cmd_purchase(*params):
    try:
        if params[1] == "EoCMD":
            gear_raw = params[0]
            quantity = 1
        else:
            gear_raw = params[1]
            quantity = int(params[0])

        item = None
        for combo in data.list_gear_dict.values():
            if gear_raw in combo[0]:
                item = combo[1](combo[0][gear_raw])
                break

        if item.SHOP:
            if data.pouch.remove(data.pouchitems.gold, item.VALUE * quantity):
                Output.buy(quantity, item.NAME, item.VALUE)
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

        data.inventory.remove(item, quantity, verbose=False)
        Output.sold1(item.NAME)
        data.pouch.add(data.pouchitems.gold, int((item.VALUE * quantity) / 2))
    except (KeyError, AttributeError, ValueError):
        try:
            hero = data.party.get_member_with_this_equipment(params[0])
            item = hero.get_equipment(params[0])
            empty_item = data.inventory.get_empty_of_this_type(item.TYPE)

            hero.set_equipment(empty_item, verbose=False)
            Output.sold1(item.NAME)
            Output.sold2(item.NAME, hero.NAME)
            data.pouch.add(data.pouchitems.gold, int(item.VALUE / 2))
        except (AttributeError, ValueError):
            print("sell ([quantity]) [gear_name_without_spaces]")


def cmd_equip(*params):
    try:
        hero = data.party[params[0]]
        selected_item = data.inventory[params[1]]
        equipped_item = hero.get_same_type_from_equipment(selected_item)

        if hero.set_equipment(selected_item):
            data.inventory.add(equipped_item, verbose=False if "empty" in equipped_item.RAW else True)
            data.inventory.remove(selected_item, verbose=False)
    except (KeyError, AttributeError):
        print("equip [hero_name_in_party] [gear_name_without_spaces]")


def cmd_unequip(*params):
    try:
        hero = data.party[params[0]]
        equipped_item = hero.get_equipment(params[1])
        empty_item = data.inventory.get_empty_of_this_type(equipped_item.TYPE)

        data.inventory.add(equipped_item)
        hero.set_equipment(empty_item, verbose=False)
    except (KeyError, AttributeError):
        print("unequip [hero_name_in_party] [{}]".format("/".join(Output.INV_SORT)))


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
    for param in params:
        if 'empty' in param:
            return
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
        Output.cmd_pouch()
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
