import pytest
from evercraft.models.character import Character
from evercraft.models.fighter import Fighter
from evercraft.models.rogue import Rogue
from evercraft.models.monk import Monk
from evercraft.models.paladin import Paladin

def test_class():
    c1 = Fighter()
    assert c1.name == "Billy"

## Human ##
def test_create_human():
    c1 = Character()
    assert c1.race == "human"

def test_create_rogue_human():
    c1 = Rogue()
    assert c1.race == "human"

## Orc ##

# +2 to Strength Modifier, -1 to Intelligence, Wisdom, and Charisma Modifiers
# +2 to Armor Class due to thick hide

def test_mod_rogue_orc_abilities_strength():
    c1 = Rogue({"race" : "orc"})
    c1.is_orc()
    assert c1.abilities["strength"] == 12

def test_mod_rogue_orc_abilities_intelligence():
    c1 = Rogue({"race" : "orc"})
    c1.is_orc()
    assert c1.abilities["intelligence"] == 9

def test_mod_rogue_orc_abilities_armor():
    c1 = Rogue({"race" : "orc"})
    c1.is_orc()
    assert c1.armor == 12

## Dwarf ##

# +1 to Constitution Modifier, -1 to Charisma Modifier

def test_mod_rogue_dwarf_abilities_constitution():
    c1 = Rogue({"race" : "dwarf"})
    c1.is_dwarf()
    assert c1.abilities["constitution"] == 11

def test_mod_rogue_dwarf_abilities_charisma():
    c1 = Rogue({"race" : "dwarf"})
    c1.is_dwarf()
    assert c1.abilities["charisma"] == 9

# doubles Constitution Modifier per level (if positive)


# +2 bonus to attack/damage when attacking orcs (Dwarves hate Orcs)


## Elf ##

# +1 to Dexterity Modifier, -1 to Constitution Modifier
# does adds 1 to critical range for critical hits (20 -> 19-20, 19-20 -> 18-20)
# +2 to Armor Class when being attacked by orcs

## Halfling ##

# +1 to Dexterity Modifier, -1 to Strength Modifier
# +2 to Armor Class when being attacked by non Halfling (they are small and hard to hit)
# cannot have Evil alignment