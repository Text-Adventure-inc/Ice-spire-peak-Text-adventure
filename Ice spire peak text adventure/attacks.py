import character_creation
from character_creation import weapon
import random
longsword_attack = character_creation.StrengthMod + character_creation.longsword_proficiency
greatsword_attack = character_creation.StrengthMod + character_creation.greatsword_proficiency
bow_attack = character_creation.DexterityMod + character_creation.bow_proficiency
dagger_attack = character_creation.DexterityMod + character_creation.dagger_proficiency
damage_roll = 0
if weapon == "one handed":
    damage_roll = random.randint[1:8] + character_creation.StrengthMod
elif weapon == "two handed":
    damage_roll = random.randint[1:6]+random.randint[1:6] + character_creation.StrengthMod
elif weapon == "bow":
    damage_roll = random.randint[1:8] + character_creation.DexterityMod
elif weapon == "dagger":
    damage_roll = random.randint[1:4] + character_creation.DexterityMod
