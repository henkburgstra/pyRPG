
from util import DotDict

# prijzen nog bepalen

boots = DotDict({
    'emptyboots': DotDict(dict(name="Empty Boots",             raw="emptyboots",      value=0,    shop=False, weight=0, protection=0, sort=0)),

    'leatherboots': DotDict(dict(name="Leather Boots",         raw="leatherboots",    value=100,  shop=True,  weight=1, protection=1, sort=1)),
    'bronzeboots': DotDict(dict(name="Bronze Boots",           raw="bronzeboots",     value=200,  shop=True,  weight=2, protection=2, sort=2)),
    'ironboots': DotDict(dict(name="Iron Boots",               raw="ironboots",       value=400,  shop=True,  weight=3, protection=3, sort=3)),
    'steelboots': DotDict(dict(name="Steel Boots",             raw="steelboots",      value=800,  shop=True,  weight=4, protection=4, sort=4)),
    'silverboots': DotDict(dict(name="Silver Boots",           raw="silverboots",     value=1600, shop=True,  weight=5, protection=5, sort=5)),
    'titaniumboots': DotDict(dict(name="Titanium Boots",       raw="titaniumboots",   value=3200, shop=False, weight=1, protection=5, sort=6)),

    'bootsofmotion': DotDict(dict(name="Boots of Motion",      raw="bootsofmotion",   value=1000, shop=True,  weight=2, protection=1, movepoints=1, sort=7)),
    'bootsofmotion+': DotDict(dict(name="Boots of Motion +",   raw="bootsofmotion+",  value=1100, shop=False, weight=3, protection=2, movepoints=1, sort=8)),
    'bootsofspeed': DotDict(dict(name="Boots of Speed",        raw="bootsofspeed",    value=2000, shop=True,  weight=2, protection=1, movepoints=2, sort=9)),
    'bootsofspeed+': DotDict(dict(name="Boots of Speed +",     raw="bootsofspeed+",   value=2200, shop=False, weight=3, protection=2, movepoints=2, sort=10)),
    'woodsmansboots': DotDict(dict(name="Woodsman's Boots",    raw="woodsmansboots",  value=1000, shop=True,  weight=2, protection=1, ranger=1,     sort=11)),
    'woodsmansboots+': DotDict(dict(name="Woodsman's Boots +", raw="woodsmansboots+", value=1100, shop=False, weight=3, protection=2, ranger=1,     sort=12)),
    'silenceboots': DotDict(dict(name="Silence Boots",         raw="silenceboots",    value=1000, shop=True,  weight=2, protection=1, stealth=1,    sort=13)),
    'silenceboots+': DotDict(dict(name="Silence Boots +",      raw="silenceboots+",   value=1100, shop=False, weight=3, protection=2, stealth=1,    sort=14)),
})

for boot in boots.values():
    if 'movepoints' not in boot:
        boot.movepoints = None
    if 'ranger' not in boot:
        boot.ranger = None
    if 'stealth' not in boot:
        boot.stealth = None
