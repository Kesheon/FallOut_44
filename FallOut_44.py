            
import characterinventory
import characterinventory2
import characterinventory3
import characterinventory4
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
RING1 = 'Nora\'s wedding ring' # this variable also goes in the
                               # prevent_exploit list
                               
RING2 = 'Your wedding ring' # this variable also goes in the
                            # prevent_exploit list

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
                            
ARMOR3 = 'T-60 Power Armor' # this variable also goes in the
                            # prevent_exploit list
WEAPON3 = 'Scoped .50 Cal Sniper'
WEAPON4 = 'MiniGun'
DEATHCLAW_MEAT = 'DeathClaw Meat' # This variable can pontentially be
                                  # assigned a different name than
                                  # what it is currently assigned,
                                  # that other name is:
                                  # 'Sewer Creature Meat'. This can
                                  # be seen under the concord def
                                  # function: choice2/MYSTERIOUS_SEWER

    




# Variables that go into the character_inventory4 list under def main
#--------------------------------------------------------------------
    # FIRST_AID3 goes in this list but also goes into the
    # prevent_exploit3 list

FUSION_CORE2 = 'Fusion Core' # this variable also goes in the
                             # prevent_exploit2 list


TELEPORT_REMOTE = 'Teleportation Remote'


    

# Variables that go into the quest_inventory list under def main
#---------------------------------------------------------------
MAN_SIZED_RATS = 'Man-sized rats already defeated'
READ_ABOUT_NICK = 'Knew about Nick before going to Diamond City'
MUTANT_DOGS = 'Mutant dogs already defeated'
READ_RED_ROCKET_COMPUTER = 'Read computer at Red Rocket Truck Stop'
RAIDERS_1 = 'Raiders already defeated'
DEATH_CLAW = 'Death Claw already defeated'
DIAMOND_CITY_TRAVEL = 'Your first time going to Diamond City'
TALKED_TO_NICK = 'Nick has explained much about the CommonWealth'
TALKED_TO_MERCHANT = 'Unique dialouge with merchant was read'
ENCOUNTERED_MAFIA = 'You uninvoluntarily got involved with a mafia'
BOUNTY_QUEST = 'You accepted the Feral Ghoul bounty'
PURSUE_KELLOG = 'You pursued and fought Kellog the Courser'



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
THINK_SELF15 = 'Fifteenth thought'
THINK_SELF16 = 'Sixteenth thought'
# there is a "think to self" in the diamond city def func
# under MERCHANT (option2) but it is not included here as
# it is exceptional



# Variables for the first aid kits that can be collected
# in various places within the program
#--------------------------------------------------------------------------------
FIRST_AID1 = 'First Aid Kit' # this variable goes in both the character_inventory2
                             # list and the prevent_exploit list
                             
FIRST_AID2 = 'First Aid Kit' # this variable goes in both the character_inventory3
                             # list and the prevent_exploit2 list

FIRST_AID3 = 'First Aid Kit' # this variable goes in both the character_inventory4
                             # list and the prevent_exploit3 list 


                             

# Variable that hold's that players money
#----------------------------------------
MONEY = 6000




# Variables for the money and the value of in game items
#------------------------------------------------------------
CASH1 = 250 # this variable goes in the prevent_exploit list

CASH2 = 250 # this variable goes in the prevent_exploit2 list

SNIPER_VALUE = 1500

MINIGUN_VALUE = 1500

FIRSTAIDKIT3_VALUE = 100

ARMOR3_VALUE = 3000 

FUSION_CORE2_VALUE = 1100

RING1_VALUE = 1250

RING2_VALUE = 1250

DEATH_CLAW_MEAT_VALUE = 500

MAFIA_MONEY_VALUE = 6000

BOUNTY_POSTER_VALUE = 2000



# File that the program saves to
#-------------------------------
FILENAME = 'FallOut44.txt'

def main():
    
    # global variables that go into character_inventory list
    #-------------------------------------------------------
    global WEAPON1
    global AMMO1
    global RING1 # this variable also goes in the
                 # prevent_exploit list
                 
    global RING2 # this variable also goes in the
                 # prevent_exploit list
    
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

    global ARMOR3 # this variable also goes in the
                  # prevent_exploit list
    global WEAPON3
    global WEAPON4
    global DEATHCLAW_MEAT # This variable can pontentially be
                          # assigned a different name than
                          # what it is currently assigned,
                          # that other name is:
                          # 'Sewer Creature Meat'. This can
                          # be seen under the concord def
                          # function: choice2/MYSTERIOUS_SEWER

                          


    # global variables that go into the character_inventory4 list
    #------------------------------------------------------------

        # FIRST_AID3 goes in this list but also goes into the
        # prevent_exploit3 list
        
    global FUSION_CORE2 # this variable goes in this list but also
                        # goes into the prevent_exploit2 list

    global TELEPORT_REMOTE



        

        
    # global variables that go into the quest_inventory list
    #-------------------------------------------------------
    global MAN_SIZED_RATS
    global READ_ABOUT_NICK
    global MUTANT_DOGS
    global READ_RED_ROCKET_COMPUTER
    global RAIDERS_1
    global DEATH_CLAW
    global DIAMOND_CITY_TRAVEL
    global TALKED_TO_NICK
    global TALKED_TO_MERCHANT
    global ENCOUNTERED_MAFIA
    global BOUNTY_QUEST
    global PURSUE_KELLOG


    

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
    global THINK_SELF15
    global THINK_SELF16
    # there is a "think to self" in the diamond city def func
    # under MERCHANT (option2) but it is not included here as
    # it is exceptional


    

    # global variable that holds the player's money
    #----------------------------------------------
    global MONEY

    

    # global variables for the money and the value of in game items
    #----------------------------------------------------------------
    global CASH1 # this variable goes in the prevent_exploit list
    
    global CASH2 # this variable goes in the prevent_exploit2 list

    global SNIPER_VALUE

    global MINIGUN_VALUE

    global FIRSTAIDKIT3_VALUE

    global ARMOR3_VALUE 

    global FUSION_CORE2_VALUE

    global RING1_VALUE

    global RING2_VALUE

    global DEATH_CLAW_MEAT_VALUE

    global MAFIA_MONEY_VALUE

    global BOUNTY_POSTER_VALUE

    
    
    # global variables for the first aid kits that can be collected
    # in various places within the program
    #--------------------------------------------------------------
    global FIRST_AID1 # this variable goes in both the character_inventory2
                      # list and the prevent_exploit list
                      
    global FIRST_AID2 # this variable goes in both the character_inventory3
                      # list and the prevent_exploit2 list

    global FIRST_AID3 #this variable goes in both the character_inventory4
                      # list and the prevent_exploit3 list

                      

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




    #character_inventory4 is a fourth list that stores the players collected items
    # It is an object importred from the characterinventory4 file
    #-----------------------------------------------------------------------------
    character_inventory4 = []
    inventory4 = characterinventory4.CharacterInventory4(character_inventory4)

    

    # quest_inventory is a list that prevents the same messages for various quest
    # from being displayed more than once in certain areas of the program
    #----------------------------------------------------------------------------
    quest_inventory = []

    

    # think_inventory is a list that prevents various thoughts of the player
    # from being displayed more than once
    #-----------------------------------------------------------------------
    think_inventory = []
    

    # prevent_exploit is a list that prevents variables CASH1,
    # FIRST_AID1, BOTTLED_WATER, FOOD1, FUSION_CORE1, ARMOR2,
    # RING1, and RING2 from being collected more than once/ exploited
    #----------------------------------------------------------------
    prevent_exploit = []



    # prevent_exploit2 is a list that prevents variables CASH2,
    # FIRST_AID2, and FUSION_CORE2 from being collected more
    # than once/ exploited
    #--------------------------------------------------------------
    prevent_exploit2 = []


    # prevent_exploit3 is a list that prevents the variables
    # FIRST_AID3 and ARMOR3 from being collected
    # more than once/ exploited
    #-------------------------------------------------------
    prevent_exploit3 = []
    
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
            print(character_inventory4)
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

        elif choice == DIAMOND_CITY:
            Diamond_City = diamond_city(character_inventory, character_inventory2,
                                        character_inventory3, character_inventory4,
                                        quest_inventory, think_inventory,
                                        prevent_exploit, prevent_exploit2,
                                        prevent_exploit3)
        elif choice == FORT_HAGEN:
            Fort_Hagen = fort_hagen(character_inventory3, character_inventory4,
                                    quest_inventory)

        elif choice == INSTITUTE:
            Institute = institute(character_inventory4)
            
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
'\n\nbigger due to the radiation that comes from the atomic bombs that dropped 210 years ago. I wish I could'+
'\n\nhave seen what animals were like in the pre-apocalyptic world: I hate that I was born in this post-apocalyptic'+
'\n\nworld. I stored some canned beans in a safe at Red Rocket Truck Stop so that I can have a guaranteed meal'+
'\n\nin the case of an emergency. Reminder to self: the passcode to that safe is 12345. There is also some light'+
'\n\nkevlar armor in there. It helps to wear armor since so many people and things want to hurt one another in this'+
'\n\npost-apocalyptic world. I also put $250 behind the Red Rocket Truck Stop\'s public toilet and a first aid'+
'\n\nkit in the storage room\'s file cabinet. I would carry all these things on me, but I have don\'t want to draw'+
'\n\nto much attention to myself. Honestly I\'m crying as I write this. Life is so hard out here. I had three'+
'\n\noptions and all of them were bad. I could have stayed in Diamond City and risked the danger of the Institute'+
'\n\nand their synths. I could leave Diamond City and hope to find a better place to settle; I chose this and it'+
'\n\nis not going well. Or I could have chosen to leave the CommonwWealth in the hope of something better being'+
'\n\nout there. But that is too risky if you ask me.'+
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
                        input('SYSTEM: Password to Red Rocket Truck Stop safe has been added to your inventory.'+
                          '\n\nPress enter to continue. ')
            else:
                input('SYSTEM: You need a weapon and ammunition for the weapon before coming here. There are rats' +
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
                     input('SYSTEM: You have already opened the safe and collected the 10mm Pistol'+
                           '\n\nthat was inside of it. Press enter to continue. ')
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
                    input('SYSTEM: You have already opened the glove compartment and have'+
                          '\n\ncollected the 10mm Pistol Ammunition that was inside of'+
                          '\n\nit. Press enter to continue. ')
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
                if READ_ABOUT_NICK not in quest_inventory:
                    quest_inventory.append(READ_ABOUT_NICK)
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
                  '\n\nhere I am in our home 210 years later: alone..... Wait a minute...'+
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
                if RING1 and RING2 in prevent_exploit:
                    input('SYSTEM: You have already collected the wedding'+
                          '\n\nrings. Press enter to continue. ')
                else:
                    prevent_exploit.append(RING1)
                    prevent_exploit.append(RING2)
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
            input('SYSTEM: You kill all of the mutant dogs that are outside of'+
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
                      '\n\npatched up my wound. But this patching won\'t hold forever. If'+
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
                    input('Thinking to self: How terrible. I wonder if I can head that way and'+
                          '\n\nretrieve Officer Miles\' gear. But I wonder: how I can power up his'+
                          '\n\npower armor? He said that the fusion core went dead. If I find a'+
                          '\n\nway to power it up there\'s no doubt that I can use it. I know how'+
                          '\n\nto after all: I did fight in power armor for the special forces in'+
                          '\n\nthe World War 3. Plus, they had us learn how to operate practically'+
                          '\n\nany type of weapon we come across: I\'m more than sure that I still'+
                          '\n\nknow how to shoot a simple Assualt Rifle properly.'+
                          '\n\n(SYSTEM: Press enter to continue. ')
                    think_inventory.append(THINK_SELF10)
                    print()
                    
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
    global CASH2
    global DEATHCLAW_MEAT
    
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
                        print()
                        print()
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
                    if THINK_SELF11 not in think_inventory:
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
                    print()
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
                          '\n\nsince all of you are soon about to be out of a job. Jackson you should also stop'+
                          '\n\nstealing money out of the cash register and hiding it in the ticket booth so that'+
                          '\n\nyou can take it for later: no you are not slick. Jocelyn you should learn to'+
                          '\n\nrespect people\'s personal space and should try taking a shower sometime. One'+
                          '\n\nday you came by my work space and I swear I was about to pass out. Koby, you'+
                          '\n\nneed to decide what you want to do with your life. Work a full time job or sell'+
                          '\n\ndrugs. I got tired of seeing police coming to the muesuem every other day asking PETER'+
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
                                input('Power Armor Computer speaking (robotically): Systems initializing. Power armor'+
                                      '\n\ncombat readiness grade: B minus. This is because the power armor has not had'+
                                      '\n\nmaintenance in....calculating....calculating... 210 years. Power armor hull'+
                                      '\n\nintegrity: 100%. Emergency Attack Mode: Available. All other systems online'+
                                      '\n\nand ready.'+
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
                        input('SYSTEM: You have already collected the T-45'+
                              '\n\npower armor. Press enter to continue. ')
                    
                else:
                    input('SYSTEM: Check your inventory! You need stronger armor before'+
                          '\n\nhere. There are men outside who are armed and they do not'+
                          '\n\nlook friendly. It seems they are looking for something'+
                          '\n\ninside of the muesuem...'+
                          '\n\nPress enter to continue. ')
                    

            else:
                input('SYSTEM: Check your inventory! You need a stronger weapon and'+
                      '\n\nammunition for the weapon before coming here. There are'+
                      '\n\nmen outside who are armed and they do not look friendly.'+
                      '\n\nIt seems they are looking for something inside of the'+
                      '\n\nmuesuem...'+
                      '\n\nPress enter to continue. ')
        
        elif choice2 == MYSTERIOUS_SEWER:
            if ARMOR2 in character_inventory3:
                if WEAPON2 in character_inventory2 and AMMO2 in character_inventory3:
                    if TALKED_TO_NICK not in quest_inventory:
                        if DEATH_CLAW not in quest_inventory:
                            quest_inventory.append(DEATH_CLAW)
                            input('SYSTEM: You go down the street from the Muesuem of Freedom'+
                                  '\n\nand you notice that something is growling while banging'+
                                  '\n\non a sewer lid. You get closer and some creature springs'+
                                  '\n\nout from the inside of the sewer: it towers over you at'+
                                  '\n\naround 10 feet tall, (you are 6 feet tall but due to being'+
                                  '\n\nin your power armor you are 7 feet tall) it\'s hands are'+
                                  '\n\nclaw-like, it has the horns of a bull (but 10 times bigger,'+
                                  '\n\nand they point forward and straight instead of wide and upward),'+
                                  '\n\nand it\'s skin appears to be very thick.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('Creature: RAAAAAAAAGGGGGGGHHHHHHHH....RAAAAGGGHHHHH!!!!'+
                                  '\n\n(SYSTEM: Press enter to continue.)')
                            print()
                            print()
                            input('SYSTEM: The creature charges at you, but you manage to evade it.'+
                                  '\n\nBut this was pure luck. It is obviously much faster than you: you are'+
                                  '\n\nin a steel suit after all. It got it\'s horns stuck inside of a nearby'+
                                  '\n\nrusted car, but he quickly recovers. You manage to pull out one of your'+
                                  '\n\nstrongest weapons and start to shoot at it. This is obviously working as'+
                                  '\n\nthe creature is starting to weaken, but it doesn\'t stop him from relentlessly'+
                                  '\n\ncharging at you. This is because the bullets do not fully penetrate his thick'+
                                  '\n\nskin. He grabs hold of you, picks you up while inside of your T-45 power armor,'+
                                  '\n\nand slams you into the ground while ramming his horns into the torso of your armor.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You screaming in pain: AGGGGGGHHHHH!!!'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('Power Armor Computer speaking (robotically): Warning! Momentous damage'+
                                  '\n\ntaken in the armor\'s torso. Power armor hull integrity is now at'+
                                  '\n\n58%. Proceed attentively and fully combat ready.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You yelling at Power Armor Computer: I KNOW THAT DANG IT! '+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You speaking fast: *heavy breathing* I know that this power armor'+
                                  '\n\nis an older model, but it can take on *heavy breathing* multiple'+
                                  '\n\ntank shells with mild damage. How did this creature nearly put a'+
                                  '\n\nhole in the sturdiest part of my armor?!?! *heavy breathing*'+
                                  '\n\nIs the physical force of his horn ramming my armor seriously'+
                                  '\n\nequivalent to about 12 exploding tank shells hitting me all'+
                                  '\n\nat the same time but in one concentrated shot?!?!'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('Power Armor Computer speaking (robotically): Calculating'+
                                  '\n\ndamage...............That is precise, actually.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You yelling at Power Armor Computer: SHUT UP!'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('SYSTEM: After pinning you down and ramming it\'s horns into your'+
                                 '\n\narmor\'s torso: the creature runs backwards preparing for it\'s'+
                                 '\n\nfinal charge, but it staggers and falls a few times because you'+
                                 '\n\nweakend it by shooting it with one of your stronger weapons earlier.'+
                                 '\n\nYou hurry to your feet and shower the creature with as many bullets'+
                                 '\n\nas you can, but again, none of the bullets fully penetrate him. As'+
                                 '\n\nit is about to reach you, you have to reload, but have no time to do so.'+
                                 '\n\nYou choose to not use the gun....'+
                                 '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You yelling at Power Armor Computer: **heavier breathing**'+
                                  '\n\nCOMPUTER INITIATE EMERGENCY ATTACK MODE RIGHT NOW!!'+
                                  '\n\n(SYSTEM: Press enter to continue. )')
                            print()
                            print()
                            input('Power Armor Computer speaking fast (robotically): Urgency detected!'+
                                  '\n\nWarning! Emergency attack mode strains the power source of the'+
                                  '\n\npower armor (the fusion core) to increase your physical attack energy'+
                                  '\n\noutput by 3,257% and your attack speed by 250% for 5 seconds. There is'+
                                  '\n\na 35%-40% chance that the power armor will go dead upon activation of'+
                                  '\n\nthis mode due to straining it\'s power source. If that happens...'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('Creature: RAGGHHHHHHHH... RAGGGHHHHH'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You yelling at Power Armor Computer: DO IT NOOOOWWWW!!!'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('Power Armor Computer speaking even faster (robotically): Desperation'+
                                  '\n\ndetected! Emergency Attack Mode initiated. Emergency Attack'+
                                  '\n\nMode successfully activated. Warning! Power source (fusion core)'+
                                  '\n\nbeing strained! Warning! Emergency Attack Mode will last only 5'+
                                  '\n\nseconds!'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('SYSTEM: As the creature is about to grab a hold of you, you dodge it\'s'+
                                  '\n\nclaw-like hands extremely fast: earlier you dodged him out of pure luck,'+
                                  '\n\nbut this time it\'s thanks to the speed Emergency Attack Mode provides.'+
                                  '\n\nYou prepare to punch the creature as hard as you can.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You screaming as you prepare a devestating punch: AAAAGGGGGHHHHH!!!!'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('SYSTEM: You punch a hole through the thick skin of the creature (in'+
                                  '\n\nthe chest area) that not even bullets from your strongest weapons'+
                                  '\n\ncould penetrate. You drive the creature not only to the ground,'+
                                  '\n\nbut somewhat through the ground: creating a mini-crater that\'s'+
                                  '\n\nabout 4 feet deep. It\'s as if Emergency Attack Mode strapped a'+
                                  '\n\nrocket to your arm to create such a devestating punch.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You speaking to Power Armor Computer: **heavy breathing** Computer'+
                                  '\n\n**heavy breathing** scan the enemy **heavy breathing** and give'+
                                  '\n\nme a battle report.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('Power Armor Computer speaking (robotically): Scanning'+
                                  '\n\nenemy..........Enemy\'s heart is missing. The enemy'+
                                  '\n\nhas passed. Battle report:..............Emergency'+
                                  '\n\nAttack Mode Deactivated. The 5 seconds are over.'+
                                  '\n\nPower source (fusion core) no longer being strained.'+
                                  '\n\nPower armor hull intergrity: 58% as last reported.'+
                                  '\n\nMomentous damage was taken to the torso of the armor.'+
                                  '\n\nScanning your vitals....Scan complete. You have ex-'+
                                  '\n\nperienced an adrenaline rush and a PTSD attack: which'+
                                  '\n\nmay be a result of past battle experiences haunting'+
                                  '\n\nyour mental psyche. However you have handled it well.'+
                                  '\n\nImmediate treatment: if possible sit down and try to'+
                                  '\n\ncontrol your breathing. To help I will activate the power'+
                                  '\n\narmor\'s oxygen reserves, because you are lacking oxygen.'+
                                  '\n\nSerious medical help: not needed. However, after regaining'+
                                  '\n\nyour breath you should exit the armor for a while and apply'+
                                  '\n\n1 or 2 first aid kits to yourself. The armor\'s torso area'+
                                  '\n\ncaved in much and has your chest area slighly bleeding.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You speaking to Power Armor Computer: ***much heavier breathing*** No!'+
                                  '\n\nDeactivate ***Wheezing*** the oxygen ***much heavier breathing'+
                                  '\n\n*** reserves. You don\'t ***Wheezing*** act without my'+
                                  '\n\n****much heavier breathing**** permission.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('Power Armor Computer speaking (robotically): I am programmed'+
                                  '\n\nto keep the user of the armor alive. Oxygen will continue'+
                                  '\n\nto be released. Scanners indicate that without at least 11'+
                                  '\n\nmore minutes of using the oxygen reserves: you will surely'+
                                  '\n\ndie from shortness of breath. Sit down and breath in and out'+
                                  '\n\nslowly.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You softly speaking to Power Armor Computer: *lessened heavy breathing*'+
                                  '\n\nOk.............*lessened heavy breathing* you win...*lessened heavy'+
                                  '\n\nbreathing*.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            if FIRST_AID1 in character_inventory2:
                                character_inventory2.remove(FIRST_AID1)
                            elif FIRST_AID2 in character_inventory3:
                                character_inventory3.remove(FIRST_AID2)
                            print()
                            print()
                            input('SYSTEM: After calming down, regaining your breath, and applying 1 or'+
                                  '\n\nfirst aid kits to yourself: you skin the creature by breaking off'+
                                  '\n\na sharp piece of steel off of a nearby rusted car and use it as'+
                                  '\n\na knife. You then store it\'s meat in your inventory. You do this'+
                                  '\n\nknowing that it might be good to sale: if you can find a buyer.'+
                                  '\n\nPress enter to continue. ')
                            
                            DEATHCLAW_MEAT = 'Sewer Creature Meat'
                            if DEATHCLAW_MEAT not in character_inventory3:
                                character_inventory3.append(DEATHCLAW_MEAT)

                        else:
                            input('SYSTEM: You have already defeated the'+
                                  '\n\ncreature that came out of the sewer. '+
                                  '\n\nPress enter to continue. ')
                    else:
                        if DEATH_CLAW not in quest_inventory:
                            quest_inventory.append(DEATH_CLAW)
                            input('SYSTEM: You go down the street from the Muesuem of Freedom'+
                                  '\n\nand you notice that something is growling while banging'+
                                  '\n\non a sewer lid. You get closer and a DeathClaw springs'+
                                  '\n\nout from the inside of the sewer: it towers over you at'+
                                  '\n\naround 10 feet tall, (you are 6 feet tall but due to being'+
                                  '\n\nin your power armor you are 7 feet tall) it\'s hands are'+
                                  '\n\nclaw-like, it has the horns of a bull (but 10 times bigger,'+
                                  '\n\nand they point forward and straight instead of wide and upward),'+
                                  '\n\nand it\'s skin appears to be very thick. The DeathClaw\'s'+
                                  '\n\nappearance fits the description Nick Valentine gave you in'+
                                  '\n\nback in Diamond City.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('DeathClaw: RAAAAAAAAGGGGGGGHHHHHHHH....RAAAAGGGHHHHH!!!!'+
                                  '\n\n(SYSTEM: Press enter to continue.)')
                            print()
                            print()
                            input('SYSTEM: The DeathClaw charges at you, but you manage to evade it.'+
                                  '\n\nBut this was pure luck. It is obviously much faster than you: you are'+
                                  '\n\nin a steel suit after all. It got it\'s horns stuck inside of a nearby'+
                                  '\n\nrusted car, but he quickly recovers. You manage to pull out one of your'+
                                  '\n\nstrongest weapons and start to shoot at it. This is obviously working as'+
                                  '\n\nthe DeathClaw is starting to weaken, but it doesn\'t stop him from relentlessly'+
                                  '\n\ncharging at you. This is because the bullets do not fully penetrate his thick'+
                                  '\n\nskin. He grabs hold of you, picks you up while inside of your T-45 power armor,'+
                                  '\n\nand slams you into the ground while ramming his horns into the torso of your armor.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You screaming in pain: AGGGGGGHHHHH!!!'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('Power Armor Computer speaking (robotically): Warning! Momentous damage'+
                                  '\n\ntaken in the armor\'s torso. Power armor hull integrity is now at'+
                                  '\n\n58%. Proceed attentively and fully combat ready.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You yelling at Power Armor Computer: I KNOW THAT DANG IT! '+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You speaking fast: *heavy breathing* I know that this power armor'+
                                  '\n\nis an older model, but it can take on *heavy breathing* multiple'+
                                  '\n\ntank shells with mild damage. How did this DeathClaw nearly put a'+
                                  '\n\nhole in the sturdiest part of my armor?!?! *heavy breathing*'+
                                  '\n\nIs the physical force of his horn ramming my armor seriously'+
                                  '\n\nequivalent to about 12 exploding tank shells hitting me all'+
                                  '\n\nat the same time but in one concentrated shot?!?!'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('Power Armor Computer speaking (robotically): Calculating'+
                                  '\n\ndamage...............That is precise, actually.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You yelling at Power Armor Computer: SHUT UP!'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('SYSTEM: After pinning you down and ramming it\'s horns into your'+
                                  '\n\narmor\'s torso: the DeathClaw runs backwards preparing for it\'s'+
                                  '\n\nfinal charge, but it staggers and falls a few times because you'+
                                  '\n\nweakend it by shooting it with one of your stronger weapons earlier.'+
                                  '\n\nYou hurry to your feet and shower the DeathClaw with as many bullets'+
                                  '\n\nas you can, but again, none of the bullets fully penetrate him. As'+
                                  '\n\nit is about to reach you, you have to reload, but have no time to.'+
                                  '\n\ndo so. You choose to not use the gun....'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You yelling at Power Armor Computer: **heavier breathing**'+
                                  '\n\nCOMPUTER INITIATE EMERGENCY ATTACK MODE RIGHT NOW!!'+
                                  '\n\n(SYSTEM: Press enter to continue. )')
                            print()
                            print()
                            input('Power Armor Computer speaking fast (robotically): Urgency detected!'+
                                  '\n\nWarning! Emergency attack mode strains the power source of the'+
                                  '\n\npower armor (the fusion core) to increase your physical attack energy'+
                                  '\n\noutput by 3,257% and your attack speed by 250% for 5 seconds. There is'+
                                  '\n\na 35%-40% chance that the power armor will go dead upon activation of'+
                                  '\n\nthis mode due to straining it\'s power source. If that happens...'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('DeathClaw: RAGGHHHHHHHH... RAGGGHHHHH!!!'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You yelling at Power Armor Computer: DO IT NOOOOWWWW!!!'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('Power Armor Computer speaking even faster (robotically): Desperation'+
                                  '\n\ndetected! Emergency Attack Mode initiated. Emergency Attack'+
                                  '\n\nMode successfully activated. Warning! Power source (fusion core)'+
                                  '\n\nbeing strained! Warning! Emergency Attack Mode will last only 5'+
                                  '\n\nseconds!'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('SYSTEM: As the DeathClaw is about to grab a hold of you, you dodge it\'s'+
                                  '\n\nclaw-like hands extremely fast: earlier you dodged him out of pure luck,'+
                                  '\n\nbut this time it\'s thanks to the speed Emergency Attack Mode provides.'+
                                  '\n\nYou prepare to punch the DeathClaw as hard as you can.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You screaming as you prepare a devestating punch: AAAAGGGGGHHHHH!!!!'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('SYSTEM: You punch a hole through the thick skin of the DeathClaw (in'+
                                  '\n\nthe chest area) that not even bullets from your strongest weapons'+
                                  '\n\ncould penetrate. You drive the DeathClaw not only to the ground,'+
                                  '\n\nbut somewhat through the ground: creating a mini-crater that\'s'+
                                  '\n\nabout 4 feet deep. It\'s as if Emergency Attack Mode strapped a'+
                                  '\n\nrocket to your arm to create such a devestating punch.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You speaking to Power Armor Computer: **heavy breathing** Computer'+
                                  '\n\n**heavy breathing** scan the enemy **heavy breathing** and give'+
                                  '\n\nme a battle report.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('Power Armor Computer speaking (robotically): Scanning'+
                                  '\n\nenemy..........Enemy\'s heart is missing. The enemy'+
                                  '\n\nhas passed. Battle report:..............Emergency'+
                                  '\n\nAttack Mode Deactivated. The 5 seconds are over.'+
                                  '\n\nPower source (fusion core) no longer being strained.'+
                                  '\n\nPower armor hull intergrity: 58% as last reported.'+
                                  '\n\nMomentous damage was taken to the torso of the armor.'+
                                  '\n\nScanning your vitals....Scan complete. You have ex-'+
                                  '\n\nperienced an adrenaline rush and a PTSD attack: which'+
                                  '\n\nmay be a result of past battle experiences haunting'+
                                  '\n\nyour mental psyche. However you have handled it well.'+
                                  '\n\nImmediate treatment: if possible sit down and try to'+
                                  '\n\ncontrol your breathing. To help I will activate the power'+
                                  '\n\narmor\'s oxygen reserves, because you are lacking oxygen.'+
                                  '\n\nSerious medical help: not needed. However, after regaining'+
                                  '\n\nyour breath you should exit the armor for a while and apply'+
                                  '\n\n1 or 2 first aid kits to yourself. The armor\'s torso area'+
                                  '\n\ncaved in much and has your chest area slighly bleeding.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You speaking to Power Armor Computer: ***much heavier breathing*** No!'+
                                  '\n\nDeactivate ***Wheezing*** the oxygen ***much heavier breathing'+
                                  '\n\n*** reserves. You don\'t ***Wheezing*** act without my'+
                                  '\n\n****much heavier breathing**** permission.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('Power Armor Computer speaking (robotically): I am programmed'+
                                  '\n\nto keep the user of the armor alive. Oxygen will continue'+
                                  '\n\nto be released. Scanners indicate that without at least 11'+
                                  '\n\nmore minutes of using the oxygen reserves: you will surely'+
                                  '\n\ndie from shortness of breath. Sit down and breath in and out'+
                                  '\n\nslowly.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            print()
                            print()
                            input('You softly speaking to Power Armor Computer: *lessened heavy breathing*'+
                                  '\n\nOk.............*lessened heavy breathing* you win...*lessened heavy'+
                                  '\n\nbreathing*.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                            if FIRST_AID1 in character_inventory2:
                                character_inventory2.remove(FIRST_AID1)
                            elif FIRST_AID2 in character_inventory3:
                                character_inventory3.remove(FIRST_AID2)
                            print()
                            print()
                            input('SYSTEM: After calming down, regaining your breath, and applying 1 or'+
                                  '\n\nfirst aid kits to yourself: you skin the DeathClaw by breaking off'+
                                  '\n\na sharp piece of steel off of a nearby rusted car and use it as a'+
                                  '\n\nknife. You then store it\'s meat in your inventory. You do this'+
                                  '\n\nknowing that it might be good to sale: if you can find a buyer.'+
                                  '\n\nPress enter to continue. ')
                            
                            if DEATHCLAW_MEAT not in character_inventory3:
                                character_inventory3.append(DEATHCLAW_MEAT)

                        else:
                            input('SYSTEM: You have already defeated the De-'+
                                  '\n\nathClaw that came out of the sewer.'+
                                  '\n\nPress enter to continue. ')
                            

                else:
                    if TALKED_TO_NICK in quest_inventory:
                        input('SYSTEM: You go down the street from the Muesuem of Freedom'+
                              '\n\nand you notice that something is growling while banging'+
                              '\n\non a sewer lid. You look intensely and notice that it is'+
                              '\n\na DeathClaw staring intently at you through the lid. You'+
                              '\n\nbook it out of there. (You need a stronger weapon and ammo'+
                              '\n\nfor the weapon before coming here.'+
                              '\n\nPress enter to continue. ')
                    else:
                        input('SYSTEM: You go down the street from the Muesuem of Freedom'+
                              '\n\nand you notice that something is growling while banging'+
                              '\n\non a sewer lid. You look intensely and notice that it is'+
                              '\n\na strange creature staring intently at you through the'+
                              '\n\nlid. You book it out of there. (You need a stronger'+
                              '\n\nweapon and ammmo for the weapon before coming here.'+
                              '\n\nPress enter to continue. ')
            else:
                if ARMOR3 in character_inventory3:
                    if WEAPON2 in character_inventory2 and AMMO2 in character_inventory3: 
                        if TALKED_TO_NICK not in quest_inventory:
                            if DEATH_CLAW not in quest_inventory:
                                quest_inventory.append(DEATH_CLAW)
                                input('SYSTEM: You go down the street from the Muesuem of Freedom'+
                                      '\n\nand you notice that something is growling while banging'+
                                      '\n\non a sewer lid. You get closer and some creature springs'+
                                      '\n\nout from the inside of the sewer: it towers over you at'+
                                      '\n\naround 10 feet tall, (you are 6 feet tall but due to being'+
                                      '\n\nin your power armor you are 7 feet tall) it\'s hands are'+
                                      '\n\nclaw-like, it has the horns of a bull (but 10 times bigger,'+
                                      '\n\nand they point forward and straight instead of wide and upward),'+
                                      '\n\nand it\'s skin appears to be very thick.'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('Creature: RAAAAAAAAGGGGGGGHHHHHHHH....RAAAAGGGHHHHH!!!!'+
                                  '\n\n(SYSTEM: Press enter to continue.)')
                                print()
                                print()
                                input('SYSTEM: The creature charges at you, but you manage to evade it.'+
                          '\n\nIt got it\'s horns stuck inside of a nearby rusted car, but he quickly'+
                          '\n\nrecovers. You manage to pull out one of your strongest weapons and start'+
                          '\n\nto shoot at it. This is obviously working as the creature is starting to'+
                          '\n\nweaken, but it doesn\'t stop him from relentlessly charging at you. This'+
                          '\n\nis because the bullets do not fully penetrate his thick skin. He grabs'+
                          '\n\nhold of you, picks you up while inside of your T-60 power armor, and slams'+
                          '\n\nyou into the ground while ramming his horns into the torso of your armor.'+
                          '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('You speaking aloud: You\'ll have to do better than that.'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('Power Armor Computer speaking (robotically): Reporting:'+
                                     '\n\nno damage taken, only mild scratches on the armor\'s'+
                                     '\n\ntorso. Power armor hull integrity: 100%. Proceed att-'+
                                     '\n\nentively and fully combat ready.'+
                                     '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('You replying confidently to Power Armor Computer: I always do. '+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('You confidently speaking aloud: Good thing I\'m wearing the latest model'+
                                     '\n\nof power armor. This T-60 was made to take on any explosives'+
                                     '\n\nand/or bullets coming from a fighter jet. Of course this cr-'+
                                     '\n\neature can\'t take me on.'+
                                     '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('Power Armor Computer speaking (robotically): Do not grow'+
                                      '\n\noverconfident. You will find yourself dead should you'+
                                      '\n\nremain smug.'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('You replying to Power Armor Computer: Shut up...'+
                                      '\n\n(SYSTEM: Press enter to continue. ')
                                print()
                                print()
                                input('SYSTEM: After pinning you down and ramming it\'s horns into your'+
                                  '\n\narmor\'s torso: the creature runs backwards preparing for it\'s'+
                                  '\n\nfinal charge, but it staggers and falls a few times because you'+
                                  '\n\nweakend it by shooting it with one of your stronger weapons earlier.'+
                                  '\n\nYou hurry to your feet and shower the creature with as many bullets'+
                                  '\n\nas you can, but again, none of the bullets fully penetrate him. As'+
                                  '\n\nit is about to reach you, you have to reload, but have no time to do so.'+
                                  '\n\nYou choose to not use the gun....'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('You speaking to Power Armor Computer: Computer,'+
                                      '\n\ninitiate Emergency Attack Mode.'+
                                      '\n\n(SYSTEM: Press enter to continue. ')
                                print()
                                print()
                                input('Power Armor Computer speaking (robotically): There'+
                                      '\n\nis no need to do so. This enemy only put mild'+
                                      '\n\nscratches on the armor. The hull integrity is at'+
                                      '\n\n100%. You are simply trying to show out and would'+
                                      '\n\nbe....'+
                                      '\n\n(SYSTEM: Press enter to continue. ')
                                print()
                                print()
                                input('You yelling at Power Armor Computer: I'+
                                      '\n\nSAID DO IT NOW!!!'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('Power Armor Computer speaking fast (robotically): Urgency Detected!'+
                                      '\n\nWarning! Emergency attack mode strains the power source of the'+
                                      '\n\npower armor (the fusion core) to increase your physical'+
                                      '\n\nattack energy output by 3,257% and your attack speed by'+
                                      '\n\n250% for 5 seconds. There is a 35%-40% chance that the'+
                                      '\n\npower armor will go dead upon activation this mode due to'+
                                      '\n\nstraining it\'s power source. If that happens...'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('Creature: RAGGHHHHHHHH... RAGGGHHHHH'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('You yelling at Power Armor Computer: NOW!!!'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('Power Armor Computer speaking even faster (robotically): Emergency'+
                                      '\n\nAttack Mode initiated... Emergency Attack Mode successfully act-'+
                                      '\n\nivated. Warning! Power source (fusion core) being strained!'+
                                      '\n\nWarning! Emergency Attack Mode will last only 5 seconds!'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('SYSTEM: As the creature is about to grab a hold of you, you dodge it\'s'+
                                  '\n\nclaw-like hands extremely fast: he was no match for you from the start,'+
                                  '\n\nbut with Emergency Attack Mode activated you are simply dominating the'+
                                  '\n\ncreature. You prepare to punch the creature as hard as you can.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('You screaming as you prepare a devestating punch: AAAAGGGGGHHHHH!!!!'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('SYSTEM: You punch a hole through the thick skin of the creature (in'+
                                  '\n\nthe chest area) that not even bullets from your strongest weapons'+
                                  '\n\ncould penetrate. You drive the creature not only to the ground,'+
                                  '\n\nbut somewhat through the ground: creating a mini-crater that\'s'+
                                  '\n\nabout 4 feet deep. It\'s as if Emergency Attack Mode strapped a'+
                                  '\n\nrocket to your arm to create such a devestating punch.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('You speaking to Power Armor Computer: Computer'+
                                  '\n\nscan the enemy and give me a battle report.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('Power Armor Computer speaking (robotically): Scanning'+
                                  '\n\nenemy..........Enemy\'s heart is missing. The enemy'+
                                  '\n\nhas passed. Battle report:..............Emergency'+
                                  '\n\nAttack Mode Deactivated. The 5 seconds are over.'+
                                  '\n\nPower source (fusion core) no longer being strained.'+
                                  '\n\nPower armor hull intergrity: 100% as last reported.'+
                                  '\n\nNo damage was taken to the torso of the armor: except'+
                                  '\n\nminor scratches. Scanning your vitals....Scan complete.'+
                                  '\n\nYou\'re condition: good.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('SYSTEM: After dominating the creature: you skin the creature by'+
                                      '\n\nbreaking off a sharp piece of steel off of a nearby rusted'+
                                      '\n\ncar and use it as a knife. You then store it\'s meat in your'+
                                      '\n\ninventory. You do this knowing that it might be good to sale:'+
                                      '\n\nif you can find a buyer.'+
                                      '\n\nPress enter to continue. ')
                            
                                DEATHCLAW_MEAT = 'Sewer Creature Meat'
                                if DEATHCLAW_MEAT not in character_inventory3:
                                    character_inventory3.append(DEATHCLAW_MEAT)

                            else:
                                input('SYSTEM: You have already defeated the'+
                                  '\n\ncreature that came out of the sewer. '+
                                  '\n\nPress enter to continue. ')

                        else:
                            if DEATH_CLAW not in quest_inventory:
                                quest_inventory.append(DEATH_CLAW)
                                input('SYSTEM: You go down the street from the Muesuem of Freedom'+
                                      '\n\nand you notice that something is growling while banging'+
                                      '\n\non a sewer lid. You get closer and a DeathClaw springs'+
                                      '\n\nout from the inside of the sewer: it towers over you at'+
                                      '\n\naround 10 feet tall, (you are 6 feet tall but due to being'+
                                      '\n\nin your power armor you are 7 feet tall) it\'s hands are'+
                                      '\n\nclaw-like, it has the horns of a bull (but 10 times bigger,'+
                                      '\n\nand they point forward and straight instead of wide and upward),'+
                                      '\n\nand it\'s skin appears to be very thick. The DeathClaw\'s'+
                                      '\n\nappearance fits the description Nick Valentine gave you in'+
                                      '\n\nback in Diamond City.'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('DeathClaw: RAAAAAAAAGGGGGGGHHHHHHHH....RAAAAGGGHHHHH!!!!'+
                                      '\n\n(SYSTEM: Press enter to continue.)')
                                print()
                                print()
                                input('SYSTEM: The DeathClaw charges at you, but you manage to evade it.'+
                          '\n\nIt got it\'s horns stuck inside of a nearby rusted car, but he quickly'+
                          '\n\nrecovers. You manage to pull out one of your strongest weapons and start'+
                          '\n\nto shoot at it. This is obviously working as the DeathClaw is starting to'+
                          '\n\nweaken, but it doesn\'t stop him from relentlessly charging at you. This'+
                          '\n\nis because the bullets do not fully penetrate his thick skin. He grabs'+
                          '\n\nhold of you, picks you up while inside of your T-60 power armor, and slams'+
                          '\n\nyou into the ground while ramming his horns into the torso of your armor.'+
                          '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('You speaking aloud: You\'ll have to do better than that.'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('Power Armor Computer speaking (robotically): Reporting:'+
                                      '\n\nno damage taken, only mild scratches on the armor\'s'+
                                      '\n\ntorso. Power armor hull integrity: 100%. Proceed att-'+
                                      '\n\nentively and fully combat ready.'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('You replying confidently to Power Armor Computer: I always do. '+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('You confidently speaking aloud: Good thing I\'m wearing the latest m-'+
                                      '\n\nodel of power armor. This T-60 was made to take on any explosives'+
                                      '\n\nand/or bullets coming from a fighter jet. Of course this cr-'+
                                      '\n\neature can\'t take me on.'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('Power Armor Computer speaking (robotically): Do not grow'+
                                      '\n\noverconfident. You will find yourself dead should you'+
                                      '\n\nremain smug.'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('You replying to Power Armor Computer: Shut up...'+
                                      '\n\n(SYSTEM: Press enter to continue. ')
                                print()
                                print()
                                input('SYSTEM: After pinning you down and ramming it\'s horns into your'+
                                      '\n\narmor\'s torso: the creature runs backwards preparing for it\'s'+
                                      '\n\nfinal charge, but it staggers and falls a few times because you'+
                                      '\n\nweakend it by shooting it with one of your stronger weapons earlier.'+
                                      '\n\nYou hurry to your feet and shower the creature with as many bullets'+
                                      '\n\nas you can, but again, none of the bullets fully penetrate him. As'+
                                      '\n\nit is about to reach you, you have to reload, but have no time to do so.'+
                                      '\n\nYou choose to not use the gun....'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('You speaking to Power Armor Computer: Computer,'+
                                      '\n\ninitiate Emergency Attack Mode.'+
                                      '\n\n(SYSTEM: Press enter to continue. ')
                                print()
                                print()
                                input('Power Armor Computer speaking (robotically): There'+
                                      '\n\nis no need to do so. This enemy only put mild'+
                                      '\n\nscratches on the armor. The hull integrity is at'+
                                      '\n\n100%. You are simply trying to show out and would'+
                                      '\n\nbe....'+
                                      '\n\n(SYSTEM: Press enter to continue. ')
                                print()
                                print()
                                input('You yelling at Power Armor Computer: I'+
                                      '\n\nSAID DO IT NOW!!!'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('Power Armor Computer speaking fast (robotically): Urgency Detected!'+
                                      '\n\nWarning! Emergency attack mode strains the power source of the'+
                                      '\n\npower armor (the fusion core) to increase your physical'+
                                      '\n\nattack energy output by 3,257% and your attack speed by'+
                                      '\n\n250% for 5 seconds. There is a 35%-40% chance that the'+
                                      '\n\npower armor will go dead upon activation this mode due to'+
                                      '\n\nstraining it\'s power source. If that happens...'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('DeathClaw: RAGGHHHHHHHH... RAGGGHHHHH'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('You yelling at Power Armor Computer: NOW!!!'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('Power Armor Computer speaking even faster (robotically): Emergency'+
                                      '\n\nAttack Mode initiated... Emergency Attack Mode successfully act-'+
                                      '\n\nivated. Warning! Power source (fusion core) being strained!'+
                                      '\n\nWarning! Emergency Attack Mode will last only 5 seconds!'+
                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('SYSTEM: As the DeathClaw is about to grab a hold of you, you dodge it\'s'+
                                  '\n\nclaw-like hands extremely fast: he was no match for you from the start,'+
                                  '\n\nbut with Emergency Attack Mode activated you are simply dominating the'+
                                  '\n\ncreature. You prepare to punch the creature as hard as you can.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('You screaming as you prepare a devestating punch: AAAAGGGGGHHHHH!!!!'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('SYSTEM: You punch a hole through the thick skin of the DeathClaw (in'+
                                  '\n\nthe chest area) that not even bullets from your strongest weapons'+
                                  '\n\ncould penetrate. You drive the DeathClaw not only to the ground,'+
                                  '\n\nbut somewhat through the ground: creating a mini-crater that\'s'+
                                  '\n\nabout 4 feet deep. It\'s as if Emergency Attack Mode strapped a'+
                                  '\n\nrocket to your arm to create such a devestating punch.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('You speaking to Power Armor Computer: Computer'+
                                  '\n\nscan the enemy and give me a battle report.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('Power Armor Computer speaking (robotically): Scanning'+
                                  '\n\nenemy..........Enemy\'s heart is missing. The enemy'+
                                  '\n\nhas passed. Battle report:..............Emergency'+
                                  '\n\nAttack Mode Deactivated. The 5 seconds are over.'+
                                  '\n\nPower source (fusion core) no longer being strained.'+
                                  '\n\nPower armor hull intergrity: 100% as last reported.'+
                                  '\n\nNo damage was taken to the torso of the armor: except'+
                                  '\n\nminor scratches. Scanning your vitals....Scan complete.'+
                                  '\n\nYou\'re condition: good.'+
                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                print()
                                print()
                                input('SYSTEM: After dominating the DeathClaw: you skin the DeathClaw by'+
                                      '\n\nbreaking off a sharp piece of steel off of a nearby rusted'+
                                      '\n\ncar and use it as a knife. You then store it\'s meat in your'+
                                      '\n\ninventory. You do this knowing that it might be good to sale:'+
                                      '\n\nif you can find a buyer.'+
                                      '\n\nPress enter to continue. ')
                            
                                if DEATHCLAW_MEAT not in character_inventory3:
                                    character_inventory3.append(DEATHCLAW_MEAT)

                            else:
                                input('SYSTEM: You have already defeated the'+
                                  '\n\nDeathClaw that came out of the sewer. '+
                                  '\n\nPress enter to continue. ')

                    else:
                        if TALKED_TO_NICK in quest_inventory:
                            input('SYSTEM: You go down the street from the Muesuem of Freedom'+
                              '\n\nand you notice that something is growling while banging'+
                              '\n\non a sewer lid. You look intensely and notice that it is'+
                              '\n\na DeathClaw staring intently at you through the lid. You'+
                              '\n\nbook it out of there. (You need a stronger weapon and ammo'+
                              '\n\nfor the weapon before coming here.'+
                              '\n\nPress enter to continue. ')
                        else:
                            input('SYSTEM: You go down the street from the Muesuem of Freedom'+
                              '\n\nand you notice that something is growling while banging'+
                              '\n\non a sewer lid. You look intensely and notice that it is'+
                              '\n\na strange creature staring intently at you through the'+
                              '\n\nlid. You book it out of there. (You need a stronger'+
                              '\n\nweapon and ammo for the weapon before coming here.)'+
                              '\n\nPress enter to continue. ')


                else:
                    input('SYSTEM: You go down the street from the Muesuem of Freedom'+
                      '\n\nand you notice that something is growling while banging'+
                      '\n\non a sewer lid. You look intensely and notice that it is'+
                      '\n\nsome huge creature staring intently at you. You book it'+
                      '\n\nout of there. (You need stronger armor before coming'+
                      '\n\nhere.) Press enter to continue. ')

def diamond_city(character_inventory, character_inventory2,
                 character_inventory3, character_inventory4,
                 quest_inventory, think_inventory,
                 prevent_exploit, prevent_exploit2,
                 prevent_exploit3):
    global MONEY
    global CASH1
    global CASH2
    global SNIPER_VALUE
    global MINIGUN_VALUE
    global FIRSTAIDKIT3_VALUE
    global FUSION_CORE2_VALUE
    global RING1_VALUE
    global RING2_VALUE
    global DEATH_CLAW_MEAT
    global DEATHCLAW_MEAT
    global MAFIA_MONEY_VALUE
    global BOUNTY_POSTER_VALUE
    if ARMOR2 or ARMOR3 in character_inventory3:
        if WEAPON2 in character_inventory2:
            if AMMO2 in character_inventory3:
                if BOTTLED_WATER in character_inventory:
                    if FOOD1 in character_inventory2:
                        if DIAMOND_CITY_TRAVEL not in quest_inventory:
                            quest_inventory.append(DIAMOND_CITY_TRAVEL)
                            input('SYSTEM: Having all that you need, you set out to find'+
                                  '\n\nDiamond City. It takes you 4 days to find it. Over'+
                                  '\n\nthe course of those 4 days: you sparingly drink your'+
                                  '\n\nwater and eat your canned beans. Fortunately, you ran'+
                                  '\n\ninto a friendly stranger that pointed you in the right'+
                                  '\n\ndirection to Diamond City on the early morning of the'+
                                  '\n\nthird day. He even told you, "Please be-uh careful frien\'.'+
                                  '\n\nDhere is so much sufferin\' and wrong-doin\' in dis here-uh'+
                                  '\n\npost-apocalyptic world. But Imma sure you-uh gon\' be ok'+
                                  '\n\nwearin\' dat suit dhere made of steel and toting dat dhere'+
                                  '\n\n\'ssualt rifle. HAHAHA!! Anyway-uh, I gotta get back to'+
                                  '\n\nfarmin\' my fall veggies. Again, you-uh be safe!" You made'+
                                  '\n\nit to Diamond City in the later part of the morning on the'+
                                  '\n\nfourth day.'+
                                  '\n\nPress enter to continue. ')
                            print()
                            print()
                            input('SYSTEM: But before entering Diamond City you notice that the'+
                                  '\n\ncity is actually just the old CommonWealth baseball stadium'+
                                  '\n\nthat you and your wife Nora used to go to 210+ years ago'+
                                  '\n\nto watch your favorite professional baseball team: the'+
                                  '\n\nCommonWealth Blue Sox. You note that these people born into'+
                                  '\n\nthis post-apocalyptic world must be using the stadium walls'+
                                  '\n\nas a way to keep unwanted guest out of the inside of the'+
                                  '\n\nstadium, or the "city".'+
                                  '\n\nPress enter to continue. ')
                            print()
                            print()
                            input('SYSTEM: You also hear gunfire and people shouting to, "SHOOT BACK!"'+
                                  '\n\nand "TAKE COVER!" You see men in blue uniforms with heavy kevlar'+
                                  '\n\narmor and shotguns shooting at something. That something appears'+
                                  '\n\nto be green men that are about 8 feet tall with extremely large'+
                                  '\n\nmuscles and they are armed with hunting rifles. They seem to be'+
                                  '\n\non the less intelligent side as they yell out, "COME AND PLAY LIL\''+
                                  '\n\nSTUPID HU- HUMANS!", "ALL HUMANS DIE!!", "STOP HIDING BEHIND WALL!",'+
                                  '\n\n"I GET YOU SOON!" You don\'t know what exactly is going on but you'+
                                  '\n\nrush torward the scene...'+
                                  '\n\nPress enter to continue. ')
                            print()
                            print()
                            input('SYSTEM: As you pull up at the scene, you notice that the men in blue'+
                                  '\n\nuniforms are the security guards of Diamond City. They yell at you'+
                                  '\n\n"WHAT DO YOU THINK YOU\'RE DOING STRANGER! YOU\'RE GONNA---..." But'+
                                  '\n\nthey quickly go silent as they realize you are wearing T-45 power'+
                                  '\n\narmor and start to shoot at the green men with your assualt rifle.'+
                                  '\n\nYou rid of all of the green men that were attacking the Diamond City'+
                                  '\n\nsecurity team. The green men tried shooting their hunting rifles at'+
                                  '\n\nyou while inside of your T-45 Power Armor. But all of their ammunition'+
                                  '\n\njust bounced right off. The Diamond City security team bombard you with'+
                                  '\n\nquestions after your amazing display, "Where did you get that power'+
                                  '\n\narmor?", "How do you even know how to use power armor? Most people'+
                                  '\n\ntoday can\'t use it: only people in the pre-apocalyptic world that'+
                                  '\n\nwere assigned it in the military knew how to use it.", "Where did you'+
                                  '\n\nget an assualt rifle mate?", "How did you even power up that armor?'+
                                  '\n\nPower Armor suit\'s need fusion cores, we haven\'t seen you around'+
                                  '\n\nhere before so you definitely didn\'t buy a fusion core from the'+
                                  '\n\nDiamond City merchant.", "Where are you from?" You answered all of'+
                                  '\n\ntheir questions. In fact you gave them your whole story. But you tell'+
                                  '\n\nthem that they musn\'t tell anyone else or their heads are yours. You'+
                                  '\n\ndon\'t want too much attention being drawn to you as you search for the'+
                                  '\n\nman that killed your wife and kidnapped your infant son.'+
                                  '\n\nYou finally make it inside of Diamond City.'+
                                  '\n\nPress enter to continue. ')
                            print()
                            print()
                            if THINK_SELF15 not in think_inventory:
                                think_inventory.append(THINK_SELF15)
                                input('Thinking to self: Wow. So this is Diamond City?'+
                                      '\n\nThese people have actually turned a baseball'+
                                      '\n\nstadium into a mini city. It\'s not so diff-'+
                                      '\n\nerent from the world I once knew. I see some'+
                                      '\n\npeople are sleeping on dirty mattresses outside'+
                                      '\n\non the ground, while others live in small sh-'+
                                      '\n\nacks, and then others are living up further up'+
                                      '\n\nin the stands in bigger shacks. And I\'ll take'+
                                      '\n\na wild guess and assume that those that control'+
                                      '\n\nthe political system of this city are living way'+
                                      '\n\nup there in the enclosed, and spacious staff and'+
                                      '\n\nVIP rooms of this stadium. I see businesses to the'+
                                      '\n\nleft and right of me, and people everywhere just'+
                                      '\n\ntrying to get by in their everyday life. It\'s like'+
                                      '\n\nI\'m in a bootleg New York City-- a place that I\'m'+
                                      '\n\nsure doesn\'t even exist anymore. So much has ch-'+
                                      '\n\nanged in this world, yet so much is still the'+
                                      '\n\nsame. This is a post-apocalyptic world and I\'ve'+
                                      '\n\njust stumbled across a lower class, a middle class,'+
                                      '\n\nand an upper class system.'+
                                      '\n\nPress enter to continue. ')
                                print()
                                print()
                                input('Further thinking to self: I\'m not sure how I feel about'+
                                      '\n\nall of this. This world is clearly worse than before,'+
                                      '\n\nbut the before was already terrible. There just seems'+
                                      '\n\nto be no hope at all. We as humans are constantly fi-'+
                                      '\n\nghting and the result is always the same. But the fi-'+
                                      '\n\nghting 210+ years ago was the final straw. That nuclear'+
                                      '\n\nwar ended in every single country dropping nuclear bombs'+
                                      '\n\nand shooting nuclear missles at one another. The result'+
                                      '\n\nof that fighting has been before my very eyes since I was'+
                                      '\n\nmysteriously released from Vault 111.....and I\'ve seen'+
                                      '\n\nenough of this result already....I hate all of this....'+
                                      '\n\nPress enter to continue. ')
                                print()

                        choice2 = 0
                        NICK_VALENTINES_OFFICE = 1 
                        MERCHANT = 2
                        MAFIA_BOSS = 3
                        BOUNTY_POSTER = 4
                        QUIT2 = 5
                        while choice2 != QUIT2:
                            print()
                            print('Inside of Diamond City\'s Walls')
                            print('-------------------------------')
                            print()
                            print('1. Nick Valentine\'s Detective Agency'+
                                  '\n2. Diamond City Merchant'+
                                  '\n3. ?'+
                                  '\n4. Bounty poster'+
                                  '\n5. Go back to map (The CommonWealth)')
                            print()
                            choice2 = int(input('Enter your choice: '))
                            print()
                            while choice2 < NICK_VALENTINES_OFFICE or choice2 > QUIT2:
                                choice2 = int(input('Enter a valid choice: '))
                                print()
                            if choice2 == NICK_VALENTINES_OFFICE:
                                if TALKED_TO_NICK not in quest_inventory:
                                    if READ_ABOUT_NICK in quest_inventory:
                                        input('SYSTEM: You walk into Nick Valentine\'s Detective Agency'+
                                              '\n\nwanting to get a lead on who kidnapped your infant son'+
                                              '\n\nand gunned down your wife in Vault 111. But you exit'+
                                              '\n\nyour power armor before going in. Upon entering you'+
                                              '\n\nplace your weapons in a large bin that says, "Place'+
                                              '\n\nweapons here,and make sure they\'re unloaded and off."'+
                                              '\n\nApparently you are allowed to open carry in Diamond'+
                                              '\n\nCity: you got lucky. You noticed the big letters on the'+
                                              '\n\nfront of the building as you walked in, they read:'+
                                              '\n\n"Nick Valentine\'s Detective Agency". You also noticed'+
                                              '\n\nthat these letters have neon: they must light up at'+
                                              '\n\nnight, as do many other businesses in Diamond City.'+
                                              '\n\nPress enter to continue. ')
                                        print()
                                        print()
                                        if THINK_SELF16 not in think_inventory:
                                            think_inventory.append(THINK_SELF16)
                                            input('Thinking to self: Well, I\'m here. I remember reading'+
                                                  '\n\nsome ex- Diamond City resident\'s computer entry in'+
                                                  '\n\nSanctuary Hills about this place. He talked about'+
                                                  '\n\nhow he found Nick Valentine creepy because he is a'+
                                                  '\n\nsynth. He said that synths aren\'t people? What in'+
                                                  '\n\nworld is a synth? He also typed about the "broken mask'+
                                                  '\n\nincident" that happened in Diamond City 10 years ago'+
                                                  '\n\nin 2277 apparently. What happened exactly? Hopefully'+
                                                  '\n\nNick can explain more about this post-apocalyptic world'+
                                                  '\n\nto me, because I\'m so lost.'+
                                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                            print()
                                            print()
                                        input('Handsome young man: *appears very surprised*'+
                                              '\n\nWhy, Hello. How may I help you sir?'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Yes, I am looking for a, Nick Valentine?'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Handsome young man: *appears very surprised with raised eyebrows*'+
                                              '\n\nWell, I\'m assuming you must have a case that needs solving if'+
                                              '\n\nyou\'re walking in here. But I must admit that I am very sur-'+
                                              '\n\nprised.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: *looking on dumbfoundedly* Please, come again?'+
                                              '\n\nWhat is there to be surprised about exactly?'+
                                              '\n\nPress enter to continue.')
                                        print()
                                        print()
                                        input('Handsome young man: *chuckles with hand over mouth and closed eyes*'+
                                              '\n\nHmmmmmm. You must be new to this city? *runs right hand through'+
                                              '\n\nhis medium brush up haircut*'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Ok what\'s really going on? Is this place even a legitimate'+
                                              '\n\nbusiness? I have the feeling your\'re about to try and do'+
                                              '\n\nsomething to me....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Handsome young man: Don\'t be alarmed friend; I\'ll help anyone'+
                                              '\n\nthat needs it. It\'s just that I have not had a person walk in'+
                                              '\n\nhere in over 10 years since I announced to the city that I am'+
                                              '\n\na synth. I did it right after the broken mask incident; I felt'+
                                              '\n\nit was better if people knew what I truly am rather than living'+
                                              '\n\na lie day in and out.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Ok....Hold on...*grabs head with both hands confused*'+
                                              '\n\nI have three questions and probably a lot more to come.'+
                                              '\n\n1. You must be telling me that YOU are Nick Valentine'+
                                              '\n\n2. What is a synth? 3. I have read a computer entry in'+
                                              '\n\nSanctuary Hills that mentioned this "broken mask'+
                                              '\n\nincident" Please explain, I am so confused...*sighs*'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Friend, I will have to be quick about all of'+
                                              '\n\nthis as I want to prioritize your case more so than your'+
                                              '\n\ncuriosity. Yes, I am Nick Valentine and I am a synth'+
                                              '\n\ncreated by the Institute. The Institute is a scientific'+
                                              '\n\norganization that are like ghost. Most of anything people'+
                                              '\n\nknow about them is that they create us synths, people who'+
                                              '\n\nappear to be human, everything about us is human. Except'+
                                              '\n\nthat we have a synth component, or, a computer chip in'+
                                              '\n\nour brains. We are manufactured by the Insititute. The'+
                                              '\n\nInstitute is extremely advanced in science. They have'+
                                              '\n\nmanaged to recreate the human body with beyond high tech'+
                                              '\n\nmachinery.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                              
                                        input('Nick Valentine: They send us synths to kill someone and basically'+
                                              '\n\nsteal their identity, and we are supposed to give reports to'+
                                              '\n\nInstitute scientist when they visit us so they can see how'+
                                              '\n\nwell the results of their experiments are going. Often their'+
                                              '\n\nexperiments succeed. So often, in fact, that most people in this'+
                                              '\n\ncity, in the CommonWealth period, are distrusting of each other.'+
                                              '\n\nNo one knows who might get replaced by a synth in the middle of'+
                                              '\n\nthe night. So there is a lot of paranoia and for good reason.'+
                                              '\n\nAnd we can easily kill a human, as our bodies are far superior.'+
                                              '\n\nTo help us rid of the person\'s body, the scientist take it'+
                                              '\n\nand teleport with it to the Institute and dispose of it somehow:'+
                                              '\n\nI\'m not sure. And yes you heard me right: they all can teleport'+
                                              '\n\nthanks to some teleporting machine they created.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        
                                        input('Nick Valentine: I have never killed anyone myself. I was a prototype'+
                                              '\n\nsynth, the Institute just dumped me outside of Diamond City one'+
                                              '\n\nday deciding that I was a failed experiment. They made sure to'+
                                              '\n\nerase most of my memories. So I can\'t say where they are or expose'+
                                              '\n\neverything that they do. You\'d think they\'d kill me knowing as much'+
                                              '\n\nas I do. Yes, my body is far superior to a humans, so you\'d ask,'+
                                              '\n\n"how can they kill me?". Well those Institute scientist have these'+
                                              '\n\nsynths called coursers that follow their every command. Basically'+
                                              '\n\ncoursers are synths in the Institute that have underwent intensive'+
                                              '\n\ncombat training and had their bodies enhanced with technology. So they'+
                                              '\n\nare FAR stronger than a regular synth: and a regular synth is already FAR'+
                                              '\n\nstronger than a human, so you think hard about that. They can teleport'+
                                              '\n\njust like the scientist too. They are the "ultimate fighting machines"'+
                                              '\n\nas I recall the Institute scientist saying.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: *Nick stares at you.* I don\'t even know what to'+
                                              '\n\nsay. Sorry if I seem rude.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Well I\'m not done, so don\'t say anything'+
                                              '\n\nmore just yet. The broken mask incident happened ten'+
                                              '\n\nyears ago in Diamond City. It was when the Institute'+
                                              '\n\naccidentally revealed to the CommonWealth that they'+
                                              '\n\nexist. They had one of their first synths try to blend'+
                                              '\n\nin with humans, but he malfunctioned one night drinking'+
                                              '\n\nat a bar. He whipped out a gun and started blasting every'+
                                              '\n\nnperson in sight. His name was Micheal. All humans thought'+
                                              '\n\nhe was the same funny Micheal that used to crack jokes at'+
                                              '\n\nthe bar on a Friday night after work. But that Micheal was'+
                                              '\n\nabducted and killed by the Institute. That started all of'+
                                              '\n\nthis synth and Institute paranoia, but it\'s understandable.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Come friend, I have given you the information'+
                                              '\n\nyou have sought, now let\'s hear about your case. Come'+
                                              '\n\nand sit down with me in my office.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('SYSTEM: You follow Nick to his office and he sits you in a'+
                                              '\n\ncustomer\'s chair while he sits in his chair on the'+
                                              '\n\nother side of his office desk.'+
                                              '\n\nPress enter to continue. ')
                                        print()
                                        print()
                                        input('Nick: Sorry, I never got your name.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: It\'s Nate. Nate McPherson. I\'d like to apologize'+
                                              '\n\nas well. The reason I was so surprised that you were'+
                                              '\n\nNick Valentine is that fact that you look so young'+
                                              '\n\nand handsome for a detective. I imagine detectives'+
                                              '\n\nto be old guys with saggy eye bags because they never'+
                                              '\n\nget any sleep.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: HAHAHA, HAHAHA. Ok...Oh my goodness, sorry.'+
                                              '\n\nMan you really are clueless. I suppose I am young. I\'m'+
                                              '\n\nonly 10 years old, but with the appearnace of a handsome'+
                                              '\n\nyoung man. But I stole this man\'s identity, like I told'+
                                              '\n\nyou earlier: I didn\'t kill him, but the Institute did'+
                                              '\n\nrecreate this man: and I\'m that recreation. They must'+
                                              '\n\nhave killed him themselves. I took his name and everything.'+
                                              '\n\nApparently he was an exceptional detective for him to only'+
                                              '\n\nbe 23 years old. But his age is something I can\'t steal,'+
                                              '\n\nhe\'d be 33 right now if he weren\'t dead: while I\'m 10.'+
                                              '\n\nI\'m only an exceptional detective because of him. But it'+
                                              '\n\ndoesn\'t matter because everyone is so afraid of synths that'+
                                              '\n\nthey never come to do business with me. I did tell you earlier'+
                                              '\n\nthat no one has been in here for 10 years. Basically ever since'+
                                              '\n\nI told everyone I was synth: which I did when I was 10 months'+
                                              '\n\nold, it was shortly after the broken mask incident. That\'s why'+
                                              '\n\nI was so surprised when you came in. And before you ask: no.'+
                                              '\n\nI was never a child, all synths are created with adult bodies'+
                                              '\n\nand intellect, but again, both are superior to a normal humans.'+
                                              '\n\nSo I was but a few hours old when I started doing all of this.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Ok, but you\'d think you would at least age huh?'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: No, we synths do not age. You\'d think those'+
                                              '\n\n"oh so smart" Institute scientist would see that as a'+
                                              '\n\nflaw. We replace people\'s entire being, so surely their'+
                                              '\n\nloved ones would notice that we are not aging while they'+
                                              '\n\nare. That only blows our cover. But again, there is a lot'+
                                              '\n\nI don\'t remember, I\'m sure they counter it somehow. The'+
                                              '\n\nInstitute probably replaces the synth with one that looks'+
                                              '\n\nolder, and they might do this as many times as it takes'+
                                              '\n\nto make it appear that the synth is aging to all humans.'+
                                              '\n\nWe also don\'t need food, water, or sleep. We can enjoy'+
                                              '\n\nthem. But they are not required for us to function.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Ok, all of this is crazy. I don\'t want to believe'+
                                              '\n\nany of this but I guess I have seen some pretty weird'+
                                              '\n\nthings already.....'+
                                               '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: *staring intensely and speaking very serious*'+
                                              '\n\nNow\'s it\'s my turn to ask questions. Before we discuss'+
                                              '\n\nyour case, I have to know....Why do you act as if you were'+
                                              '\n\nborn yesterday? You act like this world is completely new'+
                                              '\n\nto you....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: *staring back at Nick and speaking very serious*'+
                                              '\n\nI\'ll give you my story then. Unlucky for you, my'+
                                              '\n\nentire life from the year 2077 to this year, 2287,'+
                                              '\n\nis the case. '+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: *very surprised* You\'re telling me your'+
                                              '\n\n210+ years old? You were born AND raised before this'+
                                              '\n\nworld had that worldwide nuclear war? How have you'+
                                              '\n\nlived so long? Only us synths are immortal: unless'+
                                              '\n\nwe are killed somehow....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: *speaking fast* But hold those thoughts for a'+
                                              '\n\nmoment, let me get my pen and notepad out to take notes.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('SYSTEM: *Nick Prepares his notepad*'+
                                              '\n\nPress enter to continue. ')
                                        print()
                                        print()
                                        input('Nick: Ok, open up the dam\'s gates my friend. '+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                                  
                                        input('You: I served in the U.S. military. It went out of commission the'+
                                              '\n\nday the nukes exploded worldwide as I\'m sure you know. That'+
                                              '\n\nday my family and I had coincidentally just signed up for a'+
                                              '\n\nprogram called Vault-Tec. The world was at war, world war 3.'+
                                              '\n\nBut a worldwide nuclear war was feared by everyone, because'+
                                              '\n\neveryday world leaders threatend one another. So this Vault-Tec'+
                                              '\n\ntook advantage of this and started up their company that offered'+
                                              '\n\npeople a safe place inside of a vault in the case that the nuclear'+
                                              '\n\nwar started. Everyone who signed up for the vaults had to pay a'+
                                              '\n\nmembership, but it was really my wife who convinced me to do it:'+
                                              '\n\nI hate salesmen with a passion. I hate their job not the person,'+
                                              '\n\njust to make that clear. Anyways, October 23, 2077: it was reported'+
                                              '\n\nthat nukes were going off worldwide. Everyone who signed up for the'+
                                              '\n\nvault rushed to it for dear life: my family included. I had my wife,'+
                                              '\n\nNora, running beside me, and she had our son, Shaun, in arms. The'+
                                              '\n\nsirens were so scary. *Tears slowly fall down your eyes as you wipe'+
                                              '\n\nthem*.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Now, now. One step at a time. It\'s ok.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: The people who didn\'t sign up for the vaults...Nick!'+
                                              '\n\n*Burst out crying* You should have heard their screams'+
                                              '\n\nand cries! Entire families killed because of evil men!'+
                                              '\n\nLittle children: KILLED! Lovers: KILLED! People living'+
                                              '\n\nhonest lives: KILLED! FOR WHAT?!? BECAUSE HUMANS NEVER'+
                                              '\n\nLEARN! WHAT IS OUR PROBLEM NICK!??! WHY DOES THIS ALWAYS'+
                                              '\n\nHAPPEN?!?!'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: *sincerely speaking* Please, try to'+
                                              '\n\ntake deeps breaths, you\'re getting a bit off'+
                                              '\n\ntopic. I know this hits close to home, but,'+
                                              '\n\nplease focus my friend...'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: *slowly but surely calmed down* When we entered the'+
                                              '\n\nvaults everything was seemingly fine. Vault-Tec told'+
                                              '\n\nus that to proceed deeper into the vault we would have'+
                                              '\n\nto be decontaminated in cryogenic pods. Everyone was in'+
                                              '\n\na state of dissassociation. No one could believe nor'+
                                              '\n\naccept that the fact that the entire world had just went'+
                                              '\n\nup in smoke and billions of people with it. I kissed my'+
                                              '\n\ninfant son, Shaun, on the forehead and told him I loved'+
                                              '\n\nhim. I proceeded to do the same thing to my wife, but she'+
                                              '\n\nbeat me to it. We were put in the cryogenic pods and'+
                                              '\n\nmy wife\'s pod was directly across from mine. Before we'+
                                              '\n\nwere "decontaminated" my wife and I waved at each other'+
                                              '\n\nthrough the glass of the cryogenic pods. She had my infant'+
                                              '\n\nson, Shaun, with her. Nick. Vault-Tec had lied. We didn\'t'+
                                              '\n\nwake up in a few minutes. We woke up just recently. Hundreds'+
                                              '\n\nof years later! Vault Tec were just mad scientist doing ex-'+
                                              '\n\nperiemts on us! And apparently after they experimented on us'+
                                              '\n\nthey just lived out the rest of their days in that vault and died:'+
                                              '\n\nleaving us in those cryogenic pods! I don\'t know what the year'+
                                              '\n\nwas, but my wife was gunned down in front of me by two guys'+
                                              '\n\nin what seemed like biohazard suits, and a man in an all black'+
                                              '\n\nleather trench coat with a huge white gun. The details are'+
                                              '\n\nhazy, but...'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print('You: The guy in the black leather trench coat told my wife to let'+
                                              '\n\ngo of my son. She refused naturally. And the man told her that,'+
                                              '\n\n"I\'m only going to tell you once, let go of the child or die."'+
                                              '\n\nMy wife basically told him to go do himself in and he shot her.'+
                                              '\n\n*trying to fight your emotions* The people wearing biohazard'+
                                              '\n\nsuits took my son and the man in the black leather trench coat'+
                                              '\n\nsaid, "At least we still have the backup.", as he looked at me.'+
                                              '\n\nI was refrozen by them after all of that happened.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: *looks very anxious* Noooooo, my friend, nooo.'+
                                              '\n\nOk. I have a very bad feeling. But I\'m going to assume'+
                                              '\n\nthat feeling is not true and try to be logical and look'+
                                              '\n\nat all of our options before I jump to any conclusions.'+
                                              '\n\nI will rule out some things though. I know supermutants'+
                                              '\n\ndidn\'t do this because they are dumb as rocks and you did'+
                                              '\n\nsay that people did this, not 8 foot tall green, muscular'+
                                              '\n\nmen....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Wait, a minute! I saw those when I came to the city!'+
                                              '\n\nI helped defend the Diamond City security team! I was'+
                                              '\n\nwondering what those things were....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Ok, I will explain something on a side note here, because'+
                                              '\n\nyou get off topic very easily. To prevent this from happening again'+
                                              '\n\nI will explain some things about the world you are currently in since'+
                                              '\n\nit\'s basically new to you. Supermutants come from the Institute.'+
                                              '\n\nThey were once humans themselves, but the institute kidnapped them and'+
                                              '\n\nattempted to make "super humans". This was before their synth research.'+
                                              '\n\nThere are also these things called DeathClaws. They often are under'+
                                              '\n\nsewers. They have claw-like hands, are about 10 feet tall, and have horns'+
                                              '\n\non their heads that point forward and straight instead of wide and upward'+
                                              '\n\nlike you would see on a bull. These creatures also were created by the'+
                                              '\n\nInstitute. What were they trying to do? I don\'t know. They do anything'+
                                              '\n\nin the name of science and care not for the repercussions of their'+
                                              '\n\nreckless experiments....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: I also know that raiders did not do this as they'+
                                              '\n\nonly care about robbing people of their valuables: whether'+
                                              '\n\nthey have to kill the person for them or not. The last thing'+
                                              '\n\nthey would want is to kill your wife to get an infant child.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        if DEATH_CLAW in quest_inventory:
                                            input('You: Yeah I definitely have ran into a DeathClaw...'+
                                                  '\n\nkilled it too...it was back in Concord....'+
                                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                                  
                                            print()
                                            print()
                                            input('Nick Valentine: What?!?! You....a human.... killed a'+
                                                  '\n\nDeathClaw? Nevermind that....your case please...'+
                                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                            print()
                                            print()
                                        if DEATHCLAW_MEAT in character_inventory3:
                                            character_inventory3.remove(DEATHCLAW_MEAT)
                                            DEATHCLAW_MEAT = 'DeathClaw Meat'
                                            character_inventory3.append(DEATHCLAW_MEAT)

                                        input('You: I\'ve definitely ran into those raiders you\'re'+
                                              '\n\ntalking about. I had a shootout with them at the'+
                                              '\n\nMuesuem of Freedom. Got hit in the left shoulder.'+
                                              '\n\nI took care of them though.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Well Nate. I also know it that it wasn\'t'+
                                              '\n\nthe Diamond City Mafia. Those goons only care about'+
                                              '\n\nhow much money they can make. They\'re not getting'+
                                              '\n\nany money out of a crying infant and it\'s dead'+
                                              '\n\nmother. So I apologize. What I was denying earlier'+
                                              '\n\nis true.....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('SYSTEM: *room goes silent* *Nick stares down'+
                                              '\n\nat the floor in disbelief*'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Nick! What the heck?!?! What\'s so bad?'+
                                              '\n\nTell me something...'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: *staring at the floor and speaking very seriously*'+
                                              '\n\nI wish that I could tell you I\'d be at the bottom of this'+
                                              '\n\ncase by this weekend.....But Nate.....oh Nate... *facepalms*'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Nick! Stop and tell me! You\'re killing me!'+
                                              '\n\nOh my goodness! Is it something about those'+
                                              '\n\nguys in the vault?'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: The Institute killed your wife and'+
                                              '\n\ntook your child Nate...'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('SYSTEM: There is an eerie silence and a lot of staring at'+
                                              '\n\nthe floor by both You and Nick for about 5 minutes.'+
                                              '\n\nPress enter to continue. ')
                                        print()
                                        print()
                                        input('You: Nick this can\'t be true: I mean....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick: Stop! This is the truth. I knew it as soon as'+
                                              '\n\nyou mentioned what the people were wearing....the'+
                                              '\n\npeople that killed your wife and took your infant'+
                                              '\n\nson. But I didn\'t want it to be true.*sigh* Those'+
                                              '\n\ntwo people wearing biosuits were definitely Institute'+
                                              '\n\nscientist that needed your son for some type of ex-'+
                                              '\n\nperiment. The man in the black trench coat, "with a'+
                                              '\n\nbig white gun" as you said: was definitely an Institute'+
                                              '\n\ncourser. The gun your wife was killed with was a gun'+
                                              '\n\nthat shoots blue laser beams. Institute Coursers are'+
                                              '\n\ntrained to use these deadly weapons. Though I haven\'t'+
                                              '\n\nseen those weapons in action. So, I\'m not sure how strong'+
                                              '\n\nthose laser beams are, but they\'d definitely rip right'+
                                              '\n\nthrough a human and literally melt their flesh and'+
                                              '\n\ninternal organs upon contact. May I ask, did you look'+
                                              '\n\nat your wife\'s body after you woke up and got out of your'+
                                              '\n\ncryogenic pod?'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Yes, and I passed out. I\'m not sure for how long. But'+
                                              '\n\nI had to be sure....you know? I was in such strong'+
                                              '\n\ndenial that she was gone. Then I just blanked out.'+
                                              '\n\nAnd before you ask...I don\'t know how I got out'+
                                              '\n\nof my pod. It just seemingly stopped the icing'+
                                              '\n\nprocess or malfunctioned or something and I was'+
                                              '\n\nable to get out.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Ok, maybe we don\'t have to worry'+
                                              '\n\nabout how you got out. That\'s not the problem'+
                                              '\n\nat hand. Can you tell me what that Institute'+
                                              '\n\ncourser sounded like? What hairstyle he had?'+
                                              '\n\nMaybe some facial features? I may know his'+
                                              '\n\nname and his whereabouts. It\'s defintely a'+
                                              '\n\nsuicide mission to go after him, but as hard'+
                                              '\n\nas it can be: I\'ll to give you all the inf-'+
                                              '\n\normation that I can. But he might be one of'+
                                              '\n\nthose coursers that only work inside of the'+
                                              '\n\nInstitute and not among us.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: His voice was deep and rough: like sandpaper'+
                                              '\n\ngoing across your face. He had a buzzcut. And'+
                                              '\n\nhe had a huge scar going across his entire face.'+
                                              '\n\nFor you to call coursers so tough, somebody'+
                                              '\n\ndefinitely did him in with a knife to the face'+
                                              '\n\nin the past.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: No! Please don\'t ever do that'+
                                              '\n\nagain! Do not underestimate coursers! The only'+
                                              '\n\nthing that could have cut his face like that'+
                                              '\n\nwas another synth that was trying out to become'+
                                              '\n\na courser that I\'m sure he fought during his'+
                                              '\n\nintense training. Synths have to kill each other'+
                                              '\n\nunder that intense training to become coursers.'+
                                              '\n\nOf course the last man standing is the one who'+
                                              '\n\nbecomes the Institute\'s newest courser. So the'+
                                              '\n\ncourser you just insulted killed ten if not hundreds'+
                                              '\n\nof others abnormally strong synths to get his position.'+
                                              '\n\nThat\'s how strong he is. He was the last one standing.'+
                                              '\n\nAnd I know exactly which courser it is and where he is'+
                                              '\n\ncurrently.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: *eyes grow wide with fear*'+
                                              '\n\nSo he is one of the most experienced and'+
                                              '\n\nbattle hardend coursers the Institute has?'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Don\'t grow scared now! You talked'+
                                              '\n\nabout him like he was just some punk a second'+
                                              '\n\nago. And yes he is the most experienced courser'+
                                              '\n\nthat he institute has. Remember how I told you'+
                                              '\n\nwe synths are FAR stronger than you humans?'+
                                              '\n\nWell also remember that I told you that coursers'+
                                              '\n\nare synths that are FAR stronger than regular'+
                                              '\n\nsynths like myself. And this courser I\'m talking'+
                                              '\n\nabout: Kellog, is hands down the strongest courser'+
                                              '\n\nthe Institute has. Not to be rude: but you\'re just'+
                                              '\n\na human. So to paint the picture even better, I will'+
                                              '\n\ngo from strongest to weakest: there is Kellog, the'+
                                              '\n\nstrongest courser the Institute has, then there are'+
                                              '\n\nall of the other coursers, then there are regular'+
                                              '\n\nsynths like me, and finally there are you weak'+
                                              '\n\nhumans. If they sent HIM to help retrieve your'+
                                              '\n\ninfant son, then your son was defintely used in'+
                                              '\n\nan experiment that the Institute probably labeled,'+
                                              '\n\n"confidential". I don\'t know what it could be'+
                                              '\n\nbut it had to be VERY important to them. And I fear'+
                                              '\n\nbecause the Institute scientist have no morals. They'+
                                              '\n\nwill conduct ANY experiment. They see the people of'+
                                              '\n\nthe CommonWealth as inferior people......'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: The reason for that is because most people living'+
                                              '\n\nin the CommonWealth have bad genetics. There is radiation'+
                                              '\n\neverywhere and people are badly affected by it whether they'+
                                              '\n\nrealize it or not. Now, I don\'t know where the Institute is, but'+
                                              '\n\nI do know they are in a place where they are not affected by the'+
                                              '\n\nradiation. I\'ve tried so hard to remember the place, but they'+
                                              '\n\nwiped my memory pretty darn good. Wherever they are, they must be'+
                                              '\n\nthe offspring of some pretty intelligent people that somehow'+
                                              '\n\nsurvived the nuclear war hundreds of years ago...'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Getting back on topic.....Kellog will definitely be'+
                                              '\n\nstationed at that old military fort for the next few months. I'+
                                              '\n\nthink the fort\'s name is Fort Hagen. It\'s an old Army base.'+
                                              '\n\nSurely you know where to find that since you were in the military'+
                                              '\n\nAND lived during a time when it was still in operation?'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: TO THE PIT WITH KELLOG! Yes, I admit, I am scared.'+
                                              '\n\nBut one of us is gonna be hanging our combat boots'+
                                              '\n\nup real soon and it\'s NOT gonna be me. You think'+
                                              '\n\nI\'m just going to let him DESTROY MY FAMILY, and let'+
                                              '\n\nhim continue breathing without AT LEAST making him'+
                                              '\n\nbleed? I\'ll go there as soon as I can, but how do'+
                                              '\n\nyou know for certain that he is there Nick? And yes,'+
                                              '\n\nI know exactly where it\'s at. I signed up for the'+
                                              '\n\nmilitary there hundreds of years back.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Well let\'s just say I know when the Institute'+
                                              '\n\nis snooping around. I\'ve passed by that Fort Hagen area the'+
                                              '\n\nother day as I was taking a walk. It was heavily fortified.'+
                                              '\n\nThere are robot machine gun turrets surrounding it that will'+
                                              '\n\nshoot at anyone who gets too close. It has to be the Institute'+
                                              '\n\nrunning some sort of operation over there. Who else could it be?'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Thank you so much Nick! I know nothing is over yet'+
                                              '\n\nbut I\'ll be leaving your office with such a far deeper'+
                                              '\n\nunderstanding of everything that is going on around me.'+
                                              '\n\nAnd you gave me a lead. Since that Kellog guy is a courser'+
                                              '\n\nhe can teleport to the Insitute. Well....he\'s going to'+
                                              '\n\ntake me straight to the Institute so that I can find my'+
                                              '\n\nson. If he doesn\'t want to be calm and collected about'+
                                              '\n\nit all: then you best bet that one of us is hanging our'+
                                              '\n\ncombat boots.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: This is what I was afraid of. I knew I wouldn\'t'+
                                              '\n\nbe able to stop you: you\'re head strong. Of course you are:'+
                                              '\n\nyou must have served in one of those military special forces for'+
                                              '\n\ncrazy people. You know, the ones where people undergo stupid'+
                                              '\n\ncrazy training....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: *smiles at Nick*'+
                                              '\n\nSYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: *smiles* I\'ll take that as a yes. Do you'+
                                              '\n\nwant me to help you? I\'m not living for anything else...'+
                                              '\n\nI\'d be willing to lay my life on the line to help you...'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Nick....I so appreciate you saying that. But I must do this'+
                                              '\n\nalone.....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Yeah.....you\'re a special type of crazy'+
                                              '\n\nalright. Well I noticed you had on some power armor'+
                                              '\n\nwhen you got here. Not to sound creepy, but I was looking'+
                                              '\n\nthrough the window....You best use that armor to fight him.'+
                                              '\n\nTo my understanding T-60 power armor was the strongest'+
                                              '\n\narmor created by the U.S. military hundreds of years ago.'+
                                              '\n\nSo if you don\'t have that T-60 power armor already I can'+
                                              '\n\ntell you that the merchant is selling a suit he found at'+
                                              '\n\nan old military checkpoint. He got together with some other'+
                                              '\n\nguys and fixed it up. They knew how to fix it because the'+
                                              '\n\nschematics for it were apparently inside of it. It must\'ve'+
                                              '\n\nbeen a new suit back in the day. It\'s not like I talk to'+
                                              '\n\nanyone: everyone hates me because I\'m a synth. I just'+
                                              '\n\nhappened to walk by one day and.....I guess eavesdropped'+
                                              '\n\non their conversation.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        if ARMOR3 in character_inventory3:
                                            input('You: Thanks for the info Nick, but I already have the T-60'+
                                                  '\n\npower armor. The one you saw me come here in is the T-60.'+
                                                  '\n\nBut uhhh....how much is your service?'+
                                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                            print()
                                            print()
                                        else:
                                            input('You: Ok Nick, I\'ll go check that out. Thanks for that info.'+
                                                  '\n\nBut uhhh....how much is your service?'+
                                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                            print()
                                            print()

                                        input('Nick Valentine: HAHAHAHHAHAHA. You really think I\'m going'+
                                              '\n\nto charge you? What do I even need money for? I don\'t'+
                                              '\n\nneed food, water, or sleep my man. Just the clothes on'+
                                              '\n\nmy back. You\'re good to go. But please.....please be'+
                                              '\n\ncareful. You\'re the only person in my life that has'+
                                              '\n\ntreated me like a person. The Institute dumped me like'+
                                              '\n\nlike trash and the people in this city have hated me my'+
                                              '\n\nentire short life of 10 years. We may not ever become'+
                                              '\n\nfriends, but I\'d like to visit Fort Hagen one day and'+
                                              '\n\nsee the remains of "Kellog the Courser". Because I\'ll know'+
                                              '\n\nexactly who did it. I\'ll know that you got into the'+
                                              '\n\nInstitute and found your son. Where will you be? I won\'t'+
                                              '\n\nknow: this may be the last time I see you. But I\'m sure'+
                                              '\n\nwherever you go Nate, you will make the best of your'+
                                              '\n\nsituation. Good luck to you: I really enjoyed you and will'+
                                              '\n\nnever forget this day.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Goodbye, Nick! You may not be human exactly. But I feel'+
                                              '\n\nif my circumstances had allowed it: we could have been'+
                                              '\n\nthe best of friends. I\'ll never forget you myself.'+
                                              '\n\nI\'ll give you something to smile about when you visit'+
                                              '\n\nFort Hagen: don\'t you worry. I will win, and I will'+
                                              '\n\nmake the best of my situation: whatever it comes to be.'+
                                              '\n\nThat\'s all anyone can do. Goodbye, Nick!'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Goodbye, Nate! Be safe!'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('SYSTEM: You leave Nick Valentine\'s Detective Agency:'+
                                              '\n\nWith a new lead, a smile on your face, and a friend'+
                                              '\n\nthat you may never see again, but he might be watching'+
                                              '\n\nyou through the window...You decide to not look back'+
                                              '\n\nand let the memories be all that you need. You enter'+
                                              '\n\nyour power armor you left at the entrance of the building'+
                                              '\n\nyou and have already collected your weapons on your way'+
                                              '\n\nout of the door.'+
                                              '\n\nPress enter to contine. ')
                                            
                                        if TALKED_TO_NICK not in quest_inventory:
                                            quest_inventory.append(TALKED_TO_NICK)


                                                  
                                    else:
                                        input('SYSTEM: You walk into Nick Valentine\'s Detective Agency'+
                                              '\n\nwanting to get a lead on who kidnapped your infant son'+
                                              '\n\nand gunned down your wife in Vault 111. But you exit'+
                                              '\n\nyour power armor before going in. Upon entering you'+
                                              '\n\nplace your weapons in a large bin that says, "Place'+
                                              '\n\nweapons here,and make sure they unloaded and off."'+
                                              '\n\nApparently you are allowed to open carry in Diamond'+
                                              '\n\nCity: you got lucky. You noticed the big letters on'+
                                              '\n\nfront of the building as you walked in, they read:'+
                                              '\n\n"Nick Valentine\'s Detective Agency". You also noticed'+
                                              '\n\nthat these letters have neon: they must light up at'+
                                              '\n\nnight, as do many other businesses in Diamond City.'+
                                              '\n\nPress enter to continue. ')
                                        print()
                                        print()
                                        input('Handsome young man: *appears very surprised*'+
                                              '\n\nWhy, Hello. How may I help you sir?'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Yes, I am looking for a, Nick Valentine?'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Handsome young man: *appears very surprised with raised eyebrows*'+
                                              '\n\nWell, I\'m assuming you must have a case that needs solving if'+
                                              '\n\nyou\'re walking in here. But I must admit that I am very sur-'+
                                              '\n\nprised.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: *looking on dumbfoundedly* Please, come again?'+
                                              '\n\nWhat is there to be surprised about exactly?'+
                                              '\n\nPress enter to continue.')
                                        print()
                                        print()
                                        input('Handsome young man: *chuckles with hand over mouth and closed eyes*'+
                                              '\n\nHmmmmmm. You must be new to this city? *runs right hand through'+
                                              '\n\nhis medium brush up haircut*'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Ok what\'s really going on? Is this place even a legitimate'+
                                              '\n\nbusiness? I have the feeling your\'re about to try and do'+
                                              '\n\nsomething to me....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Handsome young man: Don\'t be alarmed friend; I\'ll help anyone'+
                                              '\n\nthat needs it. It\'s just that I have not had a person walk in'+
                                              '\n\nhere in over 10 years since I announced to the city that I am'+
                                              '\n\na synth. I did it right after the broken mask incident; I felt'+
                                              '\n\nit was better if people knew what I truly am rather than living'+
                                              '\n\na lie day in and out.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Ok....Hold on...*grabs head with both hands confused*'+
                                              '\n\nI have three questions and probably a lot more to come.'+
                                              '\n\n1. You must be telling me that YOU are Nick Valentine'+
                                              '\n\n2. What is a synth? 3. What is the "broken mask incident?"'+
                                              '\n\nPlease explain, I am so confused...*sighs*'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Friend, I will have to be quick about all of'+
                                              '\n\nthis as I want to prioritize your case more so than your'+
                                              '\n\ncuriosity. Yes, I am Nick Valentine and I am a synth'+
                                              '\n\ncreated by the Institute. The Institute is a scientific'+
                                              '\n\norganization that are like ghost. Most of anything people'+
                                              '\n\nknow about them is that they create us synths, people who'+
                                              '\n\nappear to be human, everything about us is human. Except'+
                                              '\n\nthat we have a synth component, or, a computer chip in'+
                                              '\n\nour brains. We are manufactured by the Insititute. The'+
                                              '\n\nInstitute is extremely advanced in science. They have'+
                                              '\n\nmanaged to recreate the human body with beyond high tech'+
                                              '\n\nmachinery.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                                  
                                        input('Nick Valentine: They send us synths to kill someone and basically'+
                                              '\n\nsteal their identity, and we are supposed to give reports to'+
                                              '\n\nInstitute scientist when they visit us so they can see how'+
                                              '\n\nwell the results of their experiments are going. Often their'+
                                              '\n\nexperiments succeed. So often, in fact, that most people in this'+
                                              '\n\ncity, in the CommonWealth period, are distrusting of each other.'+
                                              '\n\nNo one knows who might get replaced by a synth in the middle of'+
                                              '\n\nthe night. So there is a lot of paranoia and for good reason.'+
                                              '\n\nAnd we can easily kill a human, as our bodies are far superior.'+
                                              '\n\nTo help us rid of the person\'s body, the scientist take it'+
                                              '\n\nand teleport with it to the Institute and dispose of it somehow:'+
                                              '\n\nI\'m not sure. And yes you heard me right: they all can teleport'+
                                              '\n\nthanks to some teleporting machine they created.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                            
                                        input('Nick Valentine: I have never killed anyone myself. I was a prototype'+
                                              '\n\nsynth, the Institute just dumped me outside of Diamond City one'+
                                              '\n\nday deciding that I was a failed experiment. They made sure to'+
                                              '\n\nerase most of my memories. So I can\'t say where they are or expose'+
                                              '\n\neverything that they do. You\'d think they kill me knowing as much'+
                                              '\n\nas I do. Yes, my body is far superior to a humans, so you\'d ask,'+
                                              '\n\n"how can they kill me?". Well those Institute scientist have these'+
                                              '\n\nsynths called coursers that follow their every command. Basically'+
                                              '\n\ncoursers are synths in the Institute that have underwent intensive'+
                                              '\n\ncombat training and had their bodies enhanced with technology. So they'+
                                              '\n\nare FAR stronger than a regular synth: and a regular synth is already FAR'+
                                              '\n\nstronger than a human, so you think hard about that. They can teleport'+
                                              '\n\njust like the scientist too. They are the "ultimate fighting machines"'+
                                              '\n\nas I recall the institute scientist saying.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: *Nick stares at you.* I don\'t even know what to'+
                                              '\n\nsay. Sorry if I seem rude.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Well I\'m not done, so don\'t say anything'+
                                              '\n\nmore just yet. The broken mask incident happened ten'+
                                              '\n\nyears ago in Diamond City. It was when the Institute'+
                                              '\n\naccidentally revealed to the CommonWealth that they'+
                                              '\n\nexist. They had one of their first synths try to blend'+
                                              '\n\nin with humans, but he malfunctioned one night drinking'+
                                              '\n\nat a bar. He whipped out a gun and started blasting every'+
                                              '\n\nperson in sight. His name was Micheal. All humans thought'+
                                              '\n\nhe was the same funny Micheal that used to crack jokes at'+
                                              '\n\nthe bar on a Friday night after work. But that Micheal was'+
                                              '\n\nabducted and killed by the Institute. That started all of'+
                                              '\n\nthis synth and Institute paranoia, but it\'s understandable.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Come friend, I have given you the information'+
                                              '\n\nyou have sought, now let\'s hear about your case. Come'+
                                              '\n\nand sit down with me in my office.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('SYSTEM: You follow Nick to his office and he sits you in a'+
                                              '\n\ncustomer\'s chair while he sits in his chair on the'+
                                              '\n\nother side of his office desk.'+
                                              '\n\nPress enter to continue. ')
                                        print()
                                        print()
                                        input('Nick: Sorry, I never got your name.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: It\'s Nate. Nate McPherson. I\'d like to apologize'+
                                              '\n\nas well. The reason I was so surprised that you were'+
                                              '\n\nNick Valentine is that fact that you look so young'+
                                              '\n\nand handsome for a detective. I imagine detectives'+
                                              '\n\nto be old guys with saggy eye bags because they never'+
                                              '\n\nget any sleep.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: HAHAHA, HAHAHA. Ok...Oh my goodness, sorry.'+
                                              '\n\nMan you really are clueless. I suppose I am young. I\'m'+
                                              '\n\nonly 10 years old, but with the appearnace of a handsome'+
                                              '\n\nyoung man. But I stole this man\'s identity, like I told'+
                                              '\n\nyou earlier: I didn\'t kill him, but the Institute did'+
                                              '\n\nrecreate this man: andI\'m that recreation. They must'+
                                              '\n\nhave killed him themselves. I took his name and everything.'+
                                              '\n\nApparently he was an exceptional detective for him to only'+
                                              '\n\nbe 23 years old. But his age is something I can\'t steal,'+
                                              '\n\nhe\'d be 33 right now if he weren\'t dead: while I\'m 10.'+
                                              '\n\nI\'m only an exceptional detective because of him. But it'+
                                              '\n\ndoesn\'t matter because everyone is so afraid of synths that'+
                                              '\n\nthey never come to do business with me. I did tell you earlier'+
                                              '\n\nthat no one has been in here for 10 years. Basically ever since'+
                                              '\n\nI told everyone I was synth: which I did when I was 10 months'+
                                              '\n\nold, it was shortly after the broken mask incident. That\'s why'+
                                              '\n\nI was so surprised when you came in. And before you ask: no.'+
                                              '\n\nI was never a child, all synths are created with adult bodies'+
                                              '\n\nand intellect, but again, both are superior to a normal humans.'+
                                              '\n\nSo I was but a few hours old when I started doing all of this.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Ok, but you\'d think you would at least age huh?'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: No, we synths do not age. You\'d think those'+
                                              '\n\n"oh so smart" Institute scientist would see that as a'+
                                              '\n\nflaw. We replace people\'s entire being, so surely their'+
                                              '\n\nloved ones would notice that we are not aging while they'+
                                              '\n\nare. That only blows our cover. But again, there is a lot'+
                                              '\n\nI don\'t remember, I\'m sure they counter it somehow. The'+
                                              '\n\nInstitute probably replaces the synth with one that looks'+
                                              '\n\nolder, and they might do this as many times as it takes'+
                                              '\n\nto make it appear that the synth is aging to all humans.'+
                                              '\n\nWe also don\'t need food, water, or sleep. We can enjoy'+
                                              '\n\nthem. But they are not required for us to function.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Ok, all of this is crazy. I don\'t want to believe'+
                                              '\n\nany of this but I guess I have seen some pretty weird'+
                                              '\n\nthings already.....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: *staring intensely and speaking very serious*'+
                                              '\n\nNow\'s it\'s my turn to ask questions. Before we discuss'+
                                              '\n\nyour case, I have to know....Why do you act as if you were'+
                                              '\n\nborn yesterday? You act like this world is completely new'+
                                              '\n\nto you....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: *staring back at Nick and speaking very serious*'+
                                              '\n\nI\'ll give you my story then. Unlucky for you, my'+
                                              '\n\nentire life from the year 2077 to this year, 2287,'+
                                              '\n\nis the case. '+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: *very surprised* You\'re telling me your'+
                                              '\n\n210+ years old? You were born AND raised before this'+
                                              '\n\nworld had that worldwide nuclear war? How have you'+
                                              '\n\nlived so long? Only us synths are immortal: unless'+
                                              '\n\nwe are killed somehow....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: *speaking fast* But hold those thoughts for a'+
                                              '\n\nmoment, let me get my pen and notepad out to take notes.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('SYSTEM: *Nick Prepares his notepad*'+
                                              '\n\nPress enter to continue. ')
                                        print()
                                        print()
                                        input('Nick: Ok, open up the dam\'s gates my friend. '+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                                  
                                        input('You: I served in the U.S. military. It went out of commission the'+
                                              '\n\nday the nukes exploded worldwide as I\'m sure you know. That'+
                                              '\n\nday my family and I had coincidentally just signed up for a'+
                                              '\n\nprogram called Vault-Tec. The world was at war, world war 3.'+
                                              '\n\nBut a worldwide nuclear war was feared by everyone, because'+
                                              '\n\neveryday world leaders threatend one another. So this Vault-Tec'+
                                              '\n\ntook advantage of this and started up their company that offered'+
                                              '\n\npeople a safe place inside of a vault in the case that the nuclear'+
                                              '\n\nwar started. Everyone who signed up for the vaults had to pay a'+
                                              '\n\nmembership, but it was really my wife who convinced me to do it:'+
                                              '\n\nI hate salesmen with a passion. I hate their job not the person,'+
                                              '\n\njust to make that clear. Anyways, October 23, 2077: it was reported'+
                                              '\n\nthat nukes were going off worldwide. Everyone who signed up for the'+
                                              '\n\nvault rushed to it for dear life: my family included. I had my wife,'+
                                              '\n\nNora, running beside me, and she had our son, Shaun, in arms. The'+
                                              '\n\nsirens were so scary. *Tears slowly fall down your eyes as you wipe'+
                                              '\n\nthem*.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Now, now. One step at a time. It\'s ok.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: The people who didn\'t sign up for the vaults...Nick!'+
                                              '\n\n*Burst out crying* You should have heard their screams'+
                                              '\n\nand cries! Entire families killed because of evil men!'+
                                              '\n\nLittle children: KILLED! Lovers: KILLED! People living'+
                                              '\n\nhonest lives: KILLED! FOR WHAT?!? BECAUSE HUMANS NEVER'+
                                              '\n\nLEARN! WHAT IS OUR PROBLEM NICK!??! WHY DOES THIS ALWAYS'+
                                              '\n\nHAPPEN?!?!'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: *sincerely speaking* Please, try to'+
                                              '\n\ntake deeps breaths, you\'re getting a bit off'+
                                              '\n\ntopic. I know this hits close to home, but,'+
                                              '\n\nplease focus my friend...'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: *slowly but surely calmed down* When we entered the'+
                                              '\n\nvaults everything was seemingly fine. Vault-Tec told'+
                                              '\n\nus that to proceed deeper into the vault we would have'+
                                              '\n\nto be decontaminated in cryogenic pods. Everyone was in'+
                                              '\n\na state of dissassociation. No one could believe nor'+
                                              '\n\naccept that the fact that the entire world had just went'+
                                              '\n\nup in smoke and billions of people with it. I kissed my'+
                                              '\n\ninfant son, Shaun, on the forehead and told him I loved'+
                                              '\n\nhim. I proceeded to do the same thing to my wife, but she'+
                                              '\n\nbeat me too it. We were put in the cryogenic pods and'+
                                              '\n\nmy wife\'s pod was directly across from mine. Before we'+
                                              '\n\nwere "decontaminated" my wife and I waved at each other'+
                                              '\n\nthrough the glass of the cryogenic pods. She had my infant'+
                                              '\n\nson, Shaun with her. Nick. Vault-Tec had lied. We didn\'t'+
                                              '\n\nwake up in a few minutes. We woke up just recently. Hundreds'+
                                              '\n\nof years later! Vault Tec were just mad scientist doing ex-'+
                                              '\n\nperiemts on us! And apparently after they experimented on us'+
                                              '\n\nthey just lived out the rest of their days in that vault and died:'+
                                              '\n\nleaving us in those cryogenic pods! I don\'t know what the year'+
                                              '\n\nwas, but my wife was gunned down in front of me by two guys'+
                                              '\n\nin what seemed like biohazard suits, and a man in an all black'+
                                              '\n\nleather trench coat with a huge white gun. The details are'+
                                              '\n\nhazy, but...'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: The guy in the black leather trench coat told my wife to let'+
                                              '\n\ngo of my son. She refused naturally. And the man told her that,'+
                                              '\n\n"I\'m only going to tell you once, let go of the child or die."'+
                                              '\n\nMy wife basically told him to go do himself in and he shot her.'+
                                              '\n\n*trying to fight your emotions* The people wearing biohazard'+
                                              '\n\nsuits took my son and the man in the black leather trench coat'+
                                              '\n\nsaid, "At least we still have the backup.", as he looked at me.'+
                                              '\n\nI was refrozen by them after all of that happened.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: *looks very anxious* Noooooo, my friend, nooo.'+
                                              '\n\nOk. I have a very bad feeling. But I\'m going to assume'+
                                              '\n\nthat feeling is not true and try to be logical and look'+
                                              '\n\nat all of our options before I jump to any conclusions.'+
                                              '\n\nI will rule out some things though. I know supermutants'+
                                              '\n\ndidn\'t do this because they are dumb as rocks and you did'+
                                              '\n\nsay that people did this, not 8 foot tall green, muscular'+
                                              '\n\nmen....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Wait, a minute! I saw those when I came to the city!'+
                                              '\n\nI helped defend the Diamond City security team! I was'+
                                              '\n\nWondering what those things were....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Ok, I will explain something on a side note here, because'+
                                              '\n\nyou get off topic very easily. To prevent this from happening again'+
                                              '\n\nI will explain some things about the world you are currently in since'+
                                              '\n\nit\'s basically new to you. Supermutants come from the Institute.'+
                                              '\n\nThey were once humans themselves, but the institute kidnapped them and'+
                                              '\n\nattempted to make "super humans". This was before their synth research.'+
                                              '\n\nThere are also these things called DeathClaws. They often are under'+
                                              '\n\nsewers. They have claw-like hands, are about 10 feet tall, and have horns'+
                                              '\n\non their heads that point forward and straight instead of wide and upward'+
                                              '\n\nlike you would see on a bull. These creatures also were created by the'+
                                              '\n\nInstitute. What were they trying to do? I don\'t know. They do anything'+
                                              '\n\nin the name of science and care not for the repercussions of their'+
                                              '\n\nreckless experiments....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: I also know that raiders did not do this as they'+
                                              '\n\nonly care about robbing people of their valuables: whether'+
                                              '\n\nthey have to kill the person for them or not. The last thing'+
                                              '\n\nthey would want is to kill your wife to get an infant child.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        if DEATH_CLAW in quest_inventory:
                                            input('You: Yeah I definitely have ran into a DeathClaw...'+
                                                  '\n\nkilled it too...it was back in Concord....'+
                                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                                      
                                            print()
                                            print()
                                            input('Nick Valentine: What?!?! You....a human.... killed a'+
                                                      '\n\nDeathClaw? Nevermind that....your case please...'+
                                                      '\n\n(SYSTEM: Press enter to continue.) ')
                                            print()
                                            print()

                                        input('You: I\'ve definitely ran into those raiders you\'re'+
                                              '\n\ntalking about. I had a shootout with them at the'+
                                              '\n\nMuesuem of Freedom. Got hit in the left shoulder.'+
                                              '\n\nI took care of them though.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        if DEATHCLAW_MEAT in character_inventory3:
                                            character_inventory3.remove(DEATHCLAW_MEAT)
                                            DEATHCLAW_MEAT = 'DeathClaw Meat'
                                            character_inventory3.append(DEATHCLAW_MEAT)
                                        print()
                                        print()
                                        input('Nick Valentine: Well Nate. I also know it that it wasn\'t'+
                                              '\n\nthe Diamond City Mafia. Those goons only care about'+
                                              '\n\nhow much money they can make. They\'re not getting'+
                                              '\n\nany money out of a crying infant and a it\'s dead'+
                                              '\n\nmother. So I apologize. What I was denying earlier'+
                                              '\n\nis true.....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('SYSTEM: *room goes silent* *Nick stares down'+
                                              '\n\nat the floor in disbelief*'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Nick! What the heck?!?! What\'s so bad?'+
                                              '\n\nTell me something...'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: *staring at the floor and speaking very seriously*'+
                                              '\n\nI wish that I could tell you I\'d be at the bottom of this'+
                                              '\n\ncase by this weekend.....But Nate.....oh Nate... *facepalms*'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Nick! Stop and tell me! You\'re killing me!'+
                                              '\n\nOh my goodness! Is it something about those'+
                                              '\n\nguys in the vault?'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: The Institute killed your wife and'+
                                              '\n\ntook your child Nate...'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('SYSTEM: There is an eerie silence and a lot of staring at'+
                                              '\n\nthe floor by both You and Nick for about 5 minutes.'+
                                              '\n\nPress enter to continue. ')
                                        print()
                                        print()
                                        input('You: Nick this can\'t be true: I mean....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick: Stop! This is the truth. I knew it as soon as'+
                                              '\n\nyou mentioned what the people were wearing....the'+
                                              '\n\npeople that killed your wife and took your infant'+
                                              '\n\nson. But I didn\'t want it to be true.*sigh* Those'+
                                              '\n\ntwo people wearing biosuits were definitely Institute'+
                                              '\n\nscientist that needed your son for some type of ex-'+
                                              '\n\nperiment. The man in the black trench coat, "with a'+
                                              '\n\nbig white gun" as you said: was definitely an Institute'+
                                              '\n\ncourser. The gun your wife was killed with was a gun'+
                                              '\n\nthat shoots blue laser beams. Institute Coursers are'+
                                              '\n\ntrained to use these deadly weapons. Though I haven\'t'+
                                              '\n\nseen those weapons in action. So, I\'m not sure how strong'+
                                              '\n\nthose laser beams are, but they\'d definitely rip right'+
                                              '\n\nthrough a human and literally melt their flesh and'+
                                              '\n\ninternal organs upon contact. May I ask, did you look'+
                                              '\n\nat your wife\'s body after you woke up and got out of your'+
                                              '\n\ncryogenic pod?'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Yes, and I passed out. I\'m not sure for how long. But'+
                                             '\n\nI had to be sure....you know? I was in such strong'+
                                             '\n\ndenial that she was gone. Then I just blanked out.'+
                                             '\n\nAnd before you ask...I don\'t know how I got out'+
                                             '\n\nof my pod. It just seemingly stopped the icing'+
                                             '\n\nprocess or malfunctioned or something and I was'+
                                             '\n\nable to get out.'+
                                             '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Ok, maybe we don\'t have to worry'+
                                              '\n\nabout how you got out. That\'s not the problem'+
                                              '\n\nat hand. Can you tell me what that Institute'+
                                              '\n\ncourser sounded like? What hairstyle he had?'+
                                              '\n\nMaybe some facial features? I may know his'+
                                              '\n\nname and his whereabouts. It\'s defintely a'+
                                              '\n\nsuicide mission to go after him, but as hard'+
                                              '\n\nas it can be: I\'ll to give you all the inf-'+
                                              '\n\normation that I can. But he might be one of'+
                                              '\n\nthose coursers that only work inside of the'+
                                              '\n\nInstitute and not so much among us.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: His voice was deep and rough: like sandpaper'+
                                              '\n\ngoing across your face. He had a buzzcut. And'+
                                              '\n\nhe had a huge scar going across his entire face.'+
                                              '\n\nFor you to call coursers so tough, somebody'+
                                              '\n\ndefinitely did him in with a knife to the face'+
                                              '\n\nin the past.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: No! Please don\'t ever do that'+
                                              '\n\nagain! Do not underestimate coursers! The only'+
                                              '\n\nthing that could have cut his face like that'+
                                              '\n\nwas another synth that was trying out to become'+
                                              '\n\na courser that I\'m sure he fought during his'+
                                              '\n\nintense training. Synths have to kill each other'+
                                              '\n\nunder that intense training to become coursers.'+
                                              '\n\nOf course the last man standing is the one who'+
                                              '\n\nbecomes the Institute\'s newest courser. So the'+
                                              '\n\ncourser you just insulted killed ten if not hundreds'+
                                              '\n\nof others abnormally strong synths to get his position.'+
                                              '\n\nThat\'s how strong he is. He was the last one standing.'+
                                              '\n\nAnd I know exactly which courser it is and where he is'+
                                              '\n\ncurrently.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: *eyes grow wide with fear*'+
                                              '\n\nSo he is one of the most experienced and'+
                                              '\n\nbattle hardend coursers the Institute has?'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Don\'t grow scared now! You talked'+
                                              '\n\nabout him like he was just some punk a second'+
                                              '\n\nago. And yes he is the most experienced courser'+
                                              '\n\nthat he institute has. Remember how I told you'+
                                              '\n\nwe synths are FAR stronger than you humans?'+
                                              '\n\nWell also remember that I told you that coursers'+
                                              '\n\nare synths that are FAR stronger than regular'+
                                              '\n\nsynths like myself. And this courser I\'m talking'+
                                              '\n\nabout: Kellog, is hands down the strongest courser'+
                                              '\n\nthe Institute has. Not to be rude: but you\'re just'+
                                              '\n\na human. So to paint the picture even better, I will'+
                                              '\n\ngo from strongest to weakest: there is Kellog, the'+
                                              '\n\nstrongest courser the Institute has, then there are'+
                                              '\n\nall of the other coursers, then there are regular'+
                                              '\n\nsynths like me, and finally there are you weak'+
                                              '\n\nhumans. If they sent HIM to help retrieve your'+
                                              '\n\ninfant son, then your son was defintely used in'+
                                              '\n\nan experiment that the Institute probably labeled,'+
                                              '\n\n"confidential". I don\'t know what it could be'+
                                              '\n\nbut it had to be VERY important to them. And I fear'+
                                              '\n\nbecause the Institute scientist have no morals. They'+
                                              '\n\nwill conduct ANY experiment. They see the people of'+
                                              '\n\nthe CommonWealth as inferior people......'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: The reason for that is because most people living'+
                                              '\n\nin the CommonWealth have bad genetics. There is radiation'+
                                              '\n\neverywhere and people are badly affected by it whether they'+
                                              '\n\nrealize it or not. Now, I don\'t know where the Institute is, but'+
                                              '\n\nI do know they are in a place where they are not affected by the'+
                                              '\n\nradiation. I\'ve tried so hard to remember the place, but they'+
                                              '\n\nwiped my memory pretty darn good. Wherever they are, they must be'+
                                              '\n\nthe offspring of some pretty intelligent people that somehow'+
                                              '\n\nsurvived the nuclear war hundreds of years ago...'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Getting back on topic.....Kellog will definitely be'+
                                              '\n\nstationed at that old military fort for the next few months. I'+
                                              '\n\nthink the fort\'s name is Fort Hagen. It\'s an old Army base.'+
                                              '\n\nSurely you know where to find that since you were in the military'+
                                              '\n\nAND lived during a time when it was still in operation?'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: TO THE PIT WITH KELLOG! Yes, I admit, I am scared.'+
                                              '\n\nBut one of us is gonna be hanging our combat boots'+
                                              '\n\nup real soon and it\'s NOT gonna be me. You think'+
                                              '\n\nI\'m just going to let him DESTROY MY FAMILY, and let'+
                                              '\n\nhim continue breathing without AT LEAST making him'+
                                              '\n\nbleed? I\'ll go there as soon as I can, but how do'+
                                              '\n\nyou know for certain that he is there Nick? And yes,'+
                                              '\n\nI know exactly where it\'s at. I signed up for the'+
                                              '\n\nmilitary there hundreds of years back.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Well let\'s just say I know when the Institute'+
                                              '\n\nis snooping around. I\'ve passed by that Fort Hagen area the'+
                                              '\n\nother day as I was taking a walk. It was heavily fortified.'+
                                              '\n\nThere are robot machine gun turrets surrounding it that will'+
                                              '\n\nshoot at anyone who gets too close. It has to be the Institute'+
                                              '\n\nrunning some sort of operation over there. Who else could it be?'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Thank you so much Nick! I know nothing is over yet'+
                                              '\n\nbut I\'ll be leaving your office with such a far deeper'+
                                              '\n\nunderstanding of everything that is going on around me.'+
                                              '\n\nAnd you gave me a lead. Since that Kellog guy is a courser'+
                                              '\n\nhe can teleport to the Insitute. Well....he\'s going to'+
                                              '\n\ntake me straight to the Institute so that I can find my'+
                                              '\n\nson. If he doesn\'t want to be calm and collected about'+
                                              '\n\nit all: then you best bet that one of us is hanging our'+
                                              '\n\ncombat boots.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: This is what I was afraid of. I knew I wouldn\'t'+
                                              '\n\nbe able to stop you: you\'re head strong. Of course you are:'+
                                              '\n\nYou must have served in one of those military special forces for'+
                                              '\n\ncrazy people. You know, the ones where people undergo stupid'+
                                              '\n\ncrazy training....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: *smiles at Nick*'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: *smiles* I\'ll take that as a yes. Do you'+
                                              '\n\nwant me to help you? I\'m not living for anything else...'+
                                              '\n\nI\'d be willing to lay my life on the line to help you...'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Nick....I so appreciate you saying that. But I must do this'+
                                              '\n\nalone.....'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Yeah.....you\'re a special type of crazy'+
                                              '\n\nalright. Well I noticed you had on some power armor'+
                                              '\n\nwhen you got here. Not to sound creepy, but I was looking'+
                                              '\n\nthrough the window....You best use that armor to fight him.'+
                                              '\n\nTo my understanding T-60 power armor was the strongest'+
                                              '\n\narmor created by the U.S. military hundreds of years ago.'+
                                              '\n\nSo if you don\'t have that T-60 power armor already I can'+
                                              '\n\ntell you that the merchant is selling a suit he found at'+
                                              '\n\nan old military checkpoint. He got together with some other'+
                                              '\n\nguys and fixed it up. They knew how to fix it because the'+
                                              '\n\nschematics for it were apparently inside of it. It must\'ve'+
                                              '\n\nbeen a new suit back in the day. It\'s not like I talk to'+
                                              '\n\nanyone: everyone hates me because I\'m a synth. I just'+
                                              '\n\nhappened to walk by one day and.....I guess eavesdropped'+
                                              '\n\non their conversation.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        if ARMOR3 in character_inventory3:
                                            input('You: Thanks for the info Nick, but I already have the T-60'+
                                                  '\n\npower armor. The one you saw me come here in is the T-60.'+
                                                  '\n\nBut uhhh....how much is your service?'+
                                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                            print()
                                            print()
                                        else:
                                            input('You: Ok Nick, I\'ll go check that out. Thanks for that info.'+
                                                  '\n\nBut uhhh....how much is your service?'+
                                                  '\n\n(SYSTEM: Press enter to continue.) ')
                                            print()
                                            print()

                                        input('Nick Valentine: HAHAHAHHAHAHA. You really think I\'m going'+
                                              '\n\nto charge you? What do I even need money for? I don\'t'+
                                              '\n\nneed food, water, or sleep my man. Just the clothes on'+
                                              '\n\nmy back. You\'re good to go. But please.....please be'+
                                              '\n\ncareful. You\'re the only person in my life that has'+
                                              '\n\ntreated me like a person. The Institute dumped me like'+
                                              '\n\nlike trash and the people in this city have hated me my'+
                                              '\n\nentire short life of 10 years. We may not ever become'+
                                              '\n\nfriends, but I\'d like to visit Fort Hagen one day and'+
                                              '\n\nsee the remains of "Kellog the Courser". Because I\'ll know'+
                                              '\n\nexactly who did it. I\'ll know that you got into the'+
                                              '\n\nInstitute and found your son. Where will you be? I won\'t'+
                                              '\n\nknow: this may be the last time I see you. But I\'m sure'+
                                              '\n\nwherever you go Nate, you will make the best of your'+
                                              '\n\nsituation. Good luck to you: I really enjoyed you and will'+
                                              '\n\nnever forget this day.'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('You: Goodbye, Nick! You may not be human exactly. But I feel'+
                                              '\n\nif my circumstances had allowed it: we could have been'+
                                              '\n\nthe best of friends. I\'ll never forget you myself.'+
                                              '\n\nI\'ll give you something to smile about when you visit'+
                                              '\n\nFort Hagen: don\'t you worry. I will win, and I will'+
                                              '\n\nmake the best of my situation: whatever it comes to be.'+
                                              '\n\nThat\'s all anyone can do. Goodbye, Nick!'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('Nick Valentine: Goodbye, Nate! Be safe!'+
                                              '\n\n(SYSTEM: Press enter to continue.) ')
                                        print()
                                        print()
                                        input('SYSTEM: You leave Nick Valentine\'s Detective Agency:'+
                                              '\n\nWith a new lead, a smile on your face, and a friend'+
                                              '\n\nthat you may never see again, but he might be watching'+
                                              '\n\nyou through the window...You decide to not look back'+
                                              '\n\nand let the memories be all that you need. You enter'+
                                              '\n\nyour power armor you left at the entrance of the building'+
                                              '\n\nyou and have already collected your weapons on your way'+
                                              '\n\nout of the door.'+
                                              '\n\nPress enter to contine. ')
                                            
                                        if TALKED_TO_NICK not in quest_inventory:
                                            quest_inventory.append(TALKED_TO_NICK)

                                else:
                                    input('SYSTEM: You have already visited Nick Valentine\'s Detective Agency.'+
                                          '\nPress enter to continue.')

                            elif choice2 == MERCHANT:
                                choice3 = 0
                                BUY = 1
                                SELL = 2
                                QUIT3 = 3
                                while choice3 != QUIT3:
                                    print()
                                    print('Diamond City Merchant')
                                    print('---------------------')
                                    print()
                                    print('1. Buy'+
                                          '\n2. Sell'+
                                          '\n3. Leave Diamond City Merchant')
                                    print()
                                    choice3 = int(input('Enter your choice: '))
                                    print()
                                    while choice3 < BUY or choice3 > QUIT3:
                                        choice3 = int(input('Enter a valid choice: '))
                                        print()

                                    if choice3 == BUY:
                                        choice4 = 0
                                        SNIPER = 1
                                        MINIGUN = 2
                                        FIRSTAIDKIT = 3
                                        T60POWERARMOR =4
                                        FUSIONCORE = 5
                                        QUIT4 = 6
                                        while choice4 != QUIT4:
                                            print()
                                            print('Diamond City Merchant (buying)')
                                            print('----------------------')
                                            print()
                                            print('1. Scoped .50 Cal Sniper ($1500) (comes with ammo)'+
                                                  '\n2. MiniGun ($1500) (comes with ammo)'+
                                                  '\n3. First Aid Kit ($100)'+
                                                  '\n4. T-60 Power Armor (?)'+
                                                  '\n5. Fusion Core ($1100)'+
                                                  '\n6. Quit')
                                            print()
                                            choice4 = int(input('Enter your choice: '))
                                            print()
                                            while choice4 < SNIPER or choice4 > QUIT4:
                                                choice4 = int(input('Enter a valid choice: '))
                                                print()
                                            if choice4 == SNIPER:
                                                # are_you_sure confirms the player's purchase
                                                are_you_sure = str(input('Diamond City Merchant: Are ya sure ya'+
                                                                         '\nwant to buy the Scoped .50 Cal Sniper'+
                                                                         '\nfor $1500?'+
                                                                         '\nSYSTEM: Enter yes to buy or no to quit (use lowercase): '))
                                                print()
                                                if are_you_sure == str('yes'):
                                                    if MONEY < SNIPER_VALUE:
                                                        input('Diamond City Merchant: Come back when ya have'+
                                                              '\n$1500 or more my friend.'+
                                                              '\n(SYSTEM: Press enter to continue.) ')
                                                        print()
                                                        print()
                                                    else:
                                                        if WEAPON3 not in character_inventory3:
                                                            character_inventory3.append(WEAPON3)
                                                            MONEY -= SNIPER_VALUE
                                                            input('Diamond City Merchant: Thank ya for yer'+
                                                                  '\npurchase friend!(SYSTEM: Scoped .50 Cal'+
                                                                  '\nSniper has been added to your inventory.'+
                                                                  '\nPress enter to continue.) ')
                                                        else:
                                                            input('Diamond City Merchant: Sorry friend, by law we\'re not'+
                                                                  '\nallowed to sell ya the same weapon ya\'ve already'+
                                                                  '\npurchased.'+
                                                                  '\n(SYSTEM: Press enter to continue.) ')
                                                        
                                                else:
                                                    input('Diamond City Merchant: Maybe some other time then...'+
                                                          '\n(SYSTEM: Press enter to continue.) ')
                                            elif choice4 == MINIGUN:
                                                # are_you_sure_2 confirms the player's purchase
                                                are_you_sure2 = str(input('Diamond City Merchant: Are ya sure ya'+
                                                                          '\nwant to buy the MiniGun for $1500?'+
                                                                          '\nSYSTEM: Enter yes to buy, or no to quit'+
                                                                          '\n(use lowercase): '))
                                                print()
                                                if are_you_sure2 == str('yes'):
                                                    if MONEY < MINIGUN_VALUE:
                                                        input('Diamond City Merchant: Come back when ya have'+
                                                              '\n$1500 or more my friend.'+
                                                              '\n(SYSTEM: Press enter to continue.) ')
                                                        print()
                                                        print()
                                                    else:
                                                        if WEAPON4 not in character_inventory3:
                                                            character_inventory3.append(WEAPON4)
                                                            MONEY -= MINIGUN_VALUE
                                                            input('Diamond City Merchant: Thank ya for yer'+
                                                                  '\npurchase friend! (SYSTEM: A MiniGun has'+
                                                                  '\nbeen added to your inventory. Press enter'+
                                                                  '\nto continue.) ')
                                                        else:
                                                            input('Diamond City Merchant: Sorry friend, by law we\'re not'+
                                                                  '\nallowed to sell ya the same weapon ya\'ve already'+
                                                                  '\npurchased.'+
                                                                  '\n(SYSTEM: Press enter to continue.) ')
                                                else:
                                                    input('Diamond City Merchant: Maybe some other time then...'+
                                                          '\n(SYSTEM: Press enter to continue.) ')
                                            elif choice4 == FIRSTAIDKIT:
                                                # are_you_sure3 confirms the player's purchase
                                                are_you_sure3 = str(input('Diamond City Merchant: Are ya sure ya'+
                                                                          '\nwant to buy a First Aid Kit for $100?'+
                                                                          '\nSYSTEM: Enter yes to buy, or no to quit'+
                                                                          '\n(use lowercase): '))
                                                print()
                                                if are_you_sure3 == str('yes'):
                                                    if MONEY < FIRSTAIDKIT3_VALUE:
                                                        input('Diamond City Merchant: Come back when ya have'+
                                                              '\n$100 or more my friend.'+
                                                              '\n(SYSTEM: Press enter to contine.) ')
                                                        print()
                                                        print()
                                                    else:
                                                        if FIRST_AID3 not in prevent_exploit3:
                                                            prevent_exploit3.append(FIRST_AID3)
                                                            character_inventory4.append(FIRST_AID3)
                                                            MONEY -= FIRSTAIDKIT3_VALUE
                                                            input('Diamond City Merchant: Thank ya for yer'+
                                                                  '\npurchase friend! (SYSTEM: A First Aid Kit'+
                                                                  '\nhas been added to your inventory. Press'+
                                                                  '\nenter to continue.) ')
                                                        else:
                                                            input('Diamond City Merchant: Sorry friend, by law we\'re not'+
                                                                  '\nallowed to sell ya multiple first aid in such a short'+
                                                                  '\namount of time. Ya understand.... medical supplies'+
                                                                  '\nshould go around evenly. The days of people having'+
                                                                  '\nhealthcare are long gone. Even then people struggled.'+
                                                                  '\nBut nowadays first aid kits are about as good as we'+
                                                                  '\ncan do living in this post-apocalyptic world...'+
                                                                  '\n(SYSTEM: Press enter to continue.) ')
                                                            print()
                                                            input('You: I completely understand. No Worries.'+
                                                                  '\n(SYSTEM: Press enter to contine.) ')
                                                else:
                                                    input('Diamond City Merchant: Maybe some other time then...'+
                                                          '\n(SYSTEM: Press enter to continue.) ')

                                            elif choice4 == T60POWERARMOR:
                                                if FUSION_CORE2 in character_inventory4:
                                                    if TALKED_TO_MERCHANT not in quest_inventory: 
                                                        quest_inventory.append(TALKED_TO_MERCHANT)
                                                        if ARMOR3 not in prevent_exploit:
                                                            input('You: I\'d like to buy that T-60 Power armor.'+
                                                                  '\n(SYSTEM: Press enter to continue). ')
                                                            print()
                                                            print()
                                                            input('Diamond City Merchant: What!?! Son. Do ya even'+
                                                                  '\nknow how to use this here T-60 armor? Most people'+
                                                                  '\nNowadays have no idea how to operate Power Armor.'+
                                                                  '\nIssa shame really. Issa hands down the best armor'+
                                                                  '\nout there. So, I assume ya wander this dangerous'+
                                                                  '\nCommonWealth unlike the spoiled "city" folk around'+
                                                                  '\nhere?'+
                                                                  '\n(SYSTEM: Press enter to continue.) ')
                                                            print()
                                                            print()
                                                            input('You: Yes sir! You best believe I know how to use it.'+
                                                                  '\nAnd yeah....I\'ve been traveling the CommonWealth'+
                                                                  '\na while now. I\'ve ran into my fair share of troubles'+
                                                                  '\nbeyond this cities\' walls.'+
                                                                  '\n(SYSTEM: Press enter to continue.) ')
                                                            print()
                                                            print()
                                                            input('Diamond City Merchant: HAHAHAHA!!! Son! *pssh*'+
                                                                  '\nI\'m yanking yer leg! Ya already wearing'+
                                                                  '\nT-45 Power Armor for crying out loud, HAHAHA!'+
                                                                  '\nOf course I know that ya know how to operate'+
                                                                  '\nthe T-60 suit: the T-45 and T-60 basically'+
                                                                  '\noperate the same.'+
                                                                  '\n(SYSTEM: Press enter to continue.) ')
                                                            print()
                                                            print()
                                                            if DEATH_CLAW and TALKED_TO_NICK in quest_inventory:
                                                                input('Diamond City Merchant: And son, I\'ve noticed ya'+
                                                                      '\nsince you came into this city. I couldn\'t help'+
                                                                      '\nbut notice the guy wearing military armor while'+
                                                                      '\neveryone else is wearing their everyday clothin\'.'+
                                                                      '\nHAHAHAHA!! But I\'ve yet to ask ya, how in the'+
                                                                      '\nworld did you get that huge dent--almost a hole--'+
                                                                      '\nin that T-45 Power Armor there? No stranger to action'+
                                                                      '\nare ya?'+
                                                                      '\n(SYSTEM: Press enter to continue.) ')
                                                                print()
                                                                print()
                                                                input('You: I fought a Dea....'+
                                                                      '\n(SYSTEM: Press enter to continue.) ')
                                                                print()
                                                                print()
                                                                input('Diamond City Merchant: A DeathClaw? Well son....'+
                                                                      '\nI respected ya enough seeing ya stroll around'+
                                                                      '\nin that suit. But now I respect ya 1000 times'+
                                                                      '\nover. I\'ve never heard of a human defeating a'+
                                                                      '\nDeathClaw. Those stories often end in horror:'+
                                                                      '\na fool thinkin\' he can take em on. It\'s only'+
                                                                      '\npossible in Power Armor for a human. But you'+
                                                                      '\nhave to know how to operate the power armor as'+
                                                                      '\nwell. I\'m not goin-ta ask how ya found out to'+
                                                                      '\noperate power armor. But ya best believe I really'+
                                                                      '\nhave a deep respect for ya for defeating that'+
                                                                      '\nDeathClaw and living to tell the tale. And I know'+
                                                                      '\nyour notta liar because those marks are undeniably'+
                                                                      '\nfrom a DeathClaw. I\'ve seen them in person myself.'+
                                                                      '\nBut never crazy enough to get too close to em.'+
                                                                      '\nHAHHAHA!! Ya must be a real nut job son! Crazy'+
                                                                      '\nas they come eh? But you, "walk the walk", no?'+
                                                                      '\n(SYSTEM: Press enter to continue.) ')
                                                                print()
                                                                print()
                                                                input('Diamond City Merchant: I\'m so impressed son that I\'m'+
                                                                      '\nwilling to sell ya this here T-60 power armor at half'+
                                                                      '\nprice. I myself have used it 3 times. But never in'+
                                                                      '\ncombat....I just was hoping that someone like ya would'+
                                                                      '\ncome along and snatch it up. And boy-oh my wishes have'+
                                                                      '\ncome to fruition. The original price is $6000, but ya'+
                                                                      '\ncan take it at $3000 son. Heck I\'d give it to ya free,'+
                                                                      '\nbut a man\'s gotta make a living, no? But I\'ll make the'+
                                                                      '\ndeal with ya only if ya give me that T-45 Power armor'+
                                                                      '\nand the fusion core that\'s in the back of it. I know'+
                                                                      '\nit\'s damaged and the fusion core\'s energy is probably'+
                                                                      '\nlow, but yer walking inna relic son. A relic I\'d like-da'+
                                                                      '\nhave, but I won\'t steal your story and glorify myself.'+
                                                                      '\nHAHAHA! Whenever someone ask me about the marks on the armor,'+
                                                                      '\nI\'ll tell em about the man who stands before me.'+
                                                                      '\n(SYSTEM: Press enter to continue.) ')
                                                                print()
                                                                print()
                                              
                                                                #are_you_sure4 confirms the player's purchase
                                                                are_you_sure4 = str(input('Diamond City Merchant: What\'d ya say son, willing'+
                                                                                          '\nto make this deal?'+
                                                                                          '\nSYSTEM: Enter yes to buy or enter no to quit (use'+
                                                                                          '\nlowercase): '))
                                                                print()
                                                                print()
                                                                if are_you_sure4 == str('yes'):
                                                                    if MONEY < ARMOR3_VALUE:
                                                                        input('Diamond City Merchant: Ah, that\'s great son, but come back when ya'+
                                                                              '\nhave $3000. I promise I\'ll reserve it for ya!'+
                                                                              '\n(SYSTEM:Press enter to continue.) ')
                                                                        print()
                                                                        print()

                                                                    else:
                                                                        if ARMOR3 not in prevent_exploit:
                                                                            prevent_exploit.append(ARMOR3)
                                                                            character_inventory3.append(ARMOR3)
                                                                            character_inventory3.remove(ARMOR2)
                                                                            character_inventory2.remove(FUSION_CORE1)
                                                                            MONEY -= ARMOR3_VALUE
                                                                            input('Diamond City Merchant: Nice doin\' business with ya son!'+
                                                                                  '\nAnd it was nice getting to know one of my customers a'+
                                                                                  '\nlil bit more well.'+
                                                                                  '\n(SYSTEM: Press enter to continue.) ')
                                                                        else:
                                                                            input('SYSTEM: You\'ve already bought the T-60 Power Armor.'+
                                                                                  '\nPress enter to continue.)')
                                                                else:
                                                                    input('Diamond City Merchant: Ok friend. Maybe some other time.'+
                                                                          '\nBut I\'m sure ya gonna be back. *smiles*'+
                                                                          '\n(SYSTEM: Press enter to continue.)')
                                                                
                                                            input('Diamond City Merchant: And son, I\'ve noticed ya'+
                                                                  '\nsince you came inta the city. I couldn\'t help'+
                                                                  '\nbut notice the guy wearing military armor while'+
                                                                  '\neveryone else is wearing their everyday clothin\'.'+
                                                                  '\nHAHAHAHA!! I respect ya for knowing how to operate'+
                                                                  '\npower armor. For that I\'m willing to cut the price'+
                                                                  '\nof this T-60 from $6000 to $3000. But I\'ll only do'+
                                                                  '\nit if ya give me that T-45 Power Armor and the fusion'+
                                                                  '\ncore that\'s in the back of it. I know the fusion core\'s'+
                                                                  '\nenergy is probably low, but I\'m willing to do a trade-in'+
                                                                  '\nof sorts with ya.'+
                                                                  '\n(SYSTEM: Press enter to continue.) ')
                                                            print()
                                                            print()

                                                            #are_you_sure5 confirms the player's purchase
                                                            are_you_sure5 = str(input('Diamond City Merchant: What\'d ya say'+
                                                                                      '\nson, willing-duh make this deal?'+
                                                                                      '\nSYSTEM: Enter yes to buy or enter no to quit (use'+
                                                                                      '\nlowercase): '))
                                                            print()
                                                            if are_you_sure5 == str('yes'):
                                                                if MONEY < ARMOR3_VALUE:
                                                                    input('Diamond City Merchant: Ah, that\'s great son, but come back when ya'+
                                                                          '\nhave $3000. I promise I\'ll reserve it for ya!'+
                                                                          '\n(SYSTEM:Press enter to continue.) ')
                                                                    print()
                                                                    print()

                                                                else:
                                                                    if ARMOR3 not in prevent_exploit:
                                                                        prevent_exploit.append(ARMOR3)
                                                                        character_inventory3.append(ARMOR3)
                                                                        character_inventory3.remove(ARMOR2)
                                                                        character_inventory2.remove(FUSION_CORE1)
                                                                        MONEY -= ARMOR3_VALUE
                                                                        input('Diamond City Merchant: Nice doin\' business with ya son!'+
                                                                              '\nAnd it was nice getting to know one of my customers a'+
                                                                              '\nlil bit more well.'+
                                                                              '\n(SYSTEM: Press enter to continue.) ')
                                                                    else:
                                                                        input('SYSTEM: You\'ve already bought the T-60 Power Armor.'+
                                                                              '\nPress enter to continue.)')
                                                            else:
                                                                input('Diamond City Merchant: Ok friend. Maybe some other time.'+
                                                                      '\nBut I\'m sure ya gonna be back. *smiles*'+
                                                                      '\n(SYSTEM: Press enter to continue.)')
                                                                
                                                    else:
                                                        #are_you_sure6 confirms the player's purchase
                                                        are_you_sure6 = str(input('Diamond City Merchant: Welcome back! Would ya like-da'+
                                                                                  '\nbuy the T-60 Power Armor for $3000? If ya do, ya gonna'+
                                                                                  '\nhave to swap it for that T-45 Power Armor you\'re wearing.'+
                                                                                  '\nThose are muh terms. The T-60 is better than the T-45 in'+
                                                                                  '\nthe field of combat. The price is originally $6000, but'+
                                                                                  '\nfor ya T-45 Power Armor I\'ll cut the price in half.'+
                                                                                  '\nWhat\'d ya say?'+
                                                                                  '\nSYSTEM: Enter yes to buy or enter no to quit (use lowercase): '))
                                                        print()
                                                        print()
                                                        if are_you_sure6 == str('yes'):
                                                            if MONEY < ARMOR3_VALUE:
                                                                input('Diamond City Merchant: Ah, that\'s great son, but come back when ya'+
                                                                      '\nhave $3000. I promise I\'ll reserve it for ya!'+
                                                                      '\n(SYSTEM:Press enter to continue.) ')
                                                                print()
                                                                print()

                                                            else:
                                                                if ARMOR3 not in prevent_exploit:
                                                                    prevent_exploit.append(ARMOR3)
                                                                    character_inventory3.append(ARMOR3)
                                                                    character_inventory3.remove(ARMOR2)
                                                                    character_inventory2.remove(FUSION_CORE1)
                                                                    MONEY -= ARMOR3_VALUE
                                                                    input('Diamond City Merchant: Nice doin\' business with ya son!'+
                                                                          '\n(SYSTEM: Press enter to continue.) ')
                                                                else:
                                                                    input('SYSTEM: You\'ve already bought the T-60 Power Armor.'+
                                                                          '\nPress enter to continue.)')
                                                        else:
                                                            input('Diamond City Merchant: Ok friend. Maybe some other time.'+
                                                                  '\n(SYSTEM: Press enter to continue.)')

                                                        

                                                        
                                                else:
                                                    # normally "thinking to self" has a variable and goes in the think_inventory list
                                                    # but this is an exception
                                                    input('Thinking to self: I\'d like to buy this T-60 power armor, but'+
                                                          '\nI\'ll need to buy a fusion core for it first: otherwise the armor'+
                                                          '\nwon\'t work.'+
                                                          '\n(SYSTEM: Press enter to continue.)')

                                            elif choice4 == FUSIONCORE:
                                                #are_you_sure7 confirms the player\'s purchase
                                                are_you_sure7 = str(input('Diamond City Merchant: Are ya sure ya'+
                                                                           '\nwant to buy a Fusion Core for $1100?'+
                                                                           '\nSYSTEM: enter yes to buy or no to quit'+
                                                                           '\n(use lowercase): '))
                                                print()
                                                if are_you_sure7 == str('yes'):
                                                    if MONEY < FUSION_CORE2_VALUE:
                                                        input('Diamond City Merchant: Come back when ya have'+
                                                              '\n$1100 or more friend.'+
                                                              '\nSYSTEM: Press enter to continue. ')
                                                        print()
                                                        print()
                                                    else:
                                                        if FUSION_CORE2 not in prevent_exploit2:
                                                            prevent_exploit2.append(FUSION_CORE2)
                                                            character_inventory4.append(FUSION_CORE2)
                                                            MONEY -= FUSION_CORE2_VALUE
                                                            input('Diamond City Merchant: Thank ya for yer'+
                                                                  '\npurchase friend! (SYSTEM: A brand new'+
                                                                  '\nFusion Core has been added to your inventory.'+
                                                                  '\nPress enter to continue.)')
                                                        else:
                                                            input('Diamond City Merchant: Sorry friend, ya won\'t be able'+
                                                                  '\nto get another Fusion Core out of me. The one I\'ve'+
                                                                  '\nsold ya already was all I had in stock.'+
                                                                  '\n(SYSTEM: Press enter to continue.)')
                                                else:
                                                    input('Diamond City Merchant: Ok friend. Maybe some other time.'+
                                                          '\n(SYSTEM: Press enter to continue.)')
                                    elif choice3 == SELL:
                                        choice5 = 0
                                        RING_10 = 1
                                        RING_20 = 2
                                        DEATHCLAWMEAT = 3
                                        QUIT5 = 4
                                        while choice5 != QUIT5:
                                            if RING1 or RING2 in character_inventory or DEATHCLAW_MEAT in character_inventory3:
                                                if TALKED_TO_NICK in quest_inventory:
                                                    print()
                                                    print()
                                                    print('Diamond City Merchant (selling)')
                                                    print('-------------------------------')
                                                    print()
                                                    print('SYSTEM: These are items in your'+
                                                          '\ninventory that you can sell.'+
                                                          '\nYou have showed the merchant'+
                                                          '\nall that you have and he is only'+
                                                          '\ninterested in the following items.')
                                                    print()
                                                    print('1. Nora\'s Wedding Ring (Your Wife\'s wedding ring) ($1250)'+
                                                          '\n2. Your Wedding Ring ($1250)'+
                                                          '\n3. DeathClaw Meat ($500?)'+
                                                          '\n4 Quit')
                                                    print()
                                                    choice5 = int(input('Enter your choice: '))
                                                    print()
                                                    while choice5 < RING_10 or choice5 > QUIT5:
                                                        choice5 = int(input('Enter a valid choice: '))
                                                        print()
                                                    if choice5 == RING_10:
                                                        if RING1 in character_inventory:
                                                            character_inventory.remove(RING1)
                                                            MONEY += RING1_VALUE
                                                            input('Diamond City Merchant: Nice doing business with ya.'+
                                                                  '\n(SYSTEM: You sold Nora\'s ((your wife)) wedding ring'+
                                                                  '\nfor $1250. Press enter to continue.)')
                                                        else:
                                                            input('SYSTEM: Error! You have either sold this item'+
                                                                  '\nalready or it is not in your inventory'+
                                                                  '\nPress enter to continue. ')
                                                    elif choice5 == RING_20:
                                                        if RING2 in character_inventory:
                                                            character_inventory.remove(RING2)
                                                            MONEY += RING2_VALUE
                                                            input('Diamond City Merchant: Nice doing business with ya.'+
                                                                    '\n(SYSTEM: You sold your wedding ring for $1250.'+
                                                                    '\nPress enter to continue.)')
                                                        else:
                                                            input('SYSTEM: Error! You have either sold this item'+
                                                                  '\nalready or it is not in your inventory'+
                                                                  '\nPress enter to continue. ')
                                                    elif choice5 == DEATHCLAWMEAT:
                                                        if DEATHCLAW_MEAT in character_inventory3:
                                                            character_inventory3.remove(DEATHCLAW_MEAT)
                                                            MONEY += DEATH_CLAW_MEAT_VALUE
                                                            input('Diamond City Merchant: Nice doing business with ya.'+
                                                                  '\n(SYSTEM: You sold DeathClaw Meat for $500. Press enter'+
                                                                  '\nto continue.)')
                                                        else:
                                                            input('SYSTEM: Error! You have either sold this item'+
                                                                  '\nalready or it is not in your inventory'+
                                                                  '\nPress enter to continue. ')
                                                else:
                                                    input('Diamond City Merchant: Ya gonna have to come back later. I\'m'+
                                                          '\nnot ready to buy from my customers yet. I usually do so a few'+
                                                          '\nhours before I close. Maybe ya can walk around the city and'+
                                                          '\ncome back later? Ya seem like a newcomer. Go explore the city'+
                                                          '\na bit, eh?. I should be open by the time you come back.'+
                                                          '\n(SYSTEM: Press enter to continue.)')
                                                    print()
                                                    choice5 = int(input('Enter 4 to exit: '))
                                                    print()
                                                    while choice5 < 4 or choice5 > 4:
                                                        choice5 = int(input('You must enter 4 to exit: '))
                                                        print()
                                            else:
                                                print()
                                                input('Diamond City Merchant: Sorry lad. My customers have already'+
                                                      '\nsold me a ton of stuff last week. I\'m not interested in'+
                                                      '\nbuying anything off ya right now. But if ya come back here'+
                                                      '\nwith some rings and/or meat I\'ll buy those. The ladies love'+
                                                      '\ntheir jewelry and the families gotta eat: those are some things'+
                                                      '\nI can resell. So, come back with those things and I\'ll definitely'+
                                                      '\nbuy from ya.'+
                                                      '\n(SYSTEM: Press enter to continue.)')
                                                print()
                                                input('You: Sure thing!'+
                                                      '\n(SYSTEM: Press enter to continue.)')
                                                print()
                                                print()
                                                input('Diamond City Merchant: That\'s the spirit! Thanks for understandin\'.'+
                                                      '\n(SYSTEM: Press enter to continue.)')
                                                print()
                                                choice5 = int(input('Enter 4 to exit: '))
                                                print()
                                                while choice5 < 4 or choice5 > 4:
                                                    choice5 = int(input('You must enter 4 to exit: '))
                                                    print()

                            elif choice2 == MAFIA_BOSS:
                                if ENCOUNTERED_MAFIA not in quest_inventory:
                                    quest_inventory.append(ENCOUNTERED_MAFIA)
                                    input('SYSTEM: As you walk through Diamond City, you notice that there'+
                                          '\n\nhave been men in black three piece suits and trilby hats'+
                                          '\n\nglancing and even staring at you from a distance. Though you'+
                                          '\n\ncan\'t really see their faces, as they hide their faces under'+
                                          '\n\nthe brims of their trilby hats. As you continue walking, three'+
                                          '\n\nmen pull you to the side in an alley. It took three of them'+
                                          '\n\nbecause you are wearing Power Armor: a steel suit.'+
                                          '\n\n(Press enter to continue.)')
                                    print()
                                    print()
                                    input('Man in red pinstripe suit and red trilby hat: Nice of you\'s to join the'+
                                          '\n\nfour of us amico. Me and my three sons here have taken an interest'+
                                          '\n\nin you\'s since you\'s came into this city. Now,--'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('You: I don\'t care who you losers are; I have things to tend to, so'+
                                          '\n\ntry and intimidate someone else. I\'m assuming you\'re the boss'+
                                          '\n\nman wearing that red pinstripe suit: all of your goonies wear'+
                                          '\n\nblack suits. What do you guys want?'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('Man #1 in black suit and trilby hat: Ya watch how ya talk to the'+
                                          '\n\nFather, ya punk. He\'s here the most respectable man in all-uh'+
                                          '\n\nDiamen\' City.'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('Man #2 in black suit and trilby hat: Betta yet, keep ya tramp shut when'+
                                          '\n\nthe big man is talkin\', ya heard? Less you\'s want trouble.'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('Man #3 in black suit and trilby hat: *blows cigar smoke on the helmet'+
                                          '\n\nof your armor* You\'s in cahoots with us now kid: there ain\'t no going'+
                                          '\n\nback. You\'s was on the nose when ya said, "I have things to tend to".'+
                                          '\n\nStick around and you\'s gonna find out real quick ya got things to tend to.'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('Man in red pinstriped suit and red tribly hat: Enough children! Don\'t make'+
                                          '\n\nthe Father flip his wig! Look kid, the name\'s Smitty. That\'s-uh Father'+
                                          '\n\nSmitty to you. Don\'t be crusin\' for a brusin\' wit us now. I\'ll have you\'s'+
                                          '\n\nknow that there\'s-uh high powered sniper aiming his barrel at you right now.'+
                                          '\n\nBut it\'s no ordinary sniper. We managed to make a deal of sorts with the'+
                                          '\n\nInstitute to get this sniper. It shoots lasers and it\'s-uh, "highly concentrated'+
                                          '\n\nshot" as they told us. Even though you\'s a big metal man, that shot will go right'+
                                          '\n\nthorugh you\'s metal dome and put you\'s to sleep. So I suggest you\'s to listen up.'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('SYSTEM: You realize there is a red laser pointer on the side of your armor\'s helmet.'+
                                          '\n\nYou decide to listen to the men before you. If what he said about this sniper is true,'+
                                          '\n\nthen you\'ve decided it\'s better to play this safe than sorry.'+
                                          '\n\n(Press enter to continue.)')
                                    print()
                                    print()
                                    input('Father Smitty: If you\'s haven\'t figured by now: We\'re the Diamond City Mafia. The biggest'+
                                          '\n\nMafia in the CommonWealth. I don\'t care what you have to tend to son, all that-a stuff'+
                                          '\n\nyou was talkin\' earlier was gobbledygook. Cause you\'s workin\' for me now. There\'s a small'+
                                          '\n\ntime mafia in a nearby town called Goodneighbor. They call themselves the Goodneighbor Mafia.'+
                                          '\n\nWe\'s making a deal of sorts. Ya know: a "drink deal". Drinks aren\'t illegal around these'+
                                          '\n\nparts, but in these cities you\'s need an official license to sell it. But we don\'t play'+
                                          '\n\nby a rich politician\'s rules. Nor are we making this a clean deal with the Goodneighbor'+
                                          '\n\nMafia. We\'re wiping them\'s off\'s the maps if you speak my language. You\'s gonna be the'+
                                          '\n\none to do it. Should you\'s refuse: you\'s will die by me. You\'s might not right away. But'+
                                          '\n\nI will find you\'s. And that, "high concentrated" laser sniper that\'s aiming at you\'s now: will'+
                                          '\n\nbe the cause of your death. Nobody can hide from the Diamond City Mafia.'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('You: Why do I have to be the one to rip off a "drink deal" you set up?'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('Father Smitty: Have you\'s seen yourself in the mirror son? You\'s wearing military-grade steel armor:'+
                                          '\n\nPower Armor. Not many lads can work those these days. So, I am glad you\'s came to this city to'+
                                          '\n\nvolunteer you\'s services to the Father. The deal happens at midnight tonight. You\'s gonna go'+
                                          '\n\nthere with one of my sons here and about 82 more of my sons: we have a lotta drinks to "sell".'+
                                          '\n\nYou\'s all gonna show the Goodneighbor Mafia that the stuff is legit. Then blast em\' all and'+
                                          '\n\ntake their lettuce. It shoudln\'t be a problem with you\'s wearing that armor. It\'s a win-win for'+
                                          '\n\nme because they are offering 50,000 in lettuce. AND I get to keep my drinks and sell them some'+
                                          '\n\nother time. So, I\'m making about 100,000 in lettuce in the long term. So, this deal can\'t go'+
                                          '\n\nbelly up kid. Make the Father proud. But worry not. I\'m not making you\'s my son. You\'s just a'+
                                          '\n\n"temporary son". But the oath must still happen.'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('You: Look I really don\'t--'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('Father Smitty: --Wanna die? You\'s really don\'t wanna die? That\'s good to know. Then you\'s'+
                                          '\n\nWILL make this happen for the Father. You\'s do this for me and my 517 sons, and we\'ll'+
                                          '\n\nbe cooking gas in this Mafia business. You\'s do this one time thing for the Father and'+
                                          '\n\nyou\'s gonna be off the hook. We\'re a mafia....sure. But we don\'t joke about being men'+
                                          '\n\nof our word, being loyal, being respectable. I\'m not yanking ya leg son. In fact, I got\'s'+
                                          '\n\n6000 in lettuce for you\'s on the table WHEN you\'s do this, because there is no IF. You\'s'+
                                          '\n\nwill do this. So what will it be son? Life or Death?'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('SYSTEM: You still notice one of Father Smitty\'s sons aiming a Institute laser sniper at you.'+
                                          '\n\nThat Institute laser sniper is so strong that is can burst through your power armor in one'+
                                          '\n\nshot. They are ready to end you in the blink of an eye should you refuse them. Even if you'+
                                          '\n\nsomehow got away you know that Father Smitty has 517 "sons" in total: a small army. You give'+
                                          '\n\nin knowing that nothing good is coming from refusing them.'+
                                          '\n\n(Press enter to continue.)')
                                    print()
                                    print()
                                    input('You: *siggggghhhhs* Ok. I accept. You better at least give me that "6000 lettuce". I\'m'+
                                          '\n\nassuming your talking about money. Pay it up when I finish this. I\'m not excited over'+
                                          '\n\nhaving to kill others: in fact I have PTSD from my war days. But I guess it\'s kill or'+
                                          '\n\nbe killed for me right now.'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('Father Smitty: Now ya got\'s you\'s head screwed on right! That\'s what the Father likes to hear!'+
                                          '\n\nBut you\'s must pledge your temporary loyalty to the Father. An initiation of sorts. Come to our'+
                                          '\n\nhideout in one hour: it\'s on 147 Jewel street. The password to get in is: SwordFish. Remember'+
                                          '\n\nit kid: for your sake. You\'s can\'t get it wrong and live another 24 hours after that. No matter'+
                                          '\n\nwho you\'s are or what promises we\'ve made to one another. I\'ll see you soon: leaving my hideout'+
                                          '\n\nmaking me richer than I already am, or dead at my feet for not showing up and showing out.'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('SYSTEM: You all part your separate ways after you "volunteered" your services. You then go to the'+
                                          '\n\nlocation given to you just an hour earlier. You knock on the door.'+
                                          '\n\n(Press enter to continue.)')
                                    print()
                                    print()
                                    input('Man in three piece suit and trilby hat at door: What\'s the password?'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('You: SwordFish.'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('SYSTEM: You are allowed into the hideout: being escorted of course. You notice men in black three piece'+
                                          '\n\nsuits and trilby hats and women everywhere. There is lots of smoking, drinking, card playing, pool'+
                                          '\n\nplaying, arm wrestling, instrument playing : especially the sax, and dancing going on. It\'s very'+
                                          '\n\nloud on the inside, but surprisingly you wouldn\'t be able to tell from the outside. You\'d think'+
                                          '\n\nit was more of some sort of casino than a Mafia hideout. Minus all the armed men glancing at you'+
                                          '\n\nfrom under the brim\'s of their hats and nodding at you. You finally meet the Father in the back.'+
                                          '\n\nHe is accompanied by 25+ plus men in one room. They are all armed. You can\'t see their faces because'+
                                          '\n\nthey all are using the brims of thier hats to hide their faces.'+
                                          '\n\n(Press enter to continue.)')
                                    print()
                                    print()
                                    input('Man # 3 in trilby hat: You\'s again? *blows cigar smoke in air* I was hoping you\'s wouldn\'t come'+
                                          '\n\nso we could do you in. You had some nerve earlier talking to the Father like that.'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('SYSTEM: You notice Father Smitty sitting at the his "boss desk". It is very lavish.'+
                                          '\n\n(Press enter to continue.)')
                                    print()
                                    print()
                                    input('Father Smitty: *slams hand on desk* THAT\'S ENOUGH KENNETH! *speaks fast* I\'ve had enough'+
                                          '\n\nof you and that motor mouth an hour earlier when we met our amico here! You\'s keep'+
                                          '\n\ntalkin\' bout the man that\'s making us big lettuce and somebody\'s gonna get did in'+
                                          '\n\nfor sure: *points at Kenneth* YOU!.'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('Man # 3 in trilby hat (Kenneth): *bows down on one knee and has a lowered head*'+
                                          '\n\nPlease forgive me for my insubordination Father. You\'s right, I need to stop'+
                                          '\n\nrunnin\' my motor mouth. Thank you\'s for putting me in check. I wouldn\'t wanna'+
                                          '\n\ndisappoint the man that gave me a chance coming from a troubled life....'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('Father Smitty: Chiaccerione. Chiudere il becco. Don\'t get all touchy in a'+
                                          '\n\nroom full of men. I\'ll forgive you\'s sin son. But remain in that bowed'+
                                          '\n\nposition and kiss your Father\'s ring on his right hand for forgiveness.'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('SYSTEM: Kenneth remains on one knee and kisses Father Smitty\'s ring'+
                                          '\n\non his right hand for forgiveness.'+
                                          '\n\n(Press enter to continue.)')
                                    print()
                                    print()
                                    input('Father Smitty: Someone give me a cigar. *One of his "sons" gives him a cigar*.'+
                                          '\n\nNow light it up for me my son. *His "son" lights up his cigar for him*.'+
                                          '\n\nOk amico. Friend. *blows smoke in air*. I\'m sending you\'s with 82 of my'+
                                          '\n\nsons. Kenneth here included. Kenneth is the lead man. Now. So Diamond'+
                                          '\n\nCity security don\'t get suspicious of us, I\'ve already sent 82 of my'+
                                          '\n\nsons out of the city. Don\'t ask how. It\'s simple actually. This deal'+
                                          '\n\nhas been planned for weeks. I\'ve been sending my men out one at a time.'+
                                          '\n\nAnd you amico, came to this city at the last minute volunteering your'+
                                          '\n\nservices. Sealing the deal. Guaranteeing us success in that power armor'+
                                          '\n\nyou\'s wearing. Now you\'s and Kenneth go to the deal spot and my other 82'+
                                          '\n\nmen will be there already with the goods. Come back successful amico.'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('Kenneth: Magari, Father. Let\'s hope he is successful: for his sake. Amico come'+
                                          '\n\nwith me. Failing is not an option. It is pazzo to even consider: for me anyway.'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('Father Smitty: Aspettare, Kenneth. Our amico must become a temporary son first.'+
                                          '\n\nCome and bow down to me on one knee and kiss your Father\'s ring my soon'+
                                          '\n\nto be temporary child. Deny me....and you deny your very life....'+
                                          '\n\n(SYSTEM: Press enter to continue.)')
                                    print()
                                    print()
                                    input('SYSTEM: The room grows silent, and the men in the room glare at you from under'+
                                          '\n\nthe brims of their trilby hats. They tense up like they are ready to shoot'+
                                          '\n\nat you if you refuse the Father. Their ordinary automatic tommy guns wouldn\'t'+
                                          '\n\nbe able to penetrate your power armor. But what you fear is the man who isn\'t'+
                                          '\n\ntensed up. He is on the other side of the room pointing that Instiute laser'+
                                          '\n\nsniper at you: the one with a "concentrated shot" that can pierce through power'+
                                          '\n\narmor in one hit. You have no choice. You take off your power armor helmet, bend'+
                                          '\n\non one knee, and kiss the Father\'s ring on his right hand. You\'ll do anything'+
                                          '\n\nto find your son: something you can\'t do if you die in this room because you'+
                                          '\n\nchose to be stubborn. The room burst in everyone applauding after you become a'+
                                          '\n\n"temporary son". You put your power armor helmet back on.'+
                                          '\n\n(Press enter to continue.)')
                                    print()
                                    print()
                                    input('Father Smitty: Bene. You are now my temporary son. After you complete your mission,'+
                                          '\n\nreport to me and I will pay you your 6000 lettuce cuts. Then you will no longer'+
                                          '\n\nbe my son. Go on. You and Kenneth.'+
                                          '\n\n(Press enter to continue.)')
                                    print()
                                    print()
                                    input('SYSTEM: You and Kenneth arrive at the "drink deal". There you find 82 of Father Smitty\'s'+
                                          '\n\n"sons" awaiting your arrival. They have the "drinks" that you are going to "sell".'+
                                          '\n\nIt has just struck midnight. It is raining and thundering very hard. The ground has'+
                                          '\n\nbecome muddy. The Goodneighbor mafia arrives. You show them the drinks.'+
                                          '\n\nThey believe it to be legit so they hand over the $50,000. But you look back at Kenneth'+
                                          '\n\nand the others and yell what Kenneth told you to yell as a signal, "BENE!". A mini war'+
                                          '\n\nbreaks out. Guns are blazing left and right. You took the Goodneighbor Mafia\'s money'+
                                          '\n\nwithout giving them their "drinks". You are not affected by the bullets they shoot at you'+
                                          '\n\nbecause you are wearing power armor. You finish off most of them while the 83 of the Diamond'+
                                          '\n\nCity Mafia: including Kenneth, support you from a good distance behind you.'+
                                          '\n\n(Press enter to continue.)')
                                    print()
                                    print()
                                    input('SYSTEM: You and everyone else go back to Father Smitty\'s hideout with the $50,000'+
                                          '\n\nyou stole and the drinks that are worth $50,000 that you did not sell. Father'+
                                          '\n\nSmitty yells, "BENE!, BENE!, BENE!. He gives you the $6000 that he promised and'+
                                          '\n\ninsist that you have a celebration with the mafia in their hideout. You refused,'+
                                          '\n\nbut of course after being threatend: found yourself celebrating. Father Smitty'+
                                          '\n\ninsisted you, "let loose". You thought you could just sit around until it was'+
                                          '\n\nover. But Father Smitty threatend you again. You get out of your power armor and'+
                                          '\n\nhit the dance floor like your life depends on it: because it does. You even have'+
                                          '\n\nto drink heavy, gamble (you lost some money but got back what you lost), and play'+
                                          '\n\npool. You eventually pass out and find yourself awoke on the other side of Diamond'+
                                          '\n\nCity late in the morning: late in the morning because you were partying in the early'+
                                          '\n\npart of the morning after the "drink deal". You are in some small alley. They put'+
                                          '\n\nyou out and somehow carried your power armor suit to the other side of the city:'+
                                          '\n\nbecause it is right beside you. All of your other belongings are with you as well.'+
                                          '\n\nYou find a note in your pocket that says: "You\'s are no longer my son. Don\'t come'+
                                          '\n\nback to the hideout. The password is not SwordFish anymore for security reasons.'+
                                          '\n\nYou\'s understand how it is. You\'s did bene amico! I am a respectable man and keep my'+
                                          '\n\nword. I could have taken the money from you\'s, but I let you\'s have the 6000 lettuce.'+
                                          '\n\nIt\'s in you\'s right pocket. Keep you\'s lips zipped or you\'s gonna disappear amico.'+
                                          '\n\nArrivederci!- Father Smitty.'+
                                          '\n\n(Press enter to continue.)')
                                    MONEY += MAFIA_MONEY_VALUE
                                    print()
                                    print()
                                    input('SYSTEM: You get back in your power armor and continue on as if nothing ever happened.'+
                                          '\n\n$6000 has been added to your inventory.'+
                                          '\n\n(Press enter to continue.)')

                                else:
                                    input('SYSTEM: You have already encountered the Diamond City Mafia.'+
                                          '\n\n(Press enter to continue.)')

                            elif choice2 == BOUNTY_POSTER:
                                if BOUNTY_QUEST not in quest_inventory:
                                    quest_inventory.append(BOUNTY_QUEST)
                                    input('SYSTEM: As you walk through Diamond City, you notice a bounty poster.'+
                                          '\n\nBut it is not a poster for an individual: it is for Feral Ghouls.'+
                                          '\n\nIt says at the bottom of the poster that Feral Ghouls were once'+
                                          '\n\nnormal everyday persons. However, due to too much radiation exposure:'+
                                          '\n\ntheir flesh starts to rot and they lose their minds: attacking anyone'+
                                          '\n\nin sight. The poster also explains that Feral Ghoul\'s physical combat'+
                                          '\n\nabilities are beyond a normal humans: the poster warns that you should'+
                                          '\n\nbe a capable individual to accept this bounty hunt. It also explains that'+
                                          '\n\nthe reason for getting rid of these Feral Ghouls is so that the roads of'+
                                          '\n\nthe CommonWealth will be safer: "this is for the safety of all those'+
                                          '\n\ntravelling the CommonWealth"--it explains.'+
                                          '\n\n(Press enter to continue.)')
                                    print()
                                    print()
                                    input('SYSTEM: The poster gives the location of these ghouls: the Internal Revenue Service building'+
                                          '\n\n(IRS). Apparently there are about 23 ghouls there. The reward for accepting this bounty'+
                                          '\n\nis $2000. The poster says that to claim the reward you have to wait on a Diamond City'+
                                          '\n\nofficial to go and check to be sure that the Feral Ghouls are dead to receive your pay.'+
                                          '\n\nYou decide you will accept this bounty.'+
                                          '\n\n(Press enter to continue.)')
                                    print()
                                    print()
                                    input('SYSTEM: After leaving Diamond City hours ago: you finally arrive at the Internal Revenue'+
                                          '\n\nService building (IRS). The ghouls are laying on the ground as if they are dead persons.'+
                                          '\n\nBut as you curiously approach them: they pop up off of the ground and start charging at'+
                                          '\n\nyou. All 23 of them. You note that they are very physically strong, but they can do nothing'+
                                          '\n\nto you inside of your power armor. You finish all 23 of them off feeling sad at heart: knowing'+
                                          '\n\nthey were once human, knowing that it is the fault of people from your time period that the'+
                                          '\n\nworld has come to what it currently is. These 23 Feral Ghoul\'s didn\'t want to become like this.'+
                                          '\n\nBut they were simply exposed to too much radiation that foolish people from your generation'+
                                          '\n\ncaused to happen by dropping and shooting nuclear weapons on and at one another. But you know'+
                                          '\n\nthat finishing these feral ghouls off will only make travelling the CommonWealth safer for others.'+
                                          '\n\n(Press enter to continue.)')
                                    print()
                                    print()
                                    input('SYSTEM: You travel and take the elevator to the staff room of the baseball'+
                                          '\n\nstadium, or, "Diamond City" as it is called. There you speak to Diamond'+
                                          '\n\nCity officials about you completing the bounty hunt. The officials decided'+
                                          '\n\nthey would go check to see if you really did it and will give you the money'+
                                          '\n\nthe next day. However they can tell by the blood on your armor that you'+
                                          '\n\nfought the Feral Ghouls and they take your word. You clean your power armor'
                                          '\n\nwith some cleaning supplies for steel that the city officials offered you.'+
                                          '\n\nThey then give you the $2000 dollars and you go about your way. But they did'+
                                          '\n\nask you to please take down the poster in Diamond City so others could know'+
                                          '\n\nthis job is already completed. You do it and go about your way.'+
                                          '\n\n(Press enter to continue.)')
                                    print()
                                    print()
                                    MONEY += BOUNTY_POSTER_VALUE
                                    input('SYSTEM: $2000 has been added to your inventory'+
                                          '\n\n(Press enter to continue.)')

                                else:
                                    input('SYSTEM: You have already collected the bounty for the Feral Ghouls.'+
                                          '\n\n(Press enter to continue.)')
                                    

                                                    
                    else:
                        input('SYSTEM: You figure that you\'ll need some edible food'
                              '\n\nand to not be hungry on the way to Diamond City'+
                              '\n\n. You have no idea how far away it is from where'+
                              '\n\nyou currently are. You\'ll have to look for a'+
                              '\n\nsource of edible food. But once you know your'+
                              '\n\nway it won\'t take as long, then maybe you won\'t'+
                              '\n\nneed food the next time you travel.'+
                              '\n\nPress enter to contine. ')

                else:
                    input('SYSTEM: You figure that you\'ll need a some way'+
                          '\n\nto hydrate before moving forward. You have no'+
                          '\n\nidea how far Diamond City is from where you'+
                          '\n\ncurrently are. You\'ll have to look for some'+
                          '\n\npotable water. But once you know your'+
                          '\n\nway it won\'t take as long, then maybe you won\'t'+
                          '\n\nneed water the next time you travel.'+
                          '\n\nPress enter to contine. ')

            else:
                input('SYSTEM: You will need ammunition for your assualt rifle'+
                      '\n\nbefore traveling to Diamond City. With all that you'+
                      '\n\nhave seen so far: you know good and well that it is'+
                      '\n\nin your best interest to have ammunition for your'+
                      '\n\nstrongest weapon yet.'+
                      '\n\nPress enter to continue. ')

        else:
            input('SYSTEM: You will need a stronger weapon before traveling'+
                  '\n\nto Diamond City. With all that you have seen so far:'+
                  '\n\nYou\'re not so sure that you could make it any further'+
                  '\n\nwith the things that you currently have.'+
                  '\n\nPress enter to continue. ')

    else:
        input('SYSTEM: You will need stronger armor before you travel'+
              '\n\nto Diamond City. With all that you have seen so far:'+
              '\n\nYou\'re not sure if you could make it any further'+
              '\n\nwith the things that you currently have.'+
              '\n\nPress enter to continue. ')


def fort_hagen(character_inventory3, character_inventory4,
               quest_inventory):
    if TALKED_TO_NICK in quest_inventory:
        if WEAPON3 and WEAPON4 in character_inventory3:
            if ARMOR3 in character_inventory3:
                if FIRST_AID3 in character_inventory4:
                    if PURSUE_KELLOG not in quest_inventory:
                        quest_inventory.append(PURSUE_KELLOG)
                        input('SYSTEM: You travel to Fort Hagen in Pursuit of Kellog the synth Institute Courser.'+
                              '\n\nYou are after him because he can lead you to your kidnapped son, Shaun:'+
                              '\n\nwillingly or not. According to Nick Valentine the detective: Kellog is FAR'+
                              '\n\nstronger than all other synth Institute Coursers, all other synth Institute '+
                              '\n\n coursers are FAR stronger than regular synths like Nick Valentine, and'+
                              '\n\nregular synths like Nick Valentine are FAR stronger than a human such as'+
                              '\n\nyourself. Kellog is at the top of the food chain and you are at the bottom.'+
                              '\n\nYour T-60 power armor should give you an edge, but you know nothing is for'+
                              '\n\ncertain.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: You arrive at Fort Hagen and notice automated machinegun turrets outside'+
                              '\n\nof the fort: just as Nick Valentine mentioned. You use your scoped .50 cal'+
                              '\n\nsniper to destroy all of them from a great distance. You then go to the fort'+
                              '\n\nbut are blocked entry because of barricaded doors. You bust the doors down by'+
                              '\n\nfirst walking 50 yards backwards, then you charge the doors in your T-60 power'+
                              '\n\narmor to bust them down and make entry. You hear an intercom come on that can'+
                              '\n\nbe heard throughout the entire Fort Hagen building. The speaker is Kellog the'+
                              '\n\nsynth Institute Courser...'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('Kellog on Fort Hagen intercom: *feedback noise* You who are trespassing. You'+
                              '\n\nare interfering with Institute operations. You have no clearance to enter'+
                              '\n\nthis place.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: You remember being at Fort Hagen 210+ years ago when you were signing up'+
                              '\n\nfor the military: just as you told Nick Valentine. You remember that this'+
                              '\n\nplace does not go upstairs, but goes downstairs. It goes deep into the ground'
                              '\n\nrather than reaching higher into the air. You recall that there was a bunker'+
                              '\n\nunderdround where lots of different types of ammunitions were stored. You figure'+
                              '\n\nKellog has stationed himself there and you head to the elevators.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: You try to use the elevators to go to the bottom floor: the ammunitions bunker,'+
                              '\n\nbut it seems Kellog has shut off all the power to the elevators to prevent you from'+
                              '\n\nreaching him.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('Kellog on Fort Hagen intercom: *feedback noise* Stranger. I am doing this for your'+
                              '\n\nbenefit. Leave this place: it is in your best interest.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: You wonder how Kellog knows where you are and that you are here. You take a'+
                              'look around and see no cameras. But they have to be here, so there must be hidden'+
                              '\n\ncameras all over the fort. You decide to take the stairs. It shouldn\'t take'+
                              '\n\nlong, but you do encounter automated machine gun turrets that attack you as you'+
                              '\n\ngo down the many flights of stairs. Though they do nothing to you while wearing'+
                              '\n\nT-60 power armor.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('Kellog on Fort Hagen intercom: *feedback noise* I will admit: I do remember you.'+
                              '\n\nI am the one who killed your wife and kidnapped your son. I get it human. You'+
                              '\n\nare out seeking revenge..........No.....not only revenge. You must also be'+
                              '\n\nseeking a way to get your son back. You are seeking the Institute itself.'+
                              '\n\n.........I guess you see me as the bridge to get to your destination.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: You continue to ignore Kellog. You came here for the sake of your family.'+
                              '\n\nYour family that was destroyed by a cold-hearted machine: someone who disguises'+
                              '\n\nthemselves as human. Someone who\'s very soul was manufactured in the confines'+
                              '\n\nof a laboratory. You having nothing against synths: you like Nick Valentine after'+
                              '\n\nall. But this synth. Kellog the synth Courser: you feel the hate in your heart'+
                              '\n\ngrowing for him by the milli-second.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('Kellog on Fort Hagen intercom: *feedback noise* Your death is certain should you choose'+
                              '\n\nto remain insubordinate. I truly am trying to lead you away from me for your own'+
                              '\n\nbenefit. Fighting me is no option. Only death by me is certain should you continue'+
                              '\n\napproaching me with a fight in mind. I was created by the Institute: a synth. Far'+
                              '\n\nsuperior than any human in mind and body. Then I became an Institute courser: I'+
                              '\n\nendured rigorous training, killing my own synth brethern in the process. At that point'+
                              '\n\nI was stronger than not only humans, but also regular synths: who are FAR stronger'+
                              '\n\nthan humans to begin with. Recently I have become the strongest Institute courser'+
                              '\n\nthe Insitute has. You do the math. In terms of strength: there is me, then other'+
                              '\n\nInstitute coursers, then regular synths, and then there is you, a weak human. Turn'+
                              '\n\naround or die you fool.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: After going down even more flights of stairs and destroying more automated'+
                              '\n\nmachine gun turrets: you finally arrive at the steel door Kellog is behind.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('You (speaking to T-60 Power Armor Computer: Power armor computer. Report.'+
                              '\n\n(SYSTEM: Press enter to continue.')
                        print()
                        print()
                        input('T-60 Power Armor Computer speaking (robotically):'+
                              '\n\nThe T-45 power armor can endure multiple tank shells with mild damage. This'+
                              '\n\nT-60 Power Armor suit can take on many explosives and/or bullets from a'+
                              '\n\nfighter jet with mild damage. It is much more endurable. Summary of suit:'+
                              '\n\ngiven. Systems: already initialized. Power Armor Combat readiness grade: A+.'+
                              '\n\nPower Armor hull integrity: 100%. Emergency Attack Mode: Available. Emergency'+
                              '\n\nAttack Mode Overdrive: Available, but warning! This is very dangerous to'+
                              '\n\nuse. Emergency Attack Mode Overdrive has a 100% chance of the suit\'s fusion'+
                              '\n\ncore exploding due to the power strain. This will result in the entire suit'+
                              '\n\nbursting out in explosive flames from the inside out: with you the user inside'+
                              '\n\nof it. Emergency Attack Mode Overdrive stresses the fusion core 3 times more'+
                              '\n\nthan Emergency Attack Mode: this is why this happens.'+
                              '\n\n(SYSTEM: Press enter to continue.')
                        print()
                        print()
                        input('You: Ok good to know. But computer....I need you to have Emergency Attack Mode'+
                              '\n\nand Emergency Attack Mode Overdrive on standby.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('T-60 Power Armor Computer speaking (robotically): Negative. No enemies'+
                              '\n\ndetected in the area. This will not be necessary as these modes only'+
                              '\n\nstrain the--'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('You: COMPUTER! Shut up and listen to me! There is a "man" behind this door'+
                              '\n\nwith unbelieveable combat capabilities. The protection of my life is'+
                              '\n\nyour number one task is it not? Then listen to me the user and put these'+
                              '\n\nmodes on standby right now, so that they will activate faster when I need'+
                              '\n\nthem!'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('T-60 Power Armor Computer speaking (robotically): Argument Valid. Request'+
                              '\n\naccepted. Emergency Attack Mode:...................on standby.'+
                              '\n\nEmergency Attack Mode Overdrive:....................on standby.'+
                              '\n\nEmergency Attack Mode drains the power source of the power armor (fusion'+
                              '\n\ncore) to increase your physical attack energy output by 3,257% and your'+
                              'n\nattack speed by 250% for 5 seconds. Emergency Attack Mode Overdrive WILL'+
                              '\n\ndestroy the fusion core by exploding it and the suit will explode in flames'+
                              '\n\nfrom the inside out with the user inside of it: unless they bail in time.'+
                              '\n\nEmergency Attack Mode Overdrive increase your physical attack energy output'+
                              '\n\nby 9,771% and your attack speed by 750% for 15 seconds.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Kellog on Fort Hagen intercom: *feedback noise* Are you done with your futile'+
                              '\n\nplanning? I will let you in. I will tear you limb from limb. You have been'+
                              '\n\nwarned many times and have pursued me like a fool. Your life is mine: I was'+
                              '\n\nmade for this, but you were born with mere flesh and bone. This is why you'+
                              '\n\nhide behind that T-60 Power Armor: fully encompassing your body in the'+
                              '\n\nstrongest steel armor you humans could create before that nuclear war 210+'+
                              '\n\nyears ago. Watch me rip it and you apart. There is no stopping me now.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('You: Computer. Going forward I will need you much. Do not let me down. Please.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('T-60 Power Armor Computer speaking (robotically): Fear detected. Affirmative:'+
                              '\n\nI will not let you down. Nor should you fear. Half the battle is already'+
                              '\n\nlost with the fear I detect within you as I scan your body. But whatever'+
                              '\n\nyou lack I am programmed to supply. Proceed with confidence.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: Kellog remotely opens the steel door and you enter the underground ammunitions'+
                              '\n\nbunker he was in this entire time. You slowly walk forward with your minigun.'+
                              '\n\nThere is an eerie silence as you see him across the other side of the room.'+
                              '\n\nThe two of you stare each other down. You are about 25 yards apart from each'+
                              '\n\nother. Kellog breaks the silence....'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: And here you are. The most persistent human I have ever seen.....and the'+
                              '\n\nmost foolish. You dare defy me? My sensors indicate your nerves are on the edge.'+
                              '\n\nA war veteran like you shaking in your boots? You have yet to see me fight, yet,'+
                              '\n\nmere stories you have heard of me are enough to have you on the verge of a'+
                              '\n\nnervous breakdown. But on the same token I admire your bravery. You are'+
                              '\n\nlooking at death itself in the face and yet you strut in here for the sake of'+
                              '\n\nyour lost family.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('You: Don\'t even bother trying to mock me. I have already told Nick Valentine that I am'+
                              '\n\nscared of you. But I also said to the pit with you. I SAID that one of us will be'+
                              '\n\nhanging our combat boots. I SAID it WILL NOT be me. I SAID that I WIll at least make'+
                              '\n\nyou bleed for destroying my family. I SAID to Nick Valentine that I will give him'+
                              '\n\nsomething to smile about when he visits Fort Hagen one day. What will he be smiling'+
                              '\n\nat? *points at Kellog* YOUR remains. I SAID that I will have you lead me to my son,'+
                              '\n\neither by you being cooperative or by forcing you. And what do you mean "You dare'+
                              '\n\ndefy me?" You keep speaking to me like that and Nick Valentine won\'t find any of'+
                              '\n\nyour remains.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: And here I was complementing your bravery. But I was mistaken. You just'+
                              '\n\nhide behind shallow words and steel suits that I can cut through like'+
                              '\n\ncard-board. You have said many things. But soon your lips will not be'+
                              '\n\nmoving. Soon I will end your pain. You have gone through much to get here...'+
                              '\n\nthat I am sure of. Inside of you there is a longing for your son. The boy'+
                              '\n\nthat your wife birthed. You touch him again....and you not only have him...'+
                              '\n\nbut you believe that you will be somehow connected to your wife as well again.'+
                              '\n\nYou envision yourself embracing your son: feeling his warmth. But you also feel'+
                              '\n\nthat you will feel your wife there with the two of you: reunited. You long for'+
                              '\n\nthe day that you can hold your son and cry your heart out as you reminisce of'+
                              '\n\nthe days of your youth in which you held his mother: your wife, in the same way.'+
                              '\n\nYou\'ll hold on to him like a man hanging on for his dear life that is about'+
                              '\n\nto lose his grip as he holds on to the edge of a cliff. A lost family.....no'+
                              '\n\n....a destroyed family: reunited. This is what you seek.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: However, THIS IS SOMETHING I WILL BE SURE DOES NOT HAPPEN!!! I WILL be the final'+
                              '\n\nhurdle that BREAKS you MENTALLY and PHYSICALLY!! I know that you have PTSD....or'+
                              '\n\nso YOU THINK you have PTSD. You will really have it after I\'m finished with you.'+
                              '\n\nYes. I have made up my mind. I won\'t kill you. I will torment you physically'+
                              '\n\nand mentally. I WILL be the physical embodiment of what you humans call the'+
                              '\n\nDevil!! No....I won\'t have you begging for mercy. I WILL HAVE YOU BEGGING FOR'+
                              '\n\nDEATH ITSELF!!! DON\'T YOU DARE worry about your son!! DON\'T come at me as some'+
                              '\n\nbroken father, some wandering soul, some empty individual, as someone who is'+
                              '\n\ndepressed, or as someone who has dissassociated themselves with reality because'+
                              '\n\nthey think they are broken! YOU BETTER come at me as a SOLDIER!! *Kellog points at you*'+
                              '\n\nABANDON YOUR HUMANITY!! Just for a little while longer! If you can do it you MIGHT'+
                              '\n\njust beat me. Since you have came this far I won\'t deny that it is possible. Anyone'+
                              '\n\nelse would have succumbed to this cruel post-apocalyptic world. But allow your'+
                              '\n\nfeelings to get in the way and you will be TORMENTED by ME. Now, where do you stand!?!?'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('You: You will be the physical embodiment of what we humans call the Devil!?!? *You point'+
                              '\n\nyour thumb at yourself* Then I will be the physical emodiment of the God he betrayed!!'+
                              '\n\nTHAT IS WHERE I STAND: ABOVE YOU!! YOU WILL LEAD ME TO THE VERY THING YOU DESTRYOED:'+
                              '\n\nMY FAMILY!'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: Kellog grabs his weapon that was strapped to his back. You notice that it'+
                              '\n\nis the "big white gun" that you described to Nick Valentine. Nick said that this'+
                              '\n\ngun shoots blue laser beams that literally melt the outside and insides of a human'+
                              '\n\nupon contact with the laser beam. You worry as you don\'t know how much damage it'+
                              '\n\nwill do to your T-60 Power Armor. But you do beat Kellog to the action. You spin up'+
                              '\n\nyour minigun and start blasting at Kellog.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: As your minigun bullets shower Kellog: he stands there staring you down. Your'+
                              '\n\nminigun is of no use to you: your only other weapon that could even possibly have'+
                              '\n\na chance at being effective is your Scoped .50 Cal Sniper. But that is for long'+
                              '\n\nranged shooting: Kellog is 25 yards in front of you. The bullets are quit literally'+
                              '\n\nbouncing off of his body. You continue to fire in desperation, but Kellog disappears'+
                              '\n\nin a blinding flash of blue light! You stop firing.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('You: COMPUTER! WHERE DID HE GO!?!?!?'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('T-60 Power Armor Computer speaking (robotically): The enemy has dematerialized'+
                              '\n\nand re-materialized! The enemy is behind you! Take evasive action!'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: Kellog has teleported behind you! It\'s just as Nick Valentine said.'+
                              '\n\nInstitute coursers such as Kellog have the ability to teleport at will!'+
                              '\n\nKellog comes from behind you and snatches your heavy minigun with one'+
                              '\n\nhand. He then proceeds to smash the heavy minigun over his leg: the'+
                              '\n\nminigun breaks in half! Kellog then kicks you as hard as he can: sending'+
                              '\n\nyou flying to the other side of the bunker! You crashed into a brick wall'+
                              '\n\nand most of it is now completely destroyed. Kellog is most definitely power-'+
                              '\n\nful. He managed to send you flying with one kick while wearing a steel'+
                              '\n\nsuit that weighs many tons. Nick Valentine\'s words echo through your head'+
                              '\n\nas you try to scramble to your feet: "The Institute calls them the ultimate'+
                              '\n\nfighting machines".'+
                              '\n\n(Press enter to continue.)')
                        if WEAPON4 in character_inventory3:
                            character_inventory3.remove(WEAPON4)
                            input('SYSTEM: Your minigun has been removed from your inventory.)'+
                                  '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('You: Dang! That was the only weapon I had that even had a real chance of harming'+
                              '\n\nhim.......It\'s ok. I\'m no stranger to physical combat.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        
                        print()
                        print()
                        input('Kellog: Giving yourself a prep talk? A bit late for that is it not? And what do'+
                              '\n\nyou mean, "I\'m no stranger to physical combat?" I have my weapon right here'+
                              '\n\nin my hands. Given the context of this situation: does it really seem to you'+
                              '\n\nthat we are about to have a mixed martial arts fight?'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('You: Shut up and fight me!'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: Have it your way then. That was a mere warm-up. Now let\'s really dance...'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: Kellog starts firing his gun at you that shoots blue laser beams. You start'+
                              '\n\nto panick realizing the damage that it can do. As the beams hit your armor in'+
                              '\n\nrapid succession: the T-60 Power Armor Computer warns you to take cover. Each'+
                              '\n\nshot puts a hole through your armor. You run behind a security fence to take'+
                              '\n\ncover.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('You: Computer! Report!'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('T-60 Power Armor Computer speaking (robotically): Power armor hull integrity: 52%.'+
                              '\n\nYou must not take another round of fire from the enemy\'s weapon or you will die.'+
                              '\n\nJust a few tens of his lasers did the following: put holes in the armor all over,'+
                              '\n\nand cut the power armor hull integrity by 48%. Suggested course of action: When'+
                              '\n\nenemy teleports again I will detect it. I am able to spot him faster than you. But'+
                              '\n\nstill I can not pick up his location instantly. However, when I do find him: I will'+
                              '\n\nautomatically activate Emergency Attack Mode. When this happens: You must act as fast'+
                              '\n\nas possible, or I will do so for you. Your physical attack energy output will increase'+
                              '\n\nby 3,257% and your attack speed by 250% for 5 seconds. Calculating......calculating..'+
                              '\n\n...This will not be enough to defeat the enemy. But such a sudden burst in power'+
                              '\n\nwill catch him off guard. This should give you an opportunity to do significant'+
                              '\n\ndamage to him.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: Kellog teleports 75 yards into the air: almost reaching the 115 foot ceiling of the'+
                              '\n\nFort Hagen underground bunker. He sticks out his right foot. He plans on crushing you'+
                              '\n\nunderfoot: he is coming at you like a spaceship coming back into the earth\'s orbit.'+
                              '\n\nYour T-60 Power Armor Computer detects Kellog at 45 yards in the air. It quickly activates'+
                              '\n\nEmergency Attack Mode: but the computer realizes there is no way you as a human will'+
                              '\n\nbe able to move in to time to dodge a man that is a second away from crushing you.'+
                              '\n\nSo the computer overides your control of the T-60 Power armor suit. You as usual get'+
                              '\n\nmad at the computer screaming: HEY, WAIT! But the computer ignores you and jumps toward'+
                              '\n\nKellog. The computer catches Kellog by surprise just as it had planned...'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: Kellog trys to dodge the computer, but the computer grabs Kellog\'s leg and then'+
                              '\n\nnose-dives toward the ground: smashing Kellog 4 feet deep into the concrete ground. The'+
                              '\n\ncomputer\'s motive was not only to put significant damage on Kellog, but to more importantly'+
                              '\n\nbreak Kellog\'s laser rifle. This the computer accomplished. But the five seconds of Emergency'+
                              '\n\nAttack Mode are over. And Kellog instantly jumps back up. The computer gives you back'+
                              '\n\ncontrol of the suit. You notice that Kellog has a bloody face.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: YOU HEATHEN! USING A COMPUTER TO GET THE EDGE ON ME!'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('You: MISS ME WITH THAT! YOU ARE LITERALLY A WALKING COMPUTER! Wait a minute....'+
                              '\n\nHmph. How does it feel you sore loser? Look at your face bleeding!'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: I AM A SYNTH: GET IT RIGHT! It\'s not like it matters: you humans'+
                              '\n\ncan\'t even tell synth and human apart until you see us fight. And what'+
                              '\n\ndo you mean, "how does it feel you sore loser?"'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('You: You\'re not used to getting your tail handed to you so you\'re'+
                              '\n\nblaming anything but yourself for losing that little skirmish'+
                              '\n\nwe just had.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: I will admit. That was only the second time I\'ve received'+
                              '\n\nsuch a hard blow in my life. The first time was this knife cut'+
                              '\n\nacross my face that another synth gave me in my courser training.'+
                              '\n\n......I killed that synth. I am the srongest synth the Insstitute'+
                              '\n\nhas after all....But that was the last, "skirmish" we were going'+
                              '\n\nto have. It is time to have an all out battle. No more interruptions.'+
                              '\n\nNo more small talk. No more weapons. Just run the ones.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('You: Bet.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: You charge Kellog, pick him up, and smash him over your steel power armor knee.'+
                              '\n\nKellog makes the best of his postition and drop kicks you. You managed to grab Kellog\'s'+
                              '\n\nfoot, but he teleports above you. Kellog throws a punch that is so strong that it caves'+
                              '\n\nin not one part of your power armor torso: but your entire power armor torso.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('T-60 Power Armor Computer speaking (robotically): Warning! Power Armor hull integrity'+
                              '\n\nis now at 41%.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: You grab Kellog\'s hand after he caves in the torso of your armor. You grab his'+
                              '\n\nother hand and pull him towards you: smashing your steel armor helmet against his'+
                              '\n\nbloody face. Kellog teleports behind you and kicks you upward: sending you flying'+
                              '\n\n80 feet into the air. Kellog teleports again and kicks you toward a wall inside'+
                              '\n\nof the bunker. But before you hit that wall: Kellog teleports again and kicks you'+
                              '\n\nto the other side of the bunker. Right before you hit that wall of the bunker: Kellog'+
                              '\n\nyet again teleports and kicks you back to the wall you were about to hit earlier.'+
                              '\n\nKellog does this 8 times: kicking you from point A to point B back and forth. All'+
                              '\n\nof this happens while you and Kellog are 80 feet in the air. Kellog finally drives'+
                              '\n\nhis foot into the caved in torso of your armor. Both of you fly down from 80 feet in'+
                              '\n\nthe air at an alarming speed. Kellog pushes off of your armor with his foot: making'+
                              '\n\nyou fall down even faster. Kellog then teleports to safety. But you get buried 9 feet'+
                              '\n\ndeep: crashing through concrete ground.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('T-60 Power Armor Computer speaking (robotically): Warning! Power Armor hull intergrity'+
                              '\n\nis now at 28%. Warning! The electronics of the power armor may start to malfunction.'+
                              '\n\nEmergency Attack Mode Overdrive is on standby: tell me when you need it. But do remember'+
                              '\n\nthat this suit will explode in flames from he inside out once the 15 second duration of'+
                              '\n\nEmergency Attack Mode Overdrive expires.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: You manage to get up, but you struggle as the legs of the T-60 Power Armor start'+
                              '\n\nto malfunction. You try to walk foward, but the legs go backwards. You panic as you'+
                              '\n\nsee Kellog walking slowly toward you: trying to incite more fear within you.'+
                              '\n\nKellog then runs at you so fast that he may as well be flying. You know he is coming,'+
                              '\n\nbut everything is a blur to you, because he is moving so quick. He uppercuts your power'+
                              '\n\narmor helmet so hard that it flew off of your head and cracked into four separate'+
                              '\n\nparts. You go flying back and hit your head on the conrete of the underground bunker.'+
                              '\n\nYou have holes all throughout your armor from Kellog\'s lasers hitting you earlier, and'+
                              '\n\nnow you have lost your helmet: the part of the armor that allows you to communicate'+
                              '\n\nwith the computer....'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: Oops.....My hand slipped. Now you can\'t talk to that computer and get'+
                              '\n\nthose random power ups. Now watch as my foot slips and stomps your face in...'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: Kellog proceeds to stomp your face in multiple times. You are screaming'+
                              '\n\nthe entire time. Now your face and head are all bloodied up. But Kellog'+
                              '\n\ncontinues stomping your face. Your nose breaks and your left eye won\'t open.'+
                              '\n\nKellog finally stops.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('You: *yelling in pain* AAAAGGGGHHHHHH....AAAAAGGGGHHHHAAAAGGHHHAAGGH...'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: This is only the beginning. This isn\'t physical torment.'+
                              '\n\nAll I\'ve done is cave your face in. YOU JUST WAIT, if you'+
                              '\n\nthink this is physically bad: wait until I really get started'+
                              '\n\non you. You can\'t even begin to fathom the physical and'+
                              '\n\nmental torture techiniques the Institute has trained me to'+
                              '\n\ndo to others. I WILL BREAK YOU! Imagine a body walking around'+
                              '\n\nwith no concious. THAT WILL BE YOU WHEN I\'M FINISHED WITH YOU!'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: I told you I am the physical emodiment of what you humans call'+
                              '\n\nthe devil. You replied saying you were the physical emodiment of the'+
                              '\n\nGod the devil betrayed. You said you were above me. Yet here I stand'+
                              '\n\nover you while you are flat on your back: screaming in pain, you have'+
                              '\n\na broken nose, and you\'re even bloodier than I am. What happened to'+
                              '\n\nall that big talk?'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: Feeling desperate: you call out to your T-60 Power Armor Computer.'+
                              '\n\nBut the problem is that It can\'t be used since it can only hear you'+
                              '\n\nwith the T-60 Power Armor Helmet on: the helmet Kellog just knocked'+
                              '\n\noff your head and split into four different parts. You hope that the'+
                              '\n\ncomputer can hear you. You hope that it somehow is still on and will'+
                              '\n\nactivate your final and most strongest power boost.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('You (yelling out): Computer! Activate Emergency Attack Mode Overdrive!'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: Shut up! *Kellog stomps your face again* I destroyed your'+
                              '\n\nhelmet: that\'s where your computer resides. So the computer is'+
                              '\n\ngone as well. You lose...'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('T-60 Power Armor Computer speaking (malfunctioning): EeeeeeeMmmeerrr....'+
                              '\n\nEmergensheeeee...*feedback noises* *malfunctioning noises* Emmmerr...'+
                              '\n\nEmergency Attack Mode OverDrive: Activated. Physical attack energy'+
                              '\n\noutput increased by 9,771%. Attack speed increased by 750%.'+
                              '\n\nDuration of this mode: 15 seconds. Power Armor will explode from the'+
                              '\n\ninside out after 15 seconds. Proceed cautiously user.....*computer'+
                              '\n\ndies out*.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: WHAT!?!? HOW DID IT ACTIVATE!?!?'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('You: Though you broke the helmet: the computer just barely survived, and it'+
                              '\n\nit heard me. And why do you sound so scared Kellog *smirks at Kellog*'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: With Emergency Attack Mode OverDrive activated: you jump up and prepare to'+
                              '\n\nattack Kellog. Kellog tries to teleport above you to drop down on you with a'+
                              '\n\nheavy punch, but with a 750% increase in attack speed: you beat him. You grab'+
                              '\n\nKellog by the neck and drive him into the ground. You start strangling him.'+
                              '\n\nKellog starts to gasp for air. But he somehow manages to break free: even'+
                              '\n\nthough you have a 9,771% increase in physical attack power. However, you'+
                              '\n\nquickly grab him by the neck again and start slamming his head into the'+
                              '\n\nconcrete ground. You do this many times. You then drag Kellog by the feet and'+
                              '\n\nrun as fast as you can to the most nearby wall in the bunker. You reach back'+
                              '\n\nwith Kellog\'s foot in your hand as if you were an archer reaching back to get'+
                              '\n\na bow out of your bow holder strapped to your back. You then sling Kellog into'+
                              '\n\nthe wall: it collapses. You then hop on top of Kellog and treat his face like'+
                              '\n\na speed boxing bag: except the punches are 750% faster and the hits he takes'+
                              '\n\nare coming from fist of steel.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: You continued sitting on top of Kellog and punching him for another 7 seconds.'+
                              '\n\nKellogs face is now deformed: he is completely unrecognizable. He lays on the ground'+
                              '\n\nmotionless. Going in the fit of rage that you did: you forgot that Emergency Attack'+
                              '\n\nMode OverDrive only last for 15 seconds. The time just ran out. You try to hurry up'+
                              '\n\nand get out of your power armor before the fusion core explodes and blows the suit'+
                              '\n\nup: burning you to a crisp. You can feel the suit getting really hot and you hear a'+
                              '\n\nnoise that is getting louder and louder. It is the fusion core getting ready to'+
                              '\n\nexplode. But you don\'t have the computer around to tell it to open the armor. You'+
                              '\n\nstart to panic.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('You: COME ON!! I NEED TO GET THIS OFF OF ME......Hot! Hot! HOT!'+
                              '\n\n*you shriek* AhHhHhHHHHhhH. HEEEELLLLPPP.*you roll around as'+
                              '\n\nthe suit is on fire and gets ready to explode.* HELP ME!!'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: Just as you were about to lose all hope :the suit opens up'+
                              '\n\nand you crawl out of it and run away from it. But you can\'t'+
                              '\n\nget far because the fire has done a great deal of damage'+
                              '\n\nto everything except your face. You were in excrutiating pain'+
                              '\n\nas you ran away from the armor. You fell on the concrete and'+
                              '\n\ncried out in more pain because your skin is burned/tender.'+
                              '\n\nYou left the power armor suit right next to Kellog: it explodes'+
                              '\n\nright next to him.'+
                              '\n\n(Press enter to continue.)')
                        if ARMOR3 in character_inventory3:
                            character_inventory3.remove(ARMOR3)
                        if FUSION_CORE2 in character_inventory4:
                            character_inventory4.remove(FUSION_CORE2)
                        print()
                        print()
                        input('SYSTEM: T-60 Power Armor and Fusion Core have been removed from your inventory.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('You: Wait! This is bad! I need to get that computer chip inside of Kellog\'s head!'+
                              '\n\nThat\'s what he uses to teleport to the Institute. But it\'s over there burning'+
                              '\n\nup! I probably made it no better nearly caving his head inwards: the computer'+
                              '\n\nchip is probably damaged! Dang it!'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: You notice Kellog crawling out of the flames coming from the power armor'+
                              '\n\nexplosion.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('You: NO! IT\'S IMPOSSIBLE! HOW ARE YOU ALIVE!?!? JUST DIE ALREADY!'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: *heavy breathing* Who said I was burning up?  *continues crawling* *heavy breathing*'+
                              '\n\nAnd who\'s head is nearly caved in? **heavier breathing** And who\'s computer......'+
                              '\n\n***even heavier breating*** chip is damaged? Forget it. I have to kill you. I can\'t'+
                              '\n\nbelieve a mere human hiding *wheezes* behind steel armor could......no. It wasn\'t you'+
                              '\n\nwho did this to me.....It was that armor. You did nothing to me!'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('You: You are so ignorant. Let me strip you of all your cybernetic parts and things like your'+
                              '\n\nteleportation ability: then let\'s see who beats who. My point is: both of us used technology'+
                              '\n\nto fight one another. So shut your ignorant self up! And stop crawling towards me!!........'+
                              '\n\n*tries to move*.......*tries to move again*......WHY CAN\'T I MOVE!?!?'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: You\'re exhausted is all. You may have had on a highly advanced combat suit....but'+
                              '\n\nit wasn\'t enough to keep your body from tiring out fighting the likes of me.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: Kellog stops crawling toward you and manages to muster up the strength to get up.'+
                              '\n\nYou finally are able to get up as well, but you fall because you are still suffering'+
                              '\n\nfrom the burns the fire gave you. Kellog started to slowly walk toward you. Now Kellog'+
                              '\n\nis standing right over you.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: This is the end of the line for you. What\'s the cliche? So close but so far?'+
                              '\n\nThat\'s your son, Shaun. You were SO close. And you failed right at the end. Too bad'+
                              '\n\nfor you. I can only imagine what you must be feeling on the inside right now. I said'+
                              '\n\nthat I would torture you....but it\'s best that I kill you now. I can\'t take anymore.'+
                              '\n\nI\'m on the verge of death. You would be too if you weren\'t hiding behind all that'+
                              '\n\nsteel armor. Better yet, you would have been killed if it weren\'t for that armor.'+
                              '\n\nNow it is---'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('A familiar voice: TIME FOR YOU TO DIE! NOW IT IS TIME FOR YOU TO DIE KELLOG!'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: You see someone rush at Kellog with a sword. The sword goes through Kellog\'s'+
                              '\n\nchest. Kellog gasp for air holding the sword in his chest as if he wants to get it out.'+
                              '\n\nYou can\'t tell who this new person is, but their voice sounds familiar. You really don\'t'+
                              '\n\ncare seeing that they are here to help you: hopefully.'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: **Kellog chokes** You fool...who......are you?'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('A familiar voice: Who am I? I\'m the man that just stole the kill of my friend over there.'+
                              '\n\nIt couldn\'t be helped because you were about to kill him. I can\'t allow that to happen.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: There...*chokes* There is no way you\'re a human. Other than that human over there'+
                              '\n\n*Kellog points at you* there is no way any other humans even know about me or this place.'+
                              '\n\nYou have to be a synth!'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Nick Valentine: The names Nick. Nick Valentine. My last name is fitting isn\'t it?'+
                              '\n\nI just became your valentine! I kind of just stole your heart with this sword.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('You: What!?!? Nick!?!?'+
                              '\n\n(Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: STOP! *coughs* *coughs* *wheezes* STOP TELLING JOKES! You underhanded heathen!'+
                              '\n\nThese tactics of yours are dishonorable. You dare attack me at my weakest?'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Nick Valentine: Look punk. I just happened to get here at a convenient time.'+
                              '\n\nI don\'t care about honor. I\'m a detective. Not a fighter like you. Now'+
                              '\n\nit\'s time for you to die so my friend Nate here can take that computer'+
                              '\n\nchip inside of your head and teleport to the Institute.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Kellog: Hmph. Your friend is not a synth like me. What is he going to do? Open up'+
                              '\n\nhis head and put the computer chip in? Last I checked humans can\'t do that.'+
                              '\n\nYou might be a synth Valentine, but even you can\'t do it. You said your a'+
                              '\n\ndetective. So you live in the CommonWealth. That means the Institute scientist'+
                              '\n\ncounted you as a failed experiment and erased most of your memories. So you'+
                              '\n\nwouldn\'t even know how to put the chip in your head. Even if you did you would'+
                              '\n\nneed the Institute scientist to put it in for you.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('Nick Valentine: I might not remember much, but I do know that I can make a'+
                              '\n\nremote that can store your computer chip inside of it. It will all work'+
                              '\n\nthe same and Nate will be able to teleport into the institute using that'+
                              '\n\nremote. It\'s the same type of remote that the human scientist use to'+
                              '\n\nteleport into the Institute. But to make it I need your computer chip.'+
                              '\n\nSO DIE ALREADY!! *Nick thrust the sword further into Kellog\'s chest*'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        print()
                        print()
                        input('SYSTEM: Kellog is finally dead. Nick swooped in and saved you: even though you asked Nick not'+
                              '\n\nto help. He tells you that he couldn\'t help but worry about you. You and Nick stay inside'+
                              '\n\nthe Fort Hagen underground bunker for another month or so helping you to recover. There was'+
                              '\n\nmore than enough medical supplies with it being a military bunker: even though it is mostly'+
                              '\n\nan ammunition storage bunker. Nick would go buy you food and water from Diamond City and come'+
                              '\n\nback as fast as he could to help you recover from your fight with Kellog. You use any First'+
                              '\n\nAid Kits that you had on yourself. Nick relates to you how surprised he is that the Institute'+
                              '\n\nhas not yet come after the two of you after finding out their strongest synth courser was'+
                              '\n\ndefeated. Nick relates to you how he feels something isn\'t right.'+
                              '\n\n(SYSTEM: Press enter to continue.)')
                        if FIRST_AID1 in character_inventory2:
                            character_inventory2.remove(FIRST_AID1)
                        elif FIRST_AID2 in character_inventory3:
                            character_inventory3.remove(FIRST_AID2)
                        elif FIRST_AID3 in character_inventory4:
                            character_inventory4.remove(FIRST_AID3)
                        print()
                        print()
                        input('SYSTEM: Nick manages to get the computer chip out of Kellog\'s head. Though he keeps telling you'+
                              '\n\nto shut up everytime you ask him how he did it. You stop asking assuming it must have been'+
                              '\n\na very bad experience for Nick. You finally fully recover and Nick has the teleporting remote'+
                              '\n\nworking. It will take you straight to the Insitute. You and Nick Say goodbye to each other for'+
                              '\n\nthe second time. You again thank Nick for all he has done for you. He tells you to be safe and'+
                              '\n\nto make the best of your circumstances. You tell him that you always do. Nick heads back to'+
                              '\n\nDiamond City. And you can now use the teleporting machine to travel to the Institute to find your'+
                              '\n\nson, Shaun.'+
                              '\n\n(Press enter to continue.)')
                        if TELEPORT_REMOTE not in character_inventory4:
                            character_inventory4.append(TELEPORT_REMOTE)
                        print()
                        print()
                        input('SYSTEM: Teleporting remote has been added to your inventory.'+
                              '\n\n(Press enter to continue.)')

            else:
                input('SYSTEM: You need stronger Power Armor'+
                      '\n\nbefore coming here.'+
                      '\n\n(Press enter to continue.)')

        else:
            input('SYSTEM: You need stronger weapons before'+
                  '\n\ncoming here.'+
                  '\n\n(Press enter to continue.)')

    else:
        input('SYSTEM: You need to explore more of Diamond City before'+
              '\n\ncoming here.'+
              '\n\n(Press enter to continue.)')

def institute(character_inventory4):
    if TELEPORT_REMOTE in character_inventory4:
        input('SYSTEM: You turn on the teleporting remote that Nick Valentine'+
              '\n\nmade for you. Besides the power button. All you have to'+
              '\n\ndo is press the big red button in the middle. Kellog\'s'+
              '\n\ncomputer chip that was inside of his head is now inisde'+
              '\n\nof the remote, so you can teleport into the Institute just'+
              '\n\nas Kellog used to do.'+
              '\n\n(Press enter to continue.)')
        print()
        print()
        input('SYSTEM: You press down on the big red button in the middle of the'+
              '\n\nremote and feel as if you are, "evaporating". Your body'+
              '\n\nis dematerializing in a blinding flash of blue light: just as'+
              '\n\nKellog did many times in your battle against him.'+
              '\n\n(Press enter to continue.)')
        print()
        print()
        input('SYSTEM: You are now re-materializing in a blinding flash of blue light.'+
              '\n\nYou now find yourself in a place that looks very futuristic and clean.'+
              '\n\nYou know for certain that you have made it to the Institute. But you see'+
              '\n\nno people or synths anywhere. You appear to be in some sort of room that'+
              '\n\nis no longer being used.'+
              '\n\n(Press enter to continue.)')
        print()
        print()
        input('Institute intercom: Hello. I wondered if you\'d make it here. You\'re quite'+
              '\n\nresourceful.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('You: Who in the.....'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Institute intercom: I am known as Father; the Institute is under my guidance.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (on intercom): I know why you\'re here. I\'d like to discuss things'+
              '\n\nwith you face-to-face. Please, step into the elevator up ahead.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('SYSTEM: You go up ahead and the elevator opens up. You step inside and it closes'+
              '\n\nbehind you. It then starts to descend. You don\'t know what is about to happen,'+
              '\n\nbut you are willing to go to the moon and back to find your son.'+
              '\n\n(Press enter to continue.)')
        print()
        print()
        input('Father (on intercom): I can only imagine what you\'ve heard---what you'+
              '\n\nthink of us. I\'d like to show you that you may have....the wrong'+
              '\n\nimpression.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (on intercom): Welcome to the Institute.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('SYSTEM: Apparently the elevator is capable of blocking your view.'+
              '\n\nBecause as soon as Father said, "Welcome to the Institute", your'+
              '\n\nview became clear. You look around and are amazed at how orderly,'+
              '\n\nneat, clean, and futuristic everything looks. You see people walking'+
              '\n\naround the facility. Some of them might be synths and you just can\'t'+
              '\n\ntell: since synths easily pass as humans. You see condo like buildings'+
              '\n\nwith balconies. You also see healthy trees and plant life: something'+
              '\n\nthat you do not see in the CommonWealth. You even see a pond in the'+
              '\n\nthe distance.'+
              '\n\n(Press enter to continue.)')
        print()
        print()
        input('Father (on intercom): This is the reality of the Institute. This place,'+
              '\n\nthese people, the work we do.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (on intercom): For over 100 years we have dedicated ourselves'+
              '\n\nto the survival of humanity.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (on intercom): Decades of research, countless experiments and'+
              '\n\nand trials......A shared vision of how science can help shape the'+
              '\n\nfuture.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (on itercom): It has never been easy....and our actions are often'+
              '\n\nmisinterpreted by those above ground.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Thinking to self: He just said, "aboveground". So the Institute is underground, huh?'+
              '\n\nI guess it makes perfect since actually. Where else could they hide themselves?'+
              '\n\nAnd this elevator is still descending....they definitely reside underground.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (on intercom): Someday, perhaps, we can show them what we\'ve accomplished. But'+
              '\n\nfor now, we must remain underground.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (on intercom): There\'s too much at stake here to risk it all. As you have'+
              '\n\nseen, things above ground are......horrendous.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (on intercom): I\'d like to talk to you about what'+
              '\n\nwe can do for everyone.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (on intercom): But that can wait. You are here for a very specific,'+
              '\n\nvery personal reason. You are here for your son.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('SYSTEM: Right as "Father" finished speaking: the elevator finally stopped'+
              '\n\ndescending. The elevator opens up and what you find in front of you makes'+
              '\n\nyour heart sink and jump at the same time. It appears to be your son, Shaun.'+
              '\n\nBut it appears he is around the age of 10. So after your wife was murdered'+
              '\n\nby Kellog and he took your son: just how long were you left in vault 111?'+
              '\n\nShaun was an infant when Kellog kidnapped him......now Shaun appears to be'+
              '\n\nabout the age of 10. Were you frozen for another 10 years before you got out'+
              '\n\nof vault 111?'+
              '\n\n(Press enter to continue.)')
        print()
        print()
        input('You: .....Shaun?'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Shaun: Huh?... Yes, I\'m Shaun...'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('You: Oh my goodness....it\'s really you..'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Shaun: Who are you?'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('You: Shaun.....it\'s me.....I\'m......I\'m you dad.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Shaun: Father...What\'s going on? What\'s happening?'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('You: *voice starts to break* Shaun...are you okay?'+
              '\n\nYou\'re not hurt are you?'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Shaun: What\'s going on? Father! Father!'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('You: What do you want me to do Shaun?'+
              '\n\nWhat can I do?'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Shaun: I don\'t know you! Get away from me!'+
              '\n\nFather help! Father!'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('SYSTEM: Some nearby sliding doors open and an old man'+
              '\n\nwalks put of them. He has on a white lab coat with'+
              '\n\nbrown dress pants and brown dress shoes.'+
              '\n\n(Press enter to continue.)')
        print()
        print()
        input('Mysterious old man: Shaun....S9-23 Recall Code Cirus.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('SYSTEM: when the old man says those words: your son Shaun'+
              '\n\nappears to act like he "powered off". He is standing'+
              '\n\nthere with his arms dangling down along with his head.'+
              '\n\nYou wonder what in the world is going on.'+
              '\n\n(Press enter to continue.)')
        print()
        print()
        input('Mysterious old man: Let\'s start anew. I am Father. Welcome'+
              '\n\nto the Institute.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('You: *very serious tone* I\'ll make this simple. Where. Is. my son?'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father: He is here. In the Institute. Closer than you think.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('You: So that boy I was just speaking to....he must be a synth....'+
              '\n\nGIVE ME SHAUN! THE REAL SHAUN! RIGHT NOW!'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father: I know...I know you have gone to such great lengths to find'+
              '\n\nhim. But I need you to realize this....situation....is far more'+
              '\n\nxomplicated than you realize.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father: You have traveled very far, and suffered a great deal to find'+
              '\n\nyour son. Well, your tenacity and dedication have been rewarded.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father: It\'s good to finally meet you after all this time. It\'s me.'+
              '\n\nI am Shaun. I am...your son.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('You: NO! How is that even possible!?!? You have got to be twice my age: I\'m 30!'+
              '\n\nYour hair and beard are literally pure white! WHERE IS MY SON!?!? I AM'+
              '\n\nLOSING PATIENCE WITH YOU!'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (Shaun): I know this is a lot to take in. Hear me out. In the vault you had'+
              '\n\nno concept of the passage of time. You were released from your cryogenic'+
              '\n\npod and went searching for the son you had lost. But you had no idea how'+
              '\n\nhow old you son was. You assumed that I was still an infant. And moments'+
              '\n\nago you thought that I was a 10 year old boy.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (Shaun): Is it really so hard to believe that it was 60 years ago when Kellog'+
              '\n\nmurdered my mother and took me to the Institute? I am 60. At that time....the year'+
              '\n\nwas 2227. The Institute were experimenting with synths, but never succeeded'+
              '\n\nin making them, "perfect". To make synths appear as closely as possible to a'+
              '\n\nhuman and give them the perfect genetics was the goal. To make synths....DNA'+
              '\n\nwas needed from people above ground. But everyone above ground is affected'+
              '\n\nby radiation in some way or another. So they found me, the perfect specimen'+
              '\n\nsealed away in a vault with uncorrupted DNA: I was ideal and beyond. So every'+
              '\n\nsynth you see and meet: You and I are their family in a way. Because all'+
              '\n\nsynths have my uncorrupted genetics, and you are my father: we are all'+
              '\n\nrelated.....at least by genes. And this is why I am called "Father" because'+
              '\n\nthrough science: we are all related. I\'m sure you have seen synths that'+
              '\n\nlook nothing like me nor you. That is simply thanks to high tech genetic'+
              '\n\nengineering.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('You: Ok....It really is you...I must admit though. I really wish you were younger'+
              '\n\nShaun. I\'m heartbroken. But why do you talk about your mother as if she is'+
              '\n\njust collateral damage!?!? And the year is currently 2287! WHY WAS I LEFT IN'+
              '\n\nTHE VAULT!?!? *burst out crying* Why did they not take me with you!?!? Why'+
              '\n\nleave me in there for sixty years!?!?'+
              '\n\nI had been in there since the year 2077. I was in there 210 years total!'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (Shaun): I\'m afraid I have little experience with loving others. Please try'+
              '\n\nto understand my situation. I have been raised down here in the Institute as a'+
              '\n\nman of science. I have lived my entire life as a man of science alongside many'+
              '\n\nother scientist down in here in the institute. Try to understand that I have not'+
              '\n\neven a single memory of my mother. I was but an infant. Had the world not become'+
              '\n\nwhat it is now: I am more than sure I would have grew up attached to her hip. I am'+
              '\n\nmore than sure I would have loved my mother so deeply. But, here we are in this'+
              '\n\nunfortunate reality of the world. Also try to understand that I have had my entire'+
              '\n\nlife to cope with the loss of my mother.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (Shaun): And as for you. You were left in the vault because the Institute saw'+
              '\n\nno need to release you. They already had the perfect specimen to help create the'+
              '\n\nperfect synths: me. But please do not take this the wrong way. In truth, in a way...'+
              '\n\nThe Institute rescued me and you from that vault. We would have been frozen in time'+
              '\n\nforever had it not been for the Institute. But here we are: reunited.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('You: Ok...ok....Listen to this...Since I\'ve been in here I can\'t help but notice this'+
              '\n\nextremely advanced technology. There is an entire pond down here! I\'m assuming'+
              '\n\nthese things: You all have good, clean, edible food, that you all have potable water,'+
              '\n\nand that you all sleep good, because I saw what are basically condos down here, and'+
              '\n\nI\'m betting you guys have the best healthcare the world has ever seen. This technology'+
              '\n\nis insane! My question: why are you not helping the people above ground? It is hades up'+
              '\n\nup there!'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (Shaun): Oh we have tried to help them! But they refused the Institute. We will look'+
              '\n\nafter our own now! I\'m sure you have heard lots of bad things about the Institute. I'+
              '\n\nwill not deny any of the things you have heard. But father....you know as well as I that'+
              '\n\nthe world above ground is doomed. Looking in history books we see that humans never change!'+
              '\n\nEven if we rebuild the world up there....again wars will break out, people will hate one'+
              '\n\nanother, the world will be divided in even the smallest of ways! Surely this hits close to'+
              '\n\nhome for you father. I know that you were a war veteran...you know just how terrible the'+
              '\n\nworld is! Humanity\'s future now resides down here, in the Institute. You have seen this'+
              '\n\nutopia of a place compared to the, as you put it, "hades up there".'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('You: Shaun...you really are my son. I do hate this world. It never changes. I can say that'+
              '\n\nhaving been around so long. But none of this justifies the Institute kidnapping people,'+
              'n\nkilling them, and replacing them with a synth. Sure....this is heaven on earth down here.'+
              '\n\nBut it does not justify you guys treating the people up there like lab rats. Is that all'+
              '\n\nthe CommonWealth is to you Institute people? A big experiment? Sure, the Institute benefits'+
              '\n\nfrom these experiemtns and it in the long-term makes you guys lives better, but at the expense'+
              '\n\nof the already struggling people above ground. The same people that have a first aid kit'+
              '\n\nfor healthcare, the same people that having nothing to wipe their behinds with, the same people'+
              '\n\nthat can\'t find potable water, the same people that can\'t find food, the same people trying'+
              '\n\nto farm for food only to get robbed by their neighbor, the same people that have no hope because'+
              '\n\nfor so long the world has been upside down! AND YOU TREAT THEM LIKE RATS!'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (Shaun): Father. You can not be too idealistic in this world. Look at the reality. Should we go'+
              '\n\nstop our experiments...how are we to continue on advancing? How are we to maintain life down here'+
              '\n\nwithout taking experimenting and sampling from people and things above ground? You think this utopia'+
              '\n\nof a life down here came without blood? It has to happen! You are trying to paint an ideal world where'+
              '\n\neveryone wins and benefits. THIS IS IDIOCY! LOOK at history books father! You know even better than I'+
              '\n\nthat the world would eventually just repeat itself: humans will bring themselves to ruin. But this way'+
              '\n\ndown here....we are so far ahead of the world technologically that no one can have a grip on us. We can'+
              '\n\nkeep everyone and anything under our control. Should it continue on this way: the Institute will thirve.'+
              '\n\nHumans will have a perfect guaranteed future: the Institute. OR we can go willy-nilly helping everyone and'+
              '\n\nin a few hundred years just repeat the mistakes of the past. Then there would be no Institute around. Who'+
              '\n\nwould preserve humanity then? WE WOULD BE DONE FOR! Father I know it is so hard to see...But you have to'+
              '\n\nthink with the greater good in mind. I would love an ideal world just as much as you, but reality is sad.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('You: *long sigh* You have a good point. Many nations would eventually rise and just want to destroy each other'+
              '\n\nfor the sake of control over various things. People would hate one another over skin color, race, ethnicity,'+
              '\n\nlanguage, beliefs, and the list can lierally go on and on and on. I remember seeing news articles 210+ years'+
              '\n\nago of people killing each other over fast food sandwiches or over cutting each other in line. People really'+
              '\n\nare no good. It just SOOOOOOO many things I can name that\'s bad about people....It\'s all racing through my'+
              '\n\nmind but it can\'t come off my tounge because it\'s just so much....where do I even start?'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (Shaun): Yes. The old world is a lost cause. It would be foolish to try to bring back something that has been'+
              '\n\nproven time and time and time and TIME again to be BEYOND faulty. The old world didn\'t work for an ocean'+
              '\n\nof reasons. So please stop it father. Don\'t even consider that faulty system of things. I ask that you stay'+
              '\n\nhere within the Institute. Become a scientist...well that is asking a lot... You don\'t have to do that of'+
              '\n\ncourse. You could become a simple maintenance worker. I simply want you to lead the best life possible. I want'+
              '\n\nyou to be apart of something great. Re-marry down here and start you a new family. You are 30 years young.'+
              '\n\nYou don\'t have to fear of a crashing economy, or fear how you are going to feed your family, or fear anything'+
              '\n\nthat the people of that old world had to fear. Father, my offer stands for you to stay here....what do you say?'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('You: *tears fall down your eyes* Shaun I hate it so much that you\'re so right. I just can\'t accept it.'+
              '\n\n*starts crying* Why does everything have to be the way it is? I\'m honestly a crybaby of a grown man:'+
              '\n\nI\'m sorry. If it\'s not one thing it\'s another. I appreciate this place. I really do. But at the same'+
              '\n\ntime I can\'t live here knowing that we are ignoring and even harming suffering people and things for the'+
              '\n\nsake of humanity\'s perservation. But on the same token, I agree with you that it\'s pointless trying to'+
              '\n\nmake things better. Throughtout history millions have tried to make things better. And things only kept'+
              '\n\ngetting progressively worse. And here we are today: we have a post-apocalytic wasteland not just here in'+
              '\n\nthe CommonWealth, but world-wide. Shaun.....I don\'t know what to choose.'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('Father (Shaun): I won\'t be inconspicuous about this. I will do everything I can to try to get you'+
              '\n\nto stay down here and rebuild your life: a life better than you previously had. But I also of'+
              '\n\ncourse am not going to hold you against your will. In the meantime....let\'s just.....talk'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('You: *sad smile* Sure son.....let\'s just talk....'+
              '\n\n(SYSTEM: Press enter to continue.)')
        print()
        print()
        input('SYSTEM: THE END! GAME OVER! CONGRATULATIONS!'+
              '\n\n(SYSTEM: YOU BEAT THE GAME! PRESS ENTER TO CONTINUE!')                   
main()

