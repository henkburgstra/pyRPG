
# simple json framework voor savegames
# aan het einde, als property's geen special voorwaarden hebben, gewoon de lokale _variablen globaal maken, dus zonder _
# misschien hoeft een enemy geen equipment te hebben of skills, maar raw stats. idee om over na te denken

# meer decorators
# meer stats voor heroes
# idee om agility erin te stoppen, ter ontlasting van dexterity. bijv movespeed, en moverange
# (denk dus ook aan het gevolg aan de items zoals shield met -dex, dat dat misschien -agi moet worden)
# prijzen hercaluleren, die van de shields zijn een voorbeeld om zo te doen.
# itemproperty sortering, bestaat al, maar wordt nog niet gebruikt in item stats, of in shop.
# wat is beter in de output class, pushen naar de output, of vanuit de output getten?

# de pouchvraag verwijderen bij buy, (misschien toch niet)

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
