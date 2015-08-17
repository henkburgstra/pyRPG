
from util import DotDict

# upgradable, min_mech, metals zijn nog niet verwerkt.

#                   value, min int/str, damage, sortering, col
weapon_material = {
    "Bronze":        (100,           0,      3,       100,   0),
    "Iron":          (900,           1,      6,       200,  32),
    "Steel":        (1700,           2,      9,       300,  64),
    "Silver":       (2500,           3,     12,       400,  96),
    "Titanium":     (3300,           0,     12,       500, 128)
}
#                   value, min int, min str, base hit, damage,   skill, type, sortering, row
weapon_type = {
    "Dagger":        (100,       0,       6,       40,      8, "Sword",    2,      1000,   0),
    "Short Sword":   (200,       0,      10,       50,      9, "Sword",    2,      2000,  32),
    "Longsword":     (400,       0,      14,       60,     10, "Sword",    2,      3000,  64),
    "Broadsword":    (800,       0,      18,       70,     11, "Sword",    2,      4000,  96),

    "Mace":          (150,       0,      12,       30,     14, "Hafted",   3,      1000, 128),
    "Axe":           (300,       0,      15,       40,     15, "Hafted",   3,      2000, 160),
    "Poleaxe":       (600,       0,      18,       50,     16, "Hafted",   3,      3000, 192),
    "Maul":         (1200,       0,      21,       60,     17, "Hafted",   3,      4000, 224),

    "Staff":          (75,       0,       8,       50,      2, "Pole",     1,      1000, 256),
    "Spear":         (150,       0,      11,       60,      3, "Pole",     1,      2000, 288),
    "Pike":          (300,       0,      14,       70,      4, "Pole",     1,      3000, 320),
    "Lance":         (600,       0,      17,       80,      5, "Pole",     1,      4000, 352),

    "Shortbow":      (200,      10,       0,       40,      8, "Missile",  4,      1000, 384),
    "Longbow":       (400,      12,       0,       50,      9, "Missile",  4,      2000, 416),
    "Great Bow":     (800,      14,       0,       60,     10, "Missile",  4,      3000, 448),
    "War Bow":      (1600,      16,       0,       70,     11, "Missile",  4,      4000, 480),

    "Dart":           (50,       4,       0,       30,      2, "Thrown",   2,      1000, 512),
    "Knife":         (100,      10,       0,       40,      3, "Thrown",   2,      2000, 544),
    "Hatchet":       (200,      16,       0,       50,      4, "Thrown",   2,      3000, 576),
    "Javelin":       (400,      22,       0,       60,      5, "Thrown",   2,      4000, 608)
}
#                   value, base hit, damage, sortering
weapon_upgraded = {
    "":              (1.0,        0,      0,        10),
    "+":             (1.1,        5,      0,        20),
    "++":            (1.2,        5,      1,        30)
}
# hoogste damage mogelijk is 30: Silver/Titanium Maul ++

weapons = DotDict(
    emptyweapon=DotDict(
        name="Empty Weapon",
        raw="emptyweapon",
        value=0,
        shop=False,
        skill="Empty",
        min_int=0,
        min_str=0,
        base_hit=0,
        damage=0,
        sort=0,
        col=0,
        row=0
    ))

for key_material, value_material in weapon_material.items():
    for key_type, value_type in weapon_type.items():
        for key_upgraded, value_upgraded in weapon_upgraded.items():

            raw_key_name = (key_material + key_type + key_upgraded).strip().lower().replace(" ", "")
            price = int((value_material[0] + value_type[0]) * (value_material[0] + value_type[0]) / 400)

            weapons[raw_key_name] = DotDict(
                name=(key_material + " " + key_type + " " + key_upgraded).strip(),
                raw=raw_key_name,

                # berekening value: material * type * upgraded
                value=int(price * value_upgraded[0]),
                shop=True,
                skill=value_type[5],

                # berekening min int/str: material * type_const + type
                min_int=value_material[1] * value_type[6] + value_type[1],
                min_str=value_material[1] * value_type[6] + value_type[2],

                # berekening base hit: type + upgraded
                base_hit=value_type[3] + value_upgraded[1],

                # berekening damage: material + type + upgraded
                damage=value_material[2] + value_type[4] + value_upgraded[2],

                # puur voor sortering in de winkels
                sort=value_material[3] + value_type[7] + value_upgraded[3],

                col=value_material[4],
                row=value_type[8]
            )

# min_int op 0 zetten voor close weapons
# min_str op 0 zetten voor range weapons
# shop uitzetten voor sommige weapons
for key, value in weapons.items():
    if value.skill in ("Sword", "Hafted", "Pole"):
        value.min_int = None
    elif value.skill in ("Missile", "Thrown"):
        value.min_str = None
    if '+' in key or 'titanium' in key:
        value.shop = False
# de laatste van shop is misschien niet nodig. dit kan ook in de shop zelf gecheckt worden. scheelt een variable.

# for i, j in weapons.items():
#     if j['skill'] == "Hafted":
#         print(i, j)
