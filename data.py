
from util import DotDict
from characters import *
import items
import decorators
import containers

stats_alagos = dict(
    int=Intelligence(18), wil=Willpower(12), dex=Dexterity(15), edu=Endurance(15), str=Strength(15), sta=Stamina(30))
stats_luana = dict(
    int=Intelligence(14), wil=Willpower(10), dex=Dexterity(22), edu=Endurance(10), str=Strength(8), sta=Stamina(20))
stats_grindan = dict(
    int=Intelligence(10), wil=Willpower(8), dex=Dexterity(25), edu=Endurance(20), str=Strength(20), sta=Stamina(40))

stats_brownbat = dict(
    int=Intelligence(4), wil=Willpower(3), dex=Dexterity(14), edu=Endurance(5), str=Strength(8), sta=Stamina(10))
stats_darkbat = dict(
    int=Intelligence(4), wil=Willpower(3), dex=Dexterity(12), edu=Endurance(5), str=Strength(9), sta=Stamina(14))

skills_alagos = dict(
    chm=Chemist(), dip=Diplomat(), lor=Loremaster(), mec=Mechanic(), med=Medic(), mer=Merchant(),
    ran=Ranger(), sci=Scientist(1), stl=Stealth(1), thf=Thief(), trb=Troubadour(1), war=Warrior(3),
    haf=Hafted(1), mis=Missile(3), pol=Pole(), shd=Shield(3), swd=Sword(3), thr=Thrown())
skills_luana = dict(
    chm=Chemist(), dip=Diplomat(), lor=Loremaster(), mec=Mechanic(1), med=Medic(), mer=Merchant(),
    ran=Ranger(), sci=Scientist(), stl=Stealth(3), thf=Thief(3), trb=Troubadour(), war=Warrior(),
    haf=Hafted(-1), mis=Missile(-1), pol=Pole(), shd=Shield(-1), swd=Sword(1), thr=Thrown(2))
skills_grindan = dict(
    chm=Chemist(-1), dip=Diplomat(), lor=Loremaster(), mec=Mechanic(), med=Medic(), mer=Merchant(),
    ran=Ranger(), sci=Scientist(-1), stl=Stealth(1), thf=Thief(-1), trb=Troubadour(), war=Warrior(4),
    haf=Hafted(), mis=Missile(-1), pol=Pole(), shd=Shield(4), swd=Sword(4), thr=Thrown(2))

equipment_alagos = dict(
    wpn=items.Weapon.factory(decorators.weapons.bronzeshortsword),
    shd=items.Shield.factory(decorators.shields.woodenbuckler),
    hlm=items.Helmet.factory(decorators.helmets.emptyhelmet),
    arm=items.Armor.factory(decorators.armors.mediumleatherarmor)
)
equipment_luana = dict(
    wpn=items.Weapon.factory(decorators.weapons.bronzedagger),
    shd=items.Shield.factory(decorators.shields.emptyshield),
    hlm=items.Helmet.factory(decorators.helmets.emptyhelmet),
    arm=items.Armor.factory(decorators.armors.lightleatherarmor)
)
equipment_grindan = dict(
    wpn=items.Weapon.factory(decorators.weapons.ironlongsword),
    shd=items.Shield.factory(decorators.shields.irontarge),
    hlm=items.Helmet.factory(decorators.helmets.emptyhelmet),
    arm=items.Armor.factory(decorators.armors.mediumbronzearmor)
)

heroes = DotDict(dict(
    alagos=Hero('Alagos',   1, Level(1),    500, stats_alagos,  skills_alagos,  equipment_alagos),
    luana=Hero('Luana',     2, Level(1),    500, stats_luana,   skills_luana,   equipment_luana),
    grindan=Hero('Grindan', 3, Level(8), 102000, stats_grindan, skills_grindan, equipment_grindan),
))
villains = DotDict(dict(
    # brownbat=Villain('Brown Bat', Level(2), stats_brownbat),
    # darkbat=Villain('Dark Bat',   Level(2), stats_darkbat)
))

pouchitems = DotDict(dict(
    gold=items.PouchItem("Gold"),
    herbs=items.PouchItem("Herbs"),
    spices=items.PouchItem("Spices")
))

inventory = containers.GearContainer("Backpack")
pouch = containers.SmallContainer("Pouch")
party = containers.PartyContainer("Party", 5)
party.add(heroes.alagos, False)
