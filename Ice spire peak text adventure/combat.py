import attacks
import character_creation
import random
if enemy_attitude == "hostile":
    fight_start == 1
if fight_start == 1:
    character_creation.pc_initiative = random.randint(1,20)+character_creation.DexterityMod
    enemy_initiative = random.randint(1,20)+enemy_DexterityMod
    if character_creation.pc_initiative > enemy_initiative:
        pc_turn = 1
        enemy_turn = 2
    elif enemy_initiative > character_creation.pc_initiative:
        pc_turn = 2
        enemy_turn = 1

