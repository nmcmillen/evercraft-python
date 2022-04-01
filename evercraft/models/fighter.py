from evercraft.models.character import Character

class Fighter(Character):
    
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
    
    def level_check(self):
        self.level = 1 + self.XP//1000
        self.HP = self.base_HP+(10*(self.level-1)) + self.modifier(self.abilities["constitution"])