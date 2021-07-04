from typing import SupportsComplex


name = input("what is your characters name?")

### Stats

Strength = 8
Dexterity = 8
Intelligence = 8
Constitution = 8
Wisdom = 8
Charisma = 8

StrengthMod = Strength - 10/2
DexterityMod = Dexterity - 10/2
IntelligenceMod = Intelligence - 10/2
ConstitutionMod = Constitution - 10/2
WisdomMod = Wisdom - 10/2
CharismaMod = Wisdom - 10/2

StrengthMax = 20
DexterityMax = 20
IntelligenceMax = 20
ConstitutionMax = 20
WisdomMax = 20
CharismaMax = 20

Stat_Points = 30
Stat_change_Points = Stat_Points

def Create_character():
    while Stat_change_Points <= 30:
        print("your strength score is"+(str(Strength))+" , your dexterity score is"+(str(Dexterity))+", your Intelligence Score is"+(str(Intelligence))+" , your constitution score is"+(str(Constitution))+" , your wisdom score is"+(str(Wisdom))+" , your charisma score is"+(str(Charisma)))
        Score_change = input("What scores do you wish to increase?")
        if Score_change == "strength":
            Strength + 1, Stat_change_Points - 1
            print("Your Strength score is now : "+(str(Strength)))
        elif Score_change == "Dexterity":
            Dexterity + 1, Stat_change_Points - 1
            print("Your Dexterity score is now : "+(str(Dexterity)))
        elif Score_change == "Intelligence":
            Intelligence + 1, Stat_change_Points - 1
            print("Your Intelligence score is now : "+(str(Intelligence)))
        elif Score_change == "Constitution":
            Constitution + 1, Stat_change_Points - 1
            print("Your Constitution score is now : "+(str(Constitution)))
        elif Score_change == "Wisdom":
            Wisdom + 1, Stat_change_Points - 1
            print("Your Wisdom score is now : "+(str(Wisdom)))
        elif Score_change == "Charisma":
            Charisma + 1, Stat_change_Points - 1
            print("Your Charisma score is now : "+(str(Charisma)))
        else:
            print("Invalied Input")
            Create_character()
    
    

### Leveling systems
exp = 0
Base_Level = 1
proficiency = 2


### spell slots
spell_1 = 0
spell_2 = 0
spell_3 = 0
spell_4 = 0
spell_5 = 0
spell_6 = 0
spell_7 = 0
spell_8 = 0
spell_9 = 0

### class system
Hp = 0
ac = 10+DexterityMod
total_level = 0
fighter_level = 0
ranger_level = 0
wizard_level = 0


longsword_proficiency = 0
greatsword_proficiency = 0
bow_proficiency = 0
dagger_proficiency = 0

class_list = ["fighter", "ranger", "wizard"]
pcclass = input("what is your class")


weapon_choice = "sgsga"
### fighter shit
if pcclass == "fighter":
    Hp = 10+ConstitutionMod
    fighterLevel = fighter_level+1
    totalLevel = total_level+1
    longsword_proficiency = proficiency
    greatsword_proficiency = proficiency
    if weapon_choice != "sword" or "greatsword":
        weapon_choice = input("do you want a sword or a greatsword")
        if weapon_choice == "sword":
            weapon = "one handed"
        elif weapon_choice == "greatsword":
            weapon = "two handed"
    fighting_style_list = ["defensive", "dueling", "great weapon fighting"]
    fighting_style = input("do you want your fighting style to be defensive, dueling or great weapon fighting")
    if fighting_style == "defensive":
            ac = ac+1
    elif fighting_style == "dueling":
        if weapon == "one handed":
            attack_roll = attack_roll+2
    elif fighting_style == "great weapon fighting":
        if weapon == "two handed" and damage_roll == 1:
            damage_roll()
### ranger shit
elif pcclass == "ranger":
    Hp = 8+ConstitutionMod
    rangerLevel = ranger_level +1
    totalLevel = total_level+1
    longsword_proficiency = proficiency
    bow_proficiency = proficiency
    if weapon_choice != "sword" or "bow":
        weapon_choice = input("do you want a sword or a bow")
    if weapon_choice == "sword":
        weapon = "one handed"
    elif weapon_choice == "bow":
        weapon = "ranged"

### wizard shit
elif pcclass == "wizard":
    Hp = 6+ConstitutionMod
    spell_1 = 2
    wizardLevel = wizard_level +1
    totalLevel = total_level+1
    dagger_proficiency = proficiency
    weapon = "dagger"
    print("you have a dagger")
   
   

### Skills?
athletics = 0
survival = 0
arcana = 0
if pcclass == "fighter":
    athletics = proficiency + StrengthMod
elif pcclass == "ranger":
    survival = proficiency + WisdomMod
elif pcclass == "wizard":
    arcana = proficiency + IntelligenceMod
