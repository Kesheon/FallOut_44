
import characterinventory
import characterinventory2
import pickle

INVENTORY = 1
SANCTUARY_HILLS = 2
REDROCKET_TRUCKSTOP = 3
CONCORD = 4
DIAMOND_CITY = 5
FORT_HAGEN = 6
INSTITUTE = 7
QUIT = 8

# Variables that go into the character_inventory list under def main
WEAPON1 = '10mm Pistol'
AMMO1 = '10mm Pistol ammunition'
RING1 = 'Nora\'s wedding ring'
RING2 = 'Your wedding ring'
BOTTLED_WATER = 'Bottled Purified Water'
RED_ROCKET_PASSWORD = 'Password to Red Rocket Truck Stop safe: 12345'

# Variables that go into the character_inventory2 list under def main
ARMOR1 = 'Light Kevlar Armor'
FOOD1 = 'Canned beans'
    # FIRST_AID1 goes here as well, but it has another list
    # that it belongs to: quest_inventory. It can be seen further
    # below.

# Variables that go into quest_inventory list under def main
MAN_SIZED_RATS = 'Man-sized rats already defeated'
MUTANT_DOGS = 'Mutant dogs already defeated'

# Variables for the first aid kits that can be collected
# in various places within the program
FIRST_AID1 = 'First aid kit'

# Variable that hold's that players money
MONEY = 0

# Variables for the money that can be collected in various
# places within the program
CASH1 = 250

# File that the program saves to
FILENAME = 'FallOut44.txt'

def main():
    # global variables that go into character_inventory list 
    global WEAPON1
    global AMMO1
    global RING1
    global RING2
    global BOTTLED_WATER
    global RED_ROCKET_PASSWORD

    # global variables that go into the character_inventory2 list
    global ARMOR1
    global FOOD1
        # FIRST_AID1 goes here as well, but it has it has another list
        # that it belongs to: quest_inventory. It can be seen further
        # below.
        

    # global variables that go into the quest_inventory list
    global MAN_SIZED_RATS
    global MUTANT_DOGS

     # global variable that holds the player's money
    global MONEY

    # global variables for the money that can be collected in various
    # places within the program
    global CASH1
    
    # global variables for the first aid kits that can be collected
    # in various places within the program
    global FIRST_AID1

    # character_inventory is a list that stores the players collected items
    # It is an object imported from the characterinvenory file
    character_inventory = [WEAPON1, AMMO1]
    inventory = characterinventory.CharacterInventory(character_inventory)

    # character_inventory2 is a second list that stores the players collected items
    # It is an object imported from the characterinventory2 file
    character_inventory2 = [ARMOR1, FOOD1, FIRST_AID1]
    inventory2 = characterinventory2.CharacterInventory2(character_inventory2)

    # quest_inventory is a list that prevents the same messages from
    # being displayed more than once in certain areas of the program
    quest_inventory = []

    # prevent_exploit is a list that prevents money and first aid kits
    # from being collected more that once/ exploited
    prevent_exploit = []
    
    choice = 0 
    
    while choice != QUIT:
        choice = get_menu_choice()
        if choice == INVENTORY:
            print('Your Inventory')
            print('----------------------------')
            print(character_inventory)
            print()
            print(character_inventory2)
            print()
            print('Money:\t$',format(MONEY, ',.2f'), sep='')
            print()
            input('Press enter to continue. ')
        elif choice == SANCTUARY_HILLS:
            Sanctuary_Hills = sanctuary_hills(character_inventory, quest_inventory)
        elif choice == REDROCKET_TRUCKSTOP:
            RedRocketTruckStop = redrocket_truckstop(character_inventory, character_inventory2,
                                                     quest_inventory, prevent_exploit)
            
def get_menu_choice():
    print()
    print()
    print()
    print('The CommonWealth')
    print('------------------------------')
    print('1. Check Inventory'+
          '\n2. Go to Sanctuary Hills'+
          '\n3. Go to Red Rocket Truck Stop'+
          '\n4. Go to Concord'+
          '\n5. Go to Diamond City'+
          '\n6. Go to Fort Hagen'+
          '\n7. Go to the Institute'+
          '\n8. Quit game')
    print()
    choice = int(input('Enter your choice: '))
    print()
    while choice < INVENTORY or choice > QUIT:
        choice = int(input('Enter a valid choice: '))
        print()
    return choice
    

def sanctuary_hills(character_inventory, quest_inventory):
    RUNDOWN_HOUSE1 = 1
    RUNDOWN_HOUSE2 = 2
    NEIGHBOR_HOUSE = 3
    YOUR_HOUSE = 4
    QUIT2 = 5
    choice2 = 0
    while choice2 != QUIT2:
        print()
        print('Places in Sanctuary Hills')
        print('-------------------------')
        print()
        print('1. Go to run-down house 1'+
          '\n2. Go to run-down house 2'+
          '\n3. Go to neightbor\'s run-down house'+
          '\n4. Go to your house (run-down)'+
              '\n5. Go back to map (The CommonWealth)')
        print()
        choice2 = int(input('Enter your choice: '))
        print()
        while choice2 < RUNDOWN_HOUSE1 or choice2 > QUIT2:
            choice2 = int(input('Enter a valid choice: '))
            print()

        if choice2 == RUNDOWN_HOUSE1:
            if WEAPON1 and AMMO1 in character_inventory:
                if MAN_SIZED_RATS not in quest_inventory:
                    quest_inventory.append(MAN_SIZED_RATS)
                    input('SYSTEM: You kill all of the man-sized rats that are outside'+
                      ' \n\nof the house with your weapon of choice. You then enter the house.'+
                      ' \n\nPress enter to continue. ')
                else:
                    input('SYSTEM: You have already killed all of the man-sized rats that'+
                          '\n\nwere here earlier. You walk by their corpses. Press'+
                          '\n\nenter to continue. ')
                print()
                print()
                print('Inside of run-down house 1')
                print('--------------------------')
                print()
                print('Thinking to self: Apparently scavengers have been here. I see bottled purified'+
                      ' \n\nwater, so I should grab that to hydrate. And apparently there is'+
                      ' \n\na computer here that still works. It\'s 210 years old! I wonder what\'s on it?')
                print()
                print('1. Collect bottled water'+
                      '\n2. Read computer')
                print()
                GET_WATER = 1
                READ_COMPUTER1 = 2
                choice3 = 0
                choice3 = int(input('Enter your choice: '))    
                print()
                while choice3 <GET_WATER or choice3 > READ_COMPUTER1:
                    choice3 = int(input('Enter a valid choice: '))
                    print()
                if choice3 == GET_WATER:
                    if BOTTLED_WATER not in character_inventory:
                        character_inventory.append(BOTTLED_WATER)
                        input('SYSTEM: Bottled Purified Water has been added to your'+
                              '\n\ninventory. Press enter to continue. ')
                    else:
                        input('SYSTEM: Bottled Purified Water is already in your'+
                              '\n\ninventory. Press enter to continue. ')
                elif choice3 == READ_COMPUTER1:
                    input('Press enter to read computer. ')
                    print()
                    print('---------------------------------------------------------------------------')
                    print()
                    print('-Property of Mr.Russell')
                    print()
                    print('Computer entry 1: Dear, Mr.Green'+
'\n\nI am calling in sick today. However, it is expected of you as supervisor to host a meeting today.'+
'\n\nYou need to stress the importance of safety in this meeting. Every year we have too many'+
'\n\nmen, especially the younger ones, going out there thinking that they are Superman.'+
'\n\nI will brief you in the next email I send on the points you need to bring out to them.'+
'\n\nRecord this meeting and send it to me, please.'+
'\n\n-Mr.Russell'+
'\nBigWell Chemical Plant Inc.'+
'\nOperations Manager'+
'\nOctober 23, 2077')
                    print()
                    input('Press enter to continue. ')
                    print()
                    print('Thinking to self: I always wondered what Mr.Russell did for work. Apparently he worked at BigWell'+
'\n\nChecmical Plant. I never went out of my way to speak to him though. He was always a jerk to all'+
'\n\nof his neighbors. What am I thinking? This man has been dead for 210 years. I should move on.')
                    print()
                    input('Press enter to read computer entry 2. ')
                    print()
                    print('---------------------------------------------------------------------------')
                    print()
                    print('-Property of Mr.Russell')
                    print()
                    print('Computer entry 2: Stuck!'+
'\n\nI\'m stuck here! I should have stayed in Diamond City! I thought that'+
'\n\nSanctuary Hills would ring true to it\'s name, but it has not. Honestly,'+
'\n\nanywhere anyone goes there are people ready to shoot you for food and water, and then'+
'\n\nthere are the animals that want to rip your head off. The animals are abnormally vicious and 10 times'+
'\n\nbigger due to the radiation that comes from the atomic bombs that dropped 210 years ago. I stored'+
'\n\nsome canned beans in a safe at Red Rocket Truck Stop so that I can have a guaranteed meal in the case'+
'\n\nof an emergency. Reminder to self: the passcode to that safe is 12345. There is also some light kevlar'+
'\n\narmor in there. It helps to wear armor since so many people and things want to hurt one another in this'+
'\n\npost apocalyptic world. I also put $250 behind the Red Rocket Truck Stop\'s public toilet and a first aid'+
'\n\nkit in the storage room\'s file cabinet. I would carry all these things on me, but I have enough on me'+
'\n\nalready. So, all of the things I\'m storing at the Red Rocket Truck Stop are just backup items. Honestly,'+
'\n\nI\'m crying as I write this. Life is so hard out here. I had three options and all of them were bad. I'+
'\n\ncould have stayed in Diamond City and risked the danger of the Institute and their synths. I could leave'+
'\n\nDiamond City and hope to find a better place to settle; I chose this and it is not going well. Or I could'+
'\n\nhave chosen to leave the CommonwWealth in the hope of something better being out there. But that is too'+
'\n\nrisky if you ask me.'+
'\n\n-Rebecca'+
'\nSeptember 25, 2287')
                    print()
                    input('Press enter to continue. ')
                    print()
                    print()
                    print('Thinking to self: I should remember that passcode to that safe: 12345. I\'ll write it down.'+
                          '\n\nThis person, Rebecca, made this entry not long ago. She must have unfortunately been'+
                          '\n\nkilled by the man-sized rats outside: I did see a woman\'s corpse nearby. Well, I can'+
'\n\ntake whatever she left behind at the Red Rocket Truck Stop.')
                    print()
                    print()
                    if RED_ROCKET_PASSWORD in character_inventory:
                        input('SYSTEM: You already have the password to the Red Rocket Truck Stop'+
                              '\n\nsafe in your inventory. Press enter to continue. ')
                    else:
                        character_inventory.append(RED_ROCKET_PASSWORD)
                        input('SYSTEM: Password to Red Rocket Truck Stop Safe has been added to your inventory.'+
                          '\n\nPress enter to continue. ')
            else:
                input('SYSTEM: You need a weapon and ammunition for the weapon before coming here! There are rats' +
' \n\nthe size of a man that are threatning to attack you if you come any closer! Don\'t be like the woman who'+
                      '\n\nwas killed! You can see her corpse nearby! Press enter to continue. ')
                    
        elif choice2 == RUNDOWN_HOUSE2:
             print()
             print('Inside of run-down house 2')
             print('---------------------------')
             print()
             print('Thinking to self: There is a 10mm pistol under the bed in the master bedroom: I should take that.'+
'\n\nI wonder what information is on that computer in the living room. That computer looks like,'+
'\n\nit was made after the bombs dropped: it\'s made of scavenged materials. It might have some'+
'\n\nrelevant information on it. The person who owned it probably temporarily lived here and'+
'\n\nlater abandoned the place. It must have been recently.')
             print()
             print('1. Collect 10mm Pistol'+
                   '\n2. Read computer')
             print()
             COLLECT_WEAPON = 1
             READ_COMPUTER2 = 2
             choice4 = 0
             choice4 = int(input('Enter your choice: '))
             print()
             while choice4 < COLLECT_WEAPON or choice4 > READ_COMPUTER2:
                 choice4 = int(input('Enter a valid choice: '))
                 print()
             if choice4 == COLLECT_WEAPON:
                 if WEAPON1 not in character_inventory:
                     character_inventory.append(WEAPON1)
                     input('SYSTEM: 10mm Pistol has been added to your inventory. Press enter to continue. ')
                 else:
                     input('SYSTEM: 10mm Pistol is already in your inventory. Press enter to continue. ')
             elif choice4 == READ_COMPUTER2:
                input('Press enter to read computer. ')
                print()
                print('---------------------------------------------------------------------------')
                print()
                print('-Property of Brandis')
                print()
                print('Computer entry 1: I\'m done!'+
'\n\nI am tired of the CommonWealth. It is simply too dangerous here. I have to go and find a more, "off-grid"'+
'\n\nlocation to dwell in. The dangers of the CommonWealth are too numerous: there are Raiders, Supermutants,'+
'\n\nthe Institute and their Synths, Deathclaws, man-sized rats, and the list goes on. I have to go. I leave'+
'\n\ntomorrow.'+
'\n\n-Brandis'+
'\nApril 2, 2287')
                print()
                input('Press enter to continue. ')
                print()
                print('Thinking to self: I\'m assuming Raiders are low-lifes that work together to rob and kill'+
'\n\nfor the sake of their own survival in this post apocalyptic world. Their name,'+
'\n\n"Raiders" sort of implies that. But what in the world are Supermutants? Deathclaws?'+
'\n\nSynths? What is the Institute? Have I seen some of these things already and'+
'\n\njust didn\'t know it at the time?')
                print()
                input('Press enter to continue. ')
                
        elif choice2 == NEIGHBOR_HOUSE:
            print()
            print('Inside of neighbor\'s run-down house')
            print('--------------------------')
            print()
            print('Thinking to self: This was my neighbor\'s house 210 years ago!'+
                  '\n\nThey were a likeable family, but they were killed in the'+
                  '\n\ncryogenic pods by Vault Tec. Such a tragic end...'+
                  '\n\nThere is some 10mm pistol ammmunition in the master bedroom\'s'+
                  '\n\ncloset: I should take it. There is also a working computer here.'+
                  '\n\nI wonder if it has any relevant information on it.')
            print()
            print('1. Collect 10mm Pistol ammunition'+
                  '\n2. Read computer')
            print()
            COLLECT_AMMO = 1
            READ_COMPUTER3 = 2
            choice5 = 0
            choice5 = int(input('Enter your choice: '))
            print()
            while choice5 < COLLECT_AMMO or choice5 > READ_COMPUTER3:
                choice5 = int(input('Enter a valid choice: '))
                print()
            if choice5 == COLLECT_AMMO:
                if AMMO1 not in character_inventory:
                    character_inventory.append(AMMO1)
                    input('SYSTEM: 10mm Pistol ammunition has been'+
                          ' added to your inventory. Press enter to continue. ')
                else:
                    input('SYSTEM: 10mm Pistol ammunition is already in'+
                          ' your inventory. Press enter to continue. ')
            elif choice5 == READ_COMPUTER3:
                input('Press enter to read computer. ')
                print()
                print('---------------------------------------------------------------------------')
                print()
                print('-Property of the Armstrong family')
                print()
                print('Computer entry 1: Dear, Tim'+
'\n\nHey Tim! Just wanted to let you know that I\'ll come by your house next weekend. Sorry, but today'+
'\n\nthe wife was against me and voted that we have our family get-together with our neighbors next door:'+
'\n\nthe McPherson\'s. They\'re a likeable bunch though. Nate McPherson\'s wife, Nora, and my wife are'+
'\n\nprepping the food as I write you know. I\'ll throw down some beers with Nate today. I\'ll swing your way'+
'\n\nnext weekend. Cheers mate!'+
'\n\n-Alex Armstrong'+
'\nJune 17, 2077')
                print()
                print('Thinking to self: You and your family will be missed Alex. I\'m sorry.')
                print()
                input('Press enter to read computer entry 2. ')
                print()
                print('---------------------------------------------------------------------------')
                print()
                print('-Property of the Armstrong family')
                print()
                print('Computer entry 2: Dear, Bob'+
'\n\nDiamond city is too much for me. You can\'t tell if the people there are synths or if'+
'\n\nthey are actual people. That detective, Nick Valentine, freaks me out. He'+
'\n\nhas openly admitted to the entire city that he is in fact a synth. Yet, he'+
'\n\nis allowed to run a detective agency. It should be common sense to not trust'+
'\n\na synth, so why do authorities allow him to stay in the city? Apparently no'+
'\n\none has learned anything after the, "Broken Mask" incident. I don\'t think you'+
'\n\nwere in Diamond city yet Bob, but it happened 10 years ago in 2277. The Institute'+
'\n\nsent a synth to blend in with us humans in Diamond City and it malfunctioned. Then it....'+
'\n\nI\'ll just say it did something bad. Sure, Diamond city has job opportunities,'+
'\n\nsecurity personnel, walls protecting the city, potable water, edible food, and'+
'\n\nso on. But the Institute and it\'s synths have infiltrated the city. I\'m not'+
'\n\ncoming back to Diamond city. I\'m in some old neighborhood named Sanctuary Hills'+
'\n\nright now, and I\'m writing you on some 210 year old computer. I\'m leaving the'+
'\n\nCommonWealth tomorrow. It was nice knowing you Bob. Be safe.'+
'\n\n-Joshua'+
'\nJuly 1, 2287')
                print()
                input('Press enter to continue. ')
                print()
                print('Thinking to self: Just what exactly is the Institute and'+
                            '\n\nwhat are these synths? I should go to this "Diamond'+
                            '\n\nCity" and see if anyone there can help me find my son.'+
                            '\n\nIt is a city after all, so surely there are some people'+
                            '\n\nthere with the ability to help me. This computer entry'+
                            '\n\ndid mention that there is a detective agency there...')
                print()
                input('Press enter to continue. ')

        elif choice2 == YOUR_HOUSE:
            print()
            print('Inside of your house')
            print('--------------------')
            print()
            print('Thinking to self: I sure miss being here. My son Shaun is out there'+
                  '\n\nsomewhere, my wife, Nora, was gunned down in front of me, and'+
                  '\n\nhere I am in our home 210 years later: alone. Wait a minute...'+
                  '\n\nIs that my wedding ring and Nora\'s on the nightstand? It is!'+
                  '\n\nWe didn\'t have them on the day the bombs fell because they'+
                  '\n\nneeded repairing. They are mostly rusted out, but no doubt I'+
                  '\n\nshould take them. And what is that tape recording there? It'+
                  '\n\nhas "Nora\'s voice recording" written on it. Maybe she was going'+
                  '\n\nto surprise me with it. I should play it on the computer in our'+
                  '\n\nliving room, and listen to it. Good thing that the computer still'+
                  '\n\nseems to work. ')
            print()
            print('1. Collect wedding rings on master bedroom nightstand'+
                  '\n2. Listen to Nora\'s voice recording on living room computer')
            print()
            COLLECT_RINGS = 1
            READ_COMPUTER4 = 2
            choice6 = 0
            choice6 = int(input('Enter your choice: '))
            print()
            while choice6 < COLLECT_RINGS or choice6 > READ_COMPUTER4:
                choice6 = int(input('Enter a valid choice: '))
                print()
            if choice6 == COLLECT_RINGS:
                if RING1 and RING2 in character_inventory:
                    input('SYSTEM: The wedding rings are already in your inventory.'+
                      '\n\nPress enter to continue. ')
                else:
                    character_inventory.append(RING1)
                    character_inventory.append(RING2)
                    input('SYSTEM: You place your wedding ring on your hand and'+
                      '\n\nplace Nora\'s wedding ring in your right pocket.'+
                      '\n\nThe two rings have been added to your inventory.'+
                      '\n\nPress enter to continue. ')
            elif choice6 == READ_COMPUTER4:
                print()
                input('Press enter to listen to Nora\'s voice recording on computer. ')
                print()
                print('---------------------------------------------------------------------------')
                print()
                print('-Property of the McPherson Family')
                print()
                print('Computer playing "Nora\'s voice recording":'+
'\n\n*Feedback sound* Oops. Ha ha ha. No, no. Little fingers away. There we go.'+
'\n\nJust say it. Go ahead. *baby Shaun giggles* Ha ha! Hi honey! Listen... I'+
'\n\ndon\'t think Shaun and I need to tell you how great of a father you are...'+
'\n\nbut we\'re going to anyway. You are kind, loving, (*baby Shaun laughs*)...'+
'\n\nand funny! Ha ha. And patient. So patient..... Look, with Shaun, and us all'+
'\n\nbeing at home together...it\'s been an amazing year. But even so, I know'+
'\n\nour best days are yet to come. There will be changes sure. There will be'+
'\n\nthings we\'ll need to adjust to. You\'ll join the civilian workforce, I\'ll'+
'\n\nshake the dust off my law degree...But everything we do, no matter how hard...'+
'\n\nwe do it for our family. Now say goodbye Shaun...Say bye bye baby,(*baby Shaun'+
'\n\ngiggles*) Byyyeee Honey! We love you!'+
'\n\n-Nora and Shaun McPherson'+
'\nRecorded October 21, 2077')
                print()
                print()
                print('Thinking to self: I\'ll find Shaun. For the both of us.')
                print()
                input('Press enter to continue. ')      

    
def redrocket_truckstop(character_inventory, character_inventory2, quest_inventory,
                        prevent_exploit):
    global MONEY
    global CASH1
    if WEAPON1 and AMMO1 in character_inventory:
        if MUTANT_DOGS not in quest_inventory:
            quest_inventory.append(MUTANT_DOGS)
            input('You kill all of the mutant dogs that are outside of'+
                  '\n\nRed Rocket Truck Stop with a weapon of your choice.'+
                  '\n\nYou then enter the Red Rocket Truck Stop. Press'+
                  '\n\nenter to continue. ')
        else:
            input('SYSTEM: You have already killed all of the mutant dogs that'+
                          '\n\nwere here earlier. You walk by their corpses. Press'+
                  '\n\nenter to continue. ')
        OPEN_SAFE = 1
        READ_COMPUTER = 2
        COLLECT_CASH = 3
        COLLECT_FIRSTAID = 4
        QUIT2 = 5
        choice2 = 0
        while choice2 != QUIT2:
            print()
            print('Inside of Red Rocket Truck Stop')
            print('-------------------------------')
            print()
            print('1. Open safe in storage room'+
              '\n2. Read computer in storage room'+
                  '\n3. Collect cash behind the toilet'+
                  '\n4. Collect the first aid kit in the storage room file cabinet'+
                  '\n5. Go back to map (The CommonWealth)')
            print()
            choice2 = int(input('Enter your choice: '))
            print()
            while choice2 < OPEN_SAFE or choice2 > QUIT2:
                choice2 = int(input('Enter a valid choice: '))
                print()
            if choice2 == OPEN_SAFE:
                safe_password = int(input('Enter the safe\'s password: '))
                print()
                if safe_password != int('12345'):
                    input('SYSTEM: Wrong. Hint: The password can be found in Sanctuary'+
                          '\n\nHills. Then it will be stored in your inventory: where'+
                          '\n\nyou can view it. Press enter to continue. ')
                else:
                    if ARMOR1 and FOOD1 in character_inventory2:
                        input('SYSTEM: You have already opened the safe. Light Kevlar'+
                              '\n\nArmor and Canned beans are already in your'+
                              '\n\ninventory. Press enter to continue. ')
                    else:
                        character_inventory2.append(ARMOR1)
                        character_inventory2.append(FOOD1)
                        input('SYSTEM: You opened the safe! Light Kevlar Armor and Canned'+
                          '\n\nbeans have been added to your inventory. Press'+
                          '\n\nenter to continue. ')

            elif choice2 == READ_COMPUTER:
                input('Press enter to read computer. ')
                print()
                print('---------------------------------------------------------------------------')
                print()
                print('-Property of Red Rocket Truck Stop')
                print()
                print('Computer entry 1: Items that need to be restocked'+
                      '\n\n*Chocolate'+
                      '\n\n*Hot dogs'+
                      '\n\n*Hot dog buns'+
                      '\n\n*Jersey Beer'+
                      '\n\n-Zackery Miller'+
                      '\nRed Rocket Truck Stop personnel'+
                      '\nOctober 9, 2077')
                print()
                print('Thinking to self: Not much to see here. ')
                print()
                input('Press enter to read computer entry 2. ')
                print()
                print('---------------------------------------------------------------------------')
                print()
                print('-Property of Red Rocket Truck Stop')
                print()
                print('Computer entry 2: Distress message to nearby military units,'+
                        '\n\nOfficer Miles reporting. I am sending this message'+
                      '\n\nfrom a civilian computer in a business storefront named,'+
                      '\n\n"Red Rocket Truck Stop". I am doing this instead of using'+
                      '\n\nmy radio comms because they went dead after that nuclear bomb'+
                      '\n\nwent off. I am lucky to be alive. My helicopter crashed on'+
                      '\n\ntop of the Muesuem of Freedom in Concord. I had to leave be-'+
                      '\n\nhind my suit of T-45 Power armor, because the fusion core that powers'+
                      '\n\nit went dead. I had to leave behind my assualt rifle as well.'+
                      '\n\nWhat can I do with it? I lost an arm after my helicopter crashed.'+
                      '\n\nMy co-pilot, Junior Officer Garret, helped slow the bleeding and'+
                      '\n\nPatched up my wound. But this patching won\'t hold forever. If'+
                      '\n\nsomeone doesn\'t get here and help me within the next few hours,'+
                      '\n\nthen I\'m a dead man. Junior Officer Garret unfortunately tried to'+
                      '\n\nkill me realizing that we are stranded and have little food'+
                      '\n\nrations. I had to do what I had to do. If no one can come'+
                      '\n\nsave me at least retrieve my gear. It won\'t be good if just'+
                      '\n\nanyone takes my T-45 Power armor (if they find a way to power'+
                      '\n\nit up) and my assualt rifle. That stuff is military grade gear.'+
                      '\n\nIt is made for survival and combat, not for some doofus to steal.'+
                      '\n\n-Officer Miles'+
                      '\nOctober 23, 2077')
                print()
                input('Press enter to continue. ')
                print()
                print('Thinking to self: How terrible. I\'m no doofus, but I should try to take'+
                      '\n\nthat T-45 Power armor and that assualt rifle on the roof of the Muesuem'+
                      '\n\nof Freedom in Concord. I\'m sure it\'s still there since Officer Miles'+
                      '\n\nnever got a response from anyone to his distress call. Power armor was'+
                      '\n\nthe military\'s strongest combat armor. I should know being a war veteran'+
                      '\n\nwho used it in the American-Russian War from 2073-2076. I\'ll take anything'+
                      '\n\nthat\'ll help me survive in this post apocalyptic world so that I can find'+
                      '\n\nShaun.')
                print()
                input('Press enter to continue. ')
                
                    
            elif choice2 == COLLECT_CASH:
                if CASH1 not in prevent_exploit:
                    prevent_exploit.append(CASH1)
                    MONEY = MONEY + CASH1
                    input('SYSTEM: $250 have been added to your inventory. Press'+
                          '\n\nenter to continue. ')
                else:
                    input('SYSTEM: You have already collected the $250 behind'+
                          '\n\nthe toilet. Press enter to continue. ')

            elif choice2 == COLLECT_FIRSTAID:
                if FIRST_AID1 not in prevent_exploit:
                    prevent_exploit.append(FIRST_AID1)
                    if FIRST_AID1 not in character_inventory2:
                        character_inventory2.append(FIRST_AID1)
                        input('SYSTEM: A first aid kit has been added to your'+
                              '\n\ninventory. Press enter to continue. ')
                else:
                    input('SYSTEM: You have already collected the first aid'+
                          '\n\nkit. Press enter to continue. ')

                
    else:
        input('SYSTEM: You need a weapon and ammunition for the weapon before coming here!'+
              '\n\nThere are mutant dogs that are as big as lions threatning to attack you!'+
              '\n\nPress enter to continue. ')
            
main()
