
from util import DotDict
import characters
import items
import decorators
import containers


list_gear_dict = dict(
    weapons=(decorators.weapons,         items.Weapon.factory),
    shields=(decorators.shields,         items.Shield.factory),
    helmets=(decorators.helmets,         items.Helmet.factory),
    necklaces=(decorators.necklaces,     items.Necklace.factory),
    armors=(decorators.armors,           items.Armor.factory),
    cloaks=(decorators.cloaks,           items.Cloak.factory),
    gloves=(decorators.gloves,           items.Gloves.factory),
    belts=(decorators.belts,             items.Belt.factory),
    boots=(decorators.boots,             items.Boots.factory),
    accessories=(decorators.accessories, items.Accessory.factory)
)

heroes = {}
pouchitems = {}
inventory = {}
pouch = {}
party = {}


def build_cond(bmp1, lev1, txp1):
    return DotDict(
        bmp=bmp1, lev=characters.Level(lev1), txp=characters.Experience(txp1)
    )


def build_stats(int1, wil1, dex1, agi1, edu1, str1, sta1):
    return DotDict(
        int=characters.Intelligence(int1), wil=characters.Willpower(wil1), dex=characters.Dexterity(dex1),
        agi=characters.Agility(agi1),
        edu=characters.Endurance(edu1),    str=characters.Strength(str1),  sta=characters.Stamina(sta1)
    )


def build_skills(chm1, dip1, lor1, mec1, med1, mer1, ran1, sci1, stl1, thf1, trb1, war1,
                 haf1, mis1, pol1, shd1, swd1, thr1):
    return DotDict(
        chm=characters.Chemist(chm1),  dip=characters.Diplomat(dip1),   lor=characters.Loremaster(lor1),
        mec=characters.Mechanic(mec1), med=characters.Medic(med1),      mer=characters.Merchant(mer1),
        ran=characters.Ranger(ran1),   sci=characters.Scientist(sci1),  stl=characters.Stealth(stl1),
        thf=characters.Thief(thf1),    trb=characters.Troubadour(trb1), war=characters.Warrior(war1),
        haf=characters.Hafted(haf1),   mis=characters.Missile(mis1),    pol=characters.Pole(pol1),
        shd=characters.Shield(shd1),   swd=characters.Sword(swd1),      thr=characters.Thrown(thr1)
    )


def build_equipment(wpn1='emptyweapon', shd1='emptyshield', arm1='emptyarmor'):
    return DotDict(
        wpn=items.Weapon.factory(decorators.weapons[wpn1]),
        shd=items.Shield.factory(decorators.shields[shd1]),
        hlm=items.Helmet.factory(decorators.helmets.emptyhelmet),
        nlc=items.Necklace.factory(decorators.necklaces.emptynecklace),
        arm=items.Armor.factory(decorators.armors[arm1]),
        clk=items.Cloak.factory(decorators.cloaks.emptycloak),
        glv=items.Gloves.factory(decorators.gloves.emptygloves),
        blt=items.Belt.factory(decorators.belts.emptybelt),
        bts=items.Boots.factory(decorators.boots.emptyboots),
        acy=items.Accessory.factory(decorators.accessories.emptyaccessory)
    )


def load_all_data():

    global heroes
    global pouchitems
    global inventory
    global pouch
    global party

    path = 'resources/sprites_heroes/'
    all_cond = DotDict(
        ala=build_cond(path+'01_Alagos.png',   1,     500),
        lua=build_cond(path+'02_Luana.png',    1,     500),
        gri=build_cond(path+'03_Grindan.png',  8,  102000),
        ryd=build_cond(path+'04_Rydalin.png',  3,    7000),
        cod=build_cond(path+'05_Codrif.png',   2,    2500),
        gal=build_cond(path+'06_Galen.png',    4,   15000),
        rai=build_cond(path+'07_Raiko.png',   12,  325000),
        kia=build_cond(path+'08_Kiara.png',   12,  325000),
        lut=build_cond(path+'09_Luthais.png', 20, 1435000),
        eli=build_cond(path+'10_Elias.png',   18, 1054500),
        ona=build_cond(path+'11_Onarr.png',   18, 1054500),
        dui=build_cond(path+'12_Duilio.png',  22, 1897500),
        iel=build_cond(path+'13_Iellwen.png', 20, 1435000),
        fae=build_cond(path+'14_Faeron.png',  25, 2762500)
    )

    #                               agi
    all_stats = DotDict(
        ala=build_stats(18, 12, 15, 15, 15, 15, 30),
        lua=build_stats(14, 10, 22, 20, 10,  8, 20),
        gri=build_stats(10,  8, 25, 10, 20, 20, 40),
        ryd=build_stats(22, 16, 20, 15, 16, 10, 31),
        cod=build_stats(22, 18, 15, 12, 15, 10, 20),
        gal=build_stats(15, 15, 18, 10, 20, 25, 40),
        rai=build_stats(6,  11, 14,  8, 30, 30, 60),
        kia=build_stats(15, 10, 30, 30, 20, 15, 40),
        lut=build_stats(30, 30, 20, 12, 18,  8, 50),
        eli=build_stats(30, 30, 25, 18, 30, 20, 60),
        ona=build_stats(30, 25, 23, 15, 30, 25, 60),
        dui=build_stats(25, 25, 30, 25, 25, 25, 75),
        iel=build_stats(30, 25, 30, 25, 30, 20, 60),
        fae=build_stats(30, 30, 30, 30, 25, 15, 80)
    )

    all_skills = DotDict(
        ala=build_skills(0,   0,  0,  0,  0,  0,  0,  1,  1,  0,  1,  3,  1,  3,  0,  3,  3,  0),
        lua=build_skills(0,   0,  0,  1,  0,  0,  0,  0,  3,  3,  0,  0, -1, -1,  0, -1,  1,  2),
        gri=build_skills(-1,  0,  0,  0,  0,  0,  0, -1,  1, -1,  0,  4,  0, -1,  0,  2,  4,  2),
        ryd=build_skills(0,   0,  1,  0,  0,  1,  0,  4,  0,  0,  0,  0,  0, -1,  3,  0,  3, -1),
        cod=build_skills(3,   0,  2,  2,  0,  0,  0,  2,  0,  0,  0,  0, -1, -1,  0, -1,  1,  1),
        gal=build_skills(-1,  0,  0,  0,  0,  0,  4, -1,  3,  0,  0,  5,  5,  3,  0,  3, -1, -1),
        rai=build_skills(-1,  0, -1,  0,  0,  0,  0, -1,  1, -1, -1,  6,  0, -1,  6,  4,  6, -1),
        kia=build_skills(0,   0,  0,  0,  1,  4,  0,  4,  5,  8,  0,  0, -1,  7,  2, -1,  7, -1),
        lut=build_skills(7,   0,  9,  6,  8,  0,  0, 10,  5,  0,  0,  0,  0, -1,  8, -1,  0,  8),
        eli=build_skills(0,   8,  0,  0,  0,  0,  0,  7,  0,  0,  0,  7,  5, -1,  5, -1,  7, -1),
        ona=build_skills(-1,  0,  6,  0,  4,  0,  0, -1,  0,  0,  7,  9,  8, -1,  8,  9,  5,  8),
        dui=build_skills(5,  10,  5,  0,  0,  5,  5, 10,  5,  5, 10, 10, 10, -1, 10, 10, 10, 10),
        iel=build_skills(0,   0,  0,  0, 10,  0,  6,  8,  6,  0,  0, 10,  5,  7,  0, -1, 10, -1),
        fae=build_skills(10, 10, 10,  0,  0, 10, 10, -1, 10, 10, 10, 10, 10,  0,  0,  0, 10,  0)
    )

    all_equipment = DotDict(
        ala=build_equipment(wpn1='bronzeshortsword', shd1='woodenbuckler', arm1='lightleatherarmor'),
        lua=build_equipment(wpn1='bronzedagger',                           arm1='lightleatherarmor'),
        gri=build_equipment(wpn1='ironlongsword',    shd1='irontarge',     arm1='mediumbronzearmor'),
        ryd=build_equipment(wpn1='bronzestaff',                            arm1='mediumleatherarmor'),
        cod=build_equipment(wpn1='bronzedagger',                           arm1='lightleatherarmor'),
        gal=build_equipment(wpn1='ironaxe',          shd1='irontarge',     arm1='mediumbronzearmor'),
        rai=build_equipment(wpn1='ironbroadsword',   shd1='ironkite',      arm1='heavyironarmor'),
        kia=build_equipment(wpn1='silverdagger',                           arm1='lightbronzearmor'),
        lut=build_equipment(wpn1='bronzestaff',                            arm1='lightironarmor'),
        eli=build_equipment(wpn1='steellongsword',                         arm1='mediumironarmor'),
        ona=build_equipment(wpn1='steelpoleaxe',     shd1='steelkite',     arm1='heavyironarmor'),
        dui=build_equipment(wpn1='silvershortsword', shd1='silvertarge',   arm1='mediumsteelarmor'),
        iel=build_equipment(wpn1='steellongsword',                         arm1='mediumironarmor'),
        fae=build_equipment(wpn1='titaniummace',                           arm1='lighttitaniumarmor')
    )

    heroes = DotDict(
        alagos=characters.Hero('Alagos',   all_cond.ala, all_stats.ala, all_skills.ala, all_equipment.ala),
        luana=characters.Hero('Luana',     all_cond.lua, all_stats.lua, all_skills.lua, all_equipment.lua),
        grindan=characters.Hero('Grindan', all_cond.gri, all_stats.gri, all_skills.gri, all_equipment.gri),
        rydalin=characters.Hero('Rydalin', all_cond.ryd, all_stats.ryd, all_skills.ryd, all_equipment.ryd),
        codrif=characters.Hero('Codrif',   all_cond.cod, all_stats.cod, all_skills.cod, all_equipment.cod),
        galen=characters.Hero('Galen',     all_cond.gal, all_stats.gal, all_skills.gal, all_equipment.gal),
        raiko=characters.Hero('Raiko',     all_cond.rai, all_stats.rai, all_skills.rai, all_equipment.rai),
        kiara=characters.Hero('Kiara',     all_cond.kia, all_stats.kia, all_skills.kia, all_equipment.kia),
        luthais=characters.Hero('Luthais', all_cond.lut, all_stats.lut, all_skills.lut, all_equipment.lut),
        elias=characters.Hero('Elias',     all_cond.eli, all_stats.eli, all_skills.eli, all_equipment.eli),
        onarr=characters.Hero('Onarr',     all_cond.ona, all_stats.ona, all_skills.ona, all_equipment.ona),
        duilio=characters.Hero('Duilio',   all_cond.dui, all_stats.dui, all_skills.dui, all_equipment.dui),
        iellwen=characters.Hero('Iellwen', all_cond.iel, all_stats.iel, all_skills.iel, all_equipment.iel),
        faeron=characters.Hero('Faeron',   all_cond.fae, all_stats.fae, all_skills.fae, all_equipment.fae)
    )

    heroes.alagos.stats_update()
    heroes.luana.stats_update()
    heroes.grindan.stats_update()
    heroes.rydalin.stats_update()
    heroes.codrif.stats_update()
    heroes.galen.stats_update()
    heroes.raiko.stats_update()
    heroes.kiara.stats_update()
    heroes.luthais.stats_update()
    heroes.elias.stats_update()
    heroes.onarr.stats_update()
    heroes.duilio.stats_update()
    heroes.iellwen.stats_update()
    heroes.faeron.stats_update()

    pouchitems = DotDict(
        gold=items.PouchItem("Gold"),
        herbs=items.PouchItem("Herbs"),
        spices=items.PouchItem("Spices")
    )

    inventory = containers.GearContainer("Backpack")
    pouch = containers.SmallContainer("Pouch")
    party = containers.PartyContainer("Party", 5)

    inventory.add(items.Weapon.factory(decorators.weapons.emptyweapon), verbose=False)
    inventory.add(items.Shield.factory(decorators.shields.emptyshield), verbose=False)
    inventory.add(items.Helmet.factory(decorators.helmets.emptyhelmet), verbose=False)
    inventory.add(items.Necklace.factory(decorators.necklaces.emptynecklace), verbose=False)
    inventory.add(items.Armor.factory(decorators.armors.emptyarmor), verbose=False)
    inventory.add(items.Cloak.factory(decorators.cloaks.emptycloak), verbose=False)
    inventory.add(items.Gloves.factory(decorators.gloves.emptygloves), verbose=False)
    inventory.add(items.Belt.factory(decorators.belts.emptybelt), verbose=False)
    inventory.add(items.Boots.factory(decorators.boots.emptyboots), verbose=False)
    inventory.add(items.Accessory.factory(decorators.accessories.emptyaccessory), verbose=False)

    party.add(heroes.alagos, verbose=False)
    pouch.add(pouchitems.gold, 10, verbose=False)

    # dit hieronder is om te testen
    party.add(heroes.luana)
    party.add(heroes.elias)
    party.add(heroes.faeron)
    party.add(heroes.onarr)
    party.add(heroes.codrif)

    inventory.add(items.Weapon.factory(decorators.weapons.bronzeshortsword), 20)
    inventory.add(items.Weapon.factory(decorators.weapons.bronzelongsword), 9)
    inventory.add(items.Weapon.factory(decorators.weapons.steelbroadsword), 48)
    ###############
