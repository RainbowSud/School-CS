#Benjamin Swenson - Section 1

import random

def printSimpleBoard(die,myPts,devilPts,myTurn,myRndPts,devilRndPts): #nice beautiful board
    print("\n")
    if myTurn is True:
        print("                 *Your Turn*")
    else:
        print("                *Devil's Turn*")
    print("----------------------------------------------------")
    print("  My Total Score:", myPts, "      " "Devil's Total Score:", devilPts, "")
    print("----------------------------------------------------")
    print("  My Round Score:", myRndPts, "     ", "Devil's Round Score:", devilRndPts)
    print("----------------------------------------------------")
    print("                     die")
    print("                     ", die)


def main():
    die = 0
    myPts = 0
    devilPts = 0
    myTurn = True
    myRndPts = 0
    devilRndPts = 0
    Game = True
    print("|----------------------------------------------------------------|") #Game instructions
    print("|    Welcome to Devils Dice, try you luck at beating the devil   |") #Game instructions
    print("|                   The Rules are as follows:                    |") #Game instructions
    print("|             1. The First Person to 100 Points wins             |") #Game instructions
    print("|        2. If a 1 is rolled that player loses their turn        |") #Game instructions
    print("|             Press Q at anytime to quit the game                |") #Game instructions
    print("|----------------------------------------------------------------|") #Game instructions
    while Game is True:
        if myTurn is True: #Player Turn
            if myPts >= 100:
                printSimpleBoard(die, 100, devilPts, myTurn, 100, devilRndPts)
                print("You won the game, congrats!")
                Game = False
            else:
                printSimpleBoard(die, myPts, devilPts, myTurn, myRndPts, devilRndPts)
                response = input("What would you like to do?\n   [r]oll or [p]ass?")
                if response == 'r':
                    die = random.randint(1, 6)
                    if die >= 2:
                        print("You roll a", die)
                        myRndPts += die
                    else:
                        print("You roll a 1 and lose your turn")
                        myRndPts = myPts
                        myTurn = False
                elif response == 'p':
                    myTurn = False
                    myRndPts = myRndPts
                    myPts = myRndPts
                elif response == 'q':
                    print("Have a good day!")
                    Game = False
                else:
                    print("I don't understand your input, try again")
        else: #Devil Turn
            if devilRndPts >= 100:
                printSimpleBoard(die, myPts, 100, myTurn, myRndPts, 100)
                print("The Devil Won, you suck!")
                Game = False
            else:
                if myPts == devilPts or myPts < devilPts: #Devil logic pt 1
                    if devilRndPts - devilPts >= 21:
                        print("The devil passes his turn")
                        devilRndPts = devilRndPts
                        devilPts = devilRndPts
                        myTurn = True
                    else:
                        die = random.randint(1, 6)
                        printSimpleBoard(die, myPts, devilPts, myTurn, myRndPts, devilRndPts)
                        print("The devil rolls a", die)
                        response = input("[c]ontinue")
                        if response == 'c':
                            if die >= 2:
                                devilRndPts += die
                            else:
                                print("The devil loses his turn")
                                devilRndPts = devilPts
                                myTurn = True
                        elif response == 'q':
                            print("Have a good day!")
                            Game = False
                        else:
                            print("I don't understand your response")
                else:
                    if devilRndPts - devilPts >= 30: #Devil logic pt 2
                        print("The devil passes his turn")
                        devilRndPts = devilRndPts
                        devilPts = devilRndPts
                        myTurn = True
                    else:
                        die = random.randint(1, 6)
                        printSimpleBoard(die, myPts, devilPts, myTurn, myRndPts, devilRndPts)
                        print("The devil rolls a", die)
                        response = input("[c]ontinue")
                        if response == 'c':
                            if die >= 2:
                                devilRndPts += die
                            else:
                                print("The devil loses his turn")
                                devilRndPts = devilPts
                                myTurn = True
                        elif response == 'q':
                            print("Have a good day!")
                            Game = False
                        else:
                            print("I don't understand your response")



main()