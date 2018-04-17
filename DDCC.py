from random import randint

############################## CONSTANTS #################################

RACES = ["Dragonborn", "Drawf", "Elf", "Gnome", "Half-elf", "Half-orc", \
         "Halfling", "Human", "Tiefling"]
ALIGNMENTS = ["Chaotic Evil", "Chaotic Good", "Chaotic Neutral", \
              "Lawful Evil", "Lawful Good", "Lawful Neutral", \
              "Neutral", "Neutral Evil", "Neutral Good"]
CLASSES = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", \
           "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

############################## FUNCTIONS #################################

def getRace():
    print("""
    Here are the races:
    1. Dragonborn
    2. Dwarf
    3. Elf
    4. Gnome
    5. Half-elf
    6. Half-orc
    7. Halfling
    8. Human
    9 Tiefling
    """)
    race = 11
    # While the user has not picked a listed race
    while (race != 1 and race != 2 and race != 3 and race != 4 and \
        race != 5 and race != 6 and race != 7 and race != 8 and race != 0):
        # Subtract by 1 to easily get from RACES array
        race = int(input("What is your race? (Enter 1 - 9) ")) - 1
    return race

def getAlignment():
    print("""
    Here are the alignments:
    1. Chaotic Evil
    2. Chaotic Good
    3. Chaotic Neutral
    4. Lawful Evil
    5. Lawful Good
    6. Lawful Neutral
    7. Neutral
    8. Neutral Evil
    9. Neutral Good
    """)
    align = 11
    # While the user has not picked a listed alignment
    while (align != 1 and align != 2 and align != 3 and align != 4 and\
        align != 5 and align != 6 and align != 7 and align != 8 and align != 0):
        # Subtract by 1 to easily get from alignS array
        align = int(input("What is your alignment? (Enter 1 - 9) ")) - 1
    return align

def getClass():
    print("""
    Here are the classes:
    1. Barbarian
    2. Bard
    3. Cleric
    4. Druid
    5. Fighter
    6. Monk
    7. Paladin
    8. Ranger
    9. Rogue
    10. Sorceror
    11. Warlock
    12. Wizard
    """)
    role = 12
    # While the user has not picked a listed rolement
    while (role != 1 and role != 2 and role != 3 and role != 4 and\
        role != 5 and role != 6 and role != 7 and role != 8 and role != 9 and\
        role != 10 and role != 11 and role != 0):
        # Subtract by 1 to easily get from CLASSES array
        role = int(input("What is your role? (Enter 1 - 12) ")) - 1
    return role

def getSpells():
    spells = []
    spell = 'p'
    while spell.lower() != 'q':
        if spell != 'p':
            spells.append(spell)
        spell = input("Added a spell you know (q to quit): ")
    return spells
        
def getProfeciencies():
    proficiencies = []
    proficiency = 'p'
    while proficiency.lower() != 'q':
        if proficiency != 'p':
            proficiencies.append(proficiency)
        proficiency = input("Add a proficiency (q to quit): ")
    return proficiencies

def getEquipment():
    equipment = []
    item = 'p'
    while item.lower() != 'q':
        if item != 'p':
            equipment.append(item)
        item = input("Added an item (q to quit): ")
    return equipment

def rollStat():
    first  = randint(1,6)
    second = randint(1,6)
    third  = randint(1,6)
    fourth = randint(1,6)
    array  = [first, second, third, fourth]

    # sorts the list from greatest to least
    array.sort(reverse = True)
    stat = array[0] + array[1] + array[2]
    return stat

def rollStats():
    first  = rollStat()
    second = rollStat()
    third  = rollStat()
    fourth = rollStat()
    fifth  = rollStat()
    sixth  = rollStat()
    array  = [first, second, third, fourth, fifth, sixth]

    print("Here are the values you wrote: ")
    for value in array:
        print(str(value), end=' ')
    print()

def writeToTxtFile(name, sex, age, height, weight, background, race, \
    alignment, role, spells, proficiencies, equipment, stats):
    textFile = open(name + ".txt", 'w')
    textFile.write("Name: " + name)
    textFile.write("\nSex: " + sex)
    textFile.write("\nAge: " + age)
    textFile.write("\nHeight: " + height)
    textFile.write("\nWeight: " + weight)
    textFile.write("\nBackground:\n" + background)
    textFile.write("\nRace: " + race)
    textFile.write("\nAlignment: " + alignment)
    textFile.write("\nClass: " + role)
    textFile.write('\n'+ ("-" * 80))
    textFile.write("\nStrength Dexterity Constitution Intelligence Wisdom Charisma\n")
    textFile.write("   " + str(stats[0]) + "  ")
    textFile.write("      " + str(stats[1]) + "  ")
    textFile.write("       " + str(stats[2]) + "  ")
    textFile.write("         " + str(stats[3]) + "  ")
    textFile.write("       " + str(stats[4]) + "  ")
    textFile.write("    " + str(stats[5]) + "  ")
    textFile.write('\n')
    textFile.write("\nSpells:\n")
    for spell in spells[0:-2]:
        textFile.write(spell + ', ')
    if len(spells) > 0:
        textFile.write(spells[-1] + "\n\n")
    else:
        textFile.write("None")
    textFile.write("Proficiencies:\n")
    for prof in proficiencies[0:-2]:
        textFile.write(prof + ', ')
    if len(proficiencies) > 0:
        textFile.write(proficiencies[-1] + "\n\n")
    else:
        textFile.write("None")
    textFile.write("Equipment:\n")
    for item in equipment[0:-2]:
        textFile.write(item + ', ')
    if len(equipment) > 0:
        textFile.write(equipment[-1])
    else:
        textFile.write("None")
    textFile.close()

############################## QUESTIONS #################################

name = input("What is your characters name? ")
sex = input("What is your gender? ")
age = input("What is your age? ")
height = input("What is your height (cm)? ")
weight = input("How much do you weigh (lbs)? ")
background = input("Tell me of your past: ")
race = RACES[getRace()]
alignment = ALIGNMENTS[getAlignment()]
role = CLASSES[getClass()]
spells = getSpells()
proficiencies = getProfeciencies()
equipment = getEquipment()

############################## STATISTICS #################################
stats = rollStats()
strength = int(input("Pick a number from above for strength \
                        (can't reuse numbers): "))
dexterity = int(input("Pick a number from above for dexterity \
                        (can't reuse numbers): "))
constitution = int(input("Pick a number from above for constitution \
                        (can't reuse numbers): "))
intelligence = int(input("Pick a number from above for intelligence \
                        (can't reuse numbers): "))
wisdom = int(input("Pick a number from above for wisdom \
                        (can't reuse numbers): "))
charisma = int(input("Pick a number from above for charisma \
                        (can't reuse numbers): "))
stats = [strength, dexterity, constitution, intelligence, wisdom, charisma]

###########################################################################

writeToTxtFile(name, sex, age, height, weight, background, race, \
    alignment, role, spells, proficiencies, equipment, stats)

###########################################################################