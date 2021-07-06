import random
breath_attack_available =1
def enemy_stats():
    if enemy == "Anchorite of Talos":
        enemy_hp = 58
        enemy_ac = 13
        cr = 3
        enemy_proficiency = 2
        enemy_StrengthMod = 3
        enemy_DexterityMod = 1
        enemy_ConstitutionMod = 2
        enemy_IntelligenceMod = -1
        enemy_WisdomMod = 2
        enemy_CharismaMod = 1
        enemy_weapon = "Clawed Gauntlet"   ### 1d4
        enemy_weapon_dice_number = 4
        enemy_weapon_damage_dice = 1  ### number of dice of damage ie: 1d4 2d4 ect
        enemy_weapon2 = "Tusk" ### 1d6
        enemy_weapon2_dice_number = 6
        enemy_weapon2_damage_dice = 1
        enemy_attack_stat = enemy_StrengthMod
        ### add magic shit
    elif enemy == "Ankheg":
        enemy_hp = 39
        enemy_ac = 14
        cr = 2
        enemy_proficiency = 2
        enemy_StrengthMod = 3
        enemy_DexterityMod = 0
        enemy_ConstitutionMod = 1
        enemy_IntelligenceMod = -5
        enemy_WisdomMod = 1
        enemy_CharismaMod = - 2
        enemy_weapon = "Bite"   
        enemy_weapon_dice_number = 6
        enemy_weapon_damage_dice = 2  
        enemy_attack_stat = enemy_StrengthMod
        while breath_attack_available == 1:
            enemy_weapon2 = "Acid Spray"
            enemy_weapon2_dice_number = 6
            enemy_weapon2_damage_dice = 3
            breath_attack_available  = breath_attack_available - 1
            if random.randint(1,6) == 6:
                breath_attack_available = breath_attack_available+1
        