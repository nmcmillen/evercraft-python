import pytest
from evercraft.models.character import Character
from evercraft.models.fighter import Fighter
from evercraft.models.rogue import Rogue
from evercraft.models.monk import Monk
from evercraft.models.paladin import Paladin

#### Feature: Characters Have Classes

#As a player I want a character to have a class that customizes its capabilities so that I can play more interesting characters

def test_class():
    c1 = Fighter()
    assert c1.name == "Billy"

## Fighter ##

# attacks roll is increased by 1 for every level instead of every other level
def test_character_adds_1_to_attack_roll():
    c1 = Fighter({"level": 2, "abilities" : {"strength" : 10, "dexterity" : 10,"constitution" : 15,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    enemy = Character()
    c1.attack(enemy, 9) # default enemy AC is 10
    assert enemy.HP == 4

# has 10 hit points per level instead of 5

def test_character_gains_10_HP_on_level_up():
    c1 = Fighter({"XP":995, "abilities" : {"strength" : 10, "dexterity" : 10,"constitution" : 15,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    enemy = Character()
    c1.attack(enemy, 18)
    assert c1.HP == 17

## Rogue ##

# does triple damage on critical hits
def test_triple_damage():
    c1 = Rogue()
    enemy = Character()
    c1.attack(enemy, 20)
    assert enemy.HP == 2

# ignores an opponents Dexterity modifier (***if positive***) to Armor Class when attacking
def test_ignore_enemy_dex():
    c1 = Rogue()
    enemy = Character({"abilities" : {"strength" : 10, "dexterity" : 20,"constitution" : 10,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    c1.attack(enemy, 11)
    assert enemy.HP == 4
# adds Dexterity modifier to attacks instead of Strength
def test_dexterity_instead_of_strength():
    enemy = Character()
    c1 = Rogue({"abilities" : {"strength" : 10, "dexterity" : 15,"constitution" : 10,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    c1.attack(enemy, 19)
    assert enemy.HP == 2

# cannot have Good alignment
def test_no_good_rogue():
    c1 = Rogue({"alignment":"good"})
    assert c1.alignment == "neutral"

## Monk ##

# has 6 hit point per level instead of 5
def test_6_HP_on_level_up():
    c1 = Monk({"XP":995, "abilities" : {"strength" : 10, "dexterity" : 10,"constitution" : 15,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    enemy = Character()
    c1.attack(enemy, 18)
    assert c1.HP == 13

# does 3 points of damage instead of 1 when successfully attacking
def test_deal_3_damage():
    c1 = Monk()
    enemy = Character()
    c1.attack(enemy, 19)
    assert enemy.HP == 2

# adds Wisdom modifier (if positive) to Armor Class in addition to Dexterity
def test_add_wisdom_mod_to_armor():
    c1 = Monk({"abilities" : {"strength" : 10, "dexterity" : 10,"constitution" : 10,"wisdom" : 15,"intelligence" : 10,"charisma" : 10}})
    enemy = Character()
    assert enemy.attack(c1, 11) == "Whiff"

# attack roll is increased by 1 every 2nd and 3rd level (FIZZBUZZ)
def test_adds_1_to_attack_roll_2_and_3():
    c1 = Monk({"level": 6, "abilities" : {"strength" : 10, "dexterity" : 10,"constitution" : 15,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    enemy = Character()
    c1.attack(enemy, 9)
    assert enemy.HP == 2

def test_adds_1_to_attack_roll_2():
    c1 = Monk({"level": 2, "abilities" : {"strength" : 10, "dexterity" : 10,"constitution" : 15,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    enemy = Character()
    c1.attack(enemy, 9)
    assert enemy.HP == 2

def test_adds_1_to_attack_roll_3():
    c1 = Monk({"level": 3, "abilities" : {"strength" : 10, "dexterity" : 10,"constitution" : 15,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    enemy = Character()
    c1.attack(enemy, 9)
    assert enemy.HP == 2

def test_not_devisable_by_2_or_3():
    c1 = Monk({"level": 7, "abilities" : {"strength" : 10, "dexterity" : 10,"constitution" : 15,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    enemy = Character()
    c1.attack(enemy, 13)
    assert enemy.HP == 2

## Paladin ##

# has 8 hit points per level instead of 5
def test_8_HP_on_level_up():
    c1 = Paladin({"XP":995, "abilities" : {"strength" : 10, "dexterity" : 10,"constitution" : 15,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    enemy = Character()
    c1.attack(enemy, 18)
    assert c1.HP == 15

# +2 to attack and damage when attacking Evil characters
def test_plus_2_damage_on_evil():
    c1 = Paladin()
    enemy = Character({"alignment":"evil"})
    c1.attack(enemy, 19)
    assert enemy.HP == 2

# does triple damage when critting on an Evil character (i.e. add the +2 bonus for a regular attack, and then triple that)
def test_plus_2_times_3_damage_on_evil():
    c1 = Paladin()
    enemy = Character({"alignment":"evil", "HP":10})
    c1.attack(enemy, 20)
    assert enemy.HP == 1

# attacks roll is increased by 1 for every level instead of every other level
def test_character_adds_1_to_attack_roll_paladin():
    c1 = Paladin({"level": 2, "abilities" : {"strength" : 10, "dexterity" : 10,"constitution" : 15,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    enemy = Character()
    c1.attack(enemy, 9) # default enemy AC is 10
    assert enemy.HP == 4

# can only have Good alignment

def test_good_paladin():
    c1 = Paladin({"alignment":"neutral"})
    assert c1.alignment == "good"

def test_good_paladin_no_evil():
    c1 = Paladin({"alignment":"evil"})
    assert c1.alignment == "good"