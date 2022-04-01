from evercraft.models.character import Character

class Fighter(Character):

    DEFAULT_VALUES = {
        **Character.DEFAULT_VALUES,
        "HP_multiplier": 10
    }
    
    def attack(self, target, roll):
        # modified roll calculation and set
        modified_roll = roll + self.modifier(self.abilities["strength"]) + (self.level -1) ## no longer need odd/even
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