### for level up after character creation

import character_creation
def level_up():
    new_level = input("congratulations you've leveled up would you like to take a level in fighter, wizard or ranger")
    if new_level == "fighter":
        fighter_level = character_creation.fighter_level+1
        character_creation.total_level = character_creation.total_level+1
    elif new_level == "ranger":
        ranger_level = character_creation.ranger_level+1
        character_creation.total_level = character_creation.total_level+1
    elif new_level == "wizard":
        wizard_level = character_creation.wizard_level+1
        character_creation.total_level = character_creation.total_level+1

if character_creation.exp >= 300:
    level_up()

if character_creation.exp >= 900:
    level_up()

if character_creation.exp >= 2700:
    level_up()

if character_creation.exp >= 6500:
    level_up()

if character_creation.exp >= 14000:
    level_up()

if character_creation.exp >= 23000:
    level_up()

if character_creation.exp >= 34000:
    level_up()

if character_creation.exp >= 48000:
    level_up()

if character_creation.exp >= 64000:
    level_up()

if character_creation.exp >= 85000:
    level_up()

if character_creation.exp >= 100000:
    level_up()

if character_creation.exp >= 120000:
    level_up()

if character_creation.exp >= 140000:
    level_up()

if character_creation.exp >= 165000:
    level_up()

if character_creation.exp >= 195000:
    level_up()

if character_creation.exp >= 195000:
    level_up()

if character_creation.exp >= 225000:
    level_up()

if character_creation.exp >= 265000:
    level_up()

if character_creation.exp >= 305000:
    level_up()

if character_creation.exp >= 355000:
    level_up()

print(character_creation.total_level)



















