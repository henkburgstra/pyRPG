
def todo():
    """"
    misschien hoeft een enemy geen equipment te hebben of skills, maar raw stats. idee om over na te denken
    de pouchvraag verwijderen bij buy, (misschien toch niet)

    meer gears
    meer stats voor heroes
    prijzen weapons hercalculeren. die van de shields en armors zijn een voorbeeld om zo te doen.

    wat is beter in de output class, pushen naar de output, of vanuit de output getten?
    wel veel static methods... is dat de juiste manier?

    tkinter en pygame gebruiken (http://usingpython.com)

    idee om agility erin te stoppen, ter ontlasting van dexterity. bijv movespeed, en moverange
    (denk dus ook aan het gevolg aan de items zoals shield met -dex, dat dat misschien -agi moet worden)
    - movespeed komt van stamina
    - stamina * strength = weight possible
    - weight aan item toevoegen (fixed)
    - armor ed heeft dus invloed op movespeed
    - movespeed en turns weergeven
    - stamina gebruiken

    geen min sta meer aan armor, helmet en andere armors (fixed)
    maar alleen een weight, zodat er geen minimum meer is, maar je moet gewoon genoeg stamina hebben om te dragen
    weight heeft invloed op agility en stamina

    gebruik van dictionary doornemen, aanpassen zoals in cmd_heroes en cmd_party (fixed?)
    of iig value en key duidelijkere namen geven (fixed?)
    suggestie van kasper's mail bekijken (onnodig?)

    suggestie van kasper om 1 gear class te hebben en de rest daarvan afleiden
    """

import commands
import data
import wx
import gui


class MainWindow(gui.MainFrame):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
        self.disable_buttons()

    def disable_buttons(self):
        self.btn_party.Disable()
        self.btn_inn.Disable()
        self.btn_tavern.Disable()
        self.btn_school.Disable()
        self.btn_trainer.Disable()
        self.btn_shop.Disable()
        self.btn_materials.Disable()
        self.btn_boss.Disable()
        self.btn_enemies.Disable()
        self.btn_next.Disable()
        self.btn_previous.Disable()
        self.btn_save.Disable()

    def enable_buttons(self):
        self.btn_party.Enable()
        self.btn_inn.Enable()
        self.btn_tavern.Enable()
        self.btn_school.Enable()
        self.btn_trainer.Enable()
        self.btn_shop.Enable()
        self.btn_materials.Enable()
        self.btn_boss.Enable()
        self.btn_enemies.Enable()
        self.btn_next.Enable()
        self.btn_previous.Enable()
        self.btn_save.Enable()

    def BtnNewClick(self, event):
        self.enable_buttons()
        data.load_all_data()

    def BtnExitClick(self, event):
        commands.cmd_exit()


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
    app = wx.App(False)
    root = MainWindow(None)
    root.Show(True)
    app.MainLoop()

    play()
