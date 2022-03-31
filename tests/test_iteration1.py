import pytest
from evercraft.models.character import *
#### Feature: Create a Character
#get a name
#set a name

#make sure that a character instance can be made
# def test_makeCharacter():
#     assert Character()


# default test case for character class
def test_setCharacterName():
    ret_name = 'Evercraft'
    traits = {
    "name": "Evercraft",
    "alignment": 'good',
    "armor": 10,
    "HP": 12
    }
    c1 = Character(traits)
    assert c1.name == ret_name 

# test case for character name
# def test_getCharacterName():
#     ret_name = "Rufus"
#     traits = {
#     "name": "Rufus",
#     "alignment": 'good',
#     "armor": 10,
#     "HP": 12
#     }
#     c1 = Character(traits)
#     assert c1.get_name()==ret_name

# make character alignment good
def test_makeCharacterAlignGood():
    align_value = 'good'
    traits = {
    "name": "Rufus",
    "alignment": 'good',
    "armor": 10,
    "HP": 12
    }
    c1 = Character(traits)
    assert c1.alignment == align_value

# checking for default values
#if an empty object is passed in, will the AC==10?
# this assumes that the object being passed in is empty, so we can check for
# a default value rather than manually passing one in at creation
def test_defaultArmor():
    c2 = Character()
    assert c2.armor==10

def test_default_hit_points():
    c2 = Character()
    assert c2.HP == 5


# def test_attack_roll20():

#### Feature: Character Can Attack

# > As a combatant I want to be able to attack other combatants
#  so that I can survive to fight another day

# - roll a 20 sided die (don't code the die)
# - roll must meet or beat opponent's armor class to hit
# - a natural roll of 20 always hits

# test for a crit success regardless of enemy AC
def test_create_enemy():
    c1 = Character()
    enemy = Character()
    assert Character.attack(c1, enemy, 20) == "Critical Hit"

#test for a miss with a roll lower than the enemy AC
def test_guess_i_never_miss_huh():
    c1 = Character()
    enemy = Character()
    assert c1.attack(enemy, 9) == "Whiff"

#test for a hit with a result greater than enemy AC
def test_i_slapped_will_smith():
    c1 = Character()
    enemy= Character()
    assert c1.attack(enemy, 10) == "Hit"

#test for a hit with a roll greater than enemy AC
def test_i_slapped_will_smith_harder():
    c1 = Character()
    enemy= Character()
    assert Character.attack(c1, enemy, 14) == "Hit"


# #### Feature: Character Can Be Damaged

# > As an attacker I want to be able to damage my enemies so that they will die and I will live

# - If attack is successful, other character takes 1 point of damage when hit
# this should have the enemy take one damage on a hit that isn't a crit
def test_i_can_deal_damage():
    c1 = Character()
    enemy = Character()
    c1.attack(enemy, 19)
    assert enemy.HP == 4
# - If a roll is a natural 20 then a critical hit is dealt and the damage is doubled

def test_critical_hit():
    c1 = Character()
    enemy = Character()
    c1.attack(enemy, 20)
    assert enemy.HP == 3
    
# when hit points are 0 or fewer, the character is dead

def test_hp_zero():
    traits = {
        "name": "Rufus",
        "alignment": 'good',
        "armor": 12,
        'HP': 1,
        'alive': True
    }
    c1 = Character()
    enemy = Character(traits)
    c1.attack(enemy, 17)
    assert enemy.alive == False

# #### Feature: Character Has Abilities Scores
# > As a character I want to have several abilities so that I am not identical to other characters except in name
def test_character_abilities():
    
    c1 = Character()
    assert c1.abilities


# - Abilities are Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma
def test_character_set_abilities():
    
    c1 = Character()
    assert c1.abilities == {
        "strength" : 10,
        "dexterity" : 10,
        "constitution" : 10,
        "wisdom" : 10,
        "intelligence" : 10,
        "charisma" : 10
    }
# - Abilities range from 1 to 20 and default to 10

# - Abilities have modifiers according to the following table
def test_modifier_18():
    c1 = Character()
    assert c1.modifier(18) == 4

def test_modifier_5():
    c1 = Character()
    assert c1.modifier(5) == -3

# roll = 15
# 
def test_i_can_deal_modified_damage_default():
    c1 = Character()
    enemy = Character()
    c1.attack(enemy, 19)
    assert enemy.HP == 4

# add Strength modifier to:
    ## attack roll and damage dealt
    ## double Strength modifier on critical hits
def test_i_can_deal_modified_damage_15():
    enemy = Character()
    c1 = Character({"abilities" : {"strength" : 15, "dexterity" : 10,"constitution" : 10,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    c1.attack(enemy, 19)
    assert enemy.HP == 2

    ## minimum damage is always 1 (even on a critical hit)
def test_i_can_deal_modified_damage_2():
    enemy = Character()
    c1 = Character({"abilities" : {"strength" : 2, "dexterity" : 10,"constitution" : 10,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    c1.attack(enemy, 19)
    assert enemy.HP == 4

# add Dexterity modifier to armor class
def test_add_dexterity_mod_to_armor():
    enemy = Character({"abilities" : {"strength" : 10, "dexterity" : 15,"constitution" : 10,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    c1 = Character()
    assert c1.attack(enemy, 11) == "Whiff"
    
# add Constitution modifier to hit points (always at least 1 hit point)

def test_i_can_deal_modified_damage_2():
    enemy = Character({"abilities" : {"strength" : 10, "dexterity" : 10,"constitution" : 15,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    c1 = Character()
    c1.attack(enemy, 19)
    assert enemy.HP == 6

def test_character_gains_experience():
    c1 = Character()
    enemy = Character()
    c1.attack(enemy, 18)
    assert c1.XP == 10

def test_character_gains_a_level():
    c1 = Character({"XP":995})
    enemy = Character()
    c1.attack(enemy, 18)
    assert c1.level == 2

# For each level:
# hit points increase by 5 plus Constitution modifier

def test_character_gains_5_HP_on_level_up():
    c1 = Character({"XP":995, "abilities" : {"strength" : 10, "dexterity" : 10,"constitution" : 15,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    enemy = Character()
    c1.attack(enemy, 18)
    assert c1.HP == 12

# 1 is added to attack roll for every even level achieved

def test_character_adds_1_to_attack_roll():
    c1 = Character({"level": 6, "abilities" : {"strength" : 10, "dexterity" : 10,"constitution" : 15,"wisdom" : 10,"intelligence" : 10,"charisma" : 10}})
    enemy = Character()
    c1.attack(enemy, 9)
    assert enemy.HP == 4