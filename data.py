
import util
import stats
import skills
import items
import decorators
import characters
import containers

stats_alagos = dict(
    int=stats.Intelligence(18), wil=stats.Willpower(12), dex=stats.Dexterity(15),
    edu=stats.Endurance(15), str=stats.Strength(15), sta=stats.Stamina(30)
)
stats_luana = dict(
    int=stats.Intelligence(14), wil=stats.Willpower(10), dex=stats.Dexterity(22),
    edu=stats.Endurance(10), str=stats.Strength(8), sta=stats.Stamina(20)
)
stats_grindan = dict(
    int=stats.Intelligence(10), wil=stats.Willpower(8), dex=stats.Dexterity(25),
    edu=stats.Endurance(20), str=stats.Strength(20), sta=stats.Stamina(40)
)

stats_brownbat = dict(
    int=stats.Intelligence(4), wil=stats.Willpower(3), dex=stats.Dexterity(14),
    edu=stats.Endurance(5), str=stats.Strength(8), sta=stats.Stamina(10)
)
stats_darkbat = dict(
    int=stats.Intelligence(4), wil=stats.Willpower(3), dex=stats.Dexterity(12),
    edu=stats.Endurance(5), str=stats.Strength(9), sta=stats.Stamina(14)
)

skills_alagos = dict(
    chm=skills.Chemist(), dip=skills.Diplomat(), lor=skills.Loremaster(), mec=skills.Mechanic(), med=skills.Medic(),
    mer=skills.Merchant(), ran=skills.Ranger(), sci=skills.Scientist(1), stl=skills.Stealth(1), thf=skills.Thief(),
    trb=skills.Troubadour(1), war=skills.Warrior(3), haf=skills.Hafted(1), mis=skills.Missile(3), pol=skills.Pole(),
    shd=skills.Shield(3), swd=skills.Sword(3), thr=skills.Thrown()
)
skills_luana = dict(
    chm=skills.Chemist(), dip=skills.Diplomat(), lor=skills.Loremaster(), mec=skills.Mechanic(1), med=skills.Medic(),
    mer=skills.Merchant(), ran=skills.Ranger(), sci=skills.Scientist(), stl=skills.Stealth(3), thf=skills.Thief(3),
    trb=skills.Troubadour(), war=skills.Warrior(), haf=skills.Hafted(-1), mis=skills.Missile(-1), pol=skills.Pole(),
    shd=skills.Shield(-1), swd=skills.Sword(1), thr=skills.Thrown(2)
)
skills_grindan = dict(
    chm=skills.Chemist(-1), dip=skills.Diplomat(), lor=skills.Loremaster(), mec=skills.Mechanic(), med=skills.Medic(),
    mer=skills.Merchant(), ran=skills.Ranger(), sci=skills.Scientist(-1), stl=skills.Stealth(1), thf=skills.Thief(-1),
    trb=skills.Troubadour(), war=skills.Warrior(4), haf=skills.Hafted(), mis=skills.Missile(-1), pol=skills.Pole(),
    shd=skills.Shield(4), swd=skills.Sword(4), thr=skills.Thrown(2)
)

equipment_alagos = dict(
    wpn=items.Weapon.factory(decorators.weapons.bronzeshortsword),
    shd=items.Shield.factory(decorators.shields.woodenbuckler),
    arm=items.Armor.factory(decorators.armors.mediumleatherarmor)
)
equipment_luana = dict(
    wpn=items.Weapon.factory(decorators.weapons.bronzedagger),
    shd=items.Shield.factory(decorators.shields.emptyshield),
    arm=items.Armor.factory(decorators.armors.lightleatherarmor)
)
equipment_grindan = dict(
    wpn=items.Weapon.factory(decorators.weapons.ironlongsword),
    shd=items.Shield.factory(decorators.shields.irontarge),
    arm=items.Armor.factory(decorators.armors.mediumbronzearmor)
)

heroes = util.DotDict(dict(
    alagos=characters.Hero('Alagos',   1, stats.Level(1),    500, stats_alagos,  skills_alagos,  equipment_alagos),
    luana=characters.Hero('Luana',     2, stats.Level(1),    500, stats_luana,   skills_luana,   equipment_luana),
    grindan=characters.Hero('Grindan', 3, stats.Level(8), 102000, stats_grindan, skills_grindan, equipment_grindan),
))
villains = util.DotDict(dict(
    # brownbat=characters.Villain('Brown Bat', stats.Level(2), stats_brownbat),
    # darkbat=characters.Villain('Dark Bat',   stats.Level(2), stats_darkbat)
))

pouchitems = util.DotDict(dict(
    gold=items.PouchItem("Gold"),
    herbs=items.PouchItem("Herbs"),
    spices=items.PouchItem("Spices")
))

inventory = containers.GearContainer("Backpack")
pouch = containers.SmallContainer("Pouch")
party = containers.PartyContainer("Party", 5)
party.add(heroes.alagos, False)
