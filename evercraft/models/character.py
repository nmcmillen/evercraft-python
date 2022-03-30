# this is where your character code will go
TRAITS = {
    "name": "Rufus",
    "alignment": 'good',
    "armor": 12,
    'HP': 8
}

"""CHARACTER_DEF = {
    "name": "Evercraft",
    "alignment": "neutral",
    "armor": 10,
    "hit_point": 5
}"""

class Character:
    name = "Evercraft"
    alignment = "neutral"
    armor = 10
    HP = 5
    alive = True
    abilities = {
        "strength" : 10,
        "dexterity" : 10,
        "constitution" : 10,
        "wisdom" : 10,
        "intelligence" : 10,
        "charisma" : 10
    }
    def __init__(self, obj=None):
        if obj:
            self.name = obj["name"]
            self.alignment = obj["alignment"] 
            self.armor = obj["armor"]
            self.HP = obj["HP"]
     
    def set_name(self, name):
       self.name = name

    def get_name(self):
       return self.name
    
    def attack(target, roll):
        if roll == 20:
            target.HP = target.HP - 2
            if target.HP <= 0:
                target.alive = False
            return 'Critical Hit'
        if roll >= target.armor and roll != 20:
            target.HP = target.HP - 1
            if target.HP <= 0:
                target.alive = False
            return 'Hit'
        elif roll < target.armor:
            return "Whiff"
        else:
            return "That doesn't seem to be a number"


c1 = Character(TRAITS)
c2 = Character()
bad_guy = {
    "name": "Evil Rufus",
    "alignment": 'evil',
    "armor": 12,
    'HP': 8
}
enemy = Character(bad_guy)
print(c1.armor)