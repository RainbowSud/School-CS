import math
import random

class Table:
    def __init__(self, probability=0, trial=0, count=0):
        self.__prob = probability
        self.__trial = trial
        self.__count = count

    def getProb(self):
        return self.__prob

    def getTrial(self):
        return self.__trial

    def setProb(self):
        response = input("What is your probability?")
        self.__prob = response

    def setTrial(self):
        response = input("How many tests do you want to run?")
        self.__trial = response

    def runCalc(self):
        self.__count = 0
        stop = False
        while stop is False:
            output = random.randint(1, int(self.__prob))
            if output == int(self.__prob):
                self.__count += 1
                return self.__count
            elif output != int(self.__prob):
                self.__count += 1

    def print(self):
        print("Big booty board yes yes")
        print("Prob:", self.__prob)
        print("Trials:", self.__trial)
        print(":", self.__count)

def main():
    t1 = Table()
    t1.setProb()
    t1.setTrial()
    n = t1.getTrial()
    trials = []
    for i in range(1, int(n)+1):
        count = t1.runCalc()
        trials.append(count)
        print("Trial", i, ":", count)


main()
