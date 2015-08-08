
from util import DotDict

cloaks = DotDict({
    'emptycloak': DotDict(name="Empty Cloak",                  raw="emptycloak",         value=0,     shop=False, weight=0, protection=0,  sort=0),

    'leathercloak': DotDict(name="Leather Cloak",              raw="leathercloak",       value=100,   shop=True,  weight=1, protection=1,  sort=1),
    'battlecloak': DotDict(name="Battle Cloak",                raw="battlecloak",        value=1000,  shop=True,  weight=2, protection=2,  sort=2),

    'covercloak': DotDict(name="Cover Cloak",                  raw="covercloak",         value=100,   shop=True,  weight=1,                stealth=1, sort=3),
    'covercloak+': DotDict(name="Cover Cloak +",               raw="covercloak+",        value=110,   shop=False, weight=2, protection=1,  stealth=1, sort=4),
    'darkcloak': DotDict(name="Dark Cloak",                    raw="darkcloak",          value=300,   shop=True,  weight=1,                stealth=2, sort=5),
    'darkcloak+': DotDict(name="Dark Cloak +",                 raw="darkcloak+",         value=330,   shop=False, weight=2, protection=1,  stealth=2, sort=6),
    'disguisecloak': DotDict(name="Disguise Cloak",            raw="disguisecloak",      value=700,   shop=True,  weight=1,                stealth=3, sort=7),
    'disguisecloak+': DotDict(name="Disguise Cloak +",         raw="disguisecloak+",     value=770,   shop=False, weight=2, protection=1,  stealth=3, sort=8),
    'concealcloak': DotDict(name="Conceal Cloak",              raw="consealcloak",       value=1500,  shop=True,  weight=1,                stealth=4, sort=9),
    'concealcloak+': DotDict(name="Conceal Cloak +",           raw="consealcloak+",      value=1650,  shop=False, weight=2, protection=1,  stealth=4, sort=10),
    'nightcloak': DotDict(name="Night Cloak",                  raw="nightcloak",         value=3100,  shop=True,  weight=1,                stealth=5, sort=11),
    'nightcloak+': DotDict(name="Night Cloak +",               raw="nightcloak+",        value=3410,  shop=False, weight=2, protection=1,  stealth=5, sort=12),
    'stealthcloak': DotDict(name="Stealth Cloak",              raw="stealthcloak",       value=6300,  shop=True,  weight=1,                stealth=6, sort=13),
    'stealthcloak+': DotDict(name="Stealth Cloak +",           raw="stealthcloak+",      value=6930,  shop=False, weight=2, protection=1,  stealth=6, sort=14),
    'phantomcloak': DotDict(name="Phantom Cloak",              raw="phantomcloak",       value=12700, shop=True,  weight=1,                stealth=7, sort=15),
    'phantomcloak+': DotDict(name="Phantom Cloak +",           raw="phantomcloak+",      value=13970, shop=False, weight=2, protection=1,  stealth=7, sort=16),
    'invisibilitycloak': DotDict(name="Invisibility Cloak",    raw="invisibilitycloak",  value=25500, shop=True,  weight=1,                stealth=8, sort=17),
    'invisibilitycloak+': DotDict(name="Invisibility Cloak +", raw="invisibilitycloak+", value=28050, shop=False, weight=2, protection=1,  stealth=8, sort=18),

    'silkcloak': DotDict(name="Silk Cloak",                    raw="silkcloak",          value=2500,  shop=True,  weight=1,                thief=1, sort=19),
    'silkcloak+': DotDict(name="Silk Cloak +",                 raw="silkcloak+",         value=2750,  shop=False, weight=2, protection=1,  thief=1, sort=20),
    'thievescloak': DotDict(name="Thieves Cloak",              raw="thievescloak",       value=5000,  shop=True,  weight=1,                thief=2, sort=21),
    'thievescloak+': DotDict(name="Thieves Cloak +",           raw="thievescloak+",      value=5500,  shop=False, weight=2, protection=1,  thief=2, sort=22)
})

for cloak in cloaks.values():
    if 'protection' not in cloak:
        cloak.protection = None
    if 'stealth' not in cloak:
        cloak.stealth = None
    if 'thief' not in cloak:
        cloak.thief = None
