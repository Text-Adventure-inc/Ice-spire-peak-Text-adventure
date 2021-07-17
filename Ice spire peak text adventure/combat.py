import attacks
import character_creation
import random
from attacks import pc_attack
import character_creation
import enemy_stats 
def pc_turn():
    will_pc_attack = input("its your turn of the comabt would you like to attack with "+character_creation.weapon+" to attack say attack")
    if will_pc_attack == "attack":
        pc_attack()

if enemy_attitude == "hostile":
    fight_start = 1
if fight_start == 1:
    character_creation.pc_initiative = random.randint(1,20)+character_creation.DexterityMod
    enemy_initiative = random.randint(1,20)+enemy_stats.enemy_DexterityMod
    if character_creation.pc_initiative > enemy_initiative:
        pc_turn()
        enemy_turn = 2
    elif enemy_initiative > character_creation.pc_initiative:
        pc_turn = 2
        enemy_turn = 1

