
from util import DotDict

# col, row, upgradable, min_mech, metals zijn nog niet verwerkt.

#                     value, min sta, protection, dexterity, stealth, sortering
armor_material = {
    "Leather Armor":   (100,      20,          0,         0,       0,      1000),
    "Bronze Armor":    (600,      35,          3,        -1,      -3,      2000),
    "Iron Armor":     (1100,      50,          6,        -2,      -6,      3000),
    "Steel Armor":    (1600,      65,          9,        -3,      -9,      4000),
    "Silver Armor":   (2100,      80,         12,        -4,     -12,      5000),
    "Titanium Armor": (2600,      20,         12,         0,       0,      6000)
    # "Stealth":        (16,      10,          1,         0,       1)
}
#                     value, min sta, protection, dexterity, stealth, sortering
armor_type = {
    "Light":           (100,       0,          1,         0,       0,       100),
    "Medium":          (300,       5,          2,        -1,      -1,       200),
    "Heavy":           (500,      10,          3,        -2,      -2,       300)
}
#                     value, min sta, protection, dexterity, stealth
armor_upgraded = {
    "":                (1.0,       0,          0,         0,       0,        10),
    "+":               (1.1,       0,          0,         0,       1,        20),
    "++":              (1.2,       0,          0,         1,       2,        30)
}
# hoogste protection mogelijk is 15: Heavy Silver/Titanium Armor /+/++

armors = DotDict(dict(
    emptyarmor=DotDict(dict(
        name="Empty Armor",
        raw="emptyarmor",
        value=0,
        shop=False,
        min_sta=0,
        protection=0,
        dexterity=0,
        stealth=0,
        sort=0
    ))))

for key_material, value_material in armor_material.items():
    for key_type, value_type in armor_type.items():
        for key_upgraded, value_upgraded in armor_upgraded.items():

            raw_key_name = (key_type + key_material + key_upgraded).strip().lower().replace(" ", "")
            price = (value_material[0] + value_type[0]) * (value_material[0] + value_type[0]) / 400

            armors[raw_key_name] = DotDict(dict(
                name=(key_type + " " + key_material + " " + key_upgraded).strip(),
                raw=raw_key_name,

                # berekening value: material * type * upgraded
                value=int(price * value_upgraded[0]),
                shop=True,

                # berekening min sta: material + type
                min_sta=value_material[1] + value_type[1],

                # berekening protection: material + type
                protection=value_material[2] + value_type[2],

                # berekening dexterity: material + type + upgraded
                dexterity=value_material[3] + value_type[3] + value_upgraded[3],

                # berekening stealth: material + type + upgraded
                stealth=value_material[4] + value_type[4] + value_upgraded[4],

                # puur voor sortering
                sort=value_material[5] + value_type[5] + value_upgraded[5]
            ))

# shop uitzetten voor sommige armors
for key, value in armors.items():
    if "+" in key or "titanium" in key:
        value.shop = False
# de laatste van shop is misschien niet nodig. dit kan ook in de shop zelf gecheckt worden. scheelt een variable.

# for i, j in armors.items():
#     print(i, j)
