
from util import DotDict
import characters
import items
import decorators
import containers


list_gear_dict = dict(
    weapons=(decorators.weapons, items.Weapon.factory),
    shields=(decorators.shields, items.Shield.factory),
    helmets=(decorators.helmets, items.Helmet.factory),
    armors=(decorators.armors, items.Armor.factory),
    cloaks=(decorators.cloaks, items.Cloak.factory,)
)


def stats(int1, wil1, dex1, agi1, edu1, str1, sta1):
    return dict(
        int=characters.Intelligence(int1), wil=characters.Willpower(wil1), dex=characters.Dexterity(dex1),
        agi=characters.Agility(agi1),
        edu=characters.Endurance(edu1),    str=characters.Strength(str1),  sta=characters.Stamina(sta1)
    )

#                                agi
stats_alagos = stats(18,  12, 15, 15, 15, 15, 30)
stats_luana = stats(14,   10, 22, 20, 10,  8, 20)
stats_grindan = stats(10,  8, 25, 10, 20, 20, 40)
stats_rydalin = stats(22, 16, 20, 15, 16, 10, 31)
stats_codrif = stats(22,  18, 15, 12, 15, 10, 20)
stats_galen = stats(15,   15, 18, 10, 20, 25, 40)
stats_raiko = stats(6,    11, 14,  8, 30, 30, 60)
stats_kiara = stats(15,   10, 30, 30, 20, 15, 40)
stats_luthais = stats(30, 30, 20, 12, 18,  8, 50)
stats_elias = stats(30,   30, 25, 18, 30, 20, 60)
stats_onarr = stats(30,   25, 23, 15, 30, 25, 60)
stats_duilio = stats(25,  25, 30, 25, 25, 25, 75)
stats_iellwen = stats(30, 25, 30, 25, 30, 20, 60)
stats_faeron = stats(30,  30, 30, 30, 25, 15, 80)


def skills(chm1, dip1, lor1, mec1, med1, mer1, ran1, sci1, stl1, thf1, trb1, war1, haf1, mis1, pol1, shd1, swd1, thr1):
    return dict(
        chm=characters.Chemist(chm1),  dip=characters.Diplomat(dip1),   lor=characters.Loremaster(lor1),
        mec=characters.Mechanic(mec1), med=characters.Medic(med1),      mer=characters.Merchant(mer1),
        ran=characters.Ranger(ran1),   sci=characters.Scientist(sci1),  stl=characters.Stealth(stl1),
        thf=characters.Thief(thf1),    trb=characters.Troubadour(trb1), war=characters.Warrior(war1),
        haf=characters.Hafted(haf1),   mis=characters.Missile(mis1),    pol=characters.Pole(pol1),
        shd=characters.Shield(shd1),   swd=characters.Sword(swd1),      thr=characters.Thrown(thr1)
    )

skills_alagos = skills(0,   0,  0,  0,  0,  0,  0,  1,  1,  0,  1,  3,  1,  3,  0,  3,  3,  0)
skills_luana = skills(0,    0,  0,  1,  0,  0,  0,  0,  3,  3,  0,  0, -1, -1,  0, -1,  1,  2)
skills_grindan = skills(-1, 0,  0,  0,  0,  0,  0, -1,  1, -1,  0,  4,  0, -1,  0,  2,  4,  2)
skills_rydalin = skills(0,  0,  1,  0,  0,  1,  0,  4,  0,  0,  0,  0,  0, -1,  3,  0,  3, -1)
skills_codrif = skills(3,   0,  2,  2,  0,  0,  0,  2,  0,  0,  0,  0, -1, -1,  0, -1,  1,  1)
skills_galen = skills(-1,   0,  0,  0,  0,  0,  4, -1,  3,  0,  0,  5,  5,  3,  0,  3, -1, -1)
skills_raiko = skills(-1,   0, -1,  0,  0,  0,  0, -1,  1, -1, -1,  6,  0, -1,  6,  4,  6, -1)
skills_kiara = skills(0,    0,  0,  0,  1,  4,  0,  4,  5,  8,  0,  0, -1,  7,  2, -1,  7, -1)
skills_luthais = skills(7,  0,  9,  6,  8,  0,  0, 10,  5,  0,  0,  0,  0, -1,  8, -1,  0,  8)
skills_elias = skills(0,    8,  0,  0,  0,  0,  0,  7,  0,  0,  0,  7,  5, -1,  5, -1,  7, -1)
skills_onarr = skills(-1,   0,  6,  0,  4,  0,  0, -1,  0,  0,  7,  9,  8, -1,  8,  9,  5,  8)
skills_duillio = skills(5, 10,  5,  0,  0,  5,  5, 10,  5,  5, 10, 10, 10, -1, 10, 10, 10, 10)
skills_iellwen = skills(0,  0,  0,  0, 10,  0,  6,  8,  6,  0,  0, 10,  5,  7,  0, -1, 10, -1)
skills_faeron = skills(10, 10, 10,  0,  0, 10, 10, -1, 10, 10, 10, 10, 10,  0,  0,  0, 10,  0)


def equipment(wpn1='emptyweapon', shd1='emptyshield', arm1='emptyarmor'):
    return dict(
        wpn=items.Weapon.factory(decorators.weapons[wpn1]),
        shd=items.Shield.factory(decorators.shields[shd1]),
        hlm=items.Helmet.factory(decorators.helmets.emptyhelmet),
        arm=items.Armor.factory(decorators.armors[arm1]),
        clk=items.Cloak.factory(decorators.cloaks.emptycloak)
    )

equipment_alagos = equipment(wpn1='bronzeshortsword',  shd1='woodenbuckler', arm1='lightleatherarmor')
equipment_luana = equipment(wpn1='bronzedagger',                             arm1='lightleatherarmor')
equipment_grindan = equipment(wpn1='ironlongsword',    shd1='irontarge',     arm1='mediumbronzearmor')
equipment_rydalin = equipment(wpn1='bronzestaff',                            arm1='mediumleatherarmor')
equipment_codrif = equipment(wpn1='bronzedagger',                            arm1='lightleatherarmor')
equipment_galen = equipment(wpn1='ironaxe',            shd1='irontarge',     arm1='mediumbronzearmor')
equipment_raiko = equipment(wpn1='ironbroadsword',     shd1='ironkite',      arm1='heavyironarmor')
equipment_kiara = equipment(wpn1='silverdagger',                             arm1='lightbronzearmor')
equipment_luthais = equipment(wpn1='bronzestaff',                            arm1='lightironarmor')
equipment_elias = equipment(wpn1='steellongsword',                           arm1='mediumironarmor')
equipment_onarr = equipment(wpn1='steelpoleaxe',       shd1='steelkite',     arm1='heavyironarmor')
equipment_duillio = equipment(wpn1='silvershortsword', shd1='silvertarge',   arm1='mediumsteelarmor')
equipment_iellwen = equipment(wpn1='steellongsword',                         arm1='mediumironarmor')
equipment_faeron = equipment(wpn1='titaniummace',                            arm1='lighttitaniumarmor')


heroes = DotDict(dict(
    alagos=characters.Hero('Alagos',   characters.Level(1),      500, stats_alagos,  skills_alagos,  equipment_alagos),
    luana=characters.Hero('Luana',     characters.Level(1),      500, stats_luana,   skills_luana,   equipment_luana),
    grindan=characters.Hero('Grindan', characters.Level(8),   102000, stats_grindan, skills_grindan, equipment_grindan),
    rydalin=characters.Hero('Rydalin', characters.Level(3),     7000, stats_rydalin, skills_rydalin, equipment_rydalin),
    codrif=characters.Hero('Codrif',   characters.Level(2),     2500, stats_codrif,  skills_codrif,  equipment_codrif),
    galen=characters.Hero('Galen',     characters.Level(4),    15000, stats_galen,   skills_galen,   equipment_galen),
    raiko=characters.Hero('Raiko',     characters.Level(12),  325000, stats_raiko,   skills_raiko,   equipment_raiko),
    kiara=characters.Hero('Kiara',     characters.Level(12),  325000, stats_kiara,   skills_kiara,   equipment_kiara),
    luthais=characters.Hero('Luthais', characters.Level(20), 1435000, stats_luthais, skills_luthais, equipment_luthais),
    elias=characters.Hero('Elias',     characters.Level(18), 1054500, stats_elias,   skills_elias,   equipment_elias),
    onarr=characters.Hero('Onarr',     characters.Level(18), 1054500, stats_onarr,   skills_onarr,   equipment_onarr),
    duillio=characters.Hero('Duillio', characters.Level(22), 1897500, stats_duilio,  skills_duillio, equipment_duillio),
    iellwen=characters.Hero('Iellwen', characters.Level(20), 1435000, stats_iellwen, skills_iellwen, equipment_iellwen),
    faeron=characters.Hero('Faeron',   characters.Level(25), 2762500, stats_faeron,  skills_faeron,  equipment_faeron)
))

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
heroes.duillio.stats_update()
heroes.iellwen.stats_update()
heroes.faeron.stats_update()


# stats_brownbat = dict(
#     int=Intelligence(4), wil=Willpower(3), dex=Dexterity(14), edu=Endurance(5), str=Strength(8), sta=Stamina(10))
# stats_darkbat = dict(
#     int=Intelligence(4), wil=Willpower(3), dex=Dexterity(12), edu=Endurance(5), str=Strength(9), sta=Stamina(14))

# villains = DotDict(dict(
#     brownbat=Villain('Brown Bat', Level(2), stats_brownbat),
#     darkbat=Villain('Dark Bat',   Level(2), stats_darkbat)
# ))

pouchitems = DotDict(dict(
    gold=items.PouchItem("Gold"),
    herbs=items.PouchItem("Herbs"),
    spices=items.PouchItem("Spices")
))

inventory = containers.GearContainer("Backpack")
inventory.add(items.Weapon.factory(decorators.weapons.emptyweapon), verbose=False)
inventory.add(items.Shield.factory(decorators.shields.emptyshield), verbose=False)
inventory.add(items.Helmet.factory(decorators.helmets.emptyhelmet), verbose=False)
inventory.add(items.Armor.factory(decorators.armors.emptyarmor), verbose=False)
inventory.add(items.Cloak.factory(decorators.cloaks.emptycloak), verbose=False)

pouch = containers.SmallContainer("Pouch")

party = containers.PartyContainer("Party", 5)
party.add(heroes.alagos, verbose=False)
