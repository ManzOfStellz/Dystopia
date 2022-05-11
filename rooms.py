#MadeByKeshuvVishram
import os
import time
import random
import sys
import databasefunctions

logo = """████████▄  ▄██   ▄      ▄████████     ███      ▄██████▄     ▄███████▄  ▄█     ▄████████ 
███   ▀███ ███   ██▄   ███    ███ ▀█████████▄ ███    ███   ███    ███ ███    ███    ███ 
███    ███ ███▄▄▄███   ███    █▀     ▀███▀▀██ ███    ███   ███    ███ ███▌   ███    ███ 
███    ███ ▀▀▀▀▀▀███   ███            ███   ▀ ███    ███   ███    ███ ███▌   ███    ███ 
███    ███ ▄██   ███ ▀███████████     ███     ███    ███ ▀█████████▀  ███▌ ▀███████████ 
███    ███ ███   ███          ███     ███     ███    ███   ███        ███    ███    ███ 
███   ▄███ ███   ███    ▄█    ███     ███     ███    ███   ███        ███    ███    ███ 
████████▀   ▀█████▀   ▄████████▀     ▄████▀    ▀██████▀   ▄████▀      █▀     ███    █▀  
                                                                                        """ 
#Defining logo (ascii art)

fightroom = 0 #sets a base value for fightroom
#grabs basic variables from database so it can be referred to in any function without global
shirt = databasefunctions.getfield('shirt') 
weapon = databasefunctions.getfield('weapon')
name = databasefunctions.getfield('name')
#List of enemies that can appear in the fightroom
peoplename = [
    "Adam",
    "Smith",
    "Dave",
    "Adibola",
    "Muhammed",
    "Hussain",
    "Alexandra",
    "Brittany",
    "Yvonne",
]
#List containing damage that can be dealt if the user opts to block during a fightroom
blockdamagelist = [
    -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15
]
#List containing damage that can be dealt to the user if the user opts to damage during a fightroom
damagelist = [
    -10, -12, -17, -24, -29, -32, -11, -13, -5, -16, -13, -2, -8, -100
]


def randomisefightroom(): #Randomises fight room, throughout this program the fightroom changes position
    global fightroom
    fightroom = random.randint(1, 9)
    return fightroom


def checkfightroom(roomNum): #Used for checking if a fight should occur
    if fightroom == roomNum:
        return True


def logoprint(t): #prints each character individually with an extremely low timeout for aesthetic effect
    for l in t + '\n':
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.001)


def slowprint(s): #prints each character individually with a medium timeout for aesthetic effect
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.06)


def checkinput(userinput, field1, field2): #Checks the input user gave against predefined values, ensures program doesn't produce unpreventable errors
    while userinput.lower() != field1 and userinput.lower() != field2:
        slowprint("Please try that again , choose between " + field1 + " or " +
                  field2 + ".")
        userinput = input("")
    return userinput.lower()


def fight(): #Fight function
    opponent = peoplename[random.randint(0, 8)] #Grabs name to use
    opponenthealth = 100 #Sets opponent's health to 0
    slowprint("You are presented with an enemy who introduces themselves as " +
              opponent + ", now you must fight them, FIGHT!!!!") #User prompt
    while int(databasefunctions.getfield("health")) > 0 and opponenthealth > 0: #Battle only ends when one of the user or opponent's health drops below or to 0
        time.sleep(1)
        os.system('clear')
        temphealth = databasefunctions.getfield("health")
        slowprint("You have " + str(temphealth) + " health, " + opponent +
                  " has " + str(opponenthealth) + " health") #Gives health info to user
        slowprint("You must attack or block, what do you choose?") #Asks user if they wish to attack or block
        choice = input(" ")
        choice = checkinput(choice, "attack", "block")
#       Gets weapon and alters damage dealt depending on weapon
        if choice == "attack":
            if databasefunctions.getfield("weapon") == "handgun":
                opponenthealth = opponenthealth - 40
                slowprint("You attack " + opponent +
                          ", damaging a third of their max health")
            elif databasefunctions.getfield("weapon") == "machete":
                opponenthealth = opponenthealth - 25
                slowprint("You attack " + opponent +
                          ", damaging a quarter of their max health")
            else:
                opponenthealth = opponenthealth - 20
                slowprint("You attack " + opponent +
                          ", damaging a fifth of their max health")
            time.sleep(1)
            os.system('clear')
            block = damagelist[random.randint(0, 13)] #Grabbing damage value in event of opting for block
            damagereceived = str(block)
            databasefunctions.updateintfield("health", block)
            slowprint(opponent + " punches you, dealing " +
                      damagereceived[1:] + " damage")
            time.sleep(2)
            os.system('clear')
        else:
            damage = blockdamagelist[random.randint(0, 14)]
            tempdamage = str(damage)
            slowprint(
                opponent +
                " has attacked you, but you block it, so it deals less damage")
            slowprint("The attack deals " + tempdamage[1:] + " health")
            databasefunctions.updateintfield("health", damage)
            time.sleep(2)
            os.system('clear')
					#If your health drops to 0, game ending is forced
    if int(databasefunctions.getfield("health")) <= 0:
        slowprint(
            opponent +
            " laughs at you as you lay face down on the floor... your muscles begin to relax as you embrace the cold rush that can be described only as death."
        )
        time.sleep(2)
        os.system('clear')
        logoprint(logo)
        time.sleep(1)
        slowprint("Forced ending: Killed by " + opponent + ".")
        time.sleep(2)
        databasefunctions.formatsave()
        exit()


def incrementhealth(): #Regains some health in each room so dealing with two fights is actually possible
    if int(databasefunctions.getfield(
            "health")) < 120 and databasefunctions.getfield("shirt") == "r":
        databasefunctions.updateintfield("health", 24)
        if int(databasefunctions.getfield("health")) > 120:
            databasefunctions.overwriteintfield("health", 120)
    if int(databasefunctions.getfield(
            "health")) < 100 and databasefunctions.getfield("shirt") != "g":
        databasefunctions.updateintfield("health", 20)
        if int(databasefunctions.getfield("health")) > 100:
            databasefunctions.overwriteintfield("health", 100)


def startingroom(): #Initial room, asks for name, shirt.
    global name
    randomisefightroom()
    slowprint("Our story begins with you...")
    time.sleep(1)
    os.system('clear')
    slowprint("What shall I call you? ")
    name = input("")
    databasefunctions.updateStringfield("name", name)
    name = databasefunctions.getfield('name')
    slowprint("Hello " + name + "!")
    slowprint(
        name +
        ", you wake up in the middle of a forest, you feel the breeze on your chest as you realise that your shirt is gone."
    )
    time.sleep(1)
    slowprint(
        "But wait, were you even wearing your shirt? Were you wearing a shirt? Wait... where even are you? Who am I? Why do you hear me?"
    )
    time.sleep(1)
    os.system('clear')
    slowprint(
        "Oh look! It doesnt matter, theres three shirts in front of us... you, I mean."
    )
    slowprint(
        "Theres a green one, a blue one and a red one. Maybe they mean something... no, they can't -- I think we're, I mean you're going insane. "
    )
    slowprint("So anyways " + name + ", which do you choose? r, g or b?")
    shirt = input("")
    while shirt != "g" and shirt != "r" and shirt != "b":
        os.system('clear')
        print("Choose between r, g, and b...")
        shirt = input("")
    databasefunctions.updateStringfield("shirt", shirt)
    if shirt == "r":
        databasefunctions.overwriteintfield("health", 120)
    slowprint("Brilliant choice " + name + ", you look very smart!")
    time.sleep(1)
    os.system('clear')
    databasefunctions.overwriteintfield("roomnumber", 1)


def checkforsave(): #Checks for save by grabbing room number and comparing it wth the default of 0 or empty and asks user if they wish to continue in the event of a save being found
    if databasefunctions.getfield(
            "roomnumber") == "0" or databasefunctions.getfield(
                "roomnumber") == "":
        startingroom()
    else:
        slowprint(
            "Do you wish to continue, or start a new game (new, or continue)")
        newgame = input()
        while newgame.lower() != "new" and newgame.lower() != "continue":
            slowprint(
                "Do you wish to continue, or start a new game (new, or continue)"
            )
            newgame = input()
        if newgame.lower() == "new":
            databasefunctions.formatsave()


def ending(message): #Ending function, allows me to save many lines of code and just specify the message
    os.system('clear')
    logoprint(logo)
    time.sleep(1)
    slowprint(message)
    slowprint("Made by Keshuv Vishram. (@ManzOfStellz)")
    time.sleep(2)
    databasefunctions.formatsave()
    exit()


def room1(): #First room
    databasefunctions.overwriteintfield("roomnumber", 1)
    slowprint(
        "You see a path, crawl over and attempt to follow it... eventually, you come across a fork in the path. "
    )
    time.sleep(1)
    os.system('clear')
    slowprint(
        "To the left, you see what looks like a distant plume of smoke, and to the right a staircase descending into a grate."
    )
    time.sleep(1)
    os.system('clear')
    name = databasefunctions.getfield('name')
    slowprint("where should we go " + name + ", the grate or the path? ")
    roomshould = input("")
    roomshould = checkinput(roomshould, "grate", "path")
    if roomshould.lower() == "grate":
        databasefunctions.overwriteintfield("roomnumber", 2)
    if roomshould.lower() == "path":
        databasefunctions.overwriteintfield("roomnumber", 3)


def room2(): #Ending set 0 and ??
    if checkfightroom(2) == True:
        fight()
    slowprint(
        "You slowly descend the grate, and become aware of a faint flickery light"
    )
    time.sleep(1)
    os.system('clear')
    if databasefunctions.getfield("shirt") != "g":
        slowprint(
            "Suddenly, the light switches off, the room goes silent but you can hear a faint seriese of breaths behind you. "
        )
        time.sleep(2)
        os.system('clear')
        slowprint(
            "You feel it enter your back, you feel the blood trickle down your back and sides, but its too late to do anything. "
        )
        time.sleep(1)
        time.sleep(1)
        os.system('clear')
        ending("Ending 0: The unfortunate victim of Dystopia")
    else:
        slowprint(
            "Suddenly, the light switches off, the room goes silent but you can hear a faint seriese of breaths behind you."
        )
        slowprint(
            "You feel a hand touch your shoulder, you flinch in fear and scream at the sillhoutte before you, but you see an arm reach out towards you, it seems inviting, so you grab onto it, and it pulls you back up."
        )
        time.sleep(2)
        os.system('clear')
        slowprint(
            "After some long 5 minutes of being dragged around the vast structure you finally stop. You take your arm away from your eyes and tke a look around."
        )
        time.sleep(2)
        slowprint(
            "Awaiting your arrival is an array of wacky creatures, presumably the occupants of the legendary forest, but before you, lies an empty throne."
        )
        time.sleep(2)
        os.system('clear')
        time.sleep(2)
        slowprint("All hail king " + name + "!")
        time.sleep(2)
        os.system('clear')
        ending("Ending ??: King of Dystopia")


def room3(): #Third room
    if checkfightroom(3) == True:
        fight()
    slowprint(
        "In the distance you see a pile of scraps, as you approach you see a set of car keys, a handgun, and a machete, you can pick one up, or pass, what do you do? "
    )
    weapon = input("")
    while weapon.lower() != "handgun" and weapon.lower(
    ) != "keys" and weapon.lower() != "machete" and weapon.lower() != "pass":
        os.system('clear')
        slowprint(
            "Your input was not recognised please input any of: keys, handgun, machete or pass."
        )
        weapon = input()
    if weapon == "keys":
        databasefunctions.updateStringfield("carkey", "Yes")
    elif weapon == "handgun" or weapon == "machete":
        databasefunctions.updateStringfield("weapon", weapon)
    time.sleep(1)
    os.system('clear')
    slowprint(name +", you are presented with yet another choice, this time you must decide whether to continue following the path or to head to a distant lake. Which do you choose?")
    userchoice = input("")
    userchoice == checkinput(userchoice, "path", "lake")
    randomisefightroom()
    incrementhealth()
    time.sleep(1)
    if userchoice.lower() == "path":
        databasefunctions.overwriteintfield("roomnumber", 4)
    else:
        databasefunctions.overwriteintfield("roomnumber", 5)
    os.system('clear')


def room4(): # Fourth room
    incrementhealth
    if checkfightroom(5) == True:
        fight()
    slowprint(
        "You continue along the path and see what looks to be ruins of some sort of temple..."
    )
    time.sleep(1)
    os.system('clear')
    slowprint(
        "You must make a choice on whether to enter it or continue along the path, which leads into a low-hanging fog."
    )
    fogortemple = input("")
    fogortemple = checkinput(fogortemple, "path", "temple")
    if fogortemple == "path":
        databasefunctions.overwriteintfield("roomnumber", 6)
    else:
        databasefunctions.overwriteintfield("roomnumber", 7)
    randomisefightroom()
    os.system('clear')


def room5(): #Ending 1
    incrementhealth()
    if checkfightroom(5) == True:
        fight()
    slowprint(
        "You reach an opening which leads to the lake, in the distance you can make out the smoke plume earlier, you head over, a smile stretches across your face and you begin running when you see what looks like humanoid figures around a campfire."
    )
    time.sleep(1)
    os.system('clear')
    slowprint(
        "However, this sense of relief is short-lived, as you realise that these figures are devoid of any humanity, and instead a chill runs down your spine as they turn to face you..."
    )
    time.sleep(1)
    os.system('clear')
    slowprint(
        "They are... aliens? No, looking more like defaced bodies -- or rather bloody corpses -- living, corpses, covered from head to toe in blood."
    )
    time.sleep(1)
    os.system('clear')
    slowprint(
        "You move back instinctively, but these 'corpses' take that as a sign to attack... Tears run down your face as they begin tearing the skin from your very chest. The only thing you can do is think -- think about the time before this, the time before you were in this accursed land, the time of happiness. "
    )
    time.sleep(1)
    os.system('clear')
    slowprint(
        "You rest your head on the sandy coast, being quite literally torn apart, and as you lay there on the brink of death, you accept your fate, as yet another, victim of Dystopia."
    )
    time.sleep(2)
    ending(
        "Ending 1: Forever forgotten, laying lifelessly on the sandy beach of Dystopia."
    )


def room6(): #Ending 2
    incrementhealth()
    if checkfightroom(6) == True:
        fight()
    os.system('clear')
    slowprint(
        "You follow the path into the fog, and keep walking, and walking, and walking..."
    )
    slowprint(
        "All you can focus on is walking, you don't know where you are going, or where you came from, you are reduced to nothing but a puppet, wandering the neverending dark void of dystopia forever..."
    )
    time.sleep(2)
    os.system('clear')
    time.sleep(2)
    ending("Ending 2: Yet another wondering soul of Dystopia.")


def room7(): #Temple
    incrementhealth()
    if checkfightroom(7) == True:
        fight()
    randomisefightroom()
    slowprint(
        "You enter the ruins, and see a staircase. You descend it and come across a fork."
    )
    time.sleep(1)
    slowprint("Which do you choose "+name+", left or right?")
    leftorright = input("")
    leftorright = checkinput(leftorright, "left", "right")
    if leftorright.lower() == "left":
        databasefunctions.overwriteintfield("roomnumber", 8)
    if leftorright.lower() == "right":
        databasefunctions.overwriteintfield("roomnumber", 9)


def room8(): #Ending set 3 and 4
    incrementhealth()
    if checkfightroom(8) == True:
        fight()
    slowprint(
        "You choose to walk down the left pathway, and come across a group of people."
    )
    time.sleep(1)
    os.system('clear')
    slowprint(
        "They call out to you, asking for your name, you give it to them. (Who you perceive as) the ringleader of the group introduces herself as Bea. 'So, "
        + name +
        ", how long have you been here for?' You respond with some incomprehensible nonsense, she shakes her head and says not to worry about it."
    )
    time.sleep(3)
    os.system('clear')
    slowprint(
        "They seem to be in a rush, you follow them and are led to a plane, they tell you to get on they can all can escape this place."
    )
    time.sleep(1)
    os.system('clear')
    slowprint(
        "It appears, by some stroke of good luck, that you have survived Dystopia..."
    )
    time.sleep(2)
    os.system('clear')
    time.sleep(1)
    ending("Ending 3: Soaring across the skies of Dystopia.")


def room9(): # Ending 5
    os.system('clear')
    slowprint(
        "You take the right path and it leads you back outside, infront of you is a car."
    )
    time.sleep(1)
    os.system('clear')
    if databasefunctions.getfield("carkey") != "Yes":
        slowprint(
            "But you don't seem to have any keys, and you can't break the window..."
        )
        time.sleep(1)
        slowprint(
            "You notice it getting darker, night's about to hit, and everyone knows thats when the monsters come out"
        )
        time.sleep(1)
        os.system('clear')
        slowprint(
            "Quaking in your boots, you decide to run back into the temple and get your back up against a wall, but it is futile, the monsters will find you."
        )
        time.sleep(1)
        os.system('clear')
        slowprint(
            "You notice one green thing 'walk' up to you, it lets out a quiet hissing sound, glowing white, and then exploding, killing you in the process. Your limbs and guts alike are embedded into the walls of the temple, and you become nothing more than another relic of Dystopia."
        )
        time.sleep(2)
        os.system('clear')
        time.sleep(1)
        ending("Ending 4: Yet another Decoration of Dystopia.")
    if databasefunctions.getfield("carkey") == "Yes":
        slowprint(
            "You remember the keys you found earlier, pull them out of your pocket, and notice the model of the car, and keys, matches. You try the unlock button and by some miraculous stroke of luck, the car unlocks."
        )
        time.sleep(1)
        os.system('clear')
        slowprint(
            "You get in and turn on the engine, somehow it seems to have a full tank of fuel. You drive, as fast as you can, away from the forest. You burst through a set of gates, and you are back to the earthly landscape you remember..."
        )
        time.sleep(2)
        os.system('clear')
        time.sleep(2)
        ending("Ending 5: Escaped Dystopia!")
#MadeByKeshuvVishram
#MadeByKeshuvVishram