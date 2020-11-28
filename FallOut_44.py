
import characterinventory
import characterinventory2
import characterinventory3
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
#-------------------------------------------------------------------
WEAPON1 = '10mm Pistol'
AMMO1 = '10mm Pistol Ammunition'
RING1 = 'Nora\'s wedding ring'
RING2 = 'Your wedding ring'
BOTTLED_WATER = 'Bottled Purified Water' # this variable also goes in the
                                         # prevent_exploit list
RED_ROCKET_PASSWORD = 'Password to Red Rocket Truck Stop safe: 12345'


# Variables that go into the character_inventory2 list under def main
#--------------------------------------------------------------------
ARMOR1 = 'Light Kevlar Armor' 
FOOD1 = 'Canned Beans' # this variable also goes in the
                       # prevent_exploit list
                       
        # FIRST_AID1 goes here as well. But FIRST_AID1
        # also belongs to the prevent_exploit list.
        
MUESUEM_PASSWORD = 'Muesuem of Freedom\'s public computer password: ThePersonnelHereAreLosers'
FUSION_CORE1 = 'Fusion Core' # this variable also goes in the
                             # prevent_exploit list
WEAPON2 = 'Assualt Rifle'

                             

# Variables that go into the character_inventory3 list under def main
#--------------------------------------------------------------------
    # FIRST_AID2 goes in this list but also goes into the
    # prevent_exploit2 list
AMMO2 = '5.56 Assualt Rifle Ammunition'
ARMOR2 = 'T-45 Power Armor' # this variable also goes in the
                            # prevent_exploit list


    

# Variables that go into the quest_inventory list under def main
#---------------------------------------------------------------
MAN_SIZED_RATS = 'Man-sized rats already defeated'
MUTANT_DOGS = 'Mutant dogs already defeated'
READ_RED_ROCKET_COMPUTER = 'Read computer at Red Rocket Truck Stop'
RAIDERS_1 = 'Raiders already defeated'



# Variables that go into the think_inventory list under def main
#---------------------------------------------------------------
THINK_SELF1 = 'First thought'
THINK_SELF2 = 'Second thought'
THINK_SELF3 = 'Third thought'
THINK_SELF4 = 'Fourth thought'
THINK_SELF5 = 'Fifth thought'
THINK_SELF6 = 'Sixth thought'
THINK_SELF7 = 'Seventh thought'
THINK_SELF8 = 'Eighth thought'
THINK_SELF9 = 'Ninth thought'
THINK_SELF10 = 'Tenth thought'
THINK_SELF11 = 'Eleventh thought'
THINK_SELF12 = 'Twelveth thought'
THINK_SELF13 = 'Thirteenth thought'
THINK_SELF14 = 'Fourteenth thought'



# Variables for the first aid kits that can be collected
# in various places within the program
#--------------------------------------------------------------------------------
FIRST_AID1 = 'First Aid Kit' # this variable goes in both the character_inventory
                             # list and the prevent_exploit list
                             
FIRST_AID2 = 'First Aid Kit' # this variable goes in both the character_inventory2
                             # list and the prevent_exploit2 list


                             

# Variable that hold's that players money
#----------------------------------------
MONEY = 0.0




# Variables for the money that can be collected in various
# places within the program
#------------------------------------------------------------
CASH1 = 250 # this variable goes in the prevent_exploit list
CASH2 = 250 # this variable goes in the prevent_exploit2 list



# File that the program saves to
#-------------------------------
FILENAME = 'FallOut44.txt'

def main():
    
    # global variables that go into character_inventory list
    #-------------------------------------------------------
    global WEAPON1
    global AMMO1
    global RING1
    global RING2
    global BOTTLED_WATER # this variable also goes in the
                         # prevent_exploit list
                         
    global RED_ROCKET_PASSWORD

    

    # global variables that go into the character_inventory2 list
    #-------------------------------------------------------------
    global ARMOR1
    global FOOD1 # this variable also goes in the
                 # prevent_exploit list
                 
        # FIRST_AID1 goes here as well. But FIRST_AID1
        # also belongs to the prevent_exploit list.
        
    global MUESUEM_PASSWORD
    global FUSION_CORE1 # this variable also goes in the
                        # prevent_exploit list
    global WEAPON2
    

                        
    

    # global variables that go into the character_inventory3 list
    #------------------------------------------------------------
        # FIRST_AID2 goes in this list but also goes into the
        # prevent_exploit2 list
    global AMMO2
    global ARMOR2 # this variable also goes in the
                  # prevent_exploit list


        

        
    # global variables that go into the quest_inventory list
    #-------------------------------------------------------
    global MAN_SIZED_RATS
    global MUTANT_DOGS
    global READ_RED_ROCKET_COMPUTER
    global RAIDERS_1


    

    # global variables that go into the think_inventory list
    #-------------------------------------------------------
    global THINK_SELF1
    global THINK_SELF2
    global THINK_SELF3
    global THINK_SELF4
    global THINK_SELF5
    global THINK_SELF6
    global THINK_SELF7
    global THINK_SELF8
    global THINK_SELF9
    global THINK_SELF10
    global THINK_SELF11
    global THINK_SELF12
    global THINK_SELF13
    global THINK_SELF14


    

     # global variable that holds the player's money
     #----------------------------------------------
    global MONEY

    

    # global variables for the money that can be collected in various
    # places within the program
    #----------------------------------------------------------------
    global CASH1 # this variable goes in the prevent_exploit list
    global CASH2 # this variable goes in the prevent_exploit2 list

    
    
    # global variables for the first aid kits that can be collected
    # in various places within the program
    #--------------------------------------------------------------
    global FIRST_AID1 # this variable goes in both the character_inventory
                      # list and the prevent_exploit list
                      
    global FIRST_AID2 # this variable goes in both the character_inventory2
                      # list and the prevent_exploit2 list

                      

    # character_inventory is a list that stores the players collected items
    # It is an object imported from the characterinvenory file
    #--------------------------------------------------------------------------------------
    character_inventory = []
    inventory = characterinventory.CharacterInventory(character_inventory)

    

    # character_inventory2 is a second list that stores the players collected items
    # It is an object imported from the characterinventory2 file
    #------------------------------------------------------------------------------
    character_inventory2 = []
    inventory2 = characterinventory2.CharacterInventory2(character_inventory2)

    

    # character_inventory3 is a third list that stores the players collected items
    # It is an object imported from the characterinventory3 file
    #-----------------------------------------------------------------------------
    character_inventory3 = []
    inventory3 = characterinventory3.CharacterInventory3(character_inventory3)

    

    # quest_inventory is a list that prevents the same messages for various quest
    # from being displayed more than once in certain areas of the program
    #----------------------------------------------------------------------------
    quest_inventory = []

    

    # think_inventory is a list that prevents various thoughts of the player
    # from being displayed more than once
    #-----------------------------------------------------------------------
    think_inventory = []
    

    # prevent_exploit is a list that prevents variables CASH1,
    # FIRST_AID1, BOTTLED_WATER, FOOD1, FUSION_CORE1, and ARMOR2 
    # from being collected more than once/ exploited
    #--------------------------------------------------------
    prevent_exploit = []



    # prevent_exploit2 is a list that prevents variables CASH2
    # and FIRST_AID2 from being collected more than once/ exploited
    #--------------------------------------------------------------
    prevent_exploit2 = []

    
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
            print(character_inventory3)
            print()
            print('Money:\t$',format(MONEY, ',.2f'), sep='')
            print()
            input('Press enter to continue. ')
        elif choice == SANCTUARY_HILLS:
            Sanctuary_Hills = sanctuary_hills(character_inventory, quest_inventory,
                                              think_inventory, prevent_exploit)
        elif choice == REDROCKET_TRUCKSTOP:
            RedRocketTruckStop = redrocket_truckstop(character_inventory, character_inventory2,
                                                     quest_inventory, think_inventory,
                                                     prevent_exploit)
        elif choice == CONCORD:
            ConCord = concord(character_inventory, character_inventory2,
                              character_inventory3, quest_inventory,
                              think_inventory, prevent_exploit,
                              prevent_exploit2)
            
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
    

def sanctuary_hills(character_inventory, quest_inventory,
                    think_inventory, prevent_exploit):
    choice2 = 0
    RUNDOWN_HOUSE1 = 1
    RUNDOWN_HOUSE2 = 2
    NEIGHBOR_HOUSE = 3
    YOUR_HOUSE = 4
    QUIT2 = 5
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
                print('1. Check kitchen cabinets'+
                      '\n2. Read computer in living room')
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
                    if BOTTLED_WATER not in prevent_exploit:
                        prevent_exploit.append(BOTTLED_WATER)
                        if BOTTLED_WATER not in character_inventory:
                            character_inventory.append(BOTTLED_WATER)
                            input('SYSTEM: You find Bottled Purified Water in the kitchen cabinets.'+
                              '\n\nIt has been added to your inventory. Press enter to continue. ')
                    else:
                        input('SYSTEM: You have already collected the Bottled.'+
                              '\n\nPurified Water. Press enter to continue. ')
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
                    if THINK_SELF1 not in think_inventory:
                        print('Thinking to self: I always wondered what Mr.Russell did for work. Apparently he worked at BigWell'+
'\n\nChecmical Plant. I never went out of my way to speak to him though. He was always a jerk to all'+
'\n\nof his neighbors. What am I thinking? This man has been dead for 210 years. I should move on.')
                        think_inventory.append(THINK_SELF1)
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
                    if THINK_SELF2 not in think_inventory:
                        print('Thinking to self: I should remember that passcode to that safe: 12345.'+
                          '\n\nThis person, Rebecca, made this entry not long ago. She must have unfortunately been'+
                          '\n\nkilled by the man-sized rats outside: I did see a woman\'s corpse nearby. Well, I can'+
'\n\ntake whatever she left behind at the Red Rocket Truck Stop.')
                        think_inventory.append(THINK_SELF2)
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
'\n\nthe size of a man that are threatning to attack you if you come any closer! Don\'t be like the woman who'+
                      '\n\nwas killed! You can see her corpse nearby! Press enter to continue. ')
                    
        elif choice2 == RUNDOWN_HOUSE2:
             print()
             print('Inside of run-down house 2')
             print('---------------------------')
             print()
             print('1. Open unlocked safe under the master bedroom\'s bed'+
                   '\n2. Read computer in master bedroom')
             print()
             choice4 = 0
             COLLECT_WEAPON = 1
             READ_COMPUTER2 = 2
             choice4 = int(input('Enter your choice: '))
             print()
             while choice4 < COLLECT_WEAPON or choice4 > READ_COMPUTER2:
                 choice4 = int(input('Enter a valid choice: '))
                 print()
             if choice4 == COLLECT_WEAPON:
                 if WEAPON1 not in character_inventory:
                     character_inventory.append(WEAPON1)
                     input('SYSTEM: You open the unlocked safe under the master bedroom\'s bed'+
                           '\n\nand find a 10mm Pistol. It has been added to your'+
                           '\n\ninventory. Press enter to continue. ')
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
                if THINK_SELF3 not in think_inventory:
                    print('Thinking to self: I\'m assuming Raiders are low-lifes that work together to rob and kill'+
'\n\nfor the sake of their own survival in this post apocalyptic world. Their name,'+
'\n\n"Raiders" sort of implies that. But what in the world are Supermutants? Deathclaws?'+
'\n\nSynths? What is the Institute? Have I seen some of these things already and'+
'\n\njust didn\'t know it at the time?')
                    think_inventory.append(THINK_SELF3)
                    print()
                    input('Press enter to continue. ')
                
        elif choice2 == NEIGHBOR_HOUSE:
            print()
            print('Inside of neighbor\'s run-down house')
            print('--------------------------')
            print()
            if THINK_SELF4 not in think_inventory:
                print('Thinking to self: This was my neighbor\'s house 210 years ago.'+
                  '\n\nThey were a likeable family, but they were killed in the'+
                  '\n\ncryogenic pods by Vault Tec. Such a tragic end...')
                think_inventory.append(THINK_SELF4)
                print()
            print('1. Open rusted car\'s glove compartment in garage'+
                  '\n2. Read computer in master bedroom')
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
                    input('SYSTEM: You open the rusted car\'s glove compartment and'+
                          '\n\nfind a box of 10mm Pistol Ammunition. It has been'+
                          '\n\nadded to your inventory. Press enter to continue. ')
                else:
                    input('SYSTEM: 10mm Pistol Ammunition is already in'+
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
                if THINK_SELF5 not in think_inventory:
                    print('Thinking to self: You and your family will be missed Alex. I\'m sorry.')
                    think_inventory.append(THINK_SELF5)
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
                if THINK_SELF6 not in think_inventory:
                    print('Thinking to self: Just what exactly is the Institute and'+
                            '\n\nwhat are these synths? I should go to this "Diamond'+
                            '\n\nCity" and see if anyone there can help me find my son.'+
                            '\n\nIt is a city after all, so surely there are some people'+
                            '\n\nthere with the ability to help me. This computer entry'+
                            '\n\ndid mention that there is a detective agency there...')
                    think_inventory.append(THINK_SELF6)
                    print()
                    input('Press enter to continue. ')

        elif choice2 == YOUR_HOUSE:
            print()
            print('Inside of your house')
            print('--------------------')
            print()
            if THINK_SELF7 not in think_inventory:
                print('Thinking to self: I sure miss being here. My son Shaun is out there'+
                  '\n\nsomewhere, my wife, Nora, was gunned down in front of me, and'+
                  '\n\nhere I am in our home 210 years later: alone. Wait a minute...'+
                  '\n\nIs that my wedding ring and Nora\'s on the nightstand? It is!'+
                  '\n\nWe didn\'t have them on the day the bombs fell because they'+
                  '\n\nneeded repairing. They are surprisingly in good condition.'+
                  '\n\nAnd what is that tape recording there? It has "Nora\'s voice'+
                  '\n\nrecording" written on it. Maybe she was going to surprise me with it?'+
                  '\n\nI should play it on the computer in our living room, and listen to it.'+
                  '\n\nGood thing that the computer still seems to work. ')
                think_inventory.append(THINK_SELF7)
                print()
            print('1. Collect wedding rings on the master bedroom\'s nightstand'+
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
                if THINK_SELF8 not in think_inventory:
                    print('Thinking to self: I\'ll find Shaun. For the both of us.')
                    think_inventory.append(THINK_SELF8)
                    print()
                input('Press enter to continue. ')      

    
def redrocket_truckstop(character_inventory, character_inventory2,
                        quest_inventory, think_inventory,
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
        choice2 = 0
        OPEN_SAFE = 1
        READ_COMPUTER = 2
        COLLECT_CASH = 3
        COLLECT_FIRSTAID = 4
        QUIT2 = 5
        while choice2 != QUIT2:
            print()
            print('Inside of Red Rocket Truck Stop')
            print('-------------------------------')
            print()
            print('1. Enter safe\'s password in the storage room'+
              '\n2. Read computer in storage room'+
                  '\n3. Look behind the toilet'+
                  '\n4. Collect first aid at the clerk\'s counter'+
                  '\n5. Go back to map (The CommonWealth)')
            print()
            choice2 = int(input('Enter your choice: '))
            print()
            while choice2 < OPEN_SAFE or choice2 > QUIT2:
                choice2 = int(input('Enter a valid choice: '))
                print()
            if choice2 == OPEN_SAFE:
                # the variable safe_password is used to validate
                # the password of the Red Rocket Truck Stop's safe
                safe_password = int(input('Enter the safe\'s password: '))
                print()
                if safe_password != int('12345'):
                    input('SYSTEM: Wrong. Hint: The password can be found in Sanctuary'+
                          '\n\nHills. Then it will be stored in your inventory: where'+
                          '\n\nyou can view it. Press enter to continue. ')
                else:
                    if ARMOR1 in character_inventory:
                        if FOOD1 in prevent_exploit:
                            input('SYSTEM: You have already opened the safe and collected'+
                                  '\n\nit\'s contents. Press enter to continue. ')
                    else:
                        character_inventory2.append(ARMOR1)
                        prevent_exploit.append(FOOD1)
                        character_inventory2.append(FOOD1)
                        input('SYSTEM: You opened the safe! Light Kevlar Armor and Canned'+
                          '\n\nbeans have been added to your inventory. Press'+
                          '\n\nenter to continue. ')

            elif choice2 == READ_COMPUTER:
                if READ_RED_ROCKET_COMPUTER not in quest_inventory:
                    quest_inventory.append(READ_RED_ROCKET_COMPUTER)
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
                      '\n\n*Boston Beer'+
                      '\n\n-Zackery Miller'+
                      '\nRed Rocket Truck Stop personnel'+
                      '\nOctober 9, 2077')
                print()
                if THINK_SELF9 not in think_inventory:
                    print('Thinking to self: Not much to see here. ')
                    think_inventory.append(THINK_SELF9)
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
                if THINK_SELF10 not in think_inventory:
                    print('Thinking to self: How terrible. I\'m no doofus, but I should try to take'+
                      '\n\nthat T-45 Power armor and that assualt rifle on the roof of the Muesuem'+
                      '\n\nof Freedom in Concord. I\'m sure it\'s still there since Officer Miles'+
                      '\n\nnever got a response from anyone to his distress call. Power armor was'+
                      '\n\nthe military\'s strongest combat armor. I should know being a war veteran'+
                      '\n\nwho used it in the American-Russian War from 2073-2076. I\'ll take anything'+
                      '\n\nthat\'ll help me survive in this post apocalyptic world so that I can find'+
                      '\n\nShaun.')
                    think_inventory.append(THINK_SELF10)
                    print()
                input('Press enter to continue. ')
                    
            elif choice2 == COLLECT_CASH:
                if CASH1 not in prevent_exploit:
                    prevent_exploit.append(CASH1)
                    MONEY += CASH1
                    input('SYSTEM: You check behind the toilet and find a hidden stash of $250.'+
                          '\n\nIt has been added to your inventory. Press'+
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

def concord(character_inventory, character_inventory2,  
            character_inventory3, quest_inventory,
            think_inventory, prevent_exploit,
            prevent_exploit2):
    
    global MONEY
    global CASH1
    global CASH2
    
    choice2 = 0
    MUESUEM_OF_FREEDOM = 1
    MYSTERIOUS_SEWER = 2
    QUIT2 = 3
    while choice2 != QUIT2:
        print()
        print('Places in Concord')
        print('-----------------')
        print()
        print('1. Go to the Muesuem of Freedom'+
              '\n2. Investigate the mysterious looking sewer'+
              '\n3. Go back to map (The CommonWealth)')
        print()
        choice2 = int(input('Enter your choice: '))
        print()
        while choice2 < MUESUEM_OF_FREEDOM or choice2 > QUIT2:
            choice2 = int(input('Enter a valid choice: '))
            print()
        if choice2 == MUESUEM_OF_FREEDOM:
            if WEAPON1 and AMMO1 in character_inventory:
                if ARMOR1 in character_inventory2:
                    if RAIDERS_1 not in quest_inventory:
                        quest_inventory.append(RAIDERS_1)
                        input('SYSTEM: You get into a shoot out with a bunch of low'+
                                  '\n\nlifes who call themselves "Raiders". You take cover'+
                                  '\n\nbehind a rusted car. You can hear their bullets'+
                                  '\n\nwhistling over your head. It\'s about 7 of them'+
                                  '\n\nfrom what you can tell. But due to being an ex'+
                                  '\n\nmember of a special combat branch in the military'+
                                  '\n\nand being well equipped: you are able to mow them'+
                                  '\n\ndown with your weapon of choice. However, you'+
                                  '\n\nwere shot in the left shoulder and use a first aid'+
                                  '\n\nkit to take care of it. Press enter to continue. ')
                        if FIRST_AID1 in character_inventory2:
                            character_inventory2.remove(FIRST_AID1)
                    else:
                            input('SYSTEM: You have already killed the "Raiders" that were here. You'+
                          '\n\nwalk by their corpses. Press enter to continue. ')
                            print()
                            print()
                    print('Inside of the Muesuem of Freedom')
                    print('--------------------------------')
                    print()
                    if THINK_SELF11 in think_inventory:
                        print('Thinking to self: Man this place is run-down. There\'s a'+
                          '\n\nhole in the roof up there. The elevators have been destroyed'+
                              '\n\nit seems. I\'ll take the stairs if I need to go up.')
                        think_inventory.append(THINK_SELF11)
                        print()
                    print('1. Collect First Aid Kit by emergency exit (first floor)'+
                          '\n2. Look inside muesuem\'s old ticket booth (first floor)'+
                          '\n3. Read public computer (second floor)'+
                          '\n4. Enter public computer\'s password (second floor)'+
                          '\n5. Search the pilot seat of the crashed helicopter (rooftop)'+
                          '\n6. Search the co-pilot seat of the crashed helicopter (rooftop)'+
                          '\n7. Enter and collect T-45 Power Armor next to the crashed helicopter (rooftop)')
                    print()
                           
                else:
                    input('SYSTEM: Check your inventory! You need either a 10mm Pistol,'+
                              '\n\n10mm Pistol Ammunition, Light Kevlar Armor, and/or a First'+
                              '\n\nAid Kit before coming here. There are men outside who are'+
                              '\n\narmed and they do not look friendly. It seems they are'+
                              '\n\nlooking for something inside of the muesuem... Press'+
                              '\n\nenter to continue. ')
            else:
                input('SYSTEM: Check your inventory! You need either a 10mm pistol,'+
                              '\n\n10mm Pistol Ammunition, Light Kevlar Armor, and/or a First'+
                              '\n\nAid Kit before coming here. There are men outside who are'+
                              '\n\narmed and they do not look friendly. It seems they are'+
                              '\n\nlooking for something inside of the muesuem... Press'+
                              '\n\nenter to continue. ')
            COLLECT_FIRSTAID = 1
            COLLECT_CASH = 2
            READ_COMPUTER = 3
            COLLECT_FUSION_CORE = 4
            COLLECT_ASSUALT_RIFLE = 5
            COLLECT_ASSUALT_RIFLE_AMMO = 6
            ENTER_T45_POWER_ARMOR = 7
            choice3 = 0
            choice3 = int(input('Enter your choice: '))
            print()
            while choice3 < COLLECT_FIRSTAID or choice3 > ENTER_T45_POWER_ARMOR:
                choice3 = int(input('Enter a valid choice: '))
                print()
            if choice3 == COLLECT_FIRSTAID:
                if FIRST_AID2 not in prevent_exploit2:
                    prevent_exploit2.append(FIRST_AID2)
                    if FIRST_AID2 not in character_inventory3:
                        character_inventory3.append(FIRST_AID2)
                        input('SYSTEM: You open the First Aid Kit by the emergency exit and take it.'+
                          '\n\nIt has been added to your inventory. Press enter to continue. ')
                else:
                    input('SYSTEM: You have already collected the first aid'+
                          '\n\nkit. Press enter to continue. ')
            elif choice3 == COLLECT_CASH:
                if CASH2 not in prevent_exploit2:
                    prevent_exploit2.append(CASH2)
                    MONEY = MONEY + CASH2
                    input('SYSTEM: You look inside the muesuem\'s old ticket booth'+
                          '\n\nand find $250. It was well hidden. It has'+
                          '\n\nbeen added to your inventory. ')
                else:
                    input('SYSTEM: You have already collected the $250 inside the'+
                          '\n\nmuesuem\'s ticket booth. Press enter to continue. ')

            elif choice3 == READ_COMPUTER:
                input('Press enter to read computer. ')
                print()
                print('---------------------------------------------------------------------------')
                print()
                print('-Muesuem of Freedom\'s public computer')
                print()
                print('Computer entry 1: GOOD RIDDANCE!'+
                      '\n\nI am SICK AND TIRED of working with everyone here. I AM DONE! PERIOD!'+
                      '\n\nI am typing this on the public computer, so that ANYONE, even'+
                      '\n\ncustomers, may come and read this. I am able to shut off all of this'+
                      '\n\nfacilitie\'s power and keep it that way for as long as I want. The fusion'+
                      '\n\ncore behind this security gate powers this entire place and I can hack'+
                      '\n\ninto it and shut it down from where-ever I please at anytime. And no you'+
                      '\n\nwon\'t be able to trace my signal. Good luck trying to fix it. Who\'s hobby'+
                      '\n\nof hacking computers is worthless now, Peter? Peter, I hope you, Patrick,'+
                      '\n\nElizabeth, Jackson, Jocelyn, and Koby all lose your jobs. Everyday'+
                      '\n\nyou guys open up the muesuem I will shut the power off for 3/4 of the time'+
                      '\n\nthe muesuem is open. Good luck generating income. Peter just because'+
                      '\n\nyou\'re the boss does not give you the right to talk to me like I\'m a child.'+
                      '\n\nPatrick, how about you come to work and actually WORK sometime. I get tired'+
                      '\n\nof getting called in because you\'re too much of a lazy bum to do anything. But'+
                      '\n\nsince you all are about to lose your jobs you\'ve got all day to do that.'+
                      '\n\nElizabeth you should stop gossiping about people behind their back. I felt'+
                      '\n\nlike I was in high school all over again everyday I came there listening to you'+
                      '\n\ntalk about somebody. Jackson how about you stop being so rude to customer\'s?'+
                      '\n\nI\'m sure you\'ll find lots of time to practice that in your bathroom mirror'+
                      '\n\nsince all of you are soon about to be out of a job. Jocelyn you should learn to'+
                      '\n\nrespect people\'s personal space and should try taking a shower sometime. One'+
                      '\n\nday you came by my work space and I swear I was about to pass out. Koby, you'+
                      '\n\nneed to decide what you want to do with your life. Work a full time job or sell'+
                      '\n\ndrugs. I got tired of police coming to the muesuem every other day asking ME'+
                      '\n\nquestions about YOU. And lately there had been some rough looking guys coming'+
                      '\n\nto the muesuem asking where you were. I\'m not trying to die because you cheated'+
                      '\n\nsome thugs their 5 grams and they shoot up the muesuem. The police won\'t even'+
                      '\n\nknow where to find me since you hired me illegally, Peter. I gave you my'+
                      '\n\npaperwork and you said you\'d, "keep it on file." I literally heard and saw you'+
                      '\n\nshred it not even 30 seconds later. You have no records of me that can be used to'+
                      '\n\ntrace me, so you\'re all done for. You guys didn\'t even know my real name. I'+
                      '\n\ndeleted all footage of me as well. The police will have no leads on me at all.'+
                      '\n\nBut if you guys get tired of me shutting the place done so often: this is all you'+
                      '\n\nhave to do. Type in the new password I set on this computer\'s security gate and'+
                      '\n\nit will open. The password is: ThePersonnelHereAreLosers. Type it exactly like'+
                      '\n\nthat. No spaces. Then you can remove the fusion core behind this computer\'s'+
                      '\n\nsecurity gate and you will have removed this place\'s source of power permanently.'+
                      '\n\nThen you all can go find a new job if you so choose.'+
                      '\n\n-"TJ"'+
                      '\nAugust 21, 2077')
                print()
                input('Press enter to continue. ')
                print()
                if THINK_SELF12 not in think_inventory:
                    think_inventory.append(THINK_SELF12)
                    print('Thinking to self: Wow. What a riot. I actually remember seeing this on'+
                          '\n\nthe national news headline. This guy was never found. Crazy. This'+
                          '\n\nwas 210 years ago. To think that they all died when the bombs fell'+
                          '\n\nonly two months and two days later... So unfortunate. At least this'+
                          '\n\ndispute is just as dead as they are. He said the password to the'+
                          '\n\npublic computer in this building is: ThePersonnelHereAreLosers. No'+
                          '\n\nspaces, spelled exactly like that. I\'ll remember it just in case.')
                    print()
                    print()
                if MUESUEM_PASSWORD not in character_inventory2:
                    input('SYSTEM: The muesuem\'s public computer password has been added to your'+
                          '\n\ninventory. Press enter to continue. ')
                    print()
                else:
                    input('SYSTEM: You already have this muesuem\'s public computer'+
                          '\n\npassword. Press enter to continue. ')
                    print()

            elif choice3 == COLLECT_FUSION_CORE:
                input('Press enter to access computer. ')
                print()
                print('---------------------------------------------------------------------------')
                print()
                print('-Muesuem of Freedom\'s public computer')
                print()
                # the variable MuesuemPublicComputerPass is used to
                # validate the muesuem's public computer password
                MuesuemPublicComputerPass = input('Enter the password: ')
                print()
                if MuesuemPublicComputerPass != 'ThePersonnelHereAreLosers':
                    input('COMPUTER: ERROR. That password is incorrect.'+
                          '\n\nSYSTEM: Check your inventory for the'+
                          '\n\nMuesuem of Freedom\'s public computer'+
                          '\n\npassword. Or search around the muesuem'+
                          '\n\nto see if you can find it. Press enter'+
                          '\n\n to continue. ')
                else:
                    choice4 = 0
                    OPEN_SECURITY_GATE = 1
                    choice4 = int(input(' Computer: Access Granted: Enter 1 to open the security gate: '))
                    print()
                    while choice4 < OPEN_SECURITY_GATE or choice4 > OPEN_SECURITY_GATE:
                        choice4 = int(input('Enter a valid choice: '))
                        print()
                    if choice4 == OPEN_SECURITY_GATE:
                        if FUSION_CORE1 not in prevent_exploit:
                            prevent_exploit.append(FUSION_CORE1)
                            if FUSION_CORE1 not in character_inventory2:
                                character_inventory2.append(FUSION_CORE1)
                                input('SYSTEM: You open the security gate and are able to'+
                              '\n\ntake the fusion core out of the power generator'+
                              '\n\nthat it is sitting in. Since the fusion core'+
                              '\n\nwas the power source that gave power to the'+
                              '\n\nentire muesuem: all of the power went out in'+
                              '\n\nthe muesuem after you took the fusion core out'+
                              '\n\nof the power generator. The fusion core has'+
                              '\n\nbeen added to your inventory. Press enter to'+
                              '\n\ncontinue. ')
                        else:
                            input('SYSTEM: You have already collected the fusion core'+
                                  '\n\nbehind this computer\'s security gate. Press'+
                                  '\n\nenter to continue. ')
                                
            elif choice3 == COLLECT_ASSUALT_RIFLE:
                if WEAPON2 not in character_inventory2:
                    character_inventory2.append(WEAPON2)
                    input('SYSTEM: On the roof, you enter a crashed military'+
                          '\n\nhelicopter and notice someone\'s skeleton in it.'+
                          '\n\nThey are wearing a U.S. military\'s pilot uniform'+
                          '\n\nwith the name and title, "Junior Officer Garret"'+
                          '\n\nwritten on the their junior officer\'s uniform jacket.'+
                          '\n\nYou notice an Assualt Rifle in the pilot seat and'+
                          '\n\ntake it knowing it is a better weapon than what you'+
                          '\n\ncurrently have. The Assualt Rifle has been added to'+
                          '\n\nyour inventory. Press enter to continue. ')
                    print()
                    print()
                    if READ_RED_ROCKET_COMPUTER in quest_inventory:
                        if THINK_SELF13 not in think_inventory:
                            think_inventory.append(THINK_SELF13)
                            input('Thinking to self: So this is Junior Officer Garret'+
                                  '\n\nthat I read about at the Red Rocket Truck Stop.'+
                                  '\n\nLooking at his skeleton it seems as if his neck'+
                                  '\n\nwas snapped in half. Officer Miles had killed Garret'+
                                  '\n\nwith only one arm after Garret tried to kill him.'+
                                  '\n\nOfficer miles must have been one tough pilot. I\'m'+
                                  '\n\ngoing to have to take his assualt rifle though.'+
                                  '\n\n(SYSTEM: Press enter to continue. ) ')
                            print()
                else:
                    input('You have already collected the assualt rifle inside of'+
                          '\n\nthe crashed helicopter. Press enter to continue. ')

            elif choice3 == COLLECT_ASSUALT_RIFLE_AMMO:
                if AMMO2 not in character_inventory3:
                    character_inventory3.append(AMMO2)
                    input('SYSTEM: Inside the crashed military helicopter on the'+
                          '\n\nroof: you search the co-pilot\'s seat and find a'+
                          '\n\nbox of 5.56 Assualt Rifle Ammunition. It has been'+
                          '\n\nadded to your inventory. Press enter to continue. ')
                    print()
                else:
                    input('SYSTEM: You have already collected the 5.56 Assualt'+
                          '\n\nRifle Ammunition. Press enter to continue. ')

            elif choice3 == ENTER_T45_POWER_ARMOR:
                if ARMOR2 not in prevent_exploit:
                    prevent_exploit.append(ARMOR2)
                    if FUSION_CORE1 in character_inventory2:
                        if ARMOR2 not in character_inventory3:
                            character_inventory3.append(ARMOR2)
                            input('SYSTEM: You notice that there is T-45 Power Armor'+
                              '\n\nnext to the crashed helicopter. You turn the power'+
                              '\n\narmor on by inserting the fusion core. You then open'+
                              '\n\nthe power armor by twisting the opening valve: the'+
                              '\n\nback of the power suit opens. You then get inside of'+
                              '\n\nthe power armor from the back, as that is the only way'+
                              '\n\nto get inside of it. The back of the power armor then'+
                              '\n\nproceeds to close: fully encompassing you inside of it'+
                              '\n\nand covering every inch of your body in militarty grade'+
                              '\n\nsteel. Press enter to continue. ')
                            print()
                            print()
                            input('Power Armor Computer speaking: Systems initializing. Power armor'+
                              '\n\ncombat readiness grade: B minus. This is because the power armor has'+
                              '\n\nnot had maintenance in....calculating....calculating...'+
                              '\n\n210 years. Power armor power percentage: 100%. All systems'+
                              '\n\nonline and ready.'+
                              '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            if THINK_SELF14 not in think_inventory:
                                think_inventory.append(THINK_SELF14)
                                input('Thinking to self: Being inside of this armor doesn\'t bring back'+
                                  '\n\nthe best of memories. But I\'ve seen enough to know that it'+
                                  '\n\nis doing nothing other than helping me right now.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                    else:
                          input('SYSTEM: You need a fusion core to activate the power armor'+
                              '\n\nbefore obtaining it. Search the muesuem to see if you'+
                              '\n\ncan find a fusion core. Press enter to continue. ')
      
                else:
                    input('SYSTEM: T-45 Power Armor is already in your'+
                          '\n\ninventory. Press enter to continue. ')
main()
