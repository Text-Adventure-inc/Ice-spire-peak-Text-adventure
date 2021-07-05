import character_creation
import random
from character_creation import weapon
from character_creation import fighting_style


def do_attack():
    if weapon == "one handed":
        attack_roll = random.randint(1,20)+character_creation.StrengthMod + character_creation.longsword_proficiency
        if fighting_style == "dueling":
            attack_roll = attack_roll+2
        print(attack_roll)
    elif weapon == "two handed":
        attack_roll = random.randint(1,20)+character_creation.StrengthMod + character_creation.greatsword_proficiency
        print(attack_roll)
    elif weapon == "ranged":
        attack_roll = random.randint(1,20)+character_creation.DexterityMod + character_creation.bow_proficiency
        print(attack_roll)
    elif weapon == "dagger":
        attack_roll = random.randint(1,20)+character_creation.DexterityMod + character_creation.dagger_proficiency
        print(attack_roll)

damage_roll = 0

def do_damage():
    if weapon == "one handed":
        damage_roll = random.randint(1,8) + character_creation.StrengthMod
        print(damage_roll)
    elif weapon == "two handed":
        damage_roll1 = random.randint(1,6) + character_creation.StrengthMod
        damage_roll2 = random.randint(1,6) + character_creation.StrengthMod
        if fighting_style == "great weapon fighting" and damage_roll1 == 1:
            damage_roll1 = random.randint(1,6) + character_creation.StrengthMod
        elif fighting_style == "great weapon fighting" and damage_roll2 == 1:
            damage_roll2 = random.randint(1,6) + character_creation.StrengthMod
        damage_roll = damage_roll1+damage_roll2
        print(damage_roll)
    elif weapon == "bow":
        damage_roll = random.randint(1,8) + character_creation.DexterityMod
        print(damage_roll)
    elif weapon == "dagger":
        damage_roll = random.randint(1,4) + character_creation.DexterityMod
        print(damage_roll)