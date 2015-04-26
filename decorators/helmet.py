
from util import DotDict

helmets = DotDict(dict(
    emptyhelmet=DotDict(dict(
        name="Empty Helmet", raw="emptyhelmet",       value=0,     shop=False, min_sta=0,  protection=0, sort=0)),
    leathercap=DotDict(dict(
        name="Leather Cap", raw="leathercap",         value=100,   shop=True,  min_sta=20, protection=1, sort=1)),
    bronzehelmet=DotDict(dict(
        name="Bronze Helmet", raw="bronzehelmet",     value=300,   shop=True,  min_sta=30, protection=2, sort=2)),
    ironhelmet=DotDict(dict(
        name="Iron Helmet", raw="ironhelmet",         value=900,   shop=True,  min_sta=40, protection=3, sort=3)),
    steelhelmet=DotDict(dict(
        name="Steel Helmet", raw="steelhelmet",       value=2700,  shop=True,  min_sta=50, protection=4, sort=4)),
    silverhelmet=DotDict(dict(
        name="Silver Helmet", raw="silverhelmet",     value=8100,  shop=True,  min_sta=60, protection=5, sort=5)),
    titaniumhelmet=DotDict(dict(
        name="Titanium Helmet", raw="titaniumhelmet", value=24300, shop=False, min_sta=20, protection=5, sort=6))
))

# meer toevoegen uiteindelijk