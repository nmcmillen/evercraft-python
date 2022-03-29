# this is where your character code will go
TRAITS = {
    "name": "Rufus",
    "alignment": 'good',
    "AC": 10,
    'hit_points': 5
    }

CHARACTER_DEF = {
    "name": "Evercraft",
    "alignment": "neutral",
    "AC": 10,
    "hit_point": 5
}

class Character:
    def __init__(self, object):
        if self.name in TRAITS.keys():
            TRAITS["name"] = self.values.name
        else:
            CHARACTER_DEF["name"] = self.values.name
        self.name = object["name"], default["name"]
        self.alignment = object["alignment"] 
        self.AC = object["AC"]
    
    def set_name(self, name, alignment):
       self.name = name

    def get_name(self):
       return self.name


c1 = Character(TRAITS, CHARACTER_DEF)
#c2 = Character("Bob", "evil")

print(c1.AC) 

