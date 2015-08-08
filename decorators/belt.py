
from util import DotDict

belts = DotDict({
    'emptybelt': DotDict(name="Empty Belt",     raw="emptybelt",   value=0,   shop=False, weight=0, protection=0, sort=0),

    'leatherbelt': DotDict(name="Leather Belt", raw="leatherbelt", value=100, shop=True,  weight=1, protection=1, sort=1)
})

# for belt in belts:
#     if 'protection' not in belt:
#         belt.protection = None
