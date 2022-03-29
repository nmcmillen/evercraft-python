# this is where your character code will go
traits = {
    "name": "Rufus",
    "alignment": 'good',
    "AC": 10
    }
class Character:
    
    def __init__(self, object):
        self.name = object["name"]
        self.alignment = object["alignment"]
        self.AC = object["AC"]
    
    def set_name(self, name, alignment):
       self.name = name

    def get_name(self):
       return self.name


c1 = Character(traits)
# c2 = Character("Bob", "evil")

print(c1.AC)

c2 = Character(traits)
print(c2.AC)