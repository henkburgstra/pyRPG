
from util import DotDict

# col, row, upgradable, min_mech, metals zijn nog niet verwerkt.

#                   value, min int/str, damage, sortering
weapon_material = {
    "Bronze":          (1,           0,      3,       100),
    "Iron":            (3,           1,      6,       200),
    "Steel":           (9,           2,      9,       300),
    "Silver":         (27,           3,     12,       400),
    "Titanium":       (81,           0,     12,       500)
}
#                   value, min int, min str, base hit, damage,   skill, type, sortering
weapon_type = {
    "Dagger":        (100,       0,       6,       40,      8, "Sword",    2,      1000),
    "Short Sword":   (200,       0,      10,       50,      9, "Sword",    2,      2000),
    "Longsword":     (400,       0,      14,       60,     10, "Sword",    2,      3000),
    "Broadsword":    (800,       0,      18,       70,     11, "Sword",    2,      4000),

    "Mace":          (150,       0,      12,       30,     14, "Hafted",   3,      1000),
    "Axe":           (300,       0,      15,       40,     15, "Hafted",   3,      2000),
    "Poleaxe":       (600,       0,      18,       50,     16, "Hafted",   3,      3000),
    "Maul":         (1200,       0,      21,       60,     17, "Hafted",   3,      4000),

    "Staff":          (75,       0,       8,       50,      2, "Pole",     1,      1000),
    "Spear":         (150,       0,      11,       60,      3, "Pole",     1,      2000),
    "Pike":          (300,       0,      14,       70,      4, "Pole",     1,      3000),
    "Lance":         (600,       0,      17,       80,      5, "Pole",     1,      4000),

    "Shortbow":      (200,      10,       0,       40,      8, "Missile",  4,      1000),
    "Longbow":       (400,      12,       0,       50,      9, "Missile",  4,      2000),
    "Great Bow":     (800,      14,       0,       60,     10, "Missile",  4,      3000),
    "War Bow":      (1600,      16,       0,       70,     11, "Missile",  4,      4000),

    "Dart":           (50,       4,       0,       30,      2, "Thrown",   2,      1000),
    "Knife":         (100,      10,       0,       40,      3, "Thrown",   2,      2000),
    "Hatchet":       (200,      16,       0,       50,      4, "Thrown",   2,      3000),
    "Javelin":       (400,      22,       0,       60,      5, "Thrown",   2,      4000)
}
#                   value, base hit, damage, sortering
weapon_upgraded = {
    "":              (1.0,        0,      0,        10),
    "+":             (1.1,        5,      0,        20),
    "++":            (1.2,        5,      1,        30)
}
# hoogste damage mogelijk is 30: Silver/Titanium Maul ++

weapons = DotDict(dict(
    emptyweapon=DotDict(dict(
        name="Empty Weapon",
        raw="emptyweapon",
        value=0,
        shop=False,
        skill="Empty",
        min_int=0,
        min_str=0,
        base_hit=0,
        damage=0,
        sort=0))))

for key_material, value_material in weapon_material.items():
    for key_type, value_type in weapon_type.items():
        for key_upgraded, value_upgraded in weapon_upgraded.items():

            raw_key_name = (key_material + key_type + key_upgraded).strip().lower().replace(" ", "")

            weapons[raw_key_name] = dict(
                name=(key_material + " " + key_type + " " + key_upgraded).strip(),
                raw=raw_key_name,

                # berekening value: material * type * upgraded
                value=int(value_material[0] * value_type[0] * value_upgraded[0]),
                shop=True,
                skill=value_type[5],

                # berekening min int/str: material * type_const + type
                min_int=value_material[1] * value_type[6] + value_type[1],
                min_str=value_material[1] * value_type[6] + value_type[2],

                # berekening base hit: type + upgraded
                base_hit=value_type[3] + value_upgraded[1],

                # berekening damage: material + type + upgraded
                damage=value_material[2] + value_type[4] + value_upgraded[2],

                # puur voor sortering
                sort=value_material[3] + value_type[7] + value_upgraded[3]
            )
            weapons[raw_key_name] = DotDict(weapons[raw_key_name])

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
