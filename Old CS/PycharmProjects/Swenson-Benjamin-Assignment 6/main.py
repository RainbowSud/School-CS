# Benjamin Swenson - Assignment 6 - CS 1400 Section 1
class Artomat:  # The actual artomat class itself
    def __init__(self, money=0, hopper=0, bin1=10, bin2=10, bin3=10, bin4=10, text1="1", text2="2", text3="3", text4="4"):
        self.__status = money, hopper, bin1, bin2, bin3, bin4, text1, text2, text3, text4
        self.__quarter = .25
        self.__restock = money, hopper, bin1, bin2, bin3, bin4, text1, text2, text3, text4
        self.__money = money * .25
        self.__hopper = hopper * .25
        self.__bin1 = bin1
        self.__bin2 = bin2
        self.__bin3 = bin3
        self.__bin4 = bin4
        self.__text1 = text1
        self.__text2 = text2
        self.__text3 = text3
        self.__text4 = text4
        # init function, sets up my variables for the rest of the functions

    def printStatus(self):  # prints the status of the machine
        print("1:", self.__bin1, "packs of", self.__text1)
        print("2:", self.__bin2, "packs of", self.__text2)
        print("3:", self.__bin3, "packs of", self.__text3)
        print("4:", self.__bin4, "packs of", self.__text4)
        print("There is $", self.__money, "in the machine.")
        print("There is $", self.__hopper, "in the hopper.")
        print("                                ")

    def dropQuarter(self):  # drops a quarter into the machine, adds money to the hopper directly
        print("ching")
        self.__hopper += .25

    def pullKnob(self, x):  # pulls a knob on the machine
        if x == 1 and self.__hopper >= .75:  # says if knob one is pulled and there are at least 75 cents in hopper do task
            print("A pack of", self.__text1, "slides into view.")
            self.__bin1 -= 1
            self.__hopper = 0
            self.__money += .75
            print("                               ")
        elif x == 1 and self.__hopper < .75:  # says if knob one is pulled and there are less than 75 cents in hopper do task
            print("(nothing happens)")
            self.__money += self.__hopper
            self.__hopper = 0
        elif x == 2 and self.__hopper >= .75:
            print("A pack of", self.__text2, "slides into view.")
            self.__bin2 -= 1
            self.__hopper = 0
            self.__money += .75
            print("                               ")
        elif x == 2 and self.__hopper < .75:
            print("(nothing happens)")
            self.__money += self.__hopper
            self.__hopper = 0
        # Could easily copy those above lines and change the 2's to 3's or 4's to add options
        # For pulling all 4 knobs, but that's not needed for this assignment
        # So I just didn't do that

    def restock(self):  # restocks the machine, sets all bins to 10 and all money to 0
        print("A grouchy-looking attendant shows up, opens the back, fiddles around a bit, closes it, and leaves.")
        self.__bin1 = 10
        self.__bin2 = 10
        self.__bin3 = 10
        self.__bin4 = 10
        self.__hopper = 0
        self.__money = 0
        print("                ")

# write your class definition above this line
# make no changes below this line
def main():
    photoMachine = Artomat(text1="Adams", text2="Arbus", text3="Dali", text4="Lange")
    portraitMachine = Artomat(money=212, hopper=2, bin1=1, bin2=0, bin3=8, bin4=10, text1="Picasso", text2="Rembrandt", text3="Van Gogh", text4="Monet")

    photoMachine.printStatus()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.pullKnob(1)
    photoMachine.pullKnob(2)
    photoMachine.dropQuarter()
    photoMachine.pullKnob(2)
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.pullKnob(2)
    photoMachine.printStatus()
    photoMachine.restock()
    photoMachine.printStatus()
    print("----")
    portraitMachine.printStatus()
    portraitMachine.dropQuarter()
    portraitMachine.pullKnob(1)
    portraitMachine.printStatus()


main()
