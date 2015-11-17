

from battle import screen

import commands
from output import Output
import data
import util

import wx
import gui

import sys


def todo():
    """"
    misschien hoeft een enemy geen equipment te hebben of skills, maar raw stats. idee om over na te denken
    de pouchvraag verwijderen bij buy, (misschien toch niet)

    meer gears
    meer stats voor heroes
    prijzen van weapons, shields en armors zijn een voorbeeld

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

    todo, health bars aanpassen naar dc draw rect. http://zetcode.com/wxpython/gdi/
    """


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

    def OnBtnEnemiesClick(self, event):
        screen.BattleWindow().run()

    def OnBtnShopClick(self, event):
        ShopWindow(None).ShowModal()

    def OnBtnTavernClick(self, event):
        TavernWindow(None).ShowModal()

    def OnBtnPartyClick(self, event):
        PartyWindow(None).ShowModal()

    def OnBtnExitClick(self, event):
        sys.exit()


class ShopWindow(gui.ShopDialog):
    def __init__(self, parent):
        gui.ShopDialog.__init__(self, parent)

    def _load_buy(self, gear_dict, path, weaponskill=""):
        # moet eigenlijk data.pouch['gold'] zijn, maar werkt niet .notatie, vandaar cheat: data.pouchitems
        self.lbl_gold.LabelText = data.pouchitems.gold.NAME+": "+str(data.pouchitems.gold.quantity)

        columns = []
        for gear_item in Output.SHOP_SORT:
            if gear_item in next(iter(gear_dict.values())):
                columns.append(gear_item)
        headers = [item.title().replace("_", ".") for item in columns]
        headers[0] = ''
        headers[1] = ''
        headers.append('Backpack')

        sortlist = []
        for gear_item in sorted(gear_dict.values(), key=lambda xx: xx.sort):
            templist = []
            if gear_item.shop:
                if weaponskill == "" or gear_item.skill == weaponskill:
                    for column_name in columns:
                        if column_name in gear_item:
                            if gear_item[column_name] is None:  # or value1[item] == 0:
                                templist.append("")   # uitgezet, want het is op dit moment niet per se nodig.
                            else:
                                templist.append(str(gear_item[column_name]))
                    templist.append(str(self._shop_count(gear_item.raw)))
                    sortlist.append(templist)

        if self.grid_shop.GetNumberRows() > 1 and self.grid_shop.GetNumberCols() > 0:
            self.grid_shop.DeleteRows(1, self.grid_shop.GetNumberRows() - 1)
            self.grid_shop.DeleteCols(0, self.grid_shop.GetNumberCols())

        for x in range(len(headers)):
            self.grid_shop.AppendCols(1)
            self.grid_shop.SetCellValue(0, x, headers[x])

        for y in range(len(sortlist)):
            self.grid_shop.AppendRows(1)
            for x in range(len(headers)):
                self.grid_shop.SetCellValue(y + 1, x, sortlist[y][x])

        self.grid_shop.AutoSize()

        if path is not None:
            for y in range(len(sortlist)):
                image = wx.Image(path)
                image.Resize((32, 32), (-gear_dict[sortlist[y][0]].col, -gear_dict[sortlist[y][0]].row))
                new_img = wx.Bitmap(image)
                img_render = util.ImageRenderer(new_img)
                self.grid_shop.SetCellRenderer(y + 1, 0, img_render)

        self.grid_shop.SetColSize(0, 32)
        self.grid_shop.SetColSize(1, self.grid_shop.GetColSize(1) + 20)
        self.grid_shop.SetColSize(2, self.grid_shop.GetColSize(2) + 20)

        rows = self.grid_shop.GetNumberRows()
        for y in range(rows):
            self.grid_shop.SetRowSize(y, 32)

        w, h = self.grid_shop.GetClientSize()
        self.SetSize(w + 400, h + 400)
        self.Center()

    @staticmethod
    def _shop_count(key):
        count = data.inventory.count_item(key) + data.party.count_equipment(key)
        if count != 0:
            return count
        else:
            return ""

    def OnSelect(self, event):
        path = 'resources/icons/gear/'
        if self.radio_buy.GetValue():
            if self.combo_shop.GetValue() in ("Sword", "Hafted", "Pole", "Missile", "Thrown"):
                self._load_buy(data.list_gear_dict['weapons'][0], None, self.combo_shop.GetValue())
            elif self.combo_shop.GetValue() == "Shield":
                self._load_buy(data.list_gear_dict['shields'][0], path+'shield3.png')
            elif self.combo_shop.GetValue() == "Helmet":
                self._load_buy(data.list_gear_dict['helmets'][0], None)

    def OnClick(self, event):
        self.grid_shop.SetSelectionBackground((64, 64, 64))
        self.grid_shop.SelectRow(event.GetRow())

    def OnDClick(self, event):
        gear_raw = self.grid_shop.GetCellValue(event.GetRow(), 0)

        quantity = 1
        item = None
        for combo in data.list_gear_dict.values():
            if gear_raw in combo[0]:
                item = combo[1](combo[0][gear_raw])
                break

        if item.SHOP:
            if data.pouch.remove(data.pouchitems.gold, item.VALUE * quantity):
                Output.buy(quantity, item.NAME, item.VALUE)
                self.message("Purchased {} {} for {} gold.".format(quantity, item.NAME, item.VALUE * quantity))
                data.inventory.add(item, quantity)

        self._load_buy()

    def message(self, message, caption='Shop'):
        dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


class TavernWindow(gui.HeroDialog):
    def __init__(self, parent):
        gui.HeroDialog.__init__(self, parent)
        self._firsttime = True
        self._load()

    def _load(self):
        self.lbl_size.LabelText = "In party: "+str(len(data.party))+"/"+str(data.party.MAXIMUM)
        self.grid_heroes.SetGridCursor((0, 1))  # zodat de selector niet door alagos heen gaat

        i = 0
        for hero_raw in Output.HERO_SORT:
            hero = data.heroes[hero_raw]

            image = wx.Image(hero.BMP)
            image.Resize((32, 32), (-32, 0))
            new_img = wx.Bitmap(image)
            img_render = util.ImageRenderer(new_img)
            self.grid_heroes.SetCellRenderer(i, 0, img_render)

            self.grid_heroes.SetCellValue(i, 1, hero.NAME)
            self.grid_heroes.SetCellValue(i, 2, "("+str(hero.level.quantity)+")")
            self.grid_heroes.SetCellTextColour(i, 3, wx.GREEN)
            self.grid_heroes.SetCellValue(i, 4, "Alive")
            available = "Available"
            self.grid_heroes.SetCellTextColour(i, 4, wx.GREEN)
            self.grid_heroes.SetCellValue(i, 5, "[    ]")
            if hero in data.party:
                available = "Party member"
                self.grid_heroes.SetCellTextColour(i, 4, wx.WHITE)
                self.grid_heroes.SetCellValue(i, 5, "[ X ]")
            if hero.RAW == "alagos":
                available = "Party leader"
                self.grid_heroes.SetCellTextColour(i, 4, wx.WHITE)
                self.grid_heroes.SetCellValue(i, 5, "[ X ]")
            self.grid_heroes.SetCellValue(i, 4, available)

            i += 1
            if self._firsttime:
                self.grid_heroes.AppendRows(1)
            self.grid_heroes.SetRowSize(i, 44)

        if self._firsttime:
            rows = self.grid_heroes.GetNumberRows()
            w, h = self.grid_heroes.GetSize()
            self.SetSize(w + 300, 44 * rows + 100)
            self.Center()
            self._firsttime = False

    def OnCellClick(self, event):
        # todo, idee kasper, kolom en rij als dict key. en hero raw als value.
        if self.grid_heroes.GetCellValue(event.GetRow(), event.GetCol()) == "[    ]":
            data.party.add(data.heroes[self.grid_heroes.GetCellValue(event.GetRow(), 1).lower()])
        elif self.grid_heroes.GetCellValue(event.GetRow(), event.GetCol()) == "[ X ]":
            data.party.remove(data.heroes[self.grid_heroes.GetCellValue(event.GetRow(), 1).lower()])
        self._load()


class PartyWindow(gui.PartyDialog):
    def __init__(self, parent):
        gui.PartyDialog.__init__(self, parent)
        self._hc = 0
        self._firsttime = True

        self._party_list = []
        for hero_raw in Output.HERO_SORT:
            hero = data.heroes[hero_raw]
            if hero in data.party:
                self._party_list.append(hero)

        self._show_partymembers()
        self.refresh_window()

    def refresh_window(self):
        self._select_partymember()
        self._show_stats()
        self._show_skills()
        self._show_inventory()
        self.Refresh()

    def _show_partymembers(self):
        img_list = []
        for hero in self._party_list:
            image = wx.Image(hero.BMP)
            image.Resize((32, 32), (-32, 0))
            img_list.append(wx.Bitmap(image))

        pnl_list = [self.pnl_hero1, self.pnl_hero2, self.pnl_hero3, self.pnl_hero4, self.pnl_hero5]
        bmp_list = [self.bmp_p1,    self.bmp_p2,    self.bmp_p3,    self.bmp_p4,    self.bmp_p5]
        nam_list = [self.lbl_nam1,  self.lbl_nam2,  self.lbl_nam3,  self.lbl_nam4,  self.lbl_nam5]
        lev_list = [self.lbl_lev1,  self.lbl_lev2,  self.lbl_lev3,  self.lbl_lev4,  self.lbl_lev5]
        hp_list = [self.lbl_hp1,    self.lbl_hp2,   self.lbl_hp3,   self.lbl_hp4,   self.lbl_hp5]
        gau_list = [self.gau_p1,    self.gau_p2,    self.gau_p3,    self.gau_p4,    self.gau_p5]

        for i in range(5):
            if len(data.party) >= i + 1:
                pnl_list[i].Show()
                bmp_list[i].Bitmap = img_list[i]
                nam_list[i].LabelText = self._party_list[i].NAME
                lev_list[i].LabelText = str(self._party_list[i].level.quantity)
                hp_list[i].LabelText = str(self._party_list[i].current_hp)+" / "+str(self._party_list[i].max_hp)
                gau_list[i].Range = self._party_list[i].max_hp
                gau_list[i].Value = self._party_list[i].current_hp
            else:
                pnl_list[i].Hide()

    def _select_partymember(self):

        pnl_list = [self.pnl_hero1, self.pnl_hero2, self.pnl_hero3, self.pnl_hero4, self.pnl_hero5]

        for i in range(5):
            if self._hc == i:
                pnl_list[i].BackgroundColour = (64, 64, 64)
            else:
                pnl_list[i].BackgroundColour = wx.BLACK

    def _show_stats(self):
        hero = self._party_list[self._hc]
        value = self.grid_stats.SetCellValue

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

        value(0, 2, "")
        value(1, 2, "")
        value(2, 2, "")
        value(3, 2, "")
        value(4, 2, "")
        self._show_stats2(5, 2, hero.diff_movepoints)
        # todo, dit moet nog anders, bijv shield protection apart in het groen via show_stats2 ?
        if hero.skills.shd.positive_quantity():
            value(6, 2, "("+str(hero.equipment.shd.PROTECTION)+")")
        else:
            value(6, 2, "")
        value(7, 2, "")
        self._show_stats2(8, 2, hero.skills.war.bonus(hero.equipment.wpn))
        value(9, 2, "")
        value(10, 2, "")

        i = 11
        for stat_type_raw in Output.STAT_SORT:
            stat = hero.stats[stat_type_raw]
            value(i, 0, str(stat.NAME))
            value(i, 1, str(stat.quantity))
            self._show_stats2(i, 2, stat.extra)
            i += 1

    def _show_stats2(self, x, y, value):
        if value == 0 or value is None:
            self.grid_stats.SetCellValue(x, y, "")
        elif value > 0:
            self.grid_stats.SetCellTextColour(x, y, wx.GREEN)
            self.grid_stats.SetCellValue(x, y, "(+"+str(value)+")")
        elif value < 0:
            self.grid_stats.SetCellTextColour(x, y, wx.RED)
            self.grid_stats.SetCellValue(x, y, "("+str(value)+")")

    def _show_skills(self):
        hero = self._party_list[self._hc]
        value = self.grid_skills.SetCellValue

        skill_list = []
        for skill_type_raw in Output.SKILL_SORT:
            if self._firsttime:
                self.grid_skills.AppendRows(1)
            if hero.skills[skill_type_raw].positive_quantity():
                skill_list.append(hero.skills[skill_type_raw])

        self.grid_skills.ClearGrid()
        for i in range(self.grid_skills.GetNumberRows()):   # omdat ClearGrid() blijkbaar niet werkt voor plaatjes
            img_render = util.ImageRenderer(wx.Bitmap('resources/black.png'))
            self.grid_skills.SetCellRenderer(i, 0, img_render)

        i = 0
        for skill in skill_list:
            img_render = util.ImageRenderer(wx.Bitmap(skill.BMP))
            self.grid_skills.SetCellRenderer(i, 0, img_render)
            value(i, 0, str(skill.RAW))         # de raw onder het plaatje, wordt gebruikt voor klikherkenning

            value(i, 1, str(skill.NAME))
            value(i, 2, str(skill.quantity))
            self._show_skills2(i, 3, skill.extra)

            i += 1
            self.grid_skills.SetRowSize(i, 30)

        self._firsttime = False

        self.Layout()

    def _show_skills2(self, x, y, value):
        if value == 0:
            self.grid_skills.SetCellValue(x, y, "")
        elif value > 0:
            self.grid_skills.SetCellTextColour(x, y, wx.GREEN)
            self.grid_skills.SetCellValue(x, y, "(+"+str(value)+")")
        elif value < 0:
            self.grid_skills.SetCellTextColour(x, y, wx.RED)
            self.grid_skills.SetCellValue(x, y, "("+str(value)+")")

    def _show_inventory(self):
        pass

    @staticmethod
    def _show_inventory2(dc, gear, x, y):
        if "empty" not in gear.RAW:
            image = wx.Image(gear.BMP)
            image.Resize((32, 32), (-gear.COL, -gear.ROW))
            dc.DrawBitmap(wx.Bitmap(image), x, y, True)

    def show_gear_stats(self, item):
        self.lbl_desc.Clear()
        if "empty" in item.RAW:
            return
        self.lbl_desc.WriteText("{}\t\t{}\n".format(item.TYPE, item.NAME))
        for gear_property_name in Output.PROP_SORT:
            gear_property_value = getattr(item, gear_property_name.upper())
            if gear_property_value is not None:
                self.lbl_desc.AppendText("{}\t\t{}\n". format(gear_property_name.title().replace("_", "."),
                                                              gear_property_value))

    def OnSkillClick(self, event):
        raw = self.grid_skills.GetCellValue(event.GetRow(), 0)
        self.lbl_desc.Clear()
        if raw == "":
            return
        self.lbl_desc.WriteText(self._party_list[self._hc].skills[raw].DESC)

    def OnPanelPaint(self, event):
        hero = self._party_list[self._hc]

        dc = wx.PaintDC(self.pnl_canvas)
        gc = wx.GraphicsContext.Create(self.pnl_canvas)
        pnl_width = self.pnl_canvas.GetSize().Width
        dc.DrawBitmap(wx.Bitmap("resources/stickman.png"), ((pnl_width - 200) / 2), 10)
        red = (100, 0, 0, 128)  # transparant rood
        gc.SetPen(wx.Pen(wx.WHITE, 1))
        gc.SetBrush(wx.Brush(red))
        gc.DrawRectangle(54,  115, 32, 32)  # weapon
        gc.DrawRectangle(190, 115, 32, 32)  # shield
        gc.DrawRectangle(120, 20,  32, 32)  # helmet
        gc.DrawRectangle(120, 80,  32, 32)  # necklace
        gc.DrawRectangle(137, 115, 32, 32)  # armor
        gc.DrawRectangle(105, 115, 32, 32)  # cloak
        gc.DrawRectangle(54,  147, 32, 32)  # gloves
        gc.DrawRectangle(120, 157, 32, 32)  # belt
        gc.DrawRectangle(120, 220, 32, 32)  # boots
        gc.DrawRectangle(190, 147, 32, 32)  # accessory
        gc.DrawRectangle(190, 179, 32, 32)  # lring
        gc.DrawRectangle(54,  179, 32, 32)  # rring

        self._show_inventory2(dc, hero.equipment.wpn,  54, 115)
        self._show_inventory2(dc, hero.equipment.shd, 190, 115)

    def OnPanelHover(self, event):
        pos = self.pnl_canvas.ScreenToClient(wx.GetMousePosition())
        if 54 <= pos.x < 54 + 32 and 115 <= pos.y < 115 + 32:
            item = self._party_list[self._hc].get_equipment('Weapon')
            self.show_gear_stats(item)
        elif 190 <= pos.x < 190 + 32 and 115 <= pos.y < 115 + 32:
            item = self._party_list[self._hc].get_equipment('Shield')
            self.show_gear_stats(item)
        else:
            self.lbl_desc.Clear()

    def OnPanelClick(self, event):
        pos = self.pnl_canvas.ScreenToClient(wx.GetMousePosition())
        mpos = wx.GetMousePosition()
        if 54 <= pos.x < 54 + 32 and 115 <= pos.y < 115 + 32:
            InventoryWindow(self, self._party_list[self._hc], mpos, 'Weapon', 'wpn').Show()
        elif 190 <= pos.x < 190 + 32 and 115 <= pos.y < 115 + 32:
            InventoryWindow(self, self._party_list[self._hc], mpos, 'Shield', 'shd').Show()

    def OnBtnCloseClick(self, event):
        self.Close()

    def OnBtnNextClick(self, event):
        self._hc += 1
        if self._hc > len(data.party) - 1:
            self._hc = 0
        self.refresh_window()

    def OnBtnPrevClick(self, event):
        self._hc -= 1
        if self._hc < 0:
            self._hc = len(data.party) - 1
        self.refresh_window()


class InventoryWindow(gui.InventoryFrame):
    def __init__(self, parent, hero, position, gearname, geargroup):
        gui.InventoryFrame.__init__(self, parent)
        self._parent = parent
        self._hero = hero
        self._gearname = gearname
        self._geargroup = geargroup
        self.Move(position)
        self.SetTransparent(224)
        self.grid_items.SetFocus()

        self._load()

    def _load(self):
        value = self.grid_items.SetCellValue

        self.grid_items.ClearGrid()
        i = 0
        value(i, 0, "")
        value(i, 1, "")
        value(i, 2, "")
        value(i, 3, "Unequip " + self._gearname)
        value(i, 4, "")
        # eerst de hero's op volgorde
        for hero_raw in Output.HERO_SORT:
            hero = data.heroes[hero_raw]
            if hero in data.party:
                equipment_item = hero.equipment[self._geargroup]
                if "empty" not in equipment_item.RAW:
                    i += 1
                    self.grid_items.AppendRows(1)
                    self.grid_items.SetRowSize(i, 34)

                    image = wx.Image(hero.BMP)
                    image.Resize((32, 32), (-32, 0))
                    new_img = wx.Bitmap(image)
                    img_render = util.ImageRenderer(new_img)
                    self.grid_items.SetCellRenderer(i, 0, img_render)
                    value(i, 0, "[X]")  # cell verborgen achter het plaatje van de hero. want die mag je niet equippen.

                    image = wx.Image(equipment_item.BMP)
                    image.Resize((32, 32), (-equipment_item.COL, -equipment_item.ROW))
                    new_img = wx.Bitmap(image)
                    img_render = util.ImageRenderer(new_img)
                    self.grid_items.SetCellRenderer(i, 1, img_render)

                    value(i, 2, "1")
                    if equipment_item.WPN_SKILL is None:
                        value(i, 3, equipment_item.NAME)
                    else:
                        value(i, 3, "["+equipment_item.WPN_SKILL+"] "+equipment_item.NAME)
                    value(i, 4, equipment_item.RAW)
        # dan de rest van unequipped op volgorde
        for inventory_item in sorted(data.inventory, key=lambda x: x.SORT):
            if self._gearname == inventory_item.TYPE:
                if "empty" not in inventory_item.RAW:
                    i += 1
                    self.grid_items.AppendRows(1)
                    self.grid_items.SetRowSize(i, 34)

                    value(i, 0, "")

                    image = wx.Image(inventory_item.BMP)
                    image.Resize((32, 32), (-inventory_item.COL, -inventory_item.ROW))
                    new_img = wx.Bitmap(image)
                    img_render = util.ImageRenderer(new_img)
                    self.grid_items.SetCellRenderer(i, 1, img_render)

                    value(i, 2, str(inventory_item.quantity))
                    if inventory_item.WPN_SKILL is None:
                        value(i, 3, inventory_item.NAME)
                    else:
                        value(i, 3, "["+inventory_item.WPN_SKILL+"] "+inventory_item.NAME)
                    value(i, 4, inventory_item.RAW)

        rows = self.grid_items.GetNumberRows()
        w, h = self.grid_items.GetSize()
        self.SetSize(w + 2, 34 * rows + 2)

    def OnClick(self, event):
        self.grid_items.SetSelectionBackground((64, 64, 64))
        self.grid_items.SelectRow(event.GetRow())
        raw = self.grid_items.GetCellValue(event.GetRow(), 4)

        if event.GetRow() == 0:
            return

        try:
            item = data.inventory[raw]
        except KeyError:
            hero = data.party.get_member_with_this_equipment(raw)
            item = hero.get_equipment(raw)

        self._parent.show_gear_stats(item)

    def OnDClick(self, event):
        raw = self.grid_items.GetCellValue(event.GetRow(), 4)
        hero = self.grid_items.GetCellValue(event.GetRow(), 0)
        """Unequip"""
        if event.GetRow() == 0:
            equipped_item = self._hero.get_equipment(self._gearname.lower())
            empty_item = data.inventory.get_empty_of_this_type(equipped_item.TYPE)
            data.inventory.add(equipped_item)
            self._hero.set_equipment(empty_item)
        elif hero != "[X]":  # als er een X verborgen onder het plaatje staat, mag je die niet equippen.
            """Equip"""
            selected_item = data.inventory[raw]
            equipped_item = self._hero.get_same_type_from_equipment(selected_item)
            if self._hero.set_equipment(selected_item):
                data.inventory.add(equipped_item)
                data.inventory.remove(selected_item)

        self.Close()
        self._parent.refresh_window()

    def OnClose(self, event):
        self._parent.lbl_desc.Clear()
        self.Close()


def play():
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
