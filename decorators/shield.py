
from util import DotDict

# col, row, upgradable, min_mech, metals zijn nog niet verwerkt.

#                   value, min str, protection, defense, dexterity, stealth, sortering
shield_material = {
    "Wooden":        (200,       3,          2,       1,        -1,      -1,    100),
    "Bronze":        (500,       6,          4,       2,        -2,      -2,    200),
    "Iron":          (800,       9,          6,       3,        -3,      -3,    300),
    "Steel":        (1100,      12,          8,       4,        -4,      -4,    400),
    "Silver":       (1400,      15,         10,       5,        -5,      -5,    500),
    "Titanium":     (1700,       3,         10,       5,        -1,      -1,    600)
    # "Stealth":      (16,       1,          0,       0,        -1,      -1)
}
#                   value, min str, protection, defense, dexterity, stealth
shield_type = {
    "Buckler":       (100,       3,          1,       5,        -1,      -3,    1000),
    "Targe":         (700,       6,          2,      10,        -2,      -6,    2000),
    "Heater":       (1300,       9,          3,      15,        -3,      -9,    3000),
    "Kite":         (1900,      12,          4,      20,        -4,     -12,    4000),
    "Scutum":       (2500,      15,          5,      25,        -5,     -15,    5000)
}
#                   value, min str, protection, defense, dexterity, stealth
shield_upgraded = {
    "":              (1.0,       0,          0,       0,         0,       0,    10),
    "+":             (1.1,       0,          0,       0,         1,       2,    20),
    "++":            (1.2,       0,          0,       0,         2,       4,    30)
}
# de hoogste protection/defense mogelijk is 15/30: Large Silver/Titanium Scutum /+/++

shields = DotDict(dict(
    emptyshield=DotDict(dict(
        name="Empty Shield",
        raw="emptyshield",
        value=0,
        shop=False,
        min_str=0,
        protection=0,
        defense=0,
        dexterity=0,
        stealth=0,
        sort=0))))

for key_material, value_material in shield_material.items():
    for key_type, value_type in shield_type.items():
        for key_upgraded, value_upgraded in shield_upgraded.items():

            raw_key_name = (key_material + key_type + key_upgraded).strip().lower().replace(" ", "")
            price = (value_material[0] + value_type[0]) * (value_material[0] + value_type[0]) / 900

            shields[raw_key_name] = DotDict(dict(
                name=(key_material + " " + key_type + " " + key_upgraded).strip(),
                raw=raw_key_name,

                # berekening value: material * type * upgraded
                value=int(price * value_upgraded[0]),
                shop=True,

                # berekening min str: material + type
                min_str=value_material[1] + value_type[1],

                # berekening protection: material + type
                protection=value_material[2] + value_type[2],

                # berekening defense: material + type
                defense=value_material[3] + value_type[3],

                # berekening dexterity: material + type + upgraded
                dexterity=value_material[4] + value_type[4] + value_upgraded[4],

                # berekening stealth: material + type + upgraded
                stealth=value_material[5] + value_type[5] + value_upgraded[5],

                # puur voor sortering
                sort=value_material[6] + value_type[6] + value_upgraded[6]
            ))

# shop uitzetten voor sommige armors
for key, value in shields.items():
    if "+" in key or "titanium" in key:
        value.shop = False
# de laatste van shop is misschien niet nodig. dit kan ook in de shop zelf gecheckt worden. scheelt een variable.

# for key, value in shields.items():
#     if "+" in key and "stealth" in key:
#         shields.pop(key)
# je kunt niet verwijderen uit een dict while iterating?

# for i, j in shields.items():
#     print(i, j)