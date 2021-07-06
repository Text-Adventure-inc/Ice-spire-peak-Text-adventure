### for level up after character creation

import character_creation
def level_up():
    new_level = input("congratulations you've leveled up would you like to take a level in fighter, wizard or ranger")
    if new_level == "fighter":
        fighter_level = character_creation.fighter_level+1
        character_creation.total_level = character_creation.total_level+1
        character_creation.Hp = character_creation.Hp + 10+ character_creation.ConstitutionMod
    elif new_level == "ranger":
        ranger_level = character_creation.ranger_level+1
        character_creation.total_level = character_creation.total_level+1
        character_creation.Hp = character_creation.Hp + 8+ character_creation.ConstitutionMod
    elif new_level == "wizard":
        wizard_level = character_creation.wizard_level+1
        character_creation.total_level = character_creation.total_level+1
        character_creation.Hp = character_creation.Hp + 6 + character_creation.ConstitutionMod
### needs to be changed to follow the sexy code rules
if character_creation.exp >= 300 and character_creation.total_level <2:
    level_up()

if character_creation.exp >= 900 and character_creation.total_level <3:
    level_up()

if character_creation.exp >= 2700 and character_creation.total_level <4:
    level_up()

if character_creation.exp >= 6500 and character_creation.total_level <5:
    level_up()

if character_creation.exp >= 14000 and character_creation.total_level <6:
    level_up()

if character_creation.exp >= 23000 and character_creation.total_level <7:
    level_up()

if character_creation.exp >= 34000 and character_creation.total_level <8:
    level_up()

if character_creation.exp >= 48000 and character_creation.total_level <9:
    level_up()

if character_creation.exp >= 64000 and character_creation.total_level <10:
    level_up()

if character_creation.exp >= 85000 and character_creation.total_level <11:
    level_up()

if character_creation.exp >= 100000 and character_creation.total_level <12:
    level_up()

if character_creation.exp >= 120000 and character_creation.total_level <13:
    level_up()

if character_creation.exp >= 140000 and character_creation.total_level <14:
    level_up()

if character_creation.exp >= 165000 and character_creation.total_level <15:
    level_up()

if character_creation.exp >= 195000 and character_creation.total_level <16:
    level_up()

if character_creation.exp >= 195000 and character_creation.total_level <17:
    level_up()

if character_creation.exp >= 225000 and character_creation.total_level <18:
    level_up()

if character_creation.exp >= 265000 and character_creation.total_level <19:
    level_up()

if character_creation.exp >= 305000 and character_creation.total_level <20:
    level_up()


















