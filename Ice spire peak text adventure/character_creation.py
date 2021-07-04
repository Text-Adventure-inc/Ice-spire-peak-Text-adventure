###
name = input("what is your characters name?")

### Stats

Strength = 10
Dexterity = 10
Intelligence = 10
Constitution = 10
Wisdom = 10
Charisma = 10

StrengthMod = Strength-10/2
DexterityMod = Dexterity-10/2
IntelligenceMod = Intelligence-10/2
ConstitutionMod = Constitution-10/2
WisdomMod = Wisdom-10/2
CharismaMod = Wisdom-10/2

Stat_Points = 30

Create_character();
    Print("your strength score is"+(str(Strength))+" , your dexterity score is"+(str(Dexterity))+", your Intelligence Score is"+(str(Intelligence))+" , your constitution score is"+(str(Constitution))+" , your wisdom score is"+(str(Wisdom))+" , your charisma score is"+(str(Charisma)))
        Input("What socres do you wish to increase?")











### Leveling systems

Experience = 0
Base_Level = 1

### Skills?
Arcana_skill_value = 0
if class == "wizard"
    Arcana_skill_value = 2 + IntModifier
    if class == "fighter":
        Athletics_skill_value = proficiency + StrengthMod
Stealth_skill_value = 0
   if class == ranger
        Stealth_skill_value = 2 + DexMod


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
class_list = ["fighter", "ranger", "wizard"]
class = input("what is your class")

if class == "fighter":
    Hp = 10+ConstitutionMod
    fighting_style_list = ["defensive", "dueling", "great weapon fighting"]
    fighting_style = input("do you want your fighting style to be defensive, dueling or great weapon fighting")
    if fighting_style = "defensive":
             ac = ac+1
    elif fighting_style = "dueling":
        if weapon == one_handed:
            attack_roll = attack_roll+2

elif class == "ranger":
    Hp = 8+ConstitionMod
elif class == "wizard":
    Hp = 6+ConstitutionMod
    spell_1 = 2

