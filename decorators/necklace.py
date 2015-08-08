
from util import DotDict

necklaces = DotDict({
    'emptynecklace': DotDict(name="Empty Necklace", raw="emptynecklace", value=0,   shop=False, weight=0, protection=0, sort=0),

    'testnecklace': DotDict(name="Test Necklace",   raw="testnecklace",  value=100, shop=True,  weight=1, protection=1, sort=1)
})

# for necklace in necklaces:
#     if 'protection' not in necklace:
#         necklace.protection = None
