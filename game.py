

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
from output import Output
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
        self.btn_prev.Disable()
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
        self.btn_prev.Enable()
        self.btn_save.Enable()

    def OnBtnNewClick(self, event):
        self.enable_buttons()
        data.load_all_data()

    def OnBtnPartyClick(self, event):
        PartyWindow(None).ShowModal()

    def OnBtnExitClick(self, event):
        commands.cmd_exit()


class PartyWindow(gui.PartyDialog):
    def __init__(self, parent):
        gui.PartyDialog.__init__(self, parent)
        self.show_partymembers()

    def show_partymembers(self):
        hero_list = []
        for hero_raw in Output.HERO_SORT:
            hero = data.heroes[hero_raw]
            if hero in data.party:
                hero_list.append(hero)

        img_list = []
        for hero in hero_list:
            start_image = wx.Image(hero.BMP)
            start_image.Resize((32, 32), (-32, 0))
            img_list.append(wx.Bitmap(start_image))

        self.bmp_p1.Bitmap = img_list[0]
        self.lbl_nam1.LabelText = hero_list[0].NAME
        self.lbl_lev1.LabelText = str(hero_list[0].level.quantity)
        self.lbl_hp1.LabelText = str(hero_list[0].current_hp) + " / " + str(hero_list[0].max_hp)
        self.gau_p1.Range = hero_list[0].max_hp
        self.gau_p1.Value = hero_list[0].current_hp

        try:
            self.pnl_hero2.Show()
            self.bmp_p2.Bitmap = img_list[1]
            self.lbl_nam2.LabelText = hero_list[1].NAME
            self.lbl_lev2.LabelText = str(hero_list[1].level.quantity)
            self.lbl_hp2.LabelText = str(hero_list[1].current_hp) + " / " + str(hero_list[1].max_hp)
            self.gau_p2.Range = hero_list[1].max_hp
            self.gau_p2.Value = hero_list[1].current_hp
        except IndexError:
            self.pnl_hero2.Hide()

        try:
            self.pnl_hero3.Show()
            self.bmp_p3.Bitmap = img_list[2]
            self.lbl_nam3.LabelText = hero_list[2].NAME
            self.lbl_lev3.LabelText = str(hero_list[2].level.quantity)
            self.lbl_hp3.LabelText = str(hero_list[2].current_hp) + " / " + str(hero_list[2].max_hp)
            self.gau_p3.Range = hero_list[2].max_hp
            self.gau_p3.Value = hero_list[2].current_hp
        except IndexError:
            self.pnl_hero3.Hide()

        try:
            self.pnl_hero4.Show()
            self.bmp_p4.Bitmap = img_list[3]
            self.lbl_nam4.LabelText = hero_list[3].NAME
            self.lbl_lev4.LabelText = str(hero_list[3].level.quantity)
            self.lbl_hp4.LabelText = str(hero_list[3].current_hp) + " / " + str(hero_list[3].max_hp)
            self.gau_p4.Range = hero_list[3].max_hp
            self.gau_p4.Value = hero_list[3].current_hp
        except IndexError:
            self.pnl_hero4.Hide()

        try:
            self.pnl_hero5.Show()
            self.bmp_p5.Bitmap = img_list[4]
            self.lbl_nam5.LabelText = hero_list[4].NAME
            self.lbl_lev5.LabelText = str(hero_list[4].level.quantity)
            self.lbl_hp5.LabelText = str(hero_list[4].current_hp) + " / " + str(hero_list[4].max_hp)
            self.gau_p5.Range = hero_list[4].max_hp
            self.gau_p5.Value = hero_list[4].current_hp
        except IndexError:
            self.pnl_hero5.Hide()

    def OnBtnCloseClick(self, event):
        self.Close()


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
    MainWindow(None).Show()
    app.MainLoop()

    play()
