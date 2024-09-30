from random import *


def poison(target):
    x = target.get_effects()
    if x.get("poison") != None and x.get("poison")[0] <= 0:
        target.set_mod(target.get_minmod()) - (x.get("poison")[1])
        x["poison"][0] -= 1
    target.set_effects(x)


class Character:
    def __init__(self):
        self.health = 100
        self.damage = 10
        self.defence = 5
        self.effects = {}
        self.attackModmin = -2
        self.attackModmax = 2
        self.basehealth = self.health
        self.basedamage = self.damage
        self.basedefence = self.defence

    def get_base_health(self):
        return self.basehealth

    def get_base_damage(self):
        return self.basedamage

    def get_base_defence(self):
        return self.basedefence

    def set_health(self, health):
        self.health = health

    def set_damage(self, damage):
        self.damage = damage

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage

    def attack(self, target):
        atd = (self.damage + randint(self.attackModmin, self.attackModmax)) - target.get_defence()
        if atd > 0:
            target.set_health(target.get_health() - atd)
            print("You have been hit for " + str(atd))
        else:
            r = randint(1, 2)
            if r == 1:
                print("They clanged off your armor")
            elif r == 2:
                print("They missed")

    def get_defence(self):
        return self.defence

    def set_defence(self, defence):
        self.defence = defence

    def get_effects(self):
        return self.effects

    def set_effects(self, effects):
        self.effects = effects

    def add_effects(self, effect, dur=5, lev=1):
        effectmod = [dur, lev]
        self.effects.update({effect: effectmod})

    def get_minmod(self):
        return attackModmin

    def get_maxmod(self):
        return attackModmax

    def set_mod(self, Modmin="null", Modmax="null"):
        if Modmin == "null":
            Modmin = self.attackModmin
        if Modmax == "null":
            Modmax = self.attackModmax
        self.attackModmin = Modmin
        self.attackModmax = Modmax


class Player(Character):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.magics = []
        self.kills = 0  # You murderer
        self.powers = {}

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_kills(self):
        return self.kills

    def attack(self, target):
        atd = (self.damage + randint(self.attackModmin, self.attackModmax)) - target.get_defence()
        if atd > 0:
            for p in self.powers:
                if p == "poison":
                    dur = self.powers[p] * 4
                    lev = self.powers[p] * 3
                    target.add_effects(p, dur, lev)
            print("You have effected enemy with "+str(self.powers))
            target.set_health(target.get_health() - atd)
            print("You did " + str(atd))
        else:
            r = randint(1, 2)
            if r == 1:
                print("You clanged off their armor")
            elif r == 2:
                print("You missed")
        if target.get_health() <= 0:
            self.kills += 1

    def add_powers(self, power, level):
        self.powers[power] = level

    def get_powers(self):
        return self.powers

    def set_powers(self, powers):
        self.powers = powers


class Enemy(Character):
    def __init__(self):
        super().__init__()
        self.type = "null"
        self.nature = ""

    def get_type(self):
        return self.type

    def get_nature(self):
        return self.nature


class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.type = "Goblin"
        self.health = 25
        self.damage = 10
        self.defense = 5
        self.basehealth = self.health
        self.basedamage = self.damage
        self.basedefence = self.defence
        self.attackModmin = -3
        self.attackModmax = 1
        self.nature = "craven"


class Orc(Enemy):
    def __init__(self):
        super().__init__()
        self.type = "Orc"
        self.health = 50
        self.damage = 25
        self.defense = 10
        self.basehealth = self.health
        self.basedamage = self.damage
        self.basedefence = self.defence
        self.attackModmin = -2
        self.attackModmax = 3
        self.nature = "aggressive"
