
from util import DotDict

boots = DotDict({
    'emptyboots': DotDict(dict(name="Empty Boots",     raw="emptyboots",   value=0,   shop=False, weight=0, protection=0, sort=0)),

    'leatherboots': DotDict(dict(name="Leather Boots", raw="leatherboots", value=100, shop=True,  weight=1, protection=1, sort=1))
})

# for boot in boots.values():
#     if 'protection' not in boot:
#         boot.protection = None
