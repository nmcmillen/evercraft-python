from evercraft.models.character import Character

class Rogue(Character):
    def __init__(self, obj={}):
        for key in self.DEFAULT_VALUES:
            if key in obj:
                setattr(self, key, obj[key])
            else:
                setattr(self, key, self.DEFAULT_VALUES[key])
        if self.alignment == "good":
            self.alignment = "neutral"
        # Modify variables based on modifiers at start
        # modified damage calculation and set
        self.attack_damage = max(
            1, self.attack_damage + self.modifier(self.abilities["dexterity"]))
        self.armor = max(
            1, self.armor + self.modifier(self.abilities["dexterity"]))
        self.HP = max(
            1, self.HP + self.modifier(self.abilities["constitution"]))

    def attack(self, target, roll):
        if self.modifier(target.abilities["dexterity"]) > 0:
            target.armor = target.armor - self.modifier(target.abilities["dexterity"])
        # modified roll calculation and set
        modified_roll = roll + self.modifier(self.abilities["dexterity"]) + (self.level // 2)
        # critical hit for 20 roll
        if roll == 20:
            target.HP = target.HP - self.attack_damage*3
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