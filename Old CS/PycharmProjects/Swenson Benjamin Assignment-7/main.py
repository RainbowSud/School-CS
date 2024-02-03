# Benjamin Swenson Assignment 7 - CS 1400 - Section 1

class PiggyBank:  # Piggybank Class
    def __init__(self):  # Simple - Sets up the two variables that I am going to need
        self.__balance = 0.0
        self.__broken = False

    def deposit(self, money):  # Deposit function, talks about depositing money
        if self.__broken is not True:  # Says if the piggybank isn't broken, you can add money
            self.__balance += money
        else:  # Says if piggybank is broken, you can't add money
            self.__balance += 0.0

    def smash(self):  # Smash function, breaks the piggybank and takes out all of the money
        self.__balance = 0.0
        self.__broken = True

    def getBalance(self):  # grabs me my balance
        return self.__balance

    def getBroken(self):  # grabs me if the bank is broken or not
        return self.__broken

def printStatus(name, obj):  # prints status of machine
    if obj.getBroken() is not True:  # asking if bank is broken, if it isn't it prints this
        print(name, "has $", format(obj.getBalance(), ".2f"), "and is not broken.")
    else:  # if it is broken it prints this
        print(name, "has $", format(obj.getBalance(), ".2f"), "and is broken.")


def main():
    p1 = PiggyBank()
    p2 = PiggyBank()
    printStatus("p1", p1)
    p1.deposit(1.25)
    printStatus("p1", p1)
    p1.deposit(6.55)
    printStatus("p1", p1)
    p1.smash()
    printStatus("p1", p1)
    p1.deposit(2.15)
    printStatus("p1", p1)
    p1.__balance = 100.0
    p1.__broken = False
    printStatus("p1", p1)


main()
