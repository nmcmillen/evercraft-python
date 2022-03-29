import pytest
from evercraft.models.character import Character
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
    "AC": 10
    }
    c1 = Character(traits)
    assert c1.name == ret_name 

# test case for character name
def test_getCharacterName():
    ret_name = "Rufus"
    traits = {
    "name": "Rufus",
    "alignment": 'good',
    "AC": 10
    }
    c1 = Character(traits)
    assert c1.get_name()==ret_name

# make character alignment good
def test_makeCharacterAlignGood():
    align_value = 'good'
    traits = {
    "name": "Rufus",
    "alignment": 'good',
    "AC": "10"
    }
    c1 = Character(traits)
    assert c1.alignment == align_value

# checking for default values
#if an empty object is passed in, will the AC==10?
# this assumes that the object being passed in is empty, so we can check for
# a default value rather than manually passing one in at creation
def test_defaultAC():
    traits= {}
    c2 = Character(traits)
    assert c2.AC==10