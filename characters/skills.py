
from characters.stats import Stat


class Skill(Stat):

    TRAININGSCOSTS = (200, 80, 120, 160, 200, 240, 280, 320, 360, 400, "Max")
    MAXIMUM = 10

    def __init__(self, name, raw, upgrade, quantity):
        super().__init__(name, raw, self.MAXIMUM, upgrade, quantity)

    def positive_quantity(self):
        """ Deze is voor hero stats"""
        if self.quantity >= 1:
            return True
        return False


class Chemist(Skill):
    def __init__(self, quantity):
        super().__init__("Chemist", "chm", 1200, quantity)
        self.BMP = 'resources/icons/skills/chemist.png'
        self.DESC = "Allows the character to manufacture various potions out of Herbs, Minerals and Chemicals. " \
                    "A higher Chemist rank means a higher chance to successfully create a potion."


class Diplomat(Skill):
    def __init__(self, quantity):
        super().__init__("Diplomat", "dip", 400, quantity)
        self.BMP = 'resources/icons/skills/diplomat.png'
        self.DESC = "The higher the Diplomat rank, the lower are the conditions of new heroes who wants to join " \
                    "the party. For every 1 Diplomat rank gained, 1% lower conditions. Cumulative for all characters."


class Loremaster(Skill):
    def __init__(self, quantity):
        super().__init__("Loremaster", "lor", 600, quantity)
        self.BMP = 'resources/icons/skills/loremaster.png'
        self.DESC = "Lowers the XP needed for training Stats(?), Skills and Science. " \
                    "For every 1 Loremaster rank gained, 1% less XP is needed."


class Mechanic(Skill):
    def __init__(self, quantity):
        super().__init__("Mechanic", "mec", 400, quantity)
        self.BMP = 'resources/icons/skills/mechanic.png'
        self.DESC = "Allows the character to upgrade inventory with metals. The process also costs gold. " \
                    "A higher Mechanic rank means a higher chance to successfully upgrade an item. " \
                    "The item is destroyed when upgrade is unsuccessful."


class Medic(Skill):
    def __init__(self, quantity):
        super().__init__("Medic", "med", 800, quantity)
        self.BMP = 'resources/icons/skills/medic.png'
        self.DESC = "Allows the character to heal another character in combat. " \
                    "Character may use herbs to double the amount of damage restored. " \
                    "A higher Medic rank means more restoration of damage."


class Merchant(Skill):
    def __init__(self, quantity):
        super().__init__("Merchant", "mer", 600, quantity)
        self.BMP = 'resources/icons/skills/merchant.png'
        self.DESC = "The higher the Merchant rank, the lower the prices when buying (and the higher the " \
                    "prices when selling) in shops. For every 1 Merchant rank gained, 1% extra gold in your " \
                    "favor. Cumulative for all characters."


class Ranger(Skill):
    def __init__(self, quantity):
        super().__init__("Ranger", "ran", 800, quantity)
        self.BMP = 'resources/icons/skills/ranger.png'
        self.DESC = "Helps to increase the amount of Herbs, Minerals, Chemicals, Metals, Crystals " \
                    "and Forgestones when searching for materials. More characters " \
                    "with this skill will help to find even more materials."


class Scientist(Skill):
    def __init__(self, quantity):
        super().__init__("Scientist", "sci", 1200, quantity)
        self.BMP = 'resources/icons/skills/scientist.png'
        self.DESC = "At the moment, Scientist does nothing."


class Stealth(Skill):
    def __init__(self, quantity):
        super().__init__("Stealth", "stl", 400, quantity)
        self.BMP = 'resources/icons/skills/stealth.png'
        self.DESC = "Makes it easier to flee from combat. For every 1 Stealth rank gained, 1% more chance " \
                    "to flee. Cumulative for all characters. Also when in combat, for every 2 Stealth ranks " \
                    "gained, the enemy thinks the character is 1 position further away."


class Thief(Skill):
    def __init__(self, quantity):
        super().__init__("Thief", "thf", 800, quantity)
        self.BMP = 'resources/icons/skills/thief.png'
        self.DESC = "Improves character's chance to hit and increases damage " \
                    "inflicted FROM BEHIND in combat. For every 1 Thief rank gained, " \
                    "2% more chance to hit and 3% more damage."


class Troubadour(Skill):
    def __init__(self, quantity):
        super().__init__("Troubadour", "trb", 800, quantity)
        self.BMP = 'resources/icons/skills/troubadour.png'
        self.DESC = "Allows character to play and sing inspirationally, improving your party's chance " \
                    "to hit in combat and reducing the enemy's chance to hit. For every 1 Troubadour " \
                    "rank gained, 2% more chance to hit."


class Warrior(Skill):
    def __init__(self, quantity):
        super().__init__("Warrior", "war", 800, quantity)
        self.BMP = 'resources/icons/skills/warrior.png'
        self.DESC = "Improves base hit of character's weapon. Especially weapons with a low base hit. " \
                    "It also allows the possibility of scoring critical hits in combat. For every 1 " \
                    "Warrior rank gained, 2% extra chance for a critical hit. And overall, it improves " \
                    "combat damage and defenses."

    def bonus(self, wpn):
        if self.positive_quantity() and "empty" not in wpn.RAW:
            return round((47 - ((wpn.BASE_HIT / 10) * 5)) * (self.total / 10))


class Hafted(Skill):
    def __init__(self, quantity):
        super().__init__("Hafted", "haf", 320, quantity)
        self.BMP = 'resources/icons/skills/hafted.png'
        self.DESC = "Improves character's chance to hit and increseas damage inflicted with Hafted weapons in " \
                    "combat. For every 1 Hafted rank gained, 2% more chance to hit and 1% more damage."


class Missile(Skill):
    def __init__(self, quantity):
        super().__init__("Missile", "mis", 480, quantity)
        self.BMP = 'resources/icons/skills/missile.png'
        self.DESC = "Improves character's chance to hit and increseas damage inflicted with Missile weapons in " \
                    "combat. For every 1 Missile rank gained, 2% more chance to hit and 1% more damage."


class Pole(Skill):
    def __init__(self, quantity):
        super().__init__("Pole", "pol", 320, quantity)
        self.BMP = 'resources/icons/skills/pole.png'
        self.DESC = "Improves character's chance to hit and increseas damage inflicted with Pole weapons in combat. " \
                    "For every 1 Pole rank gained, 2% more chance to hit and 1% more damage."


class Shield(Skill):
    def __init__(self, quantity):
        super().__init__("Shield", "shd", 400, quantity)
        self.BMP = 'resources/icons/skills/shield.png'
        self.DESC = "Improves character's defenses when wearing a shield in combat. A shield doesn't defend " \
                    "character's back."


class Sword(Skill):
    def __init__(self, quantity):
        super().__init__("Sword", "swd", 480, quantity)
        self.BMP = 'resources/icons/skills/sword.png'
        self.DESC = "Improves character's chance to hit and increseas damage inflicted with all types of swords " \
                    "and daggers in combat. For every 1 Sword rank gained, 2% more chance to hit and 1% more damage."


class Thrown(Skill):
    def __init__(self, quantity):
        super().__init__("Thrown", "thr", 320, quantity)
        self.BMP = 'resources/icons/skills/thrown.png'
        self.DESC = "Improves character's chance to hit and increseas damage inflicted with Thrown weapons in " \
                    "combat. For every 1 Thrown rank gained, 2% more chance to hit and 1% more damage."
