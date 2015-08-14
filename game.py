

def todo():
    """"
    misschien hoeft een enemy geen equipment te hebben of skills, maar raw stats. idee om over na te denken
    de pouchvraag verwijderen bij buy, (misschien toch niet)

    meer gears
    meer stats voor heroes
    prijzen weapons hercalculeren. die van de shields en armors zijn een voorbeeld om zo te doen.

    wat is beter in de output class, pushen naar de output, of vanuit de output getten?
    wel veel static methods... is dat de juiste manier?

    pygame gebruiken (http://usingpython.com)

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
        self._disable_buttons()

    def _disable_buttons(self):
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

    def _enable_buttons(self):
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
        self._enable_buttons()
        data.load_all_data()

    def OnBtnLoadClick(self, event):
        pass

    def OnBtnPartyClick(self, event):
        PartyWindow(None).ShowModal()

    def OnBtnExitClick(self, event):
        commands.cmd_exit()


class PartyWindow(gui.PartyDialog):
    def __init__(self, parent):
        gui.PartyDialog.__init__(self, parent)
        self._hc = 0

        self.hero_list = []
        for hero_raw in Output.HERO_SORT:
            hero = data.heroes[hero_raw]
            if hero in data.party:
                self.hero_list.append(hero)

        self._show_partymembers()
        self._refresh_window()

    def _refresh_window(self):
        self._select_partymember()
        self._show_stats()
        self._show_skills()
        self.Refresh()

    def _show_partymembers(self):
        img_list = []
        for hero in self.hero_list:
            start_image = wx.Image(hero.BMP)
            start_image.Resize((32, 32), (-32, 0))
            img_list.append(wx.Bitmap(start_image))

        self.bmp_p1.Bitmap = img_list[0]
        self.lbl_nam1.LabelText = self.hero_list[0].NAME
        self.lbl_lev1.LabelText = str(self.hero_list[0].level.quantity)
        self.lbl_hp1.LabelText = str(self.hero_list[0].current_hp)+" / "+str(self.hero_list[0].max_hp)
        self.gau_p1.Range = self.hero_list[0].max_hp
        self.gau_p1.Value = self.hero_list[0].current_hp

        if len(data.party) >= 2:
            self.pnl_hero2.Show()
            self.bmp_p2.Bitmap = img_list[1]
            self.lbl_nam2.LabelText = self.hero_list[1].NAME
            self.lbl_lev2.LabelText = str(self.hero_list[1].level.quantity)
            self.lbl_hp2.LabelText = str(self.hero_list[1].current_hp)+" / "+str(self.hero_list[1].max_hp)
            self.gau_p2.Range = self.hero_list[1].max_hp
            self.gau_p2.Value = self.hero_list[1].current_hp
        else:
            self.pnl_hero2.Hide()

        if len(data.party) >= 3:
            self.pnl_hero3.Show()
            self.bmp_p3.Bitmap = img_list[2]
            self.lbl_nam3.LabelText = self.hero_list[2].NAME
            self.lbl_lev3.LabelText = str(self.hero_list[2].level.quantity)
            self.lbl_hp3.LabelText = str(self.hero_list[2].current_hp)+" / "+str(self.hero_list[2].max_hp)
            self.gau_p3.Range = self.hero_list[2].max_hp
            self.gau_p3.Value = self.hero_list[2].current_hp
        else:
            self.pnl_hero3.Hide()

        if len(data.party) >= 4:
            self.pnl_hero4.Show()
            self.bmp_p4.Bitmap = img_list[3]
            self.lbl_nam4.LabelText = self.hero_list[3].NAME
            self.lbl_lev4.LabelText = str(self.hero_list[3].level.quantity)
            self.lbl_hp4.LabelText = str(self.hero_list[3].current_hp)+" / "+str(self.hero_list[3].max_hp)
            self.gau_p4.Range = self.hero_list[3].max_hp
            self.gau_p4.Value = self.hero_list[3].current_hp
        else:
            self.pnl_hero4.Hide()

        if len(data.party) == 5:
            self.pnl_hero5.Show()
            self.bmp_p5.Bitmap = img_list[4]
            self.lbl_nam5.LabelText = self.hero_list[4].NAME
            self.lbl_lev5.LabelText = str(self.hero_list[4].level.quantity)
            self.lbl_hp5.LabelText = str(self.hero_list[4].current_hp)+" / "+str(self.hero_list[4].max_hp)
            self.gau_p5.Range = self.hero_list[4].max_hp
            self.gau_p5.Value = self.hero_list[4].current_hp
        else:
            self.pnl_hero5.Hide()

    def _select_partymember(self):
        if self._hc == 0:
            self.pnl_hero1.BackgroundColour = (32, 32, 32)
            self.pnl_hero2.BackgroundColour = "Black"
            self.pnl_hero3.BackgroundColour = "Black"
            self.pnl_hero4.BackgroundColour = "Black"
            self.pnl_hero5.BackgroundColour = "Black"
        elif self._hc == 1:
            self.pnl_hero1.BackgroundColour = "Black"
            self.pnl_hero2.BackgroundColour = (32, 32, 32)
            self.pnl_hero3.BackgroundColour = "Black"
            self.pnl_hero4.BackgroundColour = "Black"
            self.pnl_hero5.BackgroundColour = "Black"
        elif self._hc == 2:
            self.pnl_hero1.BackgroundColour = "Black"
            self.pnl_hero2.BackgroundColour = "Black"
            self.pnl_hero3.BackgroundColour = (32, 32, 32)
            self.pnl_hero4.BackgroundColour = "Black"
            self.pnl_hero5.BackgroundColour = "Black"
        elif self._hc == 3:
            self.pnl_hero1.BackgroundColour = "Black"
            self.pnl_hero2.BackgroundColour = "Black"
            self.pnl_hero3.BackgroundColour = "Black"
            self.pnl_hero4.BackgroundColour = (32, 32, 32)
            self.pnl_hero5.BackgroundColour = "Black"
        elif self._hc == 4:
            self.pnl_hero1.BackgroundColour = "Black"
            self.pnl_hero2.BackgroundColour = "Black"
            self.pnl_hero3.BackgroundColour = "Black"
            self.pnl_hero4.BackgroundColour = "Black"
            self.pnl_hero5.BackgroundColour = (32, 32, 32)

    def _show_stats(self):
        hero = self.hero_list[self._hc]
        value = self.grid_stats.SetCellValue

        self.grid_stats.SetColSize(0, 100)
        value(0, 0, "XP Remaining:")
        value(1, 0, "Total XP:")
        value(2, 0, "Next Level:")
        value(3, 0, "")
        value(4, 0, "Weight:")
        value(5, 0, "Movepoints:")
        value(6, 0, "Protection:")
        value(7, 0, "Defense:")
        value(8, 0, "Base Hit:")
        value(9, 0, "Damage:")
        value(10, 0, "")
        i = 11
        for stat_type_raw in Output.STAT_SORT:
            stat = hero.stats[stat_type_raw]
            value(i, 0, str(stat.NAME))
            i += 1

        self.grid_stats.SetColSize(1, 45)
        value(0, 1, str(hero.experience.remaining))
        if hero.level.quantity >= hero.level.MAXIMUM:
            value(1, 1, "Max")
            value(2, 1, "Max")
        else:
            value(1, 1, str(hero.experience.total))
            value(2, 1, str(hero.level.next(hero.experience.total)))
        value(3, 1, "")
        value(4, 1, str(hero.weight))
        value(5, 1, str(hero.own_movepoints))
        value(6, 1, str(hero.protection))
        value(7, 1, str(hero.equipment.shd.DEFENSE))
        value(8, 1, str(hero.equipment.wpn.BASE_HIT)+"%")
        value(9, 1, str(hero.equipment.wpn.DAMAGE))
        value(10, 1, "")
        i = 11
        for stat_type_raw in Output.STAT_SORT:
            stat = hero.stats[stat_type_raw]
            value(i, 1, str(stat.quantity))
            i += 1

        self.grid_stats.SetColSize(2, 45)
        value(0, 2, "")
        value(1, 2, "")
        value(2, 2, "")
        value(3, 2, "")
        value(4, 2, "")
        self._show_stats2(5, 2, hero.diff_movepoints)
        if hero.skills.shd.quantity > 0:
            value(6, 2, "("+str(hero.equipment.shd.PROTECTION)+")")
        else:
            value(6, 2, "")
        value(7, 2, "")
        if hero.skills.war.quantity > 0 and "empty" not in hero.equipment.wpn.RAW:
            self._show_stats2(8, 2, hero.skills.war.bonus(hero.equipment.wpn.BASE_HIT))
        else:
            value(8, 2, "")
        value(9, 2, "")
        value(10, 2, "")
        i = 11
        for stat_type_raw in Output.STAT_SORT:
            stat = hero.stats[stat_type_raw]
            self._show_stats2(i, 2, stat.extra)
            i += 1

        self.grid_stats.SetColSize(3, 45)

        self.grid_stats.SetColSize(4, 45)

    def _show_stats2(self, x, y, value):
        if value == 0:
            self.grid_stats.SetCellValue(x, y, "")
        elif value > 0:
            self.grid_stats.SetCellTextColour(x, y, "Green")
            self.grid_stats.SetCellValue(x, y, "(+"+str(value)+")")
        elif value < 0:
            self.grid_stats.SetCellTextColour(x, y, "Red")
            self.grid_stats.SetCellValue(x, y, "("+str(value)+")")

    def _show_skills(self):
        hero = self.hero_list[self._hc]
        value = self.grid_skills.SetCellValue

        self.grid_skills.SetColSize(0, 32)
        # value(0, 0, wx.Image(hero.skills.chm.BMP))

    def OnBtnCloseClick(self, event):
        self.Close()

    def OnBtnNextClick(self, event):
        self._hc += 1
        if self._hc > len(data.party) - 1:
            self._hc = 0
        self._refresh_window()

    def OnBtnPrevClick(self, event):
        self._hc -= 1
        if self._hc < 0:
            self._hc = len(data.party) - 1
        self._refresh_window()


def create_name():
    while True:
        name = input("What is your name? ").strip().capitalize()
        if len(name) < 1:
            continue
        if commands.yes_or_no(name+", is that your name? "):
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
