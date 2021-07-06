import character_creation
import random
from character_creation import weapon


critical = False
def pc_attack():
    def do_attack():
        if weapon == "one handed":
            attack_roll = random.randint(1,20)
            attack_roll0 = attack_roll+character_creation.StrengthMod + character_creation.longsword_proficiency
            if character_creation.fighting_style == "dueling":
                attack_roll0 = attack_roll0+2
            if attack_roll == 20:
                critical = True
            print(attack_roll)
        elif weapon == "two handed":
            attack_roll = random.randint(1,20)
            attack_roll0 = attack_roll+character_creation.StrengthMod + character_creation.greatsword_proficiency
            if attack_roll == 20:
                crit = True
            print(attack_roll)
        elif weapon == "ranged":
            attack_roll = random.randint(1,20)
            attack_roll0 = attack_roll+character_creation.DexterityMod + character_creation.bow_proficiency
            if attack_roll == 20:
                critical = True
            print(attack_roll)
        elif weapon == "dagger":
            attack_roll = random.randint(1,20)
            attack_roll0 = attack_roll+character_creation.DexterityMod + character_creation.dagger_proficiency
            if attack_roll == 20:
                crit = True
            print(attack_roll)

    damage_roll = 0

    def do_damage():
        if weapon == "one handed":
            damage_roll = random.randint(1,8) + character_creation.StrengthMod
            if critical == True:
                damage_roll = damage_roll*2
            print(damage_roll)
        elif weapon == "two handed":
            damage_roll1 = random.randint(1,6) + character_creation.StrengthMod
            damage_roll2 = random.randint(1,6) + character_creation.StrengthMod
            if character_creation.fighting_style == "great weapon fighting" and damage_roll1 == 1:
                damage_roll1 = random.randint(1,6) + character_creation.StrengthMod
            elif character_creation.fighting_style == "great weapon fighting" and damage_roll2 == 1:
                damage_roll2 = random.randint(1,6) + character_creation.StrengthMod
                damage_roll = damage_roll1+damage_roll2
            if critical == True:
                damage_roll = damage_roll*2
            print(damage_roll)
        elif weapon == "bow":
            damage_roll = random.randint(1,8) + character_creation.DexterityMod
            if critical == True:
                damage_roll = damage_roll*2
            print(damage_roll)
        elif weapon == "dagger":
            damage_roll = random.randint(1,4) + character_creation.DexterityMod
            if critical == True:
                damage_roll = damage_roll*2
        print(damage_roll)
