
from util import DotDict

gloves = DotDict({
    'emptygloves': DotDict(dict(name="Empty Gloves",     raw="emptygloves",   value=0,   shop=False, weight=0, protection=0, sort=0)),

    'leathergloves': DotDict(dict(name="Leather Gloves", raw="leathergloves", value=100, shop=True,  weight=1, protection=1, sort=1))
})

# for glove in gloves.values():
#     if 'protection' not in glove:
#         glove.protection = None
