from models.character import Character


Craig = Character({"name":"Craig"})

# player2 = Character({"name":"Joseph", "HP": 3})

print(str(Craig.__dict__))
for num in range(0,900):
    enemy = Character()
    Craig.attack(enemy, 20)
    print(Craig.XP, Craig.level, Craig.HP)