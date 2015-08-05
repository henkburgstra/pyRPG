
# misschien hoeft een enemy geen equipment te hebben of skills, maar raw stats. idee om over na te denken
# de pouchvraag verwijderen bij buy, (misschien toch niet)

# meer decorators
# meer stats voor heroes
# prijzen weapons hercalculeren. die van de shields en armors zijn een voorbeeld om zo te doen.

# wat is beter in de output class, pushen naar de output, of vanuit de output getten?
# wel veel static methods... is dat de juiste manier?
# hoe kan ik de 2 dicts aan het begin van data samenvoegen? (fixed?)

# texttable gebruiken bij stats van hero
# wx python onderzoeken


# idee om agility erin te stoppen, ter ontlasting van dexterity. bijv movespeed, en moverange
# (denk dus ook aan het gevolg aan de items zoals shield met -dex, dat dat misschien -agi moet worden)
# - movespeed komt van stamina
# - stamina * strength = weight possible
# - weight aan item toevoegen (fixed)
# - armor ed heeft dus invloed op movespeed
# - movespeed en turns weergeven
# - stamina gebruiken

# geen min sta meer aan armor, helmet en andere armors (fixed)
# maar alleen een weight, zodat er geen minimum meer is, maar je moet gewoon genoeg stamina hebben om te dragen
# weight heeft invloed op agility en stamina

# gebruik van dictionary doornemen, aanpassen zoals in cmd_heroes en cmd_party (fixed?)
# of iig value en key duidelijkere namen geven (fixed?)
# suggestie van kasper's mail bekijken (onnodig?)

import commands


def create_name():
    while True:
        name = input("What is your name? ").strip().capitalize()
        if len(name) < 1:
            continue
        if commands.yes_or_no(name + ", is that your name? "):
            return name
        else:
            continue


def play():

    # heroes.alagos.name = create_name()
    commands.cmd_cls()
    print("This is PyRPG.")
    print()
    print("Type 'help' for guidance.")
    print()

    while True:  # not heroes.alagos.is_dead():
        line = input(">> ").lower()
        cmd = line.split()
        cmd.append("EoCMD")
        cmd.append("EoCMD")
        commands.run_command(*cmd)


if __name__ == "__main__":
    play()
