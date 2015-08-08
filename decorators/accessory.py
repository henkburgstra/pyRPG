
from util import DotDict

accessories = DotDict({
    'emptyaccessory': DotDict(name="Empty Accessory", raw="emptyaccessory", value=0,   shop=False, weight=0, protection=0, sort=0),

    'testaccessory': DotDict(name="Test Accessory",   raw="testaccessory",  value=100, shop=True,  weight=1, protection=1, sort=1)
})

# for accessory in accessories:
#     if 'protection' not in accessory:
#         accessory.protection = None
