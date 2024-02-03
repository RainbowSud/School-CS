def printHeader(st,ct):
    print("    set           temp", end ="")
    if st > ct:
        print("      * heat on *")
    if st < ct:
        print("       * cooling on *")
    if st == ct:
        print("     * desired temp reached *")

def printLineofDisplay(i, st, ct):
    print("   ", end="")
    if (st < i + 5) and (st >= i):
        print(format(st, "4.0f"), " => ", end="")
    else:
        print("         ", end="")

    print(i, end="")

    if (ct < i + 5) and (ct >= i):
        print(" <= ", ct)
    else:
        print("          ")

def modifyTemp(st, ct):
    if st > ct:
        return ct + 1
    elif st < ct:
        return ct - 1

def getResponse():
    while True:
        response = input()
        if response == "q": quit = True
        if response == "": nothing = True
        if response.isnumeric(): number = True
        if quit or nothing or number: break
        print("huh?")

def main():
    setTemp = 75
    currentTemp = 50

    while True:
        printHeader(setTemp, currentTemp)

        for i in range (90, 45, -5):
            printLineofDisplay(i, setTemp, currentTemp)

        currentTemp = modifyTemp(setTemp, currentTemp)

        response = input()
        if response == "":
            continue
        elif response == "q":
            break
        else:
            setTemp = eval(response)
main()
