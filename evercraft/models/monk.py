from evercraft.models.character import Character

class Monk(Character):

    DEFAULT_VALUES = {
        **Character.DEFAULT_VALUES,
        "attack_damage": 3,
        "base_HP" : 6
    }
    
    # DEFAULT_VALUES = {
    #     "name": "Billy",
    #     "race": "human",
    #     "alignment": "neutral",
    #     "XP": 0,
    #     "level": 1,
    #     "attack_damage": 3, ## THIS IS NOW 3 INSTEAD OF 1
    #     "armor": 10,
    #     "base_HP": 5,
    #     "HP": 5,
    #     "HP_multiplier": 6,
    #     "alive": True,
    #     "abilities": {
    #         # todo: MAKE A D20 CLASS IF THERE IS TIME TO RANDOMIZE CHARACTER
    #         "strength": 10,
    #         "dexterity": 10,
    #         "constitution": 10,
    #         "wisdom": 10,
    #         "intelligence": 10,
    #         "charisma": 10
    #     }
    # }
    
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
            1, self.armor + self.modifier(self.abilities["dexterity"])+ self.modifier(self.abilities["wisdom"]))
        self.HP = max(
            1, self.HP + self.modifier(self.abilities["constitution"]))
            
    def attack(self, target, roll):
        # modified roll calculation and set
        
        modified_roll = roll + self.modifier(self.abilities["strength"]) + (self.level // 2) + (self.level // 3)
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