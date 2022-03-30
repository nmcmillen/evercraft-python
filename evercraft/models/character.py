# this is where your character code will go
def modifier(score):
            switcher = {
                1:-5,
                2:-4,
                3:-4,
                4:-3,
                5:-3,
                6:-2,
                7:-2,
                8:-1,
                9:-1,
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

class Character:
    DEFAULT_VALUES = {
        "name": "Billy",
        "alignment": "neutral",
        "armor" : 10,
        "HP" : 5,
        "alive" : True,
        "abilities" : {
            "strength" : 10,
            "dexterity" : 10,
            "constitution" : 10,
            "wisdom" : 10,
            "intelligence" : 10,
            "charisma" : 10
        }
    }
    

    def __init__(self, obj={}):   
        for key in self.DEFAULT_VALUES:
            if key in obj:
                setattr(self, key, obj[key])
            else:
                setattr(self, key, self.DEFAULT_VALUES[key])
                # self.abilties = {
                # strength}
    def attack(target, roll):
        # modified_roll = roll + modifier(self.abilities["strength"])
        # modified_roll = roll + modifier(10)
        if roll == 20:
            target.HP = target.HP - 2
            if target.HP <= 0:
                target.alive = False
            return 'Critical Hit'
        if roll >= target.armor:
            target.HP = target.HP - 1
            if target.HP <= 0:
                target.alive = False
            return 'Hit'
        elif roll < target.armor:
            return "Whiff"
        else:
            return "That doesn't seem to be a number"
    


        # take in roll 15
        # strength: 14 (get modifier score from strength +2)
        # roll score + modifier score = final
        # (15 + 2 = 17 total score)