from evercraft.models.character import Character

class Paladin(Character):
    DEFAULT_VALUES = {
        **Character.DEFAULT_VALUES,
        "HP_multiplier": 8,
    }
    def __init__(self, obj={}):
        for key in self.DEFAULT_VALUES:
            if key in obj:
                setattr(self, key, obj[key])
            else:
                setattr(self, key, self.DEFAULT_VALUES[key])
        if self.alignment == "evil" or self.alignment == "neutral":
            self.alignment = "good"
        # Modify variables based on modifiers at start
        # modified damage calculation and set
        self.attack_damage = max(
            1, self.attack_damage + self.modifier(self.abilities["dexterity"]))
        self.armor = max(
            1, self.armor + self.modifier(self.abilities["dexterity"]))
        self.HP = max(
            1, self.HP + self.modifier(self.abilities["constitution"]))

    def attack(self, target, roll):
        # modified roll calculation and set
        modified_roll = roll + self.modifier(self.abilities["strength"]) + (self.level - 1)
        # critical hit for 20 roll
        if roll == 20:
            if target.alignment == "evil":
                target.HP = target.HP - (self.attack_damage +2)*3
            else:
                target.HP = target.HP - self.attack_damage*2
            if target.HP <= 0:
                target.alive = False
            self.XP += 10
            self.level_check()
            return 'Critical Hit'
        # regular hit for roll under 1
        if modified_roll >= target.armor:
            if target.alignment == "evil":
                target.HP = target.HP - (self.attack_damage +2)
            else:
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