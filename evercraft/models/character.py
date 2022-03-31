# this is where your character code will go
import random

# todo: MAKE A D20 CLASS IF THERE IS TIME TO RANDOMIZE CHARACTER
# "strength" : random.randint(0, 20),
# "dexterity" : random.randint(0, 20),
# "constitution" : random.randint(0, 20),
# "wisdom" : random.randint(0, 20),
# "intelligence" : random.randint(0, 20),
# "charisma" : random.randint(0, 20)
# attack_damage = max(1, (1 + self.modifier(self.abilities["strength"]))
# HP = max(1, (1 + self.modifier(self.abilities["constitution"]))


class Character:
    DEFAULT_VALUES = {
        "name": "Billy",
        "alignment": "neutral",
        "XP": 0,
        "level": 1,
        "attack_damage": 1,
        "armor": 10,
        "base_HP": 5,
        "HP": 5,
        "alive": True,
        "abilities": {
            # todo: MAKE A D20 CLASS IF THERE IS TIME TO RANDOMIZE CHARACTER
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "wisdom": 10,
            "intelligence": 10,
            "charisma": 10
        }
    }

    def modifier(self, score):
        switcher = {
            1: -5,
            2: -4,
            3: -4,
            4: -3,
            5: -3,
            6: -2,
            7: -2,
            8: -1,
            9: -1,
            10: 0,
            11: 0,
            12: 1,
            13: 1,
            14: 2,
            15: 2,
            16: 3,
            17: 3,
            18: 4,
            19: 4,
            20: 5
        }
        return switcher.get(score)

    def __init__(self, obj={}):
        for key in self.DEFAULT_VALUES:
            if key in obj:
                setattr(self, key, obj[key])
            else:
                setattr(self, key, self.DEFAULT_VALUES[key])
        # Modify variables based on modifiers at start
        # modified damage calculation and set
        self.attack_damage = max(
            1, self.attack_damage + self.modifier(self.abilities["strength"]))
        self.armor = max(
            1, self.armor + self.modifier(self.abilities["dexterity"]))
        self.HP = max(
            1, self.HP + self.modifier(self.abilities["constitution"]))

    def attack(self, target, roll):
        # modified roll calculation and set
        modified_roll = roll + self.modifier(self.abilities["strength"]) + (self.level // 2)
        # critical hit for 20 roll
        if roll == 20:
            target.HP = target.HP - self.attack_damage*2
            if target.HP <= 0:
                target.alive = False
            self.XP += 10
            self.level_check()
            return 'Critical Hit'
        # regular hit for roll under 1
        if modified_roll >= target.armor:
            target.HP = target.HP - self.attack_damage
            if target.HP <= 0:
                target.alive = False
            self.XP += 10
            self.level_check()
            return 'Hit'
        elif modified_roll < target.armor:
            return "Whiff"
        else:
            return "That doesn't seem to be a number"

    def level_check(self):
        self.level = 1 + self.XP//1000
        self.HP = self.base_HP+(5*(self.level-1)) + self.modifier(self.abilities["constitution"])

        
        
        
        
        
        # take in roll 15
        # strength: 14 (get modifier score from strength +2)
        # roll score + modifier score = final
        # (15 + 2 = 17 total score)
