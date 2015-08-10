
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


def build_cond(lev1, txp1):
    return DotDict(
        lev=characters.Level(lev1), txp=txp1
    )

all_cond = DotDict(
    alagos=build_cond(1,       500),
    luana=build_cond(1,        500),
    grindan=build_cond(8,   102000),
    rydalin=build_cond(3,     7000),
    codrif=build_cond(2,      2500),
    galen=build_cond(4,      15000),
    raiko=build_cond(12,    325000),
    kiara=build_cond(12,    325000),
    luthais=build_cond(20, 1435000),
    elias=build_cond(18,   1054500),
    onarr=build_cond(18,   1054500),
    duilio=build_cond(22,  1897500),
    iellwen=build_cond(20, 1435000),
    faeron=build_cond(25,  2762500)
)


def build_stats(int1, wil1, dex1, agi1, edu1, str1, sta1):
    return DotDict(
        int=characters.Intelligence(int1), wil=characters.Willpower(wil1), dex=characters.Dexterity(dex1),
        agi=characters.Agility(agi1),
        edu=characters.Endurance(edu1),    str=characters.Strength(str1),  sta=characters.Stamina(sta1)
    )

#                                   agi
all_stats = DotDict(
    alagos=build_stats(18,  12, 15, 15, 15, 15, 30),
    luana=build_stats(14,   10, 22, 20, 10,  8, 20),
    grindan=build_stats(10,  8, 25, 10, 20, 20, 40),
    rydalin=build_stats(22, 16, 20, 15, 16, 10, 31),
    codrif=build_stats(22,  18, 15, 12, 15, 10, 20),
    galen=build_stats(15,   15, 18, 10, 20, 25, 40),
    raiko=build_stats(6,    11, 14,  8, 30, 30, 60),
    kiara=build_stats(15,   10, 30, 30, 20, 15, 40),
    luthais=build_stats(30, 30, 20, 12, 18,  8, 50),
    elias=build_stats(30,   30, 25, 18, 30, 20, 60),
    onarr=build_stats(30,   25, 23, 15, 30, 25, 60),
    duilio=build_stats(25,  25, 30, 25, 25, 25, 75),
    iellwen=build_stats(30, 25, 30, 25, 30, 20, 60),
    faeron=build_stats(30,  30, 30, 30, 25, 15, 80)
)


def build_skills(chm1, dip1, lor1, mec1, med1, mer1, ran1, sci1, stl1, thf1, trb1, war1, haf1, mis1, pol1, shd1, swd1,
                 thr1):
    return DotDict(
        chm=characters.Chemist(chm1),  dip=characters.Diplomat(dip1),   lor=characters.Loremaster(lor1),
        mec=characters.Mechanic(mec1), med=characters.Medic(med1),      mer=characters.Merchant(mer1),
        ran=characters.Ranger(ran1),   sci=characters.Scientist(sci1),  stl=characters.Stealth(stl1),
        thf=characters.Thief(thf1),    trb=characters.Troubadour(trb1), war=characters.Warrior(war1),
        haf=characters.Hafted(haf1),   mis=characters.Missile(mis1),    pol=characters.Pole(pol1),
        shd=characters.Shield(shd1),   swd=characters.Sword(swd1),      thr=characters.Thrown(thr1)
    )

all_skills = DotDict(
    alagos=build_skills(0,   0,  0,  0,  0,  0,  0,  1,  1,  0,  1,  3,  1,  3,  0,  3,  3,  0),
    luana=build_skills(0,    0,  0,  1,  0,  0,  0,  0,  3,  3,  0,  0, -1, -1,  0, -1,  1,  2),
    grindan=build_skills(-1, 0,  0,  0,  0,  0,  0, -1,  1, -1,  0,  4,  0, -1,  0,  2,  4,  2),
    rydalin=build_skills(0,  0,  1,  0,  0,  1,  0,  4,  0,  0,  0,  0,  0, -1,  3,  0,  3, -1),
    codrif=build_skills(3,   0,  2,  2,  0,  0,  0,  2,  0,  0,  0,  0, -1, -1,  0, -1,  1,  1),
    galen=build_skills(-1,   0,  0,  0,  0,  0,  4, -1,  3,  0,  0,  5,  5,  3,  0,  3, -1, -1),
    raiko=build_skills(-1,   0, -1,  0,  0,  0,  0, -1,  1, -1, -1,  6,  0, -1,  6,  4,  6, -1),
    kiara=build_skills(0,    0,  0,  0,  1,  4,  0,  4,  5,  8,  0,  0, -1,  7,  2, -1,  7, -1),
    luthais=build_skills(7,  0,  9,  6,  8,  0,  0, 10,  5,  0,  0,  0,  0, -1,  8, -1,  0,  8),
    elias=build_skills(0,    8,  0,  0,  0,  0,  0,  7,  0,  0,  0,  7,  5, -1,  5, -1,  7, -1),
    onarr=build_skills(-1,   0,  6,  0,  4,  0,  0, -1,  0,  0,  7,  9,  8, -1,  8,  9,  5,  8),
    duilio=build_skills(5,  10,  5,  0,  0,  5,  5, 10,  5,  5, 10, 10, 10, -1, 10, 10, 10, 10),
    iellwen=build_skills(0,  0,  0,  0, 10,  0,  6,  8,  6,  0,  0, 10,  5,  7,  0, -1, 10, -1),
    faeron=build_skills(10, 10, 10,  0,  0, 10, 10, -1, 10, 10, 10, 10, 10,  0,  0,  0, 10,  0)
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

all_equipment = DotDict(
    alagos=build_equipment(wpn1='bronzeshortsword',  shd1='woodenbuckler', arm1='lightleatherarmor'),
    luana=build_equipment(wpn1='bronzedagger',                             arm1='lightleatherarmor'),
    grindan=build_equipment(wpn1='ironlongsword',    shd1='irontarge',     arm1='mediumbronzearmor'),
    rydalin=build_equipment(wpn1='bronzestaff',                            arm1='mediumleatherarmor'),
    codrif=build_equipment(wpn1='bronzedagger',                            arm1='lightleatherarmor'),
    galen=build_equipment(wpn1='ironaxe',            shd1='irontarge',     arm1='mediumbronzearmor'),
    raiko=build_equipment(wpn1='ironbroadsword',     shd1='ironkite',      arm1='heavyironarmor'),
    kiara=build_equipment(wpn1='silverdagger',                             arm1='lightbronzearmor'),
    luthais=build_equipment(wpn1='bronzestaff',                            arm1='lightironarmor'),
    elias=build_equipment(wpn1='steellongsword',                           arm1='mediumironarmor'),
    onarr=build_equipment(wpn1='steelpoleaxe',       shd1='steelkite',     arm1='heavyironarmor'),
    duilio=build_equipment(wpn1='silvershortsword',  shd1='silvertarge',   arm1='mediumsteelarmor'),
    iellwen=build_equipment(wpn1='steellongsword',                         arm1='mediumironarmor'),
    faeron=build_equipment(wpn1='titaniummace',                            arm1='lighttitaniumarmor')
)


heroes = DotDict(
    alagos=characters.Hero('Alagos',   all_cond.alagos,  all_stats.alagos,  all_skills.alagos,  all_equipment.alagos),
    luana=characters.Hero('Luana',     all_cond.luana,   all_stats.luana,   all_skills.luana,   all_equipment.luana),
    grindan=characters.Hero('Grindan', all_cond.grindan, all_stats.grindan, all_skills.grindan, all_equipment.grindan),
    rydalin=characters.Hero('Rydalin', all_cond.rydalin, all_stats.rydalin, all_skills.rydalin, all_equipment.rydalin),
    codrif=characters.Hero('Codrif',   all_cond.codrif,  all_stats.codrif,  all_skills.codrif,  all_equipment.codrif),
    galen=characters.Hero('Galen',     all_cond.galen,   all_stats.galen,   all_skills.galen,   all_equipment.galen),
    raiko=characters.Hero('Raiko',     all_cond.raiko,   all_stats.raiko,   all_skills.raiko,   all_equipment.raiko),
    kiara=characters.Hero('Kiara',     all_cond.kiara,   all_stats.kiara,   all_skills.kiara,   all_equipment.kiara),
    luthais=characters.Hero('Luthais', all_cond.luthais, all_stats.luthais, all_skills.luthais, all_equipment.luthais),
    elias=characters.Hero('Elias',     all_cond.elias,   all_stats.elias,   all_skills.elias,   all_equipment.elias),
    onarr=characters.Hero('Onarr',     all_cond.onarr,   all_stats.onarr,   all_skills.onarr,   all_equipment.onarr),
    duilio=characters.Hero('Duilio',   all_cond.duilio,  all_stats.duilio,  all_skills.duilio,  all_equipment.duilio),
    iellwen=characters.Hero('Iellwen', all_cond.iellwen, all_stats.iellwen, all_skills.iellwen, all_equipment.iellwen),
    faeron=characters.Hero('Faeron',   all_cond.faeron,  all_stats.faeron,  all_skills.faeron,  all_equipment.faeron)
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


# stats_brownbat = dict(
#     int=Intelligence(4), wil=Willpower(3), dex=Dexterity(14), edu=Endurance(5), str=Strength(8), sta=Stamina(10))
# stats_darkbat = dict(
#     int=Intelligence(4), wil=Willpower(3), dex=Dexterity(12), edu=Endurance(5), str=Strength(9), sta=Stamina(14))

# villains = DotDict(
#     brownbat=Villain('Brown Bat', Level(2), stats_brownbat),
#     darkbat=Villain('Dark Bat',   Level(2), stats_darkbat)
# )

pouchitems = DotDict(
    gold=items.PouchItem("Gold"),
    herbs=items.PouchItem("Herbs"),
    spices=items.PouchItem("Spices")
)

inventory = containers.GearContainer("Backpack")
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

pouch = containers.SmallContainer("Pouch")

party = containers.PartyContainer("Party", 5)
party.add(heroes.alagos, verbose=False)
