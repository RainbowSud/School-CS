print("Welcome to the \"Art-o-mat\" machine! Use the menu to do what you want")
print("Also a warning, if you input more then 75 cents the machine will eat your extra money, no refunds!")

print("\t\t\t\ts - report the machine status")
print("\t\t\t\td - drop a quarter")
print("\t\t\t\t1 - pull the 1st knob")
print("\t\t\t\t2 - pull the 2nd knob")
print("\t\t\t\t3 - pull the 3rd knob")
print("\t\t\t\t4 - pull the 4th knob")
print("\t\t\t\tr - restock the machine")
print("\t\t\t\tq - quit")
print("--------------------------------------------------------")

inputLoop = True
moneyAdded = 0
moneyInMachine = 16.5
whittington = 4
escher = 7
daVinci = 6
pollock = 1

while inputLoop is True:
    response = input("\t\t\t\twhat would you like do?\n--------------------------------------------------------")
    if response == 's':
        print("\t\t\t\t1:", whittington, "packs of Whittington B&W photos")
        print("\t\t\t\t2:", escher, "packs of Escher woodcuts")
        print("\t\t\t\t3:", daVinci, "packs of da Vinci sketches")
        print("\t\t\t\t4:", pollock, "packs of Pollock drop cloth clippings")
        print("\t\t\t\tThere is $", moneyInMachine, "in the machine")
    elif response == 'd':
        print("added a quarter")
        moneyAdded = moneyAdded + .25
        print("you have added $", moneyAdded, "in total")
        moneyInMachine = moneyInMachine + .25
    elif response == '1':
        if moneyAdded >= .75 and whittington > 0:
            print("A pack of Whittington B&W photos slide into view")
            moneyAdded = 0
            whittington = whittington - 1
        else:
            print("nothing happens")
    elif response == '2':
        if moneyAdded >= .75 and escher > 0:
            print("A pack of Escher woodcuts slides into view")
            moneyAdded = 0
            escher = escher - 1
        else:
            print("nothing happens")
    elif response == '3':
        if moneyAdded >= .75 and daVinci > 0:
            print("A pack of da Vinci sketches slide into view")
            moneyAdded = 0
            daVinci = daVinci - 1
        else:
            print("nothing happens")
    elif response == '4':
        if moneyAdded >= .75 and pollock > 0:
            print("A pack of Pollock drop cloth clippings slide into view")
            moneyAdded = 0
            pollock = pollock - 1
        else:
            print("nothing happens")
    elif response == 'r':
        print("A kind old man restocks the machine and removes the money inside")
        moneyInMachine = 0
        whittington = 10
        escher = 10
        daVinci = 10
        pollock = 10
    elif response == 'q':
        print("Thank you for using our machine - Have a good day!")
        inputLoop = False
    else:
        print("I don't understand your input")
        print("Please try another one")
