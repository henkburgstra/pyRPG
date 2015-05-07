
from util import DotDict

helmets = DotDict({
    'emptyhelmet': DotDict(dict(name="Empty Helmet",               raw="emptyhelmet",       value=0,     shop=False, weight=0, protection=0, sort=0)),

    'leathercap': DotDict(dict(name="Leather Cap",                 raw="leathercap",        value=100,   shop=True,  weight=1, protection=1, sort=1)),
    'bronzehelmet': DotDict(dict(name="Bronze Helmet",             raw="bronzehelmet",      value=1225,  shop=True,  weight=2, protection=2, sort=2)),
    'ironhelmet': DotDict(dict(name="Iron Helmet",                 raw="ironhelmet",        value=3600,  shop=True,  weight=3, protection=3, sort=3)),
    'steelhelmet': DotDict(dict(name="Steel Helmet",               raw="steelhelmet",       value=7225,  shop=True,  weight=4, protection=4, sort=4)),
    'silverhelmet': DotDict(dict(name="Silver Helmet",             raw="silverhelmet",      value=12100, shop=True,  weight=5, protection=5, sort=5)),
    'titaniumhelmet': DotDict(dict(name="Titanium Helmet",         raw="titaniumhelmet",    value=24300, shop=False, weight=1, protection=5, sort=6)),

    'helmofknowledge': DotDict(dict(name="Helm of Knowledge",      raw="helmofknowledge",   value=5500,  shop=True,  weight=2, protection=1, intelligence=2, sort=7)),
    'helmofknowledge+': DotDict(dict(name="Helm of Knowledge +",   raw="helmofknowledge+",  value=6050,  shop=False, weight=3, protection=2, intelligence=2, sort=8)),
    'helmofwisdom': DotDict(dict(name="Helm of Wisdom",            raw="helmofwisdom",      value=5500,  shop=True,  weight=2, protection=1, willpower=2,    sort=9)),
    'helmofwisdom+': DotDict(dict(name="Helm of Wisdom +",         raw="helmofwisdom+",     value=6050,  shop=False, weight=3, protection=2, willpower=2,    sort=10)),
    'helmofcharisma': DotDict(dict(name="Helm of Charisma",        raw="helmofcharisma",    value=6600,  shop=True,  weight=2, protection=1, diplomat=1,     sort=11)),
    'helmofcharisma+': DotDict(dict(name="Helm of Charisma +",     raw="helmofcharisma+",   value=7260,  shop=False, weight=3, protection=2, diplomat=1,     sort=12)),
    'helmofinsight': DotDict(dict(name="Helm of Insight",          raw="helmofinsight",     value=7700,  shop=True,  weight=2, protection=1, loremaster=1,   sort=13)),
    'helmofinsight+': DotDict(dict(name="Helm of Insight +",       raw="helmofinsight+",    value=8470,  shop=False, weight=3, protection=2, loremaster=1,   sort=14)),
    'helmofcognizance': DotDict(dict(name="Helm of Cognizance",    raw="helmofcognizance",  value=9900,  shop=True,  weight=2, protection=1, scientist=1,    sort=15)),
    'helmofcognizance+': DotDict(dict(name="Helm of Cognizance +", raw="helmofcognizance+", value=10890, shop=False, weight=3, protection=2, scientist=1,    sort=16)),
    'helmoftempests': DotDict(dict(name="Helm of Tempests",        raw="helmoftempests",    value=8800,  shop=True,  weight=2, protection=1, warrior=1,      sort=17)),
    'helmoftempests+': DotDict(dict(name="Helm of Tempests +",     raw="helmoftempests+",   value=9680,  shop=False, weight=3, protection=2, warrior=1,      sort=18))
})

for value1 in helmets.values():
    if 'intelligence' not in value1:
        value1.intelligence = None
    if 'willpower' not in value1:
        value1.willpower = None
    if 'diplomat' not in value1:
        value1.diplomat = None
    if 'loremaster' not in value1:
        value1.loremaster = None
    if 'scientist' not in value1:
        value1.scientist = None
    if 'warrior' not in value1:
        value1.warrior = None
